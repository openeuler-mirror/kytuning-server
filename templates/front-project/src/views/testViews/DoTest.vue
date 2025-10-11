<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div id="fixed-top">
    <div class="form-container">
      <el-form :label-position="labelPosition" label-width="300px" :model="formData" ref="dataForm" :rules="rules">
        <el-form-item label="配置文件名称：">
          <el-input v-model="formData.configName"/>
        </el-form-item>
        <el-form-item label="项目名称：">
          <el-input v-model="formData.projectName"/>
        </el-form-item>
        <el-form-item label="kytuning的用户密码：">
          <el-input v-model="formData.userPassword" placeholder="因为数据库加密了，无法解密，所以只能用户输入一次密码"/>
        </el-form-item>
        <el-form-item label="测试项的迭代次数：">
          <el-form-item label="stream迭代次数：">
            <el-input v-model="formData.iterations.stream"/>
          </el-form-item>
          <el-form-item label="lmbench迭代次数：">
            <el-input v-model="formData.iterations.lmbench"/>
          </el-form-item>
          <el-form-item label="unixbench迭代次数：">
            <el-input v-model="formData.iterations.unixbench"/>
          </el-form-item>
          <el-form-item label="fio迭代次数：">
            <el-input v-model="formData.iterations.fio"/>
          </el-form-item>
          <el-form-item label="iozone迭代次数：">
            <el-input v-model="formData.iterations.iozone"/>
          </el-form-item>
          <el-form-item label="jvm2008迭代次数：">
            <el-input v-model="formData.iterations.jvm2008"/>
          </el-form-item>
          <el-form-item label="cpu2006迭代次数：">
            <el-input v-model="formData.iterations.cpu2006"/>
          </el-form-item>
          <el-form-item label="cpu2017迭代次数：">
            <el-input v-model="formData.iterations.cpu2017"/>
          </el-form-item>
        </el-form-item>
        <el-form-item label="编辑yaml配置文件：">
          <el-button type="success" class="test-button" @click="showYaml('stream')">stream</el-button>
          <el-button type="success" class="test-button" @click="showYaml('lmbench')">lmbench</el-button>
          <el-button type="success" class="test-button" @click="showYaml('unixbench')">unixbench</el-button>
          <el-button type="success" class="test-button" @click="showYaml('fio')">fio</el-button>
          <el-button type="success" class="test-button" @click="showYaml('iozone')">iozone</el-button>
          <el-button type="success" class="test-button" @click="showYaml('jvm2008')">jvm2008</el-button>
          <el-button type="success" class="test-button" @click="showYaml('cpu2006')">cpu2006</el-button>
          <el-button type="success" class="loongarch-button" @click="showYaml('cpu2006_loongarch64')">
            cpu2006_loongarch64
          </el-button>
          <el-button type="success" class="test-button" @click="showYaml('cpu2017')">cpu2017</el-button>
          <el-button type="primary" class="test-button" @click="doBase">一键摸底</el-button>
          <el-button type="primary" class="test-button" @click="lastTest">还原上次测试</el-button>
        </el-form-item>

        <el-form-item label="测试机器IP：">
          <el-input v-model="formData.testIP"/>
          <!--            <el-select v-model="testIP" placeholder="请选择测试机器IP">-->
          <!--              <el-option v-for="option in machineOptions" :key="option.value" :label="option.label"-->
          <!--                         :value="option.value"/>-->
          <!--            </el-select>-->
          <el-form-item>
            <!--              <el-button type="primary" class="button-style" @click="testlink">测试连接</el-button>-->
          </el-form-item>
        </el-form-item>

        <el-form-item label="测试机器密码：">
          <el-input v-model="formData.testPassword" placeholder="因为还没有做设备管理，所以先让用户手动输入密码"/>
          <!--            <el-select v-model="testIP" placeholder="请选择测试机器IP">-->
          <!--              <el-option v-for="option in machineOptions" :key="option.value" :label="option.label"-->
          <!--                         :value="option.value"/>-->
          <!--            </el-select>-->
          <!--            <el-form-item>-->
          <!--              <el-button type="primary" class="button-style" @click="testlink">测试连接</el-button>-->
          <!--            </el-form-item>-->
        </el-form-item>
        <el-form-item label="描述：">
          <el-input v-model="formData.message"/>
        </el-form-item>
      </el-form>
      <div class="button-container">
        <el-button type="warning" class="button-style" plain @click="select">选择配置</el-button>
        <el-button type="primary" class="button-style" plain @click="update">更新配置</el-button>
        <el-button type="primary" class="button-style" plain @click="add">新增配置</el-button>
        <el-button type="success" class="button-style" plain @click="sendTest">发起测试</el-button>
      </div>
    </div>
  </div>
  <div>
    <el-dialog :title="'修改' + yamlType +'信息'" v-model="yamlDialog" width="800px">
      <el-input v-model="formData.yamlData[yamlType]" :autosize="{ minRows: 4, maxRows: 25 }" type="textarea"
                placeholder="Please input"/>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="closeInfo">取 消</el-button>
          <el-button type="primary" @click="putYaml(formData.yamlData)">确 定</el-button>
        </span>
      </template>
    </el-dialog>

    <el-dialog :title="'选择个人配置'" v-model="configDialog" width="800px">
      <el-table ref="configTable" :data="configDatas" @selection-change="handleSelection"
                tooltip-effect="dark" border style="width: 100%" class="tableHead">
        <el-table-column type="selection" width="55"/>
        <el-table-column prop="config_name" label="配置文件名称"/>
        <el-table-column prop="message" label="描述"/>
      </el-table>

      <template #footer>
        <span class="dialog-footer">
          <el-button @click="closeInfo">取 消</el-button>
          <el-button type="primary" @click="selectConfig(scope)">确 定</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import {ref} from 'vue'
import baseYamlData from '@/utils/yaml.js';
import {ElMessage} from 'element-plus'
import {do_test_case, user_config} from "@/api/api";

export default {
  name: 'doTest',
  data() {
    return {
      labelPosition: ref('center'),
      formData: {
        configName: '',
        projectName: '',
        userPassword: '',
        yamlData: baseYamlData,
        testIP: '',
        testPassword: '',
        message: '',
        iterations: {
          stream: '',
          lmbench: '',
          unixbench: '',
          fio: '',
          iozone: '',
          jvm2008: '',
          cpu2006: '',
          cpu2006_loongarch64: '',
          cpu2017: '',
        },
      },

      yamlDialog: false,
      configDialog: false,
      yamlType: '',
      configID: 0,
      configData: '',
      configDatas: [],
      // machineOptions: [{label: '172.29.220.100', value: '172.29.220.100'}, {label: '172.29.220.101',value: '172.29.220.101'}],
      rules: {
        configName: [{required: true, message: 'configName不能为空', trigger: 'blur'}],
        projectName: [{required: true, message: 'projectName不能为空', trigger: 'blur'}],
        userPassword: [{required: true, message: 'userPassword不能为空', trigger: 'blur'}],
        yamlData: [{required: true, message: 'yamlData不能为空', trigger: 'blur'}],
      },
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
    },
    //展示yaml文件
    showYaml(yamlType) {
      this.yamlDialog = true
      this.yamlType = yamlType
    },
    //关闭对话框
    closeInfo() {
      this.yamlDialog = false
      this.configDialog = false
    },
    //修改yaml文件
    putYaml(yamlData) {
      this.formData.yamlData = yamlData
      this.yamlDialog = false;
    },
    //一键摸底
    doBase() {
      this.formData.iterations.stream = 50
      this.formData.iterations.lmbench = 3
      this.formData.iterations.unixbench = 3
      this.formData.iterations.fio = 3
      this.formData.iterations.iozone = 0
      this.formData.iterations.jvm2008 = 1
      this.formData.iterations.cpu2006 = 1
      this.formData.iterations.cpu2017 = 0
      this.formData.yamlData = baseYamlData
    },
    //最后一次测试数据
    lastTest() {
      user_config('get', {configID: 0}).then(response => {
        const config = response.data.data[0]
        this.configID = config.id
        this.formData.configName = config.config_name
        this.formData.projectName = config.project_name
        this.formData.userPassword = config.user_password
        this.formData.iterations.stream = config.stream_number
        this.formData.iterations.lmbench = config.lmbench_number
        this.formData.iterations.unixbench = config.unixbench_number
        this.formData.iterations.fio = config.fio_number
        this.formData.iterations.iozone = config.iozone_number
        this.formData.iterations.jvm2008 = config.jvm2008_number
        this.formData.iterations.cpu2006 = config.cpu2006_number
        this.formData.iterations.cpu2017 = config.cpu2017_number
        this.formData.yamlData = {
          stream: config.stream_config,
          lmbench: config.lmbench_config,
          unixbench: config.unixbench_config,
          fio: config.fio_config,
          iozone: config.iozone_config,
          jvm2008: config.jvm2008_config,
          cpu2006: config.cpu2006_config,
          cpu2006_loongarch64: config.cpu2006_loongarch64_config,
          cpu2017: config.cpu2017_config,
        }
        this.formData.testIP = config.test_ip
        this.formData.testPassword = config.test_password
        this.formData.message = config.message
      })
    },
    //选中配置列表
    select() {
      user_config('get').then(response => {
        this.configDatas = response.data.data
      })
      this.configDialog = true
    },
    //选择框只能单选
    handleSelection(val) {
      this.configData = val[0];
      if (val.length > 1) {
        this.$refs.configTable.clearSelection();
        this.$refs.configTable.toggleRowSelection(val.pop());
      }
    },
    //选中配置
    selectConfig() {
      this.configID = this.configData.id
      this.formData.configName = this.configData.config_name
      this.formData.projectName = this.configData.project_name
      this.formData.userPassword = this.configData.user_password
      this.formData.iterations.stream = this.configData.stream_number
      this.formData.iterations.lmbench = this.configData.lmbench_number
      this.formData.iterations.unixbench = this.configData.unixbench_number
      this.formData.iterations.fio = this.configData.fio_number
      this.formData.iterations.iozone = this.configData.iozone_number
      this.formData.iterations.jvm2008 = this.configData.jvm2008_number
      this.formData.iterations.cpu2006 = this.configData.cpu2006_number
      this.formData.iterations.cpu2017 = this.configData.cpu2017_number
      this.formData.yamlData.stream = this.configData.stream_config
      this.formData.yamlData.lmbench = this.configData.lmbench_config
      this.formData.yamlData.unixbench = this.configData.unixbench_config
      this.formData.yamlData.fio = this.configData.fio_config
      this.formData.yamlData.iozone = this.configData.iozone_config
      this.formData.yamlData.cpu2006 = this.configData.cpu2006_config
      this.formData.yamlData.cpu2006_loongarch64_config = this.configData.cpu2006_loongarch64_config_config
      this.formData.yamlData.cpu2017 = this.configData.cpu2017_config
      this.formData.testIP = this.configData.test_ip
      this.formData.testPassword = this.configData.test_password
      this.formData.message = this.configData.message
      this.configDialog = false
    },
    //更新配置
    update() {
      if (this.check()) {
        if (this.configID) {
          const formData = {
            id: this.configID,
            config_name: this.formData.configName,
            project_name: this.formData.projectName,
            test_ip: this.formData.testIP,
            test_password: this.formData.testPassword,
            user_password: this.formData.userPassword,
            stream: this.formData.iterations.stream,
            lmbench: this.formData.iterations.lmbench,
            unixbench: this.formData.iterations.unixbench,
            fio: this.formData.iterations.fio,
            iozone: this.formData.iterations.iozone,
            jvm2008: this.formData.iterations.jvm2008,
            cpu2006: this.formData.iterations.cpu2006,
            cpu2017: this.formData.iterations.cpu2017,
            yaml: this.formData.yamlData,
            message: this.formData.message,
          }
          user_config('put', formData).then(response => {
            ElMessage({message: response.data.message, type: 'success'})
          })
        }
      }
    },
    //新增配置
    add() {
      if (this.check()) {
        const formData = {
          config_name: this.formData.configName,
          project_name: this.formData.projectName,
          test_ip: this.formData.testIP,
          test_password: this.formData.testPassword,
          user_password: this.formData.userPassword,
          stream: this.formData.iterations.stream,
          lmbench: this.formData.iterations.lmbench,
          unixbench: this.formData.iterations.unixbench,
          fio: this.formData.iterations.fio,
          iozone: this.formData.iterations.iozone,
          jvm2008: this.formData.iterations.jvm2008,
          cpu2006: this.formData.iterations.cpu2006,
          cpu2017: this.formData.iterations.cpu2017,
          yaml: this.formData.yamlData,
          message: this.formData.message
        }
        user_config('post', formData).then(response => {
          ElMessage({message: response.data.message, type: 'success'})
        })
      }
    },
    //发起测试
    sendTest() {
      if (this.check()) {
        const formData = {
          config_name: this.formData.configName,
          project_name: this.formData.projectName,
          test_ip: this.formData.testIP,
          test_password: this.formData.testPassword,
          user_password: this.formData.userPassword,
          stream: this.formData.iterations.stream,
          lmbench: this.formData.iterations.lmbench,
          unixbench: this.formData.iterations.unixbench,
          fio: this.formData.iterations.fio,
          iozone: this.formData.iterations.iozone,
          jvm2008: this.formData.iterations.jvm2008,
          cpu2006: this.formData.iterations.cpu2006,
          cpu2017: this.formData.iterations.cpu2017,
          yaml: this.formData.yamlData,
          message: this.formData.message
        }
        do_test_case(formData).then(response => {
          console.log(response.data.code)
          this.formData.configName = ''
          this.formData.projectName = ''
          this.formData.testIP = ''
          this.formData.testPassword = ''
          this.formData.userPassword = ''
          this.formData.iterations.stream = ''
          this.formData.iterations.lmbench = ''
          this.formData.iterations.unixbench = ''
          this.formData.iterations.fio = ''
          this.formData.iterations.iozone = ''
          this.formData.iterations.jvm2008 = ''
          this.formData.iterations.cpu2006 = ''
          this.formData.iterations.cpu2017 = ''
          this.formData.yamlData = ''
          this.formData.message = ''
        });
        ElMessage({message: '发起测试完成', type: 'success'});
      }
    },
    //验证数据
    check() {
      if (!this.formData.projectName) {
        ElMessage({message: "项目名称不能为空", type: 'error'});
        return false;
      }
      if (!this.formData.userPassword) {
        ElMessage({message: "kytuning用户密码不能为空", type: 'error'});
        return false;
      }
      const iterations = {
        stream: this.formData.iterations.stream !== '' ? parseInt(this.formData.iterations.stream) : 0,
        lmbench: this.formData.iterations.lmbench !== '' ? parseInt(this.formData.iterations.lmbench) : 0,
        unixbench: this.formData.iterations.unixbench !== '' ? parseInt(this.formData.iterations.unixbench) : 0,
        fio: this.formData.iterations.fio !== '' ? parseInt(this.formData.iterations.fio) : 0,
        iozone: this.formData.iterations.iozone !== '' ? parseInt(this.formData.iterations.iozone) : 0,
        jvm2008: this.formData.iterations.jvm2008 !== '' ? parseInt(this.formData.iterations.jvm2008) : 0,
        cpu2006: this.formData.iterations.cpu2006 !== '' ? parseInt(this.formData.iterations.cpu2006) : 0,
        cpu2017: this.formData.iterations.cpu2017 !== '' ? parseInt(this.formData.iterations.cpu2017) : 0,
      };
      let result = true
      for (const key in iterations) {
        if (isNaN(iterations[key])) {
          ElMessage({message: `${key} 不是整数类型`, type: 'error'});
          result = false
          break;
        }
      }
      //处理可迭代次数
      this.formData.iterations = iterations
      return result;
    },
    testlink() {
    },
  }
};
</script>

<style scoped>
.form-container {
  /*display: flex;*/
  /*flex-direction: column;*/
  /*align-items: center;*/
  margin-top: 50px;
}

.test-button {
  width: 100px;
  height: 40px;
}

.loongarch-button {
  width: 150px;
  height: 40px;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 50px;
}

.button-style {
  margin-top: 10px;
  margin-right: 50px; /* 添加水平间距 */
}
</style>