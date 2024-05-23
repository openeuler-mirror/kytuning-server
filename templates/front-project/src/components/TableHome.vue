<template>
  <div class="tableHome">
    <template v-if="isDataLoaded">
      <Header :dataName="dataName" baseId="baseId" comparsionIds="comparsionIds" ref="headerComponent" @data-loaded="accessChildData"/>
      <Left :dataName="dataName" :baseId="baseId" :comparsionIds="comparsionIds" ref="leftComponent" @data-loaded="accessChildData"/>
<!--      <el-container class="content">-->
<!--        <el-container>-->
<!--          <Left :dataName="dataName" :baseId="baseId" :comparsionIds="comparsionIds" ref="leftComponent" @data-loaded="accessChildData"/>-->
<!--          <Base :dataName="dataName" :baseId="baseId" :comparsionIds="comparsionIds" ref="baseComponent" @data-loaded="accessChildData"/>-->
<!--          <Compar :dataName="dataName" :baseId="baseId" :comparsionIds="comparsionIds" ref="comparComponent" @data-loaded="accessChildData"/>-->
<!--        </el-container>-->
<!--      </el-container>-->
      <Footer :otherList="otherList" :tableDatas="tableDatas" :dataName="dataName"/>
    </template>
  </div>
</template>

<script>
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

      otherList: [],
      tableDatas: [],
      baseDatas: [],

      isDataLoaded: false, // 标记数据是否加载完成
    };
  },
  created() {
    this.isDataLoaded = true;
  },
  methods: {
    accessChildData() {
      const headerComponent = this.$refs.headerComponent; // 获取 Header 子组件的引用
      if (headerComponent) {
        this.otherList = headerComponent.otherList; // 访问 Header 子组件的 otherList 数据
        // 在这里处理子组件的数据
      }

      const leftComponent = this.$refs.leftComponent; // 获取 Left 子组件的引用
      if (leftComponent) {
        this.tableDatas = leftComponent.tableDatas; // 访问 Left 子组件的 tableDatas 数据
        // 在这里处理子组件的数据
      }

      const baseComponent = this.$refs.leftComponent; // 获取 Left 子组件的引用
      if (baseComponent) {
        this.baseDatas = baseComponent.tableDatas; // 访问 Left 子组件的 tableDatas 数据
        // 在这里处理子组件的数据
      }

      // const baseDatas = [
      //   {stream1: '1', stream2: '2'},
      //   {'stream1-1': '1-1', 'stream2-2': '2-2'}
      // ];
      // // 遍历列表 tableDatas，并将其属性合并到列表 baseDatas(目前没有baseDatas数据，模拟一下) 中对应位置的对象,后期还要加入compar数据。
      // baseDatas.forEach((bObj, index) => {
      //   const aObj = this.tableDatas[index];
      //   Object.assign(aObj, bObj);
      // });

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
