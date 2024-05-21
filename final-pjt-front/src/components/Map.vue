<template>
  <div>
    <h2>카카오 맵 보기</h2>
    <select v-model="selectedRegion">
      <option disabled value="">지역을 선택하세요</option>
      <option v-for="region in regions" :key="region.name" :value="region">{{ region.name }}</option>
    </select>
    <input type="text" v-model="searchQuery" placeholder="검색어를 입력하세요" />
    <button @click="searchLocation">검색</button>
    <div id="map"></div>
  </div>
</template>

<style scoped>
#map {
  width: 100%;
  height: 400px;
}
</style>

<script>
export default {
  name: "KakaoMap",
  data() {
    return {
      map: null,
      searchQuery: "",
      selectedRegion: "",
      regions: [
        { name: "서울", center: { lat: 37.5665, lng: 126.9780 } },
        { name: "부산", center: { lat: 35.1796, lng: 129.0756 } },
        { name: "대구", center: { lat: 35.8714, lng: 128.6014 } },
        { name: "인천", center: { lat: 37.4563, lng: 126.7052 } },
        { name: "광주", center: { lat: 35.1595, lng: 126.8526 } },
        { name: "대전", center: { lat: 36.3504, lng: 127.3845 } },
        { name: "울산", center: { lat: 35.5384, lng: 129.3114 } },
      ],
    };
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.loadScript();
    } else {
      this.loadScript();
    }
  },
  methods: {
    loadScript() {
      const script = document.createElement("script");
      script.src =
        "//dapi.kakao.com/v2/maps/sdk.js?appkey=27600437382fd635191f58999fe5dc7e&libraries=services&autoload=false"; 
      script.onload = () => {
        window.kakao.maps.load(this.loadMap);
      };
      document.head.appendChild(script);
    },
    loadMap() {
      const container = document.getElementById("map");
      const options = {
        center: new window.kakao.maps.LatLng(33.450701, 126.570667),
        level: 3
      };

      this.map = new window.kakao.maps.Map(container, options);
    },
    loadMarker(position) {
      const marker = new window.kakao.maps.Marker({
        position: position,
      });
      marker.setMap(this.map);
    },
    searchLocation() {
      if (!this.searchQuery) {
        alert("검색어를 입력하세요.");
        return;
      }

      if (!this.selectedRegion) {
        alert("지역을 선택하세요.");
        return;
      }

      // 중심 위치 설정
      const center = new window.kakao.maps.LatLng(this.selectedRegion.center.lat, this.selectedRegion.center.lng);
      this.map.setCenter(center);

      const ps = new window.kakao.maps.services.Places();
      const searchOption = {
        location: center, // 지역의 중심을 검색 기준으로 설정
        radius: 5000 // 반경 5km
      };

      ps.keywordSearch(this.searchQuery, this.placesSearchCB, searchOption);
    },
    placesSearchCB(data, status) {
      if (status === window.kakao.maps.services.Status.OK) {
        const bounds = new window.kakao.maps.LatLngBounds();

        for (let i = 0; i < data.length; i++) {
          const position = new window.kakao.maps.LatLng(data[i].y, data[i].x);
          this.loadMarker(position);
          bounds.extend(position);
        }

        this.map.setBounds(bounds);
      } else if (status === window.kakao.maps.services.Status.ZERO_RESULT) {
        alert("검색 결과가 존재하지 않습니다.");
      } else if (status === window.kakao.maps.services.Status.ERROR) {
        alert("검색 중 오류가 발생했습니다.");
      }
    }
  }
};
</script>
