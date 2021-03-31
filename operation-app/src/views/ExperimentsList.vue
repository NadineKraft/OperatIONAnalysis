<template>
  <div><Nav></Nav><List></List></div>
</template>

<script>
import Nav from "@/components/experiments-list/Nav";
import List from "@/components/experiments-list/List";

export default {
  name: "ExperimentsList",
  components: {
    Nav,
    List,
  },
};
</script>

<style scoped></style>
