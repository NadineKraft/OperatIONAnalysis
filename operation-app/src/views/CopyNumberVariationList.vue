<template>
  <div>
    <Nav></Nav>
    <CNVList></CNVList>
  </div>
</template>

<script>
import CNVList from "@/components/visualization/CNVList";
import Nav from "@/components/visualization/Nav";

export default {
  name: "CopyNumberVariationList",
  components: {
    CNVList,
    Nav,
  },
};
</script>

<style scoped></style>
