<template>
  <div>
    <h1>UserInfo</h1>
  </div>
  <UserInfoView />
  <hr>
  <Recommend />
</template>

<script setup>
import UserInfoView from '@/components/UserInfo.vue'
import Recommend from '@/components/Recommend.vue';
</script>

<style scoped>
h1 {
font-family: 'WavvePADO-Regular';
text-align: center;
}

@font-face {
  font-family: 'WavvePADO-Regular';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/WavvePADO-Regular.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}

</style>