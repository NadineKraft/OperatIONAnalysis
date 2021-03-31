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
  name: "CNVList",
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
    this.cnv_result = this.route.concat(
      this.name,
      "_Segment_CNV_calling_results.html"
    );
    this.iframeSrc = this.cnv_result;
    //"http://localhost:8080/results/GBM32_New_Segment_CNV_calling_results_GBM32.html";
    //this.getData();
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
