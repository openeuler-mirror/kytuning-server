<!--
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Tue Mar 12 09:59:13 2024 +0800
-->
<template>
  <div id="fixed-top">
    <AllHeader/>
    <el-container class="content">
      <Menu/>
      <div class="form-container">
        <el-form :label-position="labelPosition" label-width="300px" :model="iterations">
          <el-form-item label="项目名称：">
            <el-input v-model="projectName"/>
          </el-form-item>
          <el-form-item label="kytuning的用户密码：">
            <el-input v-model="userPassword" placeholder="因为数据库加密了，无法解密，所以只能用户输入一次密码"/>
          </el-form-item>
          <el-form-item label="测试项的迭代次数：">
            <el-form-item label="stream迭代次数：">
              <el-input v-model="iterations.stream"/>
            </el-form-item>
            <el-form-item label="lmbench迭代次数：">
              <el-input v-model="iterations.lmbench"/>
            </el-form-item>
            <el-form-item label="unixbench迭代次数：">
              <el-input v-model="iterations.unixbench"/>
            </el-form-item>
            <el-form-item label="fio迭代次数：">
              <el-input v-model="iterations.fio"/>
            </el-form-item>
            <el-form-item label="iozone迭代次数：">
              <el-input v-model="iterations.iozone"/>
            </el-form-item>
            <el-form-item label="jvm2008迭代次数：">
              <el-input v-model="iterations.jvm2008"/>
            </el-form-item>
            <el-form-item label="cpu2006迭代次数：">
              <el-input v-model="iterations.cpu2006"/>
            </el-form-item>
            <el-form-item label="cpu2017迭代次数：">
              <el-input v-model="iterations.cpu2017"/>
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
            <el-button type="success" class="test-button" @click="doBase">一键摸底</el-button>
          </el-form-item>

          <el-form-item label="测试机器IP：">
            <el-input v-model="testIP"/>
            <!--            <el-select v-model="testIP" placeholder="请选择测试机器IP">-->
            <!--              <el-option v-for="option in machineOptions" :key="option.value" :label="option.label"-->
            <!--                         :value="option.value"/>-->
            <!--            </el-select>-->
            <el-form-item>
              <!--              <el-button type="primary" class="button-style" @click="testlink">测试连接</el-button>-->
            </el-form-item>
          </el-form-item>

          <el-form-item label="测试机器密码：">
            <el-input v-model="testPassword" placeholder="因为还没有做设备管理，所以先让用户手动输入密码"/>
            <!--            <el-select v-model="testIP" placeholder="请选择测试机器IP">-->
            <!--              <el-option v-for="option in machineOptions" :key="option.value" :label="option.label"-->
            <!--                         :value="option.value"/>-->
            <!--            </el-select>-->
            <!--            <el-form-item>-->
            <!--              <el-button type="primary" class="button-style" @click="testlink">测试连接</el-button>-->
            <!--            </el-form-item>-->
          </el-form-item>
          <el-form-item label="备注：">
            <el-input v-model="message"/>
          </el-form-item>
        </el-form>
        <div class="button-container">
          <el-button type="warning" class="button-style" plain @click="select">选择配置</el-button>
          <el-button type="primary" class="button-style" plain @click="update">更新配置</el-button>
          <el-button type="primary" class="button-style" plain @click="add">新增配置</el-button>
          <el-button type="success" class="button-style" plain @click="sendTest">发起测试</el-button>
        </div>
      </div>
    </el-container>
  </div>
  <div>
    <el-dialog :title="'修改' + yamlType +'信息'" v-model="yamlDialog" width="800px">
      <el-input v-model="yamlData[yamlType]" :autosize="{ minRows: 4, maxRows: 25 }" type="textarea"
                placeholder="Please input"/>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="closeInfo">取 消</el-button>
          <el-button type="primary" @click="changeYaml(yamlData)">确 定</el-button>
        </span>
      </template>
    </el-dialog>

    <el-dialog :title="'选择个人配置'" v-model="configDialog" width="800px">
      <el-table ref="configTable" :data="configDatas" @selection-change="handleSelection"
                tooltip-effect="dark" border style="width: 100%" class="tableHead">
        <el-table-column type="selection" width="55"/>
        <el-table-column prop="project_name" label="测试项目名称"/>
        <el-table-column prop="test_ip" label="测试机器IP"/>
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
import AllHeader from "@/components/common/AllHeader";
import Menu from "@/components/common/AllMenu";
import {ref} from 'vue'
import baseYamlData from '@/utils/yaml.js';
import {ElMessage} from 'element-plus'
import {do_test_case, user_config} from "@/api/api";

export default {
  name: 'sendTest',
  components: {
    AllHeader,
    Menu,
  },
  data() {
    return {
      labelPosition: ref('right'),
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

      machineOptions: [],
      yamlDialog: false,
      yamlType: '',

      configDialog: false,
      configID: 0,
      configData: '',
      configDatas: [],
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      if (this.$route.query.configID) {
        this.configID = this.$route.query.configID
      }
      user_config('get', {configID: this.configID}).then(response => {
        const config = response.data.data[0]
        this.configID = config.id
        this.projectName = config.project_name
        this.userPassword = config.user_password
        this.iterations.stream = config.stream_number
        this.iterations.lmbench = config.lmbench_number
        this.iterations.unixbench = config.unixbench_number
        this.iterations.fio = config.fio_number
        this.iterations.iozone = config.iozone_number
        this.iterations.jvm2008 = config.jvm2008_number
        this.iterations.cpu2006 = config.cpu2006_number
        this.iterations.cpu2017 = config.cpu2017_number
        this.yamlData = {
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
        this.testIP = config.test_ip
        this.testPassword = config.test_password
        this.message = config.message
      })

      this.machineOptions =[
      {label: 'localhost1', value: 'localhost1'},
      {label: 'localhost2', value: 'localhost2'},
    ]
    },
    showYaml(yamlType) {
      this.yamlDialog = true
      this.yamlType = yamlType
    },
    closeInfo() {
      this.yamlDialog = false
      this.configDialog = false
    },
    changeYaml(yamlData) {
      this.yamlData = yamlData
      this.yamlDialog = false;
    },
    doBase() {
      this.iterations.stream = 50
      this.iterations.lmbench = 3
      this.iterations.unixbench = 3
      this.iterations.fio = 3
      this.iterations.iozone = 0
      this.iterations.jvm2008 = 1
      this.iterations.cpu2006 = 1
      this.iterations.cpu2017 = 0
      this.yamlData = baseYamlData
    },

    select() {
      user_config('get').then(response => {
        this.configDatas = response.data.data
      })
      this.configDialog = true
    },

    handleSelection(val) {
      this.configData = val[0];
      if (val.length > 1) {
        this.$refs.configTable.clearSelection();
        this.$refs.configTable.toggleRowSelection(val.pop());
      }
    },

    selectConfig() {
      this.projectName = this.configData.project_name
      this.userPassword = this.configData.user_password
      this.iterations.stream = this.configData.stream_number
      this.iterations.lmbench = this.configData.lmbench_number
      this.iterations.unixbench = this.configData.unixbench_number
      this.iterations.fio = this.configData.fio_number
      this.iterations.iozone = this.configData.iozone_number
      this.iterations.jvm2008 = this.configData.jvm2008_number
      this.iterations.cpu2006 = this.configData.cpu2006_number
      this.iterations.cpu2017 = this.configData.cpu2017_number
      this.yamlData.stream = this.configData.stream_config
      this.yamlData.lmbench = this.configData.lmbench_config
      this.yamlData.unixbench = this.configData.unixbench_config
      this.yamlData.fio = this.configData.fio_config
      this.yamlData.iozone = this.configData.iozone_config
      this.yamlData.cpu2006 = this.configData.cpu2006_config
      this.yamlData.cpu2006_loongarch64_config = this.configData.cpu2006_loongarch64_config_config
      this.yamlData.cpu2017 = this.configData.cpu2017_config
      this.testIP = this.configData.test_ip
      this.testPassword = this.configData.test_password
      this.message = this.configData.message
      this.configDialog = false
    },

    update() {
      if (this.check()) {
        if (this.configID) {
          const formData = {
            id: this.configID,
            project_name: this.projectName,
            test_ip: this.testIP,
            test_password: this.testPassword,
            user_password: this.userPassword,
            stream: this.iterations.stream,
            lmbench: this.iterations.lmbench,
            unixbench: this.iterations.unixbench,
            fio: this.iterations.fio,
            iozone: this.iterations.iozone,
            jvm2008: this.iterations.jvm2008,
            cpu2006: this.iterations.cpu2006,
            cpu2017: this.iterations.cpu2017,
            yaml: this.yamlData,
            message: this.message
          }
          user_config('put', formData).then(response => {
            console.log(response)
          })
        }
      }
    },
    add() {
      if (this.check()) {
        const formData = {
          project_name: this.projectName,
          test_ip: this.testIP,
          test_password: this.testPassword,
          user_password: this.userPassword,
          stream: this.iterations.stream,
          lmbench: this.iterations.lmbench,
          unixbench: this.iterations.unixbench,
          fio: this.iterations.fio,
          iozone: this.iterations.iozone,
          jvm2008: this.iterations.jvm2008,
          cpu2006: this.iterations.cpu2006,
          cpu2017: this.iterations.cpu2017,
          yaml: this.yamlData,
          message: this.message
        }
        user_config('post', formData).then(response => {
          console.log(response)
        })
      }
    },
    sendTest() {
      if (this.check()) {
        const formData = {
          project_name: this.projectName,
          test_ip: this.testIP,
          test_password: this.testPassword,
          user_password: this.userPassword,
          stream: this.iterations.stream,
          lmbench: this.iterations.lmbench,
          unixbench: this.iterations.unixbench,
          fio: this.iterations.fio,
          iozone: this.iterations.iozone,
          jvm2008: this.iterations.jvm2008,
          cpu2006: this.iterations.cpu2006,
          cpu2017: this.iterations.cpu2017,
          yaml: this.yamlData,
          message: this.message
        }
        do_test_case(formData).then(response => {
          console.log(response.data.code);
          this.projectName = ''
          this.testIP = ''
          this.testPassword = ''
          this.userPassword = ''
          this.iterations.stream = ''
          this.iterations.lmbench = ''
          this.iterations.unixbench = ''
          this.iterations.fio = ''
          this.iterations.iozone = ''
          this.iterations.jvm2008 = ''
          this.iterations.cpu2006 = ''
          this.iterations.cpu2017 = ''
          this.yamlData = ''
          this.message = ''
        });
        ElMessage({message: '发起测试完成，正在跳转只测试列表页面', type: 'success'});
      }
    },
    check() {
      if (!this.projectName) {
        ElMessage({message: "项目名称不能为空", type: 'error'});
        return false;
      }
      if (!this.userPassword) {
        ElMessage({message: "kytuning用户密码不能为空", type: 'error'});
        return false;
      }
      const iterations = {
        stream: this.iterations.stream !== '' ? parseInt(this.iterations.stream) : 0,
        lmbench: this.iterations.lmbench !== '' ? parseInt(this.iterations.lmbench) : 0,
        unixbench: this.iterations.unixbench !== '' ? parseInt(this.iterations.unixbench) : 0,
        fio: this.iterations.fio !== '' ? parseInt(this.iterations.fio) : 0,
        iozone: this.iterations.iozone !== '' ? parseInt(this.iterations.iozone) : 0,
        jvm2008: this.iterations.jvm2008 !== '' ? parseInt(this.iterations.jvm2008) : 0,
        cpu2006: this.iterations.cpu2006 !== '' ? parseInt(this.iterations.cpu2006) : 0,
        cpu2017: this.iterations.cpu2017 !== '' ? parseInt(this.iterations.cpu2017) : 0,
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
      this.iterations = iterations
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