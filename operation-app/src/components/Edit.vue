<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
            <div class="form-group">
        <label for="name">Name</label>
        <input
            type="text"
            class="form-control"
            id="name"
            v-model="subscription.name"
            v-validate="'required'"
            name="name"
            placeholder="Enter name"
            :class="{'is-invalid': errors.has('subscription.name') && submitted}">
        <div class="invalid-feedback">
          Please provide a valid name.
        </div>
      </div>
      <div class="form-group">
        <input
          type="checkbox"
          id="subscription.live_processing"
          value="True"
          v-model="subscription.live_processing"
        />
        <label for="subscription.live_processing">Live Processing</label>
      </div>
      <div class="form-group">
        <input
          type="checkbox"
          id="subscription.basecalling"
          value="False"
          v-model="subscription.basecalling"
        />
        <label for="subscription.basecalling">Basecalling</label>
      </div>

      <div class="form-group">
        <input
          type="checkbox"
          id="subscription.methylation_calling"
          v-model="subscription.methylation_calling"
        />
        <label for="subscription.methylation_calling">Methylationcalling</label>
      </div>
      <div class="form-group">
        <input
          type="checkbox"
          id="subscription.alignment"
          v-model="subscription.alignment"
        />
        <label for="subscription.alignment">Alignment</label>
      </div>
      <div class="form-group">
        <label for="input_directory">Input Directory</label>
        <input
            type="text"
            class="form-control"
            id="input_directory"
            v-model="subscription.input_directory"
            v-validate="'required'"
            name="Input Directory"
            placeholder="Enter directory"
            :class="{'is-invalid': errors.has('subscription.input_directory') && submitted}">
        <div class="invalid-feedback">
          Please provide a valid directory.
        </div>
      </div>
      <div class="form-group">
        <label for="output_directory">Output Directory</label>
        <input
            type="text"
            class="form-control"
            id="output_directory"
            v-model="subscription.output_directory"
            v-validate="'required'"
            name="Output Directory"
            placeholder="Enter directory"
            :class="{'is-invalid': errors.has('subscription.output_directory') && submitted}">
        <div class="invalid-feedback">
          Please provide a valid directory.
        </div>
      </div>
      <div class="form-group">
        <label for="fasta_reference_directory">Fasta Reference Directory</label>
        <input
            type="text"
            class="form-control"
            id="fasta_reference_directory"
            v-model="subscription.fasta_reference_directory"
            v-validate="'required'"
            name="Fasta Reference Directory"
            placeholder="Enter directory"
            :class="{'is-invalid': errors.has('subscription.fasta_reference_directory') && submitted}">
        <div class="invalid-feedback">
          Please provide a valid directory.
        </div>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea
            name="description"
            class="form-control"
            id="description"
            v-validate="'required'"
            v-model="subscription.description"
            cols="30"
            rows="2"
            :class="{'is-invalid': errors.has('subscription.description') && submitted}"></textarea>
        <div class="invalid-feedback">
          Please provide a valid description.
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
      subscription: {
        name: '',
        live_processing: '',
        basecalling: '',
        methylation_calling: '',
        alignment: '',
        input_directory: '',
        output_directory: '',
        fasta_reference_directory: '',
        description: '',
      },
          submitted: false
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/api/experiments/' + this.$route.params.id)
            .then( response => {
                console.log(response.data)
                this.subscription = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .put(`http://127.0.0.1:8000/api/experiments/${this.subscription.id}/`,
                        this.subscription
                    )
                    .then(response => {
                        this.$router.push('/operation');
                    })
            });
        }
    },
}
</script>