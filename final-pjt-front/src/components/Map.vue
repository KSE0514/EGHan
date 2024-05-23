<template>
  <div class="bank-search">
    <div class="search-bar">
      <h1>근처 은행 검색</h1>
      <p class="instruction-text"></p>
      <div class="search-input">
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
        <button type="button" class="btn btn-warning" @click="searchPlaces">검색하기</button>
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
      keyword: '',
      selectedCity: '',
      currentLocationMarker: null // 현재 위치 마커를 저장할 변수 추가
    };
  },
  mounted() {
    this.loadKakaoMapScript().then(() => {
      const mapContainer = document.getElementById('map');
      const mapOption = {
        center: new kakao.maps.LatLng(35.2054, 126.8115), // 중심 좌표 설정
        level: 3
      };
      this.map = new kakao.maps.Map(mapContainer, mapOption);
      this.ps = new kakao.maps.services.Places();
      this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

      // 초기 위치 기반으로 은행 검색 및 현재 위치 표시
      this.searchPlacesByCoords(35.2054, 126.8115);
      this.displayCurrentLocation(35.2054, 126.8115);
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

      const keyword = this.selectedCity + ' ' + this.keyword;
      if (!keyword.trim()) {
        alert('키워드를 입력해주세요!');
        return false;
      }
      this.ps.keywordSearch(keyword, this.placesSearchCB);
    },
    searchPlacesByCoords(latitude, longitude) {
      if (!this.ps) {
        console.error('Places 서비스 객체가 초기화되지 않았습니다.');
        return;
      }

      const coords = new kakao.maps.LatLng(latitude, longitude);
      this.ps.categorySearch('BK9', this.placesSearchCB, {
        location: coords,
        radius: 500 // 검색 반경 (단위: 미터)
      });
    },
    placesSearchCB(data, status, pagination) {
      if (status === kakao.maps.services.Status.OK) {
        this.displayPlaces(data);
        this.displayPagination(pagination);
      } else if (status === kakao.maps.services.Status.ZERO_RESULT) {
        alert('검색 결과가 존재하지 않습니다.');
      } else if (status === kakao.maps.services.Status.ERROR) {
        alert('검색 결과 중 오류가 발생했습니다.');
      }
    },
    displayPlaces(places) {
      const listEl = document.getElementById('placesList');
      const menuEl = document.getElementById('menu_wrap');
      const fragment = document.createDocumentFragment();
      const bounds = new kakao.maps.LatLngBounds();

      this.removeAllChildNods(listEl);
      this.removeMarker();

      places.forEach((place, i) => {
        const placePosition = new kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, i, place);
        const itemEl = this.getTableRow(i, place);

        bounds.extend(placePosition);

        kakao.maps.event.addListener(marker, 'click', () => {
          this.displayInfowindow(marker, place);
        });
        itemEl.onclick = () => {
          this.map.setCenter(marker.getPosition());
          this.displayInfowindow(marker, place);
        };

        fragment.appendChild(itemEl);
      });

      listEl.appendChild(fragment);
      menuEl.scrollTop = 0;
      this.map.setBounds(bounds);
    },
    getTableRow(index, place) {
      const el = document.createElement('tr');
      const itemStr = `
        <td>${index + 1}</td>
        <td><a href="https://place.map.kakao.com/${place.id}" target="_blank">${place.place_name}</a></td>
        <td>${place.road_address_name || ''}</td>
        <td>${place.address_name || ''}</td>
        <td>${place.phone || ''}</td>
      `;

      el.innerHTML = itemStr;
      return el;
    },
    addMarker(position, idx, place) {
      const imageSrc = 'https://img.icons8.com/office/40/000000/marker.png'; // 파란색 마커 이미지 URL
      const imageSize = new kakao.maps.Size(36, 37); // 이미지 크기
      const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
      const marker = new kakao.maps.Marker({
        position,
        image: markerImage
      });

      marker.setMap(this.map);
      this.markers.push(marker);
      return marker;
    },
    removeMarker() {
      this.markers.forEach(marker => marker.setMap(null));
      this.markers = [];
    },
    displayPagination(pagination) {
      const paginationEl = document.getElementById('pagination');
      const fragment = document.createDocumentFragment();

      while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild(paginationEl.lastChild);
      }

      for (let i = 1; i <= pagination.last; i++) {
        const el = document.createElement('a');
        el.innerHTML = i;

        if (i === pagination.current) {
          el.className = 'on';
        } else {
          el.onclick = () => {
            pagination.gotoPage(i);
          };
        }

        fragment.appendChild(el);
      }
      paginationEl.appendChild(fragment);
    },
    displayInfowindow(marker, place) {
      const content = `
        <div style="padding:10px;z-index:1;width:300px;white-space:normal;text-align:left;">
          <h5><a href="https://place.map.kakao.com/${place.id}" target="_blank">${place.place_name}</a></h5>
          <span>주소1: ${place.road_address_name || ''}</span>
          <br><span>주소2: ${place.address_name || ''}</span>
          <br><span>전화번호: ${place.phone || ''}</span>
        </div>
      `;
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    displayCurrentLocation(latitude, longitude) {
      if (this.currentLocationMarker) {
        this.currentLocationMarker.setMap(null);
      }
      
      const imageSrc = 'https://img.icons8.com/fluency/48/000000/marker.png'; // 빨간색 마커 이미지 URL
      const imageSize = new kakao.maps.Size(36, 37); // 이미지 크기
      const markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
      this.currentLocationMarker = new kakao.maps.Marker({
        position: new kakao.maps.LatLng(latitude, longitude),
        image: markerImage
      });

      this.currentLocationMarker.setMap(this.map);
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

.search-input select,
.search-input input {
  margin-right: 10px;
}

.search-input button {
  padding: 8px 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.map {
  width: 100%;
  height: 500px;
  margin-bottom: 20px;
}

.places-table {

  justify-content: center; /* 중앙 정렬 */
  text-align: center; /* 텍스트 중앙 정렬 */
  width: 100%;
  border-collapse: collapse;
}

.places-table th,
.places-table td {
  border: 1px solid #e6b6b6;
  /* border: 1px solid #ddd; */
  padding: 8px;
  text-align: left;
}

.places-table th {

  text-align: center; /* 텍스트 중앙 정렬 */
  background-color: #ffe0c3;
}

.places-table tr:nth-child(even) {

  background-color: #f2f2f2;
}

#pagination {
  text-align: center;
  justify-content: center; /* 중앙 정렬 */
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
  text-align: center; /* 텍스트 중앙 정렬 */
}

.pagination a.on {
  background-color: #0056b3;
}

h1 {
  font-family: 'WavvePADO-Regular';
}

@font-face {
    font-family: 'WavvePADO-Regular';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

</style>

