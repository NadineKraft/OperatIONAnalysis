<template>
  <div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">Select Analysis Parmaters for:</h5>
        <p class="card-text">Experiment Name: {{ name }}</p>
        <p class="card-text">Experiment ID: {{ id }}</p>
      </div>
      <form @submit="checkForm" @submit.prevent="create" method="post">
        <div v-if="errors.length">
          <b>Please correct the following error(s):</b>
          <ul>
            <li v-for="error in errors" :key="error">{{ error }}</li>
          </ul>
        </div>
        <div class="form-group">
          <label for="name">Name</label>
          <input
            type="text"
            class="form-control"
            id="name"
            v-model="analysis.name"
            v-validate="'required'"
            name="name"
            placeholder="Enter name"
          />
        </div>
        <div class="form-group">
          <label for="analysis.prefix">Prefix</label>
          <input
            type="text"
            class="form-control"
            id="analysis.prefix"
            v-model="analysis.prefix"
            v-validate="'required'"
            name="prefix"
            placeholder="Enter prefix"
          />
        </div>

        <div class="form-group">
          <input
            type="checkbox"
            id="analysis.methylation_analysis"
            value="False"
            v-model="analysis.methylation_analysis"
          />
          <label for="analysis.methylation_analysis"
            >Methylation Analysis</label
          >
        </div>

        <div class="form-group">
          <input
            type="checkbox"
            id="analysis.copy_number_variation_analysis"
            value="False"
            v-model="analysis.copy_number_variation_analysis"
          />
          <label for="analysis.copy_number_variation_analysis"
            >copy number variation alysis</label
          >
        </div>

        <div class="form-group">
          <input
            type="checkbox"
            id="analysis.status_parameter_analysis"
            value="False"
            v-model="analysis.status_parameter_analysis"
          />
          <label for="analysis.status_parameter_analysis"
            >status parameter analysis</label
          >
        </div>
        <button type="submit" @click="addAnalysis()" class="btn btn-primary">
          Submit
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import addAnalysis from "@/services/addAnalysis.js";

export default {
  name: "AddForm",
  data() {
    return {
      analysis: {
        name: "",
        status: "INITIATED",
        prefix: "",
        methylation_analysis: false,
        copy_number_variation_analysis: false,
        status_parameter_analysis: false,
        experiment_id: this.$route.params.id,
      },
      id: 0,
      name: "",
      errors: [],
    };
  },
  methods: {
    async addAnalysis() {
      await addAnalysis(this.analysis);
      await this.$router.push({
        name: "AnalysisList",
        params: { id: this.id, name: this.name },
      });
    },
    checkForm: function (e) {
      if (this.analysis.name && this.analysis.prefix) {
        return true;
      }
      this.errors = [];
      if (!this.analysis.name) {
        this.errors.push("Name required");
      }
      if (!this.analysis.prefix) {
        this.errors.push("Prefix required");
      }
      e.preventDefault();
    },
  },
  created() {
    (this.name = this.$route.params.name),
      (this.id = this.$route.params.id),
      this.getData();
  },
};
</script>

<style scoped></style>
