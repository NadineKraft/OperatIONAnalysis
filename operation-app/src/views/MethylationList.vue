<template>
  <div>
    <Nav></Nav>
    <MList></MList>
  </div>
</template>

<script>
import MList from "@/components/visualization/MList";
import Nav from "@/components/visualization/Nav";

export default {
  name: "MethylationList",
  components: {
    MList,
    Nav,
  },
};
</script>

<style scoped></style>
