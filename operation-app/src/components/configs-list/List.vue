<template>
  <div>
    <div v-if="configs && configs.length">
      <div class="card mb-3" v-for="config of configs" v-bind:key="config.id">
        <div class="card-body">
          <h5 class="card-title">
            Name: {{ config.name }} ID: {{ config.id }}
          </h5>
          <p class="card-title">Basecaller: {{ config.basecaller }}</p>
          <p class="card-text">Methylationcaller: {{ config.methylationcaller }}</p>
          <p class="card-text">Aligner: {{ config.aligner }}</p>
          <p class="card-text">
            Megalodon Output Directory: {{ config.megalodon_output_directory }}
          </p>
          <p class="card-text">
            Megalodon Devices: {{ config.megalodon_devices }}
          </p>
          <p class="card-text">
            Megalodon Processes: {{ config.megalodon_processes }}
          </p>

          <p class="card-text">
            Megalodon Parameters: {{ config.megalodon_parameters }}
          </p>
          <p class="card-text">
            Fasta Reference Directory: {{ config.fasta_reference_directory }}
          </p>
          <p class="card-text">Guppy Config: {{ config.guppy_config }}</p>
          <p class="card-text">
            Guppy Server Path: {{ config.guppy_server_path }}
          </p>
          <p class="card-text">Guppy Parameters {{ config.guppy_params }}</p>


          <p class="card-text">
            Status Parameter Input Directory:
            {{ config.status_parameter_input_directory }}
          </p>

          <p class="card-text">
            Copy Number Variation Input Directory: {{ config.cnv_input_directory }}
          </p>
          <button
            class="btn btn-danger btn-sm ml-1"
            @click="deleteConfig(config.id)"
          >
            Delete
          </button>
          <router-link
            :to="{
              name: 'ExperimentDetail',
              params: { id: config.id },
            }"
            class="btn btn-sm btn-primary"
            >Select Experiment
          </router-link>
          <router-link
            :to="{
              name: 'ConfigEdit',
              params: { id: config.id },
            }"
            class="btn btn-sm btn-secondary"
            >Edit Config
          </router-link>
        </div>
      </div>
    </div>
    <div v-if="loading">loading configs...</div>
  </div>
</template>

<script>
import getConfigsList from "@/services/getConfigsList";
import deleteConfig from "@/services/deleteConfig";
export default {
  name: "List",
  data() {
    return {
      configs: [],
      id: 0,
      loading: false,
    };
  },
  methods: {
    getData: async function () {
      this.loading = false;
      this.configs = await getConfigsList();
    },
    startLoading: function () {
      this.loading = true;
    },
    deleteConfig: async function (id) {
      await deleteConfig(id);
      // this.startLoading();
      await this.getData();
    },
  },
  computed() {
    this.loading = true;
  },
  created() {
    // this.startLoading();
    this.getData();
  },
};
</script>

<style scoped></style>
