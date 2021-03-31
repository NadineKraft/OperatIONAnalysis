<template>
  <div>
    <div v-if="analyses && analyses.length">
      <div
        class="card mb-3"
        style="width: 75%"
        v-for="analysis of analyses"
        v-bind:key="analysis.id"
      >
        <div class="row no-gutters">
          <div class="col-md-4">
            <img
              src="../../assets/genetic.svg"
              class="card-img-top"
              alt="..."
            />

            <title>{{ analysis.name }}</title>
            <rect width="100%" height="100%" fill="#55595c" />
          </div>

          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">
                {{ analysis.name }} (ID: {{ analysis.id }})
              </h5>
              <p class="card-text">
                Experiment ID: {{ analysis.experiment_id }}
              </p>
              <p v-if="analysis.methylation_analysis" class="card-text">
                Methylation Analysis
              </p>
              <p
                v-if="analysis.copy_number_variation_analysis"
                class="card-text"
              >
                Copy Number Variation Analysis
              </p>
              <p v-if="analysis.status_parameter_analysis" class="card-text">
                Status Parameter Analysis
              </p>
              <p class="card-text">
                Prefix:
                {{ analysis.prefix }}
              </p>
              <p class="card-text">Analysis Status: {{ analysis.status }}</p>

              <button
                class="btn btn-success btn-sm ml-1"
                @click="runAnalysis(analysis)"
              >
                Start Analysis
              </button>
              <button
                class="btn btn-danger btn-sm ml-1"
                @click="deleteAnalysis(analysis.id)"
              >
                Delete
              </button>
              <router-link
                :to="{
                  name: 'Visualization',
                  params: { id: analysis.id, name: analysis.prefix },
                }"
                class="btn btn-sm btn-primary"
                >Show visualization
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import getAnalysesList from "@/services/getAnalysesList";
import runAnalysis from "@/services/runAnalysis";
import deleteAnalysis from "@/services/deleteAnalysis";

export default {
  name: "List",
  data() {
    return {
      analyses: [],
      id: 0,
      name: "",
    };
  },
  methods: {
    getData: async function () {
      this.loading = false;
      this.analyses = await getAnalysesList();
    },
    deleteAnalysis: async function (id) {
      await deleteAnalysis(id);
      await this.getData();
    },
    runAnalysis: async function (analysis) {
      await runAnalysis(analysis);
      await this.getData();
      this.$forceUpdate();
    },
  },
  created() {
    (this.name = this.$route.params.name), (this.id = this.$route.params.id);
    this.getData();
  },
};
</script>

<style scoped></style>
