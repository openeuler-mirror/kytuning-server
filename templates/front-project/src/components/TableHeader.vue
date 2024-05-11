<template>
  <div style="overflow-x: auto;">
    <template v-if="isDataLoaded">
      <el-table :data="otherList" border :span-method="titleObjectSpanMethod" style="overflow-y: auto;" :show-header="false">
        <template v-for="i in numColumns" :key="i">
          <el-table-column :prop="`column${i}`" :width="i < 2 ? '100' : ''" align="center"></el-table-column>
        </template>
      </el-table>
    </template>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      otherList: [],
      numColumns: 0,
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
    axios.get('/api/' + this.dataName + '/?env_id=' + this.$route.params.baseId + '&comparsionIds=' +
        this.$route.params.comparsionIds).then((response) => {
          this.otherList = response.data.data.others
          this.numColumns = Object.keys(response.data.data.others[0]).length
          this.isDataLoaded = true;
          this.$emit('data-loaded', this.otherList); // 触发自定义事件并传递数据
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
</style>
