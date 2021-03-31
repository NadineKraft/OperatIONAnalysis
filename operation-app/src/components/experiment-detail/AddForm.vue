<template>
  <div class="pt-5">
    <div class="card-body">
      <h5 class="card-title">Select Experiment parameters for:</h5>
      <p class="card-text">Config ID: {{ id }}</p>
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
          v-model="experiment.name"
          v-validate="'required'"
          name="name"
          placeholder="Enter name"
        />
        <div class="invalid-feedback">Please provide a valid name.</div>
      </div>
      <div class="form-group">
        <input
          type="checkbox"
          id="experiment.live_processing"
          value="True"
          v-model="experiment.live_processing"
        />
        <label for="experiment.live_processing"
          >Live Processing (only available for Megalodon)</label
        >
      </div>
      <div class="form-group">
        <input
          type="checkbox"
          id="experiment.basecalling"
          value="False"
          v-model="experiment.basecalling"
        />
        <label for="experiment.basecalling">Basecalling</label>
      </div>

      <div class="form-group">
        <input
          type="checkbox"
          id="experiment.methylation_calling"
          value="False"
          v-model="experiment.methylation_calling"
        />
        <label for="experiment.methylation_calling">Methylationcalling</label>
      </div>
      <div class="form-group">
        <input
          type="checkbox"
          id="experiment.alignment"
          value="False"
          v-model="experiment.alignment"
        />
        <label for="experiment.alignment">Alignment</label>
      </div>
      <div class="form-group">
        <label for="name">Fast 5 Directory</label>
        <input
          type="text"
          class="form-control"
          id="fast5_dir"
          v-model="experiment.fast5_dir"
          v-validate="'required'"
          name="name"
          placeholder="Enter absolute path to FAST5 Directory"
        />
        <div class="invalid-feedback">
          Please provide a valid directory path.
        </div>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea
          name="description"
          class="form-control"
          id="description"
          v-validate="'required'"
          v-model="experiment.description"
          cols="30"
          rows="2"
        ></textarea>
        <div class="invalid-feedback">Please provide a valid description.</div>
      </div>

      <button type="submit" @click="addExperiment()" class="btn btn-primary">
        Submit
      </button>
    </form>
  </div>
</template>

<script>
import addExperiment from "@/services/addExperiment";

export default {
  name: "AddForm",
  data() {
    return {
      experiment: {
        name: "",
        live_processing: true,
        basecalling: false,
        methylation_calling: false,
        alignment: false,
        fast5_dir: "",
        processed: "INITIATED",
        config_id: this.$route.params.id,
        description: "",
      },
      id: 0,
      errors: [],
    };
  },
  methods: {
    async addExperiment() {
      await addExperiment(this.experiment);
      await this.$router.push("/experiments-list");
    },
    checkForm: function (e) {
      if (
        this.experiment.name &&
        this.experiment.fast5_dir &&
        this.experiment.description
      ) {
        return true;
      }
      this.errors = [];
      if (!this.experiment.name) {
        this.errors.push("Name required");
      }
      if (!this.experiment.fast5_dir) {
        this.errors.push("Fast5 Directory required");
      }
      if (!this.experiment.description) {
        this.errors.push("Description required");
      }
      if (this.experiment.alignment && !this.experiment.basecalling) {
        this.errors.push("Please check also basecalling or Methylationcalling");
      }
      e.preventDefault();
    },
  },
  created() {
    (this.name = this.$route.params.name), (this.id = this.$route.params.id);
    this.getData();
  },
};
</script>

<style scoped></style>
