<template>
  <div class="jumbotron">
    <h1>Select a config for your experiments</h1>
    <router-link to="/add_config" class="btn btn-group-lg btn-secondary">Add Config</router-link>
    <div v-if="confis && confis.length">

      <div class="card mb-3" v-for="confi of confis" v-bind:key="confi.id">
        <div class="card-body">
          <h5 class="card-title"> Name: {{ confi.name }}</h5>
          <p class="card-title"> Basecaller: {{ confi.basecaller }}</p>
          <p class="card-text">Methylationcaller: {{ confi.methylation_caller }}</p>
          <p class="card-text">Aligner: {{ confi.aligner }}</p>
          <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteConfig(confi)">Delete</button>
        </div>
      </div>
    </div>
    <p v-if="confis.length == 0">No Configs</p>
  </div>


</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      confis: []
    }
  },
  created() {
    this.all();
  },
  methods: {
    deleteConfig: function (confi) {
      if (confirm('Delete ' + confi.name)) {
        axios.delete(`http://127.0.0.1:8000/api/configs/${confi.id}`)
            .then(response => {
              this.all();
            });
      }
    },
    all: function () {
      axios.get('http://127.0.0.1:8000/api/configs/')
          .then(response => {
            this.confis = response.data
          });
    }
  },
}
</script>
