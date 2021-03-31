<template>
  <div>
    <Nav></Nav>
    <SPList></SPList>
  </div>
</template>

<script>
import SPList from "@/components/visualization/SPList";
import Nav from "@/components/visualization/Nav";

export default {
  name: "StatusParameterList",
  components: {
    Nav,
    SPList,
  },
};
</script>

<style scoped></style>
