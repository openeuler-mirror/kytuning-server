<template>
  <div class="tableHome">
    <template v-if="isDataLoaded">
      <Header :dataName="dataName" baseId="baseId" comparsionIds="comparsionIds" ref="headerComponent" @data-loaded="accessChildData"/>
      <el-container class="content">
        <el-container>
          <Left :dataName="dataName" :baseId="baseId" :comparsionIds="comparsionIds" ref="leftComponent" @data-loaded="accessChildData"/>
          <!--        <Base />-->
          <!--        <Compar />-->
        </el-container>
      </el-container>
          <Footer :otherList="otherList" :tableDatas="tableDatas" :dataName="dataName"/>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
import Header from "./TableHeader.vue";
import Left from "./TableLeft.vue";
// import Base from "./BaseData.vue";
// import Compar from "./ComparData.vue";
import Footer from "./TableFooter.vue";
export default {
  components: {
    Header,
    Left,
    // Base,
    // Compar,
    Footer
  },
  data() {
    return {
      dataName: this.$route.name,
      baseId: this.$route.params.baseId,
      comparsionIds: this.$route.params.comparsionIds,
      leftComponent: null, // 存储 Left 组件的引用

      otherList:[],
      tableDatas:[],

      isDataLoaded: false, // 标记数据是否加载完成
    };
  },
  created() {
    axios.get('/api/stream/?env_id=' + this.$route.params.baseId + '&comparsionIds=' + this.$route.params.comparsionIds).then((response) => {
      this.otherList = response.data.data.others
      this.numColumns = Object.keys(response.data.data.others[0]).length
      this.isDataLoaded = true;
    }).catch((error) => {
      console.error('Error fetching data:', error);
    });
  },
  methods: {
    accessChildData() {
      const headerComponent = this.$refs.headerComponent; // 获取 Header 子组件的引用
      if (headerComponent) {
        this.otherList = headerComponent.otherList; // 访问 Header 子组件的 otherList 数据
        // 在这里处理子组件的数据
        console.log(this.otherList, 444);
      }

      const leftComponent = this.$refs.leftComponent; // 获取 Left 子组件的引用
      if (leftComponent) {
        this.tableDatas = leftComponent.tableDatas; // 访问 Left 子组件的 tableDatas 数据
        // 在这里处理子组件的数据
        console.log(this.tableDatas, 555);
      }
    },
  }
};
</script>

<style>
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");

button {
  border: none;
  padding: 15px 30px;
  font-size: 16px;
  font-family: Arial, 微软雅黑;
  color: white;
  background: #447aa8;
  border-radius: 3px;
}
</style>
