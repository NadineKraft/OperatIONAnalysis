<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <b-nav tabs type="dark" align="center">
        <b-nav-item disabled
          >Visualization for Analysis: {{ this.name }}</b-nav-item
        >
        <b-nav-item
          class="app-nav-link"
          :to="{
            name: 'VisualizationStatusParameter',
            params: { id: this.id, name: this.name },
          }"
          >Status Parameter
        </b-nav-item>
        <b-nav-item
          class="app-nav-link"
          :to="{
            name: 'VisualizationMethylation',
            params: { id: this.id, name: this.name },
          }"
          >Methylation
        </b-nav-item>
        <b-nav-item
          class="app-nav-link"
          :to="{
            name: 'VisualizationCopyNumberVariation',
            params: { id: this.id, name: this.name },
          }"
          >Copy number variation
        </b-nav-item>
      </b-nav>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Nav",
  data() {
    return {
      id: 0,
      name: "",
    };
  },
  created() {
    this.name = this.$route.params.name;
    this.id = this.$route.params.id;
  },
};
</script>

<style scoped></style>
