<template>
  <div>
    <div v-if="experiments && experiments.length">
      <div
        class="card mb-3"
        style="width: 75%"
        v-for="experiment of experiments"
        v-bind:key="experiment.id"
      >
        <div class="row no-gutters">
          <div class="col-md-4">
            <img
              src="../../assets/analysis.png"
              class="card-img-top"
              alt="..."
            />

            <title>{{ experiment.name }}</title>
            <rect width="100%" height="100%" fill="#55595c" />
          </div>

          <div class="col-md-8">
            <div class="card-body">
              <h5 class="card-title">{{ experiment.name }}</h5>
              <p class="card-text">
                Experiment ID: {{ experiment.id }}, Config ID:
                {{ experiment.config_id }}
              </p>
              <p class="card-text">Parameters:</p>
              <p v-if="experiment.live_processing" class="card-text">
                Live Processing
              </p>
              <p v-if="experiment.basecalling" class="card-text">Basecalling</p>
              <p v-if="experiment.methylation_calling" class="card-text">
                Methylationcalling
              </p>
              <p v-if="experiment.alignment" class="card-text">Alignment</p>
              <p class="card-text">Processed: {{ experiment.processed }}</p>
              <button
                class="btn btn-danger btn-sm ml-1"
                @click="deleteExperiment(experiment.id)"
              >
                Delete
              </button>
              <button
                class="btn btn-success btn-sm ml-1"
                @click="runProcessing(experiment)"
              >
                Start Processing
              </button>
              <router-link
                :to="{
                  name: 'AnalysisDetail',
                  params: { id: experiment.id, name: experiment.name },
                }"
                class="btn btn-sm btn-primary"
                >Select Analysis Parameter
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="loading">loading experiments...</div>
  </div>
</template>

<script>
import getExperimentsList from "@/services/getExperimentsList";
import deleteExperiment from "@/services/deleteExperiment";
import runProcessing from "../../services/runProcessing";
export default {
  name: "List",
  data() {
    return {
      experiments: [],
      loading: false,
    };
  },
  methods: {
    getData: async function () {
      this.loading = false;
      this.experiments = await getExperimentsList();
    },
    startLoading: function () {
      this.loading = true;
    },
    deleteExperiment: async function (id) {
      await deleteExperiment(id);
      // this.startLoading();
      await this.getData();
    },

    runProcessing: async function (experiment) {
      await runProcessing(experiment);
      // this.startLoading();
      await this.getData();
      this.$forceUpdate();
    },
  },
  created() {
    // this.startLoading();
    this.getData();
  },
};
</script>

<style scoped></style>
