<template>
  <div class="row h-10 justify-content-center  " v-show="!$fetchState.pending">
    <div class="col-lg-6 col-sm-12  text-center mb--50  ">
      <v-select
        class="style-chooser "
        @input="changeCustomers"
        :reduce="(customer) => customer.id"
        label="name"
        :placeholder="$t('searchsuppliers')"
        :options="$store.state.customers.data"
      >
      </v-select>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      date: new Date().toISOString(),
    };
  },
  async fetch() {
    const customers = await this.$strapi.find("customers", {
      "sites.uid": this.$config.siteUid,
      'status':'published',
      featured:true
    });
    
    this.$store.commit("customers/SET_CUSTOMERS", customers);
  },
  methods: {
    changeCustomers(id) {
      let value = id ? id : undefined;
      this.$emit('changeSelected', value)
    },
  },
};
</script>

<style scoped >
.style-chooser .vs__clear,
.style-chooser .vs__open-indicator {
  fill: #003c71;
}
.style-chooser .vs__dropdown-menu {
      overflow-y: auto;
      z-index: 1;
}
.style-chooser .vs__selected {
  color: #025fb1;
  font-size: 16px;
}
.style-chooser .vs__dropdown-toggle {
  border: 1px solid #003c71;
  padding: 0px;
  white-space:normal;
}
.style-chooser .vs__search    {
  width: 20%;
}

</style>
