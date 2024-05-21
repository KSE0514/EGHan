<template>
  <div>
    <div>
      <label for="toCurrency">To:</label>
      <select v-model="toCurrency" id="toCurrency" @change="convertToFrom">
        <option v-for="currency in currencies" :key="currency.cur_unit" :value="currency.cur_unit">
          {{ currency.cur_nm }} ({{ currency.cur_unit }})
        </option>
      </select>
      <input type="number" v-model.number="toAmount" step="0.01" @input="convertToFrom" />
    </div>
    <div>
      <label for="fromCurrency">From:</label>
      <select v-model="fromCurrency" id="fromCurrency" @change="convertFromTo">
        <option v-for="currency in currencies" :key="currency.cur_unit" :value="currency.cur_unit">
          {{ currency.cur_nm }} ({{ currency.cur_unit }})
        </option>
      </select>
      <input type="number" v-model.number="fromAmount" step="0.01" @input="convertFromTo" />
    </div>

    <div>
      <p v-if="exchangeRate !== null">1 {{ fromCurrency }} = {{ exchangeRate }} {{ toCurrency }}</p>
      <p v-else style="color: red;">환율 정보를 가져올 수 없습니다.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      fromCurrency: 'USD',
      toCurrency: 'KRW',
      fromAmount: 0,
      toAmount: 0,
      currencies: [],
      exchangeRates: {},
      exchangeRate: null,  // 환율 저장
    };
  },
  methods: {
    async fetchExchangeRates() {
      console.log('fetchExchangeRates 호출됨');
      try {
        const response = await axios.get('http://localhost:8000/api/v1/exchange/');
        console.log('API 호출 성공');
        const data = response.data;
        console.log('API 응답 데이터 타입:', typeof data); // 응답 데이터 타입 로그 추가
        console.log('API 응답 데이터 길이:', Array.isArray(data) ? data.length : 'N/A'); // 응답 데이터 길이 로그 추가
        console.log('API 응답 데이터:', JSON.stringify(data, null, 2)); // 응답 데이터 상세 로그 추가
        
        // 데이터가 배열인지 확인 후 처리
        if (Array.isArray(data) && data.length > 0) {
          this.currencies = data;  // 응답 데이터를 currencies 배열에 저장
          data.forEach(rate => {
            this.exchangeRates[rate.cur_unit] = parseFloat(rate.deal_bas_r.replace(',', ''));
          });
          console.log('환율 데이터:', this.exchangeRates); // 콘솔 로그 추가
          this.convertFromTo(); // 초기 변환 수행
        } else {
          console.error('API 응답 데이터가 비어 있거나 유효하지 않습니다.');
        }
      } catch (error) {
        console.error('Error fetching exchange rates:', error);
      }
    },
    convertFromTo() {
      const fromRate = this.exchangeRates[this.fromCurrency];
      const toRate = this.exchangeRates[this.toCurrency];
      console.log('From rate:', fromRate); // 콘솔 로그 추가
      console.log('To rate:', toRate); // 콘솔 로그 추가
      if (fromRate && toRate) {
        if (this.fromCurrency === 'KRW') {
          this.toAmount = (this.fromAmount / toRate).toFixed(2);
          this.exchangeRate = (1 / toRate).toFixed(2);
        } else if (this.toCurrency === 'KRW') {
          this.toAmount = (this.fromAmount * fromRate).toFixed(2);
          this.exchangeRate = fromRate.toFixed(2);
        } else {
          this.toAmount = ((this.fromAmount * fromRate) / toRate).toFixed(2);
          this.exchangeRate = (fromRate / toRate).toFixed(2);
        }
      } else {
        this.toAmount = '환율 정보를 가져올 수 없습니다.';
        this.exchangeRate = null;
      }
      console.log('계산 결과:', this.toAmount); // 콘솔 로그 추가
    },
    convertToFrom() {
      const fromRate = this.exchangeRates[this.fromCurrency];
      const toRate = this.exchangeRates[this.toCurrency];
      console.log('From rate:', fromRate); // 콘솔 로그 추가
      console.log('To rate:', toRate); // 콘솔 로그 추가
      if (fromRate && toRate) {
        if (this.fromCurrency === 'KRW') {
          this.fromAmount = (this.toAmount * toRate).toFixed(2);
          this.exchangeRate = (1 / toRate).toFixed(2);
        } else if (this.toCurrency === 'KRW') {
          this.fromAmount = (this.toAmount / fromRate).toFixed(2);
          this.exchangeRate = fromRate.toFixed(2);
        } else {
          this.fromAmount = ((this.toAmount * toRate) / fromRate).toFixed(2);
          this.exchangeRate = (fromRate / toRate).toFixed(2);
        }
      } else {
        this.fromAmount = '환율 정보를 가져올 수 없습니다.';
        this.exchangeRate = null;
      }
      console.log('계산 결과:', this.fromAmount); // 콘솔 로그 추가
    },
  },
  mounted() {
    console.log('mounted hook 호출됨');
    this.fetchExchangeRates();
  },
  watch: {
    fromCurrency(newVal, oldVal) {
      this.convertFromTo();
    },
    toCurrency(newVal, oldVal) {
      this.convertFromTo();
    },
  }
};
</script>

<style scoped>
/* 스타일 정의 */
</style>
