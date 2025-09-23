<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Sat May 11 09:46:08 2024 +0800
-->
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
        <el-button type="success" @click="goTo('env')">环境信息</el-button>
        <el-button :type="buttonType('stream')" @click="goTo('stream')" :disabled="toDisabled('stream')">stream</el-button>
        <el-button :type="buttonType('lmbench')" @click="goTo('lmbench')" :disabled="toDisabled('lmbench')">lmbench</el-button>
        <el-button :type="buttonType('unixbench')" @click="goTo('unixbench')" :disabled="toDisabled('unixbench')">unixbench</el-button>
        <el-button :type="buttonType('fio')" @click="goTo('fio')" :disabled="toDisabled('fio')">fio</el-button>
        <el-button :type="buttonType('iozone')" @click="goTo('iozone')" :disabled="toDisabled('iozone')">iozone</el-button>
        <el-button :type="buttonType('jvm2008')" @click="goTo('jvm2008')" :disabled="toDisabled('jvm2008')">jvm2008</el-button>
        <el-button :type="buttonType('cpu2006')" @click="goTo('cpu2006')" :disabled="toDisabled('cpu2006')">cpu2006</el-button>
        <el-button :type="buttonType('cpu2017')" @click="goTo('cpu2017')" :disabled="toDisabled('cpu2017')">cpu2017</el-button>
      </el-row>
    </el-card>
  </div>
</template>


<script>
import {get_project} from "@/api/api.js";
import { download_excel } from "@/api/api.js";
 // import * as XLSX from 'xlsx';

export default {
  data() {
    return {
      localShowAllData: this.showAllData,
      allProjectDatas:[],
      isDataLoaded:false,
      typeClass:'',
      paramsData: {
        env_id: this.$route.params.baseId,
        comparsionIds: this.$route.params.comparsionIds,
      },
    }
  },
  props: {
    tableDatas: Array,    // 接收 table-datas 属性
    dataName: String,
    showAllData: null
  },
  created() {
    get_project({baseId: this.$route.params.baseId,comparsionIds: this.$route.params.comparsionIds}).then((response) => {
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
        // const comparsionIdsArray = this.$route.params.comparsionIds.split(',');
        let disabled = false
        if (baseData && baseData[name] === 0) {
          disabled = true
        }
        return disabled;
      };
    },
  },
  methods: {
    buttonType(name) {
      if (!this.isDataLoaded) {
        return ''; // 数据尚未加载完成，返回默认值
      }
      if (this.toDisabled(name)) {
        return 'info';
      }
      const comparsionIdsArray = this.$route.params.comparsionIds.split(',');
      let foundZero = comparsionIdsArray.some(compId => {
        const comparData = this.allProjectDatas.find(data => data.env_id === parseInt(compId));
        return comparData && comparData[name] === 0;
      });
      return foundZero ? 'warning' : 'success';
    },
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
    exportTableData() {
      console.log(this.paramsData)
      download_excel(this.paramsData).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', 'kytuning-result.xlsx')
          document.body.appendChild(link)
          link.click()
      }).catch(error => {
        console.log(error)
      })
    },
  }
}
</script>
