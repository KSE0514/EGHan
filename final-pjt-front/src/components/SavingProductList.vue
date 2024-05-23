<!-- <template>
  <div>
    <h2>적금 상품 비교</h2>
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
        url: 'http://127.0.0.1:8000/api/v1/deposit-saving-products/'
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
        url: `http://127.0.0.1:8000/api/v1/saving-product-options/${productCode}`
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
</style> -->



<template>
  <div>
    <h2>적금 상품</h2>

    <!-- 은행 선택 드롭다운 -->
    <select v-model="selectedBank" @change="filterProducts">
      <option value="">전체</option>
      <option v-for="bank in bankList" :value="bank">{{ bank }}</option>
    </select>

    <table class="product-table">
      <thead>
        <tr>
          <th>상품명</th>
          <th v-for="term in displayTerms" :key="term">{{ term }}개월</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in filteredProducts" :key="product.id">
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
    const filteredProducts = ref([]);
    const bankList = ref([]); // bankList를 추가하여 데이터로 정의합니다.
    const selectedBank = ref(''); // 선택된 은행을 저장하는 변수입니다.

    const getProducts = () => {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/v1/deposit-saving-products/'
      }).then((response) => {
        products.value = response.data;
        response.data.forEach(product => {
          getOptions(product.fin_prdt_cd);
          if (!bankList.value.includes(product.kor_co_nm)){
            bankList.value.push(product.kor_co_nm)
          }
        });
        console.log(bankList.value)
        // 은행 목록을 가져온 후에 전체 상품을 필터링합니다.
        filterProducts();
      }).catch((error) => {
        console.log(error);
      });
    }

    const getOptions = (productCode) => {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/saving-product-options/${productCode}`
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

    const filterProducts = () => {
      if (!selectedBank.value) {
        filteredProducts.value = [...products.value]; // 선택된 은행이 없으면 전체 상품을 표시합니다.
      } else {
        filteredProducts.value = products.value.filter(product => product.kor_co_nm === selectedBank.value); // 선택된 은행에 따라 상품을 필터링합니다.
      }
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
      goToDetail,
      filterProducts,
      filteredProducts,
      bankList,
      selectedBank
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
  border: 1px solid #d6a5a5;
  padding: 8px;
  text-align: center;
}

.product-table th {
  background-color: #ffddbd;
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

h2 {    
  padding-top: 10px;
  padding-bottom: 5px;
  /* font-family: 'WavvePADO-Regular'; */
  font-family: 'GongGothicMedium';
}

@font-face {
    font-family: 'WavvePADO-Regular';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

@font-face {
    font-family: 'GongGothicMedium';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10@1.0/GongGothicMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>
