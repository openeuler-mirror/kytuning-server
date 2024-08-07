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
import Footer from "./TableFooter.vue";
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
      this.tableDatas = value; // 访问 base 子组件的 tableDatas 数据
      this.isComparDataLoaded[0] = true
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
