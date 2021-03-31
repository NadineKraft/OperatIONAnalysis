<template>
  <div class="pt-5">
    <form @submit.prevent="create" method="post">
      <div class="form-group">
        <label for="name">Name</label>
        <input
          type="text"
          class="form-control"
          id="name"
          v-model="confi.name"
          v-validate="'required'"
          name="name"
          placeholder="Enter name"
          :class="{
            'is-invalid': errors.has('confi.name') && submitted
          }"
        />
        <div class="invalid-feedback">
          Please provide a valid name.
        </div>
      </div>

      <div class="form-group">
        <label for="confi.basecaller">Basecaller</label>
        <select v-model="confi.basecaller">
          <option disabled value="">Please select one</option>
          <option>Megalodon</option>
          <option>Guppy</option>
        </select>
      </div>
      <div class="form-group">

        <label for="confi.methylation_caller">Methylationcaller</label>
        <select v-model="confi.methylation_caller">
          <option disabled value="">Please select one</option>
          <option>Megalodon</option>
          <option>ngmlr</option>
        </select>
      </div>
      <div class="form-group">
        <label for="confi.aligner">Aligner</label>
        <select v-model="confi.aligner">
          <option disabled value="">Please select one</option>
          <option>Megalodon</option>
          <option>nanopolish</option>
        </select>
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      confi: {
        name: "",
        basecaller: "",
        methylation_caller: "",
        aligner: "",
      },
      submitted: false
    };
  },
  methods: {
    create: function (e) {
      this.$validator.validate().then(result => {
        this.submitted = true;
        if (!result) {
          return;
        }
        console.log(this.name);
        axios
            .post("http://127.0.0.1:8000/api/configs/", this.confi)
            .then(response => {
              this.$router.push("/config");
            });
      });
    }
  }
};
</script>
