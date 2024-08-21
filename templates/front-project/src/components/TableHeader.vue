<template>
  <div class="footer">
    <el-card>
      <el-row class="mb-4">
        <el-button type="primary" @click="exportTableData">导出表格数据</el-button>
        <el-button type="primary" @click="toggleDataVisibility">
          {{ showAllData ? '隐藏数据' : '显示全部数据' }}
        </el-button>
        <el-button type="primary" @click="$router.back()">返回上一步</el-button>
        <el-button type="primary" @click="goToHome">返回首页</el-button>
        <el-button type="success" @click="goTo('stream')" :disabled="toDisabled('stream')">stream</el-button>
        <el-button type="success" @click="goTo('lmbench')" :disabled="toDisabled('lmbench')">lmbench</el-button>
        <el-button type="success" @click="goTo('unixbench')" :disabled="toDisabled('unixbench')">unixbench</el-button>
        <el-button type="success" @click="goTo('fio')" :disabled="toDisabled('fio')">fio</el-button>
        <el-button type="success" @click="goTo('iozone')" :disabled="toDisabled('iozone')">iozone</el-button>
        <el-button type="success" @click="goTo('jvm2008')" :disabled="toDisabled('jvm2008')">jvm2008</el-button>
        <el-button type="success" @click="goTo('cpu2006')" :disabled="toDisabled('cpu2006')">cpu2006</el-button>
        <el-button type="success" @click="goTo('cpu2017')" :disabled="toDisabled('cpu2017')">cpu2017</el-button>
      </el-row>
    </el-card>
  </div>
</template>


<script>
import { project } from "@/api/api.js";
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
    project().then((response) => {
      this.allProjectDatas = response.data.data
      this.isDataLoaded = true;
    });
  },
  computed: {
    toDisabled() {
      return (name) => {
        if (!this.isDataLoaded) {
          return false; // 数据尚未加载完成，返回默认值
        }
        const baseData = this.allProjectDatas.find(data => data.env_id === parseInt(this.$route.params.baseId));
        const comparsionIdsArray = this.$route.params.comparsionIds.split(',');
        let disabled = false
        if (baseData && baseData[name] === 0) {
          disabled = true
        }
        comparsionIdsArray.some(compId => {
          const comparData = this.allProjectDatas.find(data => data.env_id === parseInt(compId));
          if (comparData && comparData[name] === 0) {
            disabled = true
          }
        });
        return disabled;
      };
    },
  },
  methods: {
    goToHome() {
      this.$nextTick(() => {
        this.$router.push({name: 'project'})
      })
    },
    goTo(name){
      this.$router.push({name: name,"params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}})
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