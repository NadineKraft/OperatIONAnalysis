<template>
  <div class="nav-bar">
    <b-nav tabs type="dark" align="left">
      <b-nav-item class="app-nav-link" :to="{ name: 'Home' }"
        >OperatION-Analysis
      </b-nav-item>
      <b-nav-item class="app-nav-link" :to="{ name: 'ConfigsList' }"
        >Select Config
      </b-nav-item>
      <b-nav-item class="app-nav-link" :to="{ name: 'ExperimentsList' }"
        >Manage Experiments
      </b-nav-item>
      <b-nav-item class="app-nav-link" :to="{ name: 'AnalysisList' }"
        >Analyse Experiment
      </b-nav-item>
    </b-nav>
  </div>
</template>

<script>
export default {
  name: "Header.vue",
};
</script>

<style scoped></style>
