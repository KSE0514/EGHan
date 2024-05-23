<template>
  <div>
    <h2>상품 상세 설명</h2>
    <div class="item">
      <ProductDetail :product-code="productCode" />
      <SavingProductDetail :product-code="productCode" />
    </div>
    <!-- <p><strong>Product Code:</strong> {{ productCode }}</p> -->
    <!-- 여기에 다른 상품 세부 정보를 표시할 수 있습니다 -->
  </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import ProductDetail from '@/components/ProductDetail.vue';
import SavingProductDetail from '@/components/SavingProductDetail.vue';

export default {
  components: {
    ProductDetail,
    SavingProductDetail
},
  setup() {
    const route = useRoute();
    const productCode = ref(null);

    const getProductDetail = () => {
      if (route.params.productCode) {
        productCode.value = route.params.productCode;
        // 여기서 상품의 세부 정보를 가져오는 API 호출 등의 로직을 수행할 수 있습니다.
        console.log(route.params)
      }
    };

    onMounted(() => {
      getProductDetail();
    });

    return {
      productCode
    };
  }
};
</script>

<style scoped>
/* 스타일 정의 */
h2 {
    /* font-family: 'April16th-Life'; */
    /* font-size: 45px; */
    font-family: 'WavvePADO-Regular';
}

@font-face {
    font-family: 'April16th-Life';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404-2@1.0/April16th-Life.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}

h5{
  font-family: 'S-CoreDream-3Light';
  font-weight: bolder;
}
p{
  font-family: 'S-CoreDream-3Light';
}
@font-face {
    font-family: 'WavvePADO-Regular';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
@font-face {
     font-family: 'S-CoreDream-3Light';
     src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
     font-weight: normal;
     font-style: normal;
}

.item {
  margin-top: 20px;
  border: 2px solid red;
  border-radius: 10px;
  padding: 20px;
}
</style>
