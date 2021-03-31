<template>
  <div><Nav></Nav><List></List></div>
</template>

<script>
import List from "@/components/configs-list/List";
import Nav from "@/components/configs-list/Nav";

export default {
  name: "ConfigsList",
  components: {
    Nav,
    List,
  },
};
</script>

<style scoped></style>
