import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      redirect: "/home",
    },
    {
      path: "/home",
      name: "Home",
      component: () => import("./views/Home.vue"),
    },
    {
      path: "/experiment-detail",
      name: "ExperimentDetail",
      component: () => import("./views/ExperimentDetail.vue"),
    },
    {
      path: "/experiments-list",
      name: "ExperimentsList",
      component: () => import("./views/ExperimentsList.vue"),
    },
    {
      path: "/configs-list",
      name: "ConfigsList",
      component: () => import("./views/ConfigsList.vue"),
    },
    {
      path: "/config-edit",
      name: "ConfigEdit",
      component: () => import("./views/ConfigEdit.vue"),
    },
    {
      path: "/config-detail",
      name: "ConfigDetail",
      component: () => import("./views/ConfigDetail.vue"),
    },
    {
      path: "/analysis-list",
      name: "AnalysisList",
      component: () => import("./views/AnalysisList.vue"),
    },
    {
      path: "/analysis-detail/:id",
      name: "AnalysisDetail",
      component: () => import("./views/AnalysisDetail.vue"),
    },
    {
      path: "/visualization",
      name: "Visualization",
      component: () => import("./views/Visualization"),
    },
    {
      path: "/visualization/copy-number-variation-list",
      name: "VisualizationCopyNumberVariation",
      component: () => import("./views/CopyNumberVariationList"),
    },
    {
      path: "/visualization/methylation-list",
      name: "VisualizationMethylation",
      component: () => import("./views/MethylationList"),
    },
    {
      path: "/visualization/status-parameter-list",
      name: "VisualizationStatusParameter",
      component: () => import("./views/StatusParameterList"),
    },
  ],
});
