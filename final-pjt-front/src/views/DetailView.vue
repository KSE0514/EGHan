<template>
  <div>
    <h2>Product Detail</h2>
    <p><strong>Product Code:</strong> {{ productCode }}</p>
    <!-- 여기에 다른 상품 세부 정보를 표시할 수 있습니다 -->
    <ProductDetail :product-code="productCode" />
    <SavingProductDetail :product-code="productCode" />
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
</style>
