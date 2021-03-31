<template>
  <div>
    <Nav></Nav>
    <div class="card mb-4" style="width: 100%">
      <div class="row no-gutters">
        <div class="col-md-4">
          <img src="../assets/infographic.png" class="card-img-top" alt="..." />

          <title>Visualization</title>
          <rect width="100%" height="100%" fill="#55595c" />
        </div>

        <div class="col-md-8">
          <div class="card-body">
            <h4 class="card-title">Visualization</h4>
            <p class="card-text">
              Select the visualization you want to see for the analysis:
              {{ this.name }} from the navigation bar
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Nav from "@/components/visualization/Nav";
export default {
  name: "Visualization",
  components: { Nav },
  data() {
    return {
      id: 0,
      name: "",
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.name = this.$route.params.name;
  },
};
</script>

<style scoped></style>
