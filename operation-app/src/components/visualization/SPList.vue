<template>
  <div>
    <div id="wropper">
      <iframe
        name="iframe1"
        id="iframe1"
        :src="this.iframeSrc"
        frameborder="0"
        border="0"
        cellspacing="0"
        style="position: absolute; width: 100%; height: 500pt; border: none"
      ></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: "SPList",
  data() {
    return {
      id: 0,
      name: "",
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.name = this.$route.params.name;
    this.route = "http://localhost:8080/results/";
    this.sp_result = this.route.concat(this.name, "_sequencing_result.html");
    this.iframeSrc = this.sp_result;
  },
};
</script>

<style scoped>
#wropper {
  position: relative;
  width: 100%;
  height: 100%;
}
</style>
