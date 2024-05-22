<template>
  <div>
    <h2>예금 상품</h2>
    <table class="product-table">
      <thead>
        <tr>
          <th>상품명</th>
          <th v-for="term in displayTerms" :key="term">{{ term }}개월</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td @click="goToDetail(product.fin_prdt_cd)">{{ product.fin_prdt_nm }}</td>
          <td v-for="term in displayTerms" :key="term">
            <ul>
              <li v-if="hasOption(product, term)" v-for="option in getProductOptionsByTerm(product, term)" :key="option.id">
                {{ option.intr_rate }}%
              </li>
              <li v-else>-</li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const products = ref([]);
    const terms = ref([]);
    const displayTerms = ref([6, 12, 24, 36]);

    const getProducts = () => {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/deposit-products/'
      }).then((response) => {
        products.value = response.data;
        response.data.forEach(product => {
          getOptions(product.fin_prdt_cd);
        });
      }).catch((error) => {
        console.log(error);
      });
    }

    const getOptions = (productCode) => {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/deposit-product-options/${productCode}`
      }).then((response) => {
        const product = products.value.find(prod => prod.fin_prdt_cd === productCode);
        if (product) {
          product.options = response.data;
          response.data.forEach(option => {
            if (!terms.value.includes(option.save_trm) && displayTerms.value.includes(option.save_trm)) {
              terms.value.push(option.save_trm);
            }
          });
        }
      }).catch((error) => {
        console.log(error);
      });
    }

    const getProductOptionsByTerm = (product, term) => {
      return product.options.filter(option => option.save_trm === term);
    }

    const hasOption = (product, term) => {
      return getProductOptionsByTerm(product, term).length > 0;
    }

    onMounted(() => {
      getProducts();
    });

    const router = useRouter()
    const goToDetail = function(productCode){
      router.push(`/product/${productCode}`)
    }

    return {
      products,
      displayTerms,
      getProductOptionsByTerm,
      hasOption,
      goToDetail
    };
  }
}
</script>

<style scoped>
.product-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.product-table th,
.product-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

.product-table th {
  background-color: #f4f4f4;
  font-weight: bold;
}

.product-table td ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.product-table td ul li {
  margin-bottom: 5px;
}
</style>
