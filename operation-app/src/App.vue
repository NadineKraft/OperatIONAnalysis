<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <Header></Header>
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import Header from "@/components/shared/Header";
export default {
  components: {
    Header,
  },
};
</script>

<style scoped>
.container {
  width: 1920px;
  max-width: 1920px;
}
</style>
