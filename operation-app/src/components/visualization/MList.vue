<template>
  <div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Number of reads</th>
          <th scope="col">Number of CpGs</th>
          <th scope="col">Possible classes</th>
          <th scope="col">Class name</th>
          <th scope="col">Class probability</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.number_reads }}</td>
          <td>{{ item.number_cpgs }}</td>
          <td>{{ item.possible_classes }}</td>
          <td>{{ item.class_name }}</td>
          <td>{{ item.class_probability }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "MList",
  data: () => ({
    id: 0,
    name: "",
    items: [
      {
        number_reads: "int value",
        number_cpgs: "int value",
        possible_classes: "class 1, class 2, class 3",
        class_name: "class name",
        class_probability: "float value",
      },
    ], // initialise to an empty array
  }),
  methods: {
    async myMethod() {
      //const res = await fetch('/Contr/Get')
      //if (!res.ok) {
      //  throw res
      //}
      //this.items = await res.json(); // assign the response array to "items"
    },
  },

  created() {
    this.id = this.$route.params.id;
    this.name = this.$route.params.name;

    //this.getData();
  },
};
</script>

<style scoped>
#wropper {
  position: relative;
  width: 100%;
  height: 100%;
}
</style>
