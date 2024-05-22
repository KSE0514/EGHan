<template>
  <div class="bank-search">
    <div class="search-bar">
      <h1>근처 은행 검색</h1>
      <p class="instruction-text"></p>
      <div class="search-input">
        <!-- Added city selection dropdown -->
        <select v-model="selectedCity">
          <option value="">지역 선택</option>
          <option value="서울">서울</option>
          <option value="부산">부산</option>
          <option value="대구">대구</option>
          <option value="인천">인천</option>
          <option value="광주">광주</option>
          <option value="대전">대전</option>
          <option value="울산">울산</option>
          <option value="세종">세종</option>
          <option value="경기">경기</option>
          <option value="강원">강원</option>
          <option value="충북">충북</option>
          <option value="충남">충남</option>
          <option value="전북">전북</option>
          <option value="전남">전남</option>
          <option value="경북">경북</option>
          <option value="경남">경남</option>
          <option value="제주">제주</option>
        </select>
        <input type="text" id="keyword" placeholder="키워드를 입력해주세요" v-model="keyword" @keyup.enter="searchPlaces" />
        <button @click="searchPlaces">검색하기</button>
      </div>
    </div>
    <div id="map" class="map"></div>
    <div id="menu_wrap" class="bg_white">
      <table id="placesTable" class="places-table">
        <thead>
          <tr>
            <th>번호</th>
            <th>은행명</th>
            <th>주소1</th>
            <th>주소2</th>
            <th>전화번호</th>
          </tr>
        </thead>
        <tbody id="placesList"></tbody>
      </table>
      <div id="pagination" class="pagination"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      map: null,
      ps: null,
      infowindow: null,
      markers: [],
      keyword: '', // 검색어 추가
      selectedCity: '' // Selected city added
    };
  },
  mounted() {
    this.loadKakaoMapScript().then(() => {
      var mapContainer = document.getElementById('map');
      var mapOption = {
        center: new kakao.maps.LatLng(37.566826, 126.9786567),
        level: 3
      };
      this.map = new kakao.maps.Map(mapContainer, mapOption);
      this.ps = new kakao.maps.services.Places();
      this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
    }).catch(error => {
      console.error('카카오맵 스크립트 로드 실패:', error);
    });
  },
  methods: {
    loadKakaoMapScript() {
      return new Promise((resolve, reject) => {
        if (window.kakao && window.kakao.maps) {
          resolve();
          return;
        }

        const script = document.createElement('script');
        script.onload = () => kakao.maps.load(resolve);
        script.onerror = reject;
        script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=27600437382fd635191f58999fe5dc7e&libraries=services&autoload=false`;
        document.head.appendChild(script);
      });
    },
    searchPlaces() {
      if (!this.ps) {
        console.error('Places 서비스 객체가 초기화되지 않았습니다.');
        return;
      }

      // Combine selected city with keyword
      var keyword = this.selectedCity + ' ' + this.keyword;
      if (!keyword.replace(/^\s+|\s+$/g, '')) {
        alert('키워드를 입력해주세요!');
        return false;
      }
      this.ps.keywordSearch(keyword, this.placesSearchCB);
    },
    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
        this.displayPlaces(data);
        this.displayPagination(pagination);
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert('검색 결과가 존재하지 않습니다.');
        return;
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert('검색 결과 중 오류가 발생했습니다.');
        return;
      }
    },
    displayPlaces(places) {
      var listEl = document.getElementById('placesList'),
        menuEl = document.getElementById('menu_wrap'),
        fragment = document.createDocumentFragment(),
        bounds = new kakao.maps.LatLngBounds();

      this.removeAllChildNods(listEl);
      this.removeMarker();

      for (var i = 0; i < places.length; i++) {
        var placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
          marker = this.addMarker(placePosition, i, places[i]),
          itemEl = this.getTableRow(i, places[i]);

        bounds.extend(placePosition);

        (function (marker, place) {
          kakao.maps.event.addListener(marker, 'click', function () {
            this.displayInfowindow(marker, place);
          }.bind(this));
          itemEl.onclick = function () {
            this.map.setCenter(marker.getPosition());
            this.displayInfowindow(marker, place);
          }.bind(this);
        }.bind(this))(marker, places[i]);

        fragment.appendChild(itemEl);
      }

      listEl.appendChild(fragment);
      menuEl.scrollTop = 0;
      this.map.setBounds(bounds);
    },
    getTableRow(index, place) {
      var el = document.createElement('tr'),
        itemStr = '<td>' + (index + 1) + '</td>' +
          '<td><a href="https://place.map.kakao.com/' + place.id + '" target="_blank">' + place.place_name + '</a></td>';

      if (place.road_address_name) {
        itemStr += '<td>' + place.road_address_name + '</td>' +
          '<td>' + place.address_name + '</td>';
      } else {
        itemStr += '<td>' + place.address_name + '</td>' +
          '<td></td>';
      }

      itemStr += '<td>' + place.phone + '</td>';

      el.innerHTML = itemStr;
      return el;
    },
    addMarker(position, idx, place) {
      var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png',
        imageSize = new kakao.maps.Size(36, 37),
        imgOptions = {
          spriteSize: new kakao.maps.Size(36, 691),
          spriteOrigin: new kakao.maps.Point(0, (idx * 46) + 10),
          offset: new kakao.maps.Point(13, 37)
        },
        markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
        marker = new kakao.maps.Marker({
          position: position,
          image: markerImage
        });

      marker.setMap(this.map);
      this.markers.push(marker);
      return marker;
    },
    removeMarker() {
      for (var i = 0; i < this.markers.length; i++) {
        this.markers[i].setMap(null);
      }
      this.markers = [];
    },
    displayPagination(pagination) {
      var paginationEl = document.getElementById('pagination'),
        fragment = document.createDocumentFragment(),
        i;

      while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild(paginationEl.lastChild);
      }

      for (i = 1; i <= pagination.last; i++) {
        var el = document.createElement('a');
        el.href = "#";
        el.innerHTML = i;

        if (i === pagination.current) {
          el.className = 'on';
        } else {
          el.onclick = (function (i) {
            return function () {
              pagination.gotoPage(i);
            };
          })(i);
        }

        fragment.appendChild(el);
      }
      paginationEl.appendChild(fragment);
    },
    displayInfowindow(marker, place) {
      var content = '<div style="padding:10px;z-index:1;width:300px;white-space:normal;text-align:left;">' +
        '<h5><a href="https://place.map.kakao.com/' + place.id + '" target="_blank">' + place.place_name + '</a></h5>' +
        '<span>주소1: ' + place.road_address_name + '</span>' +
        '<br><span>주소2: ' + place.address_name + '</span>' +
        '<br><span>전화번호: ' + place.phone + '</span>' +
        '</div>';
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    removeAllChildNods(el) {
      while (el.hasChildNodes()) {
        el.removeChild(el.lastChild);
      }
    }
  }
};
</script>

<style scoped>
.bank-search {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.search-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
}

.instruction-text {
  margin-bottom: 10px;
  font-size: 1.2em;
  color: #333;
}

.search-input {
  display: flex;
  align-items: center;
}

.search-input select {
  padding: 10px;
  font-size: 1em;
  margin-right: 10px;
}

.search-input input {
  flex: 1;
  padding: 10px;
  font-size: 1em;
  margin-right: 10px;
}

.search-input button {
  padding: 10px 20px;
  font-size: 1em;
  background-color: #333;
  color: #fff;
  border: none;
  cursor: pointer;
}

.search-input button:hover {
  background-color: #555;
}

.map {
  width: 80%;
  height: 500px;
  margin-bottom: 20px;
}

#menu_wrap {
  width: 80%;
}

.places-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.places-table th,
.places-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

.places-table th {
  background-color: #f4f4f4;
  font-weight: bold;
}

.places-table td a {
  color: #333;
  text-decoration: none;
}

.places-table td a:hover {
  text-decoration: underline;
}

#pagination {
  text-align: center;
  margin: 10px 0;
}

#pagination a {
  display: inline-block;
  margin: 0 5px;
  padding: 5px 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  text-decoration: none;
  color: #333;
}

#pagination a.on {
  background-color: #333;
  color: #fff;
  border-color: #333;
}
</style>
