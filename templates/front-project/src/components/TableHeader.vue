<template>
  <div class="footer">
    <el-card>
      <el-row class="mb-4">
        <el-button type="primary" @click="exportTableData">导出表格数据</el-button>
        <el-button type="primary" @click="toggleDataVisibility">
          {{ showAllData ? '隐藏数据' : '显示全部数据' }}
        </el-button>
        <el-button type="primary" @click="$router.back()">返回</el-button>
      </el-row>
      <br>
      <el-row class="mb-4">
        <el-button type="success" @click="goToStream" :disabled="toStream">stream</el-button>
        <el-button type="success" @click="goToLmbench">lmbench</el-button>
        <el-button type="success" @click="goToUnixbench">unixbench</el-button>
        <el-button type="success" @click="goToFio">fio</el-button>
        <el-button type="success" @click="goToIozone">iozone</el-button>
        <el-button type="success" @click="goToJvm2008">jvm2008</el-button>
        <el-button type="success" @click="goToCpu2016">cpu2016</el-button>
        <el-button type="success" @click="goToCpu2017">cpu2017</el-button>
      </el-row>
    </el-card>
  </div>
</template>


<script>
import axios from 'axios'
export default {
  data() {
    return {
      localShowAllData: this.showAllData,
      allProjectDatas:[],
      isDataLoaded:false,
    }
  },
  props: {
    tableDatas: Array,    // 接收 table-datas 属性
    dataName: String,
    showAllData: null
  },
  created() {
    axios.get('/api/project/').then((response) => {
      this.allProjectDatas = response.data.data
      console.log(this.allProjectDatas);
      this.isDataLoaded = true;
    });
  },
  computed: {
    toStream() {
      if (!this.isDataLoaded) {
      return false; // 数据尚未加载完成，返回默认值
    }
      const baseData = this.allProjectDatas.find(data => data.id === parseInt(this.$route.params.baseId));
      const comparsionIdsArray = this.$route.params.comparsionIds.split(',');
      let disabled = false
      if (baseData && baseData.stream === 0) {
        disabled = true
      }
      comparsionIdsArray.some(compId => {
        const comparData = this.allProjectDatas.find(data => data.env_id === parseInt(compId));
        if (comparData && comparData.stream === 0){
          disabled = true
        }
      });
      return disabled;
    }
  },
  methods: {
    goToStream(){
      this.$router.push({name: 'stream',"params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
    },
    goToLmbench(){
      this.$router.push({name: 'lmbench',"params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
    },
    goToUnixbench(){
      this.$router.push({name: 'unixbench', "params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
    },
    goToFio() {
      this.$router.push({name: 'fio', "params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
    },
    goToIozone() {
      this.$router.push({name: 'iozone', "params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
    },
    goToJvm2008() {
      this.$router.push({name: 'jvm2008', "params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
    },
    goToCpu2016() {
      this.$router.push({name: 'cpu2006', "params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
    },
    goToCpu2017() {
      this.$router.push({name: 'cpu2017', "params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
    },
    toggleDataVisibility() {
      this.localShowAllData = !this.localShowAllData;
      this.$emit('data-loaded', this.localShowAllData);
    },
    // 导出表格数据为 CSV 格式
    exportTableData() {
      const data = [this.tableDatas];

      // 生成 CSV 格式的数据字符串
      const csvData = data.map(rows => {
        return rows.map(row => {
          return Object.values(row).map(value => `"${value}"`).join(",");
        }).join("\n");
      }).join("\n");

      // 创建并下载 CSV 文件
      const blob = new Blob(["\uFEFF" + csvData], {type: "text/csv;charset=utf-8;"});
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = this.dataName + '_table';
      link.click();
    },
  }
}
</script>