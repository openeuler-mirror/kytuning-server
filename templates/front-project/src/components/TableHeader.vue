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
        <el-button type="primary" @click="exportTableData" :disabled=DisabledExcel>导出表格数据</el-button>
        <el-button type="primary" @click="toggleDataVisibility">
          {{ showAllData ? '隐藏数据' : '显示全部数据' }}
        </el-button>
        <el-button type="primary" @click="$router.back()">返回上一步</el-button>
        <el-button type="primary" @click="goToHome">返回数据首页</el-button>
        <el-button type="primary" @click="modify">修改数据</el-button>
        <el-button type="success" @click="goTo('env')">环境信息</el-button>
        <el-button :type="buttonType('stream')" @click="goTo('stream')" :disabled="toDisabled('stream')">stream
        </el-button>
        <el-button :type="buttonType('lmbench')" @click="goTo('lmbench')" :disabled="toDisabled('lmbench')">lmbench
        </el-button>
        <el-button :type="buttonType('unixbench')" @click="goTo('unixbench')" :disabled="toDisabled('unixbench')">
          unixbench
        </el-button>
        <el-button :type="buttonType('fio')" @click="goTo('fio')" :disabled="toDisabled('fio')">fio</el-button>
        <el-button :type="buttonType('iozone')" @click="goTo('iozone')" :disabled="toDisabled('iozone')">iozone
        </el-button>
        <el-button :type="buttonType('jvm2008')" @click="goTo('jvm2008')" :disabled="toDisabled('jvm2008')">jvm2008
        </el-button>
        <el-button :type="buttonType('cpu2006')" @click="goTo('cpu2006')" :disabled="toDisabled('cpu2006')">cpu2006
        </el-button>
        <el-button :type="buttonType('cpu2017')" @click="goTo('cpu2017')" :disabled="toDisabled('cpu2017')">cpu2017
        </el-button>
      </el-row>
    </el-card>
  </div>
  <el-dialog :title="'选择修改的数据'" v-model="selectDataDialog" width="800px">
    <el-table ref="selectDatas[0]" :data="filteredTestDatas" @selection-change="handleSelection"
              tooltip-effect="dark" border height="500" style="width: 100%" class="tableHead">
      <el-table-column type="selection" width="55"/>
      <el-table-column prop="value" label="请选择修改的数据"/>
    </el-table>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="closeTest">取 消</el-button>
        <el-button type="primary" @click="selectSure()">确 定</el-button>
      </span>
    </template>
  </el-dialog>
  <el-dialog :title="'修改stream数据'" v-model="PutStreamDialog" width="500px">
    <el-form :model="putStreamData" :rules="rules" ref="putStreamData">
      <el-form-item label="单线程 Array size" :label-width="formLabelWidth" prop="errorDescription">
        <el-input v-model="putStreamData.single_array_size" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="单线程 Copy" :label-width="formLabelWidth" prop="errorExport">
        <el-input v-model="putStreamData.single_copy" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="单线程 Scale" :label-width="formLabelWidth" prop="errorExport">
        <el-input v-model="putStreamData.single_scale" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="单线程 Add" :label-width="formLabelWidth" prop="solution">
        <el-input v-model="putStreamData.single_add" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="单线程 Triad" :label-width="formLabelWidth" prop="solution">
        <el-input v-model="putStreamData.single_triad" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="多线程 Array size" :label-width="formLabelWidth" prop="errorDescription">
        <el-input v-model="putStreamData.multi_array_size" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="多线程 Copy" :label-width="formLabelWidth" prop="errorExport">
        <el-input v-model="putStreamData.multi_copy" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="多线程 Scale" :label-width="formLabelWidth" prop="errorExport">
        <el-input v-model="putStreamData.multi_scale" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="多线程 Add" :label-width="formLabelWidth" prop="solution">
        <el-input v-model="putStreamData.multi_add" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="多线程 Triad" :label-width="formLabelWidth" prop="solution">
        <el-input v-model="putStreamData.multi_triad" autocomplete="off"></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="closeInfo('form')">取 消</el-button>
      <el-button type="primary" @click="addSure('form')">确 定</el-button>
    </template>
  </el-dialog>
</template>


<script>
// import {project, stream} from "@/api/api.js";
import {download_excel, project} from "@/api/api.js";
import {ElMessage} from 'element-plus';
import {stream} from "@/api/api.js";
import utils from '@/utils/utils';

export default {
  name: 'TableHeader',
  mixins: [utils],
  components: {},
  data() {
    return {
      localShowAllData: this.showAllData,
      allProjectDatas: [],
      isDataLoaded: false,
      DisabledExcel: false,
      api: '',
      selectDataDialog: false,
      PutStreamDialog: false,
      putStreamData: {
        single_array_size: '',
        single_copy: '',
        single_scale: '',
        single_add: '',
        single_triad: '',
        multi_array_size: '',
        multi_copy: '',
        multi_scale: '',
        multi_add: '',
        multi_triad: '',
      },
      selectDatas: [],
      selectData: '',
    }
  },
  props: {
    // tableDatas: Array,    // 接收 table-datas 属性
    // dataName: String,
    showAllData: null
  },
  created() {
    this.get_data()
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
    filteredTestDatas() {
      const keys = Object.keys(this.selectDatas[0]);
      const filteredKeys = keys.slice(2, -1);
      return filteredKeys.map(key => ({value: this.selectDatas[0][key]}));
    }
  },
  methods: {
    get_data() {
      project('get', {
        baseId: this.$route.params.baseId,
        comparsionIds: this.$route.params.comparsionIds
      }).then((response) => {
        this.allProjectDatas = response.data.data
        this.isDataLoaded = true;
      });
    },
    modify() {
      if (this.$route.path.split('/')[1] === 'stream') {
        stream({env_id: this.$route.params.baseId, comparsionIds: ''}).then((response) => {
          //弹出有哪些数据，用户选中修改哪一个数据
          this.selectDatas = response.data.data
          this.selectDataDialog = true
        });
      }
    },
    selectSure() {
      console.log(this.selectData,777)
      console.log(this.selectDatas,888)
      this.selectDataDialog = false
      this.PutStreamDialog = true
    },
    handleSelection(val) {
      this.selectData = val[0]
      if (val.length > 1) {
        this.$refs.selectDatas[0].clearSelection();
        this.$refs.selectDatas[0].toggleRowSelection(val.pop());
      }
    },
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
        this.$router.push({path: '/storeData'})
      })
    },
    goTo(name) {
      this.$router.push({
        name: name,
        "params": {baseId: this.$route.params.baseId, comparsionIds: this.$route.params.comparsionIds}
      })
    },
    toggleDataVisibility() {
      this.localShowAllData = !this.localShowAllData;
      this.$emit('data-loaded', this.localShowAllData);
    },
    // 从后端获取数据
    exportTableData() {
      this.DisabledExcel = true
      download_excel({
        env_id: this.$route.params.baseId,
        comparsionIds: this.$route.params.comparsionIds,
      }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]))
        const link = document.createElement('a')
        link.href = url
        link.setAttribute('download', 'kytuning-result.xlsx')
        document.body.appendChild(link)
        link.click()
      }).catch(error => {
        if (error.code === "ERR_BAD_REQUEST") {
          ElMessage({message: "下载失败", type: 'warning'})
        }
      }).finally(() => {
        // DisabledExcel 将被设置为 true，然后立即被设置为 false,禁用的时间非常短，不足以被用户察觉到。
        this.DisabledExcel = false;
      });
    },
  }
}
</script>
<style scoped>

</style>