<template>
  <div>
    <h2>예금 상품</h2>
    <ul>
      <li v-for="product in products" :key="product.id">
        <h3 @click="goToDetail(product.fin_prdt_cd)">{{ product.fin_prdt_nm }}</h3>
        <p><strong>Product Code:</strong> {{ product.fin_prdt_cd }}</p>
        <p><strong>Company:</strong> {{ product.kor_co_nm }}</p>
        <!-- 다른 필드들도 필요에 따라 표시할 수 있습니다 -->
        <hr>
        <!-- <h4>Options</h4>
        <ul>
          <li v-for="option in product.options" :key="option.id">
            <p><strong>Interest Rate Type:</strong> {{ option.intr_rate_type_nm }}</p>
            <p><strong>Interest Rate:</strong> {{ option.intr_rate }}</p>
          </li>
        </ul> -->
      </li>
    </ul>
  </div>
</template>

<script>
// import router from '@/router';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
export default {
  setup() {
    const products = ref([]);

    const getProducts = () => {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/deposit-products/'
      }).then((response) => {
        products.value = response.data;
      }).catch((error) => {
        console.log(error);
      });
    }

    onMounted(() => {
      getProducts();
    });

    const router = useRouter()
    const goToDetail = function(productCode){
      router.push(`/product/${productCode}`)
    }
    return {
      products,goToDetail
    };
  }

}
</script>


<style scoped>
/* 스타일 정의 */
</style>
