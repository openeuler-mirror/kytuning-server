<template>
  <div style="overflow-x: auto;">
    <template v-if="isDataLoaded">
      <el-table :data="tableDatas" border :span-method="objectSpanMethod" style="overflow-x: auto;" :show-header="false">
        <template v-for="i in numColumns" :key="i">
          <el-table-column :prop="`column${i}`" :width="i < 2 ? '100' : ''" align="center" show-tooltip-when-overflow></el-table-column>
        </template>
      </el-table>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      tableDatas:[],
      numColumns : 0,
      isDataLoaded: false,
    }
  },
  props: {
    dataName: {
      type: String,
      required: true
    },
    baseId: {
      type: String,
      required: true
    },
    comparsionIds: {
      type: String,
      required: true
    }
  },
  created() {
    axios.get('/api/'+ this.dataName +'/?env_id=' + this.$route.params.baseId + '&comparsionIds=' +
        this.$route.params.comparsionIds).then((response) => {
          this.tableDatas = response.data.data.data
          this.numColumns = Object.keys(response.data.data.others[0]).length
          this.isDataLoaded = true;
          this.$emit('data-loaded', this.tableDatas);
    })
  },
  methods: {
    titleObjectSpanMethod({columnIndex}) {
      if (columnIndex === 0) {
        return [1, 2];
      } else if (columnIndex === 1) {
        return [0, 0];
      }
    },
  },
};
</script>

<style>
.header {
  background-color: #f0f0f0;
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}
</style>
