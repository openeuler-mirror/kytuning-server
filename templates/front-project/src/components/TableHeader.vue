<template>
  <div class="tableHome">
    <template v-if="isAllDataLoaded">
<!--      <Left :dataName="dataName" :baseId="baseId" :comparsionIds="comparsionIds" ref="leftComponent" @data-loaded="accessChildData"/>-->
      <el-container class="content">
        <el-container>
          <Left :dataName="dataName" :baseId="baseId" :comparsionIds="comparsionIds" ref="leftComponent" @data-loaded="getLeftData"/>
          <Base :dataName="dataName" :baseId="baseId" comparsionIds="comparsionIds" ref="baseComponent" @data-loaded="getBaseData"/>
          <div v-for="(comparsionId,index) in comparsionIds" :key="comparsionId">{{index}}
<!--            <Compar :dataName="dataName" :baseId="comparsionId" comparsionIds="comparsionIds" ref="comparComponent" @data-loaded="accessChildData"/>-->
            <!--           传递base的数据平均值，用于计算上升还是下降 -->
            <template v-if="isComparDataLoaded[index]">
              <Compar :dataName="dataName" :baseId="comparsionId" :titleIndex="titleIndex" ref="comparComponent"
                      v-model="comparDatas[comparsionId]" @data-loaded="getComparData"/>
            </template>
          </div>
        </el-container>
      </el-container>
      <Footer :otherList="otherList" :tableDatas="tableDatas" :dataName="dataName"/>
    </template>
  </div>
</template>

<script>
// import Header from "./TableHeader.vue";
import Left from "./TableLeft.vue";
import Base from "./BaseData.vue";
import Compar from "./ComparData.vue";
import Footer from "./TableHeader.vue";

export default {
  components: {
    // Header,
    Left,
    Base,
    Compar,
    Footer
  },
  data() {
    return {
      dataName: this.$route.name,
      baseId: this.$route.params.baseId,
      titleIndex: 1,
      comparsionIds: this.$route.params.comparsionIds.split(","),

      otherList: [],
      tableTitle: [],
      tableDatas: [],
      // baseDatas:[],
      comparDatas: {}, // 初始化 comparDatas 对象

      isAllDataLoaded: false, // 标记数据是否加载完成
      isComparDataLoaded: {}, // 标记上一个compar数据是否加载完成
    };
  },
  created() {
    this.isAllDataLoaded = true;
    this.isComparDataLoaded = Array(this.comparsionIds.length + 1).fill(false)
  },
  methods: {
    getHeadrData(value) {
      // const headerComponent = this.$refs.headerComponent; // 获取 Header 子组件的引用
      // this.otherList = headerComponent.otherList; // 访问 Header 子组件的 otherList 数据

      this.otherList = value; // 访问 Header 子组件的 otherList 数据
      // 在这里处理子组件的数据

    },
    getLeftData(value) {
      this.tableTitle = value; // 访问 Left 子组件的 tableTitle 数据
      // 在这里处理子组件的数据
    },
    getBaseData(index, value) {
      this.titleIndex = index - 1
      console.log(this.isComparDataLoaded, 999);
      console.log(this.titleIndex, 888);
      this.tableDatas = value; // 访问 base 子组件的 tableDatas 数据
      this.isComparDataLoaded[0] = true
      // console.log(this.tableDatas, 333);
      // 在这里处理子组件的数据

      // const comparComponents = this.$refs.comparComponent; // 获取 base 子组件的引用
      // if (Array.isArray(comparComponents)) {
      //   // 遍历 comparComponents 数组获取每个 Compar 组件的数据
      //   comparComponents.forEach((comparComponent, index) => {
      //     const comparsionId = this.comparsionIds[index];
      //     if (comparComponent) {
      //       this.comparDatas[comparsionId] = comparComponent.comparDatas; // 访问 Compar 子组件的 comparDatas 数据
      //       console.log(comparComponent.comparDatas, 444);
      //     }
      //   });
      // }

      // const baseDatas = [
      //   {stream1: '1', stream2: '2'},
      //   {'stream1-1': '1-1', 'stream2-2': '2-2'}
      // ];
      // 遍历列表 tableDatas，并将其属性合并到列表 baseDatas(目前没有baseDatas数据，模拟一下) 中对应位置的对象,后期还要加入compar数据。
      // this.baseDatas.forEach((bObj, index) => {
      //   const aObj = this.tableDatas[index];
      //   Object.assign(aObj, bObj);
      // });
    },
    getComparData(baseId, titleIndex_, comparDatas) {
      this.comparDatas[baseId] = comparDatas;
    },
  }
};
</script>

<style>
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");
</style>
