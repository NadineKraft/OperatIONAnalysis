<template>
  <div>
    <p class="card-text">Config ID: {{ id }}</p>
    <div class="form-group">
      <label for="name">Config Name</label>
      <input
        type="text"
        class="form-control"
        id="name"
        v-model="config.name"
        v-validate="'required'"
        name="name"
        placeholder="Enter name"
      />
      <div class="invalid-feedback">Please provide a valid name.</div>
    </div>

    <div class="form-group">
      <label for="basecaller">Basecaller</label>
      <select id="basecaller" v-model="config.basecaller">
        <option disabled value="">Please select a Basecaller</option>
        <option>Megalodon</option>
        <option>Guppy</option>
      </select>
    </div>

    <div class="form-group">
      <label for="methylationcaller">Methylationcaller :</label>
      <select id="methylationcaller" v-model="config.methylationcaller">
        <option disabled value="">Please select one</option>
        <option>Megalodon</option>
        <option>ngmlr</option>
      </select>
    </div>
    <div class="form-group">
      <label for="aligner">Aligner :</label>
      <select id="aligner" v-model="config.aligner">
        <option disabled value="">Please select one</option>
        <option>Megalodon</option>
        <option>nanopolish</option>
      </select>
    </div>

    <div class="form-group">
      <label for="megalodon_output_directory">Megalodon output directory</label>
      <input
        type="text"
        class="form-control"
        id="megalodon_output_directory"
        v-model="config.megalodon_output_directory"
        v-validate="'required'"
        name="megalodon_output_directory"
        placeholder="Enter path to megalodon output directory"
      />
      <div class="invalid-feedback">Please provide a valid path.</div>
    </div>

        <div class="form-group">
      <label for="megalodon_parameters">Megalodon Parameters</label>
      <input
        type="text"
        class="form-control"
        id="megalodon_parameters"
        v-model="config.megalodon_parameters"
        v-validate="'required'"
        name="megalodon_parameters"
        placeholder="Enter additional megalodon parameters"
      />
      <div class="invalid-feedback">Please provide parameters.</div>
    </div>

        <div class="form-group">
      <label for="megalodon_processes">Megalodon processes</label>
      <input
        type="text"
        class="form-control"
        id="megalodon_processes"
        v-model="config.megalodon_processes"
        v-validate="'required'"
        name="megalodon_processes"
        placeholder="Enter megalodon processes"
      />
      <div class="invalid-feedback">Please provide valid parameters.</div>
    </div>

    <div class="form-group">
      <label for="megalodon_devices">Megalodon devices</label>
      <input
        type="text"
        class="form-control"
        id="megalodon_devices"
        v-model="config.megalodon_devices"
        v-validate="'required'"
        name="megalodon_devices"
        placeholder="Enter megalodon devices"
      />
      <div class="invalid-feedback">Please provide valid parameters.</div>
    </div>


    <div class="form-group">
      <label for="fasta_reference_directory"> Fasta Reference</label>
      <input
        type="text"
        class="form-control"
        id="fasta_reference_directory"
        v-model="config.fasta_reference_directory"
        v-validate="'required'"
        name="fasta_reference_directory"
        placeholder="Enter path to fasta reference directory"
      />
      <div class="invalid-feedback">Please provide valid parameters.</div>
    </div>

    <div class="form-group">
      <label for="guppy_config"> Guppy Config</label>
      <input
        type="text"
        class="form-control"
        id="guppy_config"
        v-model="config.guppy_config"
        v-validate="'required'"
        name="guppy_config"
        placeholder="Enter path to guppy config"
      />
      <div class="invalid-feedback">Please provide valid parameters.</div>
    </div>

    <div class="form-group">
      <label for="guppy_server_path">Guppy server path</label>
      <input
        type="text"
        class="form-control"
        id="guppy_server_path"
        v-model="config.guppy_server_path"
        v-validate="'required'"
        name="guppy_server_path"
        placeholder="Enter path to guppy server path"
      />
      <div class="invalid-feedback">Please provide valid parameters.</div>
    </div>

    <div class="form-group">
      <label for="guppy_params">Guppy params</label>
      <input
        type="text"
        class="form-control"
        id="guppy_params"
        v-model="config.guppy_params"
        v-validate="'required'"
        name="guppy_params"
        placeholder="Enter guppy params"
      />
      <div class="invalid-feedback">Please provide valid parameters.</div>
    </div>




    <div class="form-group">
      <label for="status_parameter_input_directory"
        >Status Parameter Input Directory</label
      >
      <input
        type="text"
        class="form-control"
        id="status_parameter_input_directory"
        v-model="config.status_parameter_input_directory"
        name="status_parameter_input_directory"
        placeholder="Enter path to status parameter input directory containing sequencing summary_file"
      />
      <div class="invalid-feedback">Please provide valid parameters.</div>
    </div>

    <div class="form-group">
      <label for="cnv_input_directory"
        >Copy Number Variation Input Directory</label
      >
      <input
        type="text"
        class="form-control"
        id="cnv_input_directory"
        v-model="config.cnv_input_directory"
        v-validate="'required'"
        name="cnv_input_directory"
        placeholder="Enter path to cnv input directory"
      />
      <div class="invalid-feedback">Please provide valid parameters.</div>
    </div>

    <button type="submit" @click="editConfig()" class="btn btn-primary">
      Submit
    </button>


  </div>

</template>

<script>
import editConfig from "@/services/editConfig";
import axios from "axios";

export default {
  name: "EditForm",
  data() {
    return {
      config: {
        name: "",
        basecaller: "",
        megalodon_output_directory: "",
        megalodon_parameters: "",
        fasta_reference_directory: "",
        guppy_config: "",
        guppy_server_path: "",
        guppy_params: "",
        megalodon_devices: "",
        megalodon_processes: "",
        methylationcaller: "",
        aligner: "",
        status_parameter_input_directory: "",
        cnv_input_directory: ""
      }
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/configs/" + this.$route.params.id)
      .then(response => {
        console.log(response.data);
        this.config = response.data;
      });
  },
  methods: {
    async editConfig() {
      await editConfig(this.config);
      await this.$router.push("/configs-list");
    }
  },
  created() {
    this.id = this.$route.params.id;
    this.getData();
  }
};
</script>

<style scoped></style>
