<template>
  <div>
    <el-table :data="other_list" border style="width: 100%; margin-top: 20px">
      <el-table-column prop="first" label="Unixbench" min-width="80%"></el-table-column>
      <el-table-column prop="second" label="Unixbench#1"></el-table-column>
    </el-table>
  </div>
  <div>
    <el-table :data="tableDatas" :span-method="objectSpanMethod" border style="width: 100%" :show-header="false">
      <el-table-column prop="ThreadType" align="center" min-width="30%"></el-table-column>
      <el-table-column prop="second" align="center" min-width="30%"></el-table-column>
      <el-table-column prop="third" align="center" min-width="20%"></el-table-column>
      <el-table-column prop="fourth"></el-table-column>
    </el-table>
  </div>
  <div>
    <!-- Your page content here -->
    <button @click="onClick">Click me!</button>
  </div>
</template>


<script>
import axios from 'axios'
import {ElTable, ElTableColumn} from 'element-plus';

export default {
  components: {
    ElTable,
    ElTableColumn,
  },
  data() {
    return {
      other_list: [{first: '执行命令', second: './Run -c {FUNC_THREAD_NUM}'}, {first: '修改参数：', second: 'xxx'}],
      cpu2006_datas: {
        single_int_400_perlbench: '',
        single_int_401_bzip2: '',
        single_int_403_gcc: '',
        single_int_429_mcf: '',
        single_int_445_gobmk: '',
        single_int_456_hmmer: '',
        single_int_458_sjeng: '',
        single_int_462_libquantum: '',
        single_int_464_h264ref: '',
        single_int_471_omnetpp: '',
        single_int_473_astar: '',
        single_int_483_xalancbmk: '',
        single_int_SPECint_2006: '',
        single_fp_410_bwaves: '',
        single_fp_416_gamess: '',
        single_fp_433_milc: '',
        single_fp_434_zeusmp: '',
        single_fp_435_gromacs: '',
        single_fp_436_cactusADM: '',
        single_fp_437_leslie3d: '',
        single_fp_444_namd: '',
        single_fp_447_dealII: '',
        single_fp_450_soplex: '',
        single_fp_453_povray: '',
        single_fp_454_calculix: '',
        single_fp_459_GemsFDTD: '',
        single_fp_465_tonto: '',
        single_fp_470_lbm: '',
        single_fp_481_wrf: '',
        single_fp_482_sphinx3: '',
        single_fp_SPECfp_2006: '',

        multi_int_400_perlbench: '',
        multi_int_401_bzip2: '',
        multi_int_403_gcc: '',
        multi_int_429_mcf: '',
        multi_int_445_gobmk: '',
        multi_int_456_hmmer: '',
        multi_int_458_sjeng: '',
        multi_int_462_libquantum: '',
        multi_int_464_h264ref: '',
        multi_int_471_omnetpp: '',
        multi_int_473_astar: '',
        multi_int_483_xalancbmk: '',
        multi_int_SPECint_2006: '',
        multi_fp_410_bwaves: '',
        multi_fp_416_gamess: '',
        multi_fp_433_milc: '',
        multi_fp_434_zeusmp: '',
        multi_fp_435_gromacs: '',
        multi_fp_436_cactusADM: '',
        multi_fp_437_leslie3d: '',
        multi_fp_444_namd: '',
        multi_fp_447_dealII: '',
        multi_fp_450_soplex: '',
        multi_fp_453_povray: '',
        multi_fp_454_calculix: '',
        multi_fp_459_GemsFDTD: '',
        multi_fp_465_tonto: '',
        multi_fp_470_lbm: '',
        multi_fp_481_wrf: '',
        multi_fp_482_sphinx3: '',
        multi_fp_SPECfp_2006: '',
      },
      getCpu2006Datas: [],
      multiThreaddata: [],
      singleThreaddata: [],

    }
  },
  computed: {
    tableDatas() {
      return [
        {ThreadType: '单线程', second: 'int', third: '400.perlbench', fourth: this.cpu2006_datas.single_int_400_perlbench},
        {ThreadType: '单线程', second: 'int', third: '401.bzip2', fourth: this.cpu2006_datas.single_int_401_bzip2},
        {ThreadType: '单线程', second: 'int', third: '403.gcc', fourth: this.cpu2006_datas.single_int_403_gcc},
        {ThreadType: '单线程', second: 'int', third: '429.mcf', fourth: this.cpu2006_datas.single_int_429_mcf},
        {ThreadType: '单线程', second: 'int', third: '445.gobmk', fourth: this.cpu2006_datas.single_int_445_gobmk},
        {ThreadType: '单线程', second: 'int', third: '456.hmmer', fourth: this.cpu2006_datas.single_int_456_hmmer},
        {ThreadType: '单线程', second: 'int', third: '458.sjeng', fourth: this.cpu2006_datas.single_int_458_sjeng},
        {ThreadType: '单线程', second: 'int', third: '462.libquantum', fourth: this.cpu2006_datas.single_int_462_libquantum},
        {ThreadType: '单线程', second: 'int', third: '464.h264ref', fourth: this.cpu2006_datas.single_int_464_h264ref},
        {ThreadType: '单线程', second: 'int', third: '471.omnetpp', fourth: this.cpu2006_datas.single_int_471_omnetpp},
        {ThreadType: '单线程', second: 'int', third: '473.astar', fourth: this.cpu2006_datas.single_int_473_astar},
        {ThreadType: '单线程', second: 'int', third: '483.xalancbmk', fourth: this.cpu2006_datas.single_int_483_xalancbmk},
        {ThreadType: '单线程', second: 'int', third: 'SPECint_2006', fourth: this.cpu2006_datas.single_int_SPECint_2006},
        {ThreadType: '单线程', second: 'fp', third: '410.bwaves', fourth: this.cpu2006_datas.single_fp_410_bwaves},
        {ThreadType: '单线程', second: 'fp', third: '416.gamess', fourth: this.cpu2006_datas.single_fp_416_gamess},
        {ThreadType: '单线程', second: 'fp', third: '433.milc', fourth: this.cpu2006_datas.single_fp_433_milc},
        {ThreadType: '单线程', second: 'fp', third: '434.zeusmp', fourth: this.cpu2006_datas.single_fp_434_zeusmp},
        {ThreadType: '单线程', second: 'fp', third: '435.gromacs', fourth: this.cpu2006_datas.single_fp_435_gromacs},
        {ThreadType: '单线程', second: 'fp', third: '436.cactusADM', fourth: this.cpu2006_datas.single_fp_436_cactusADM},
        {ThreadType: '单线程', second: 'fp', third: '437.leslie3d', fourth: this.cpu2006_datas.single_fp_437_leslie3d},
        {ThreadType: '单线程', second: 'fp', third: '444.namd', fourth: this.cpu2006_datas.single_fp_444_namd},
        {ThreadType: '单线程', second: 'fp', third: '447.dealII', fourth: this.cpu2006_datas.single_fp_447_dealII},
        {ThreadType: '单线程', second: 'fp', third: '450.soplex', fourth: this.cpu2006_datas.single_fp_450_soplex},
        {ThreadType: '单线程', second: 'fp', third: '453.povray', fourth: this.cpu2006_datas.single_fp_453_povray},
        {ThreadType: '单线程', second: 'fp', third: '454.calculix', fourth: this.cpu2006_datas.single_fp_454_calculix},
        {ThreadType: '单线程', second: 'fp', third: '459.GemsFDTD', fourth: this.cpu2006_datas.single_fp_459_GemsFDTD},
        {ThreadType: '单线程', second: 'fp', third: '465.tonto', fourth: this.cpu2006_datas.single_fp_465_tonto},
        {ThreadType: '单线程', second: 'fp', third: '470.lbm', fourth: this.cpu2006_datas.single_fp_470_lbm},
        {ThreadType: '单线程', second: 'fp', third: '481.wrf', fourth: this.cpu2006_datas.single_fp_481_wrf},
        {ThreadType: '单线程', second: 'fp', third: '482.sphinx3', fourth: this.cpu2006_datas.single_fp_482_sphinx3},
        {ThreadType: '单线程', second: 'fp', third: 'SPECfp_2006', fourth: this.cpu2006_datas.single_fp_SPECfp_2006},
        {ThreadType: '多线程', second: 'int', third: '400.perlbench', fourth: this.cpu2006_datas.multi_int_400_perlbench},
        {ThreadType: '多线程', second: 'int', third: '401.bzip2', fourth: this.cpu2006_datas.multi_int_401_bzip2},
        {ThreadType: '多线程', second: 'int', third: '403.gcc', fourth: this.cpu2006_datas.multi_int_403_gcc},
        {ThreadType: '多线程', second: 'int', third: '429.mcf', fourth: this.cpu2006_datas.multi_int_429_mcf},
        {ThreadType: '多线程', second: 'int', third: '445.gobmk', fourth: this.cpu2006_datas.multi_int_445_gobmk},
        {ThreadType: '多线程', second: 'int', third: '456.hmmer', fourth: this.cpu2006_datas.multi_int_456_hmmer},
        {ThreadType: '多线程', second: 'int', third: '458.sjeng', fourth: this.cpu2006_datas.multi_int_458_sjeng},
        {ThreadType: '多线程', second: 'int', third: '462.libquantum', fourth: this.cpu2006_datas.multi_int_462_libquantum},
        {ThreadType: '多线程', second: 'int', third: '464.h264ref', fourth: this.cpu2006_datas.multi_int_464_h264ref},
        {ThreadType: '多线程', second: 'int', third: '471.omnetpp', fourth: this.cpu2006_datas.multi_int_471_omnetpp},
        {ThreadType: '多线程', second: 'int', third: '473.astar', fourth: this.cpu2006_datas.multi_int_473_astar},
        {ThreadType: '多线程', second: 'int', third: '483.xalancbmk', fourth: this.cpu2006_datas.multi_int_483_xalancbmk},
        {ThreadType: '多线程', second: 'int', third: 'SPECint_2006', fourth: this.cpu2006_datas.multi_int_SPECint_2006},
        {ThreadType: '多线程', second: 'fp', third: '410.bwaves', fourth: this.cpu2006_datas.multi_fp_410_bwaves},
        {ThreadType: '多线程', second: 'fp', third: '416.gamess', fourth: this.cpu2006_datas.multi_fp_416_gamess},
        {ThreadType: '多线程', second: 'fp', third: '433.milc', fourth: this.cpu2006_datas.multi_fp_433_milc},
        {ThreadType: '多线程', second: 'fp', third: '434.zeusmp', fourth: this.cpu2006_datas.multi_fp_434_zeusmp},
        {ThreadType: '多线程', second: 'fp', third: '435.gromacs', fourth: this.cpu2006_datas.multi_fp_435_gromacs},
        {ThreadType: '多线程', second: 'fp', third: '436.cactusADM', fourth: this.cpu2006_datas.multi_fp_436_cactusADM},
        {ThreadType: '多线程', second: 'fp', third: '437.leslie3d', fourth: this.cpu2006_datas.multi_fp_437_leslie3d},
        {ThreadType: '多线程', second: 'fp', third: '444.namd', fourth: this.cpu2006_datas.multi_fp_444_namd},
        {ThreadType: '多线程', second: 'fp', third: '447.dealII', fourth: this.cpu2006_datas.multi_fp_447_dealII},
        {ThreadType: '多线程', second: 'fp', third: '450.soplex', fourth: this.cpu2006_datas.multi_fp_450_soplex},
        {ThreadType: '多线程', second: 'fp', third: '453.povray', fourth: this.cpu2006_datas.multi_fp_453_povray},
        {ThreadType: '多线程', second: 'fp', third: '454.calculix', fourth: this.cpu2006_datas.multi_fp_454_calculix},
        {ThreadType: '多线程', second: 'fp', third: '459.GemsFDTD', fourth: this.cpu2006_datas.multi_fp_459_GemsFDTD},
        {ThreadType: '多线程', second: 'fp', third: '465.tonto', fourth: this.cpu2006_datas.multi_fp_465_tonto},
        {ThreadType: '多线程', second: 'fp', third: '470.lbm', fourth: this.cpu2006_datas.multi_fp_470_lbm},
        {ThreadType: '多线程', second: 'fp', third: '481.wrf', fourth: this.cpu2006_datas.multi_fp_481_wrf},
        {ThreadType: '多线程', second: 'fp', third: '482.sphinx3', fourth: this.cpu2006_datas.multi_fp_482_sphinx3},
        {ThreadType: '多线程', second: 'fp', third: 'SPECfp_2006', fourth: this.cpu2006_datas.multi_fp_SPECfp_2006},
      ]
    }
  },
  created() {
    axios.get('/api/cpu2006/?env_id=' + this.$route.params.baseId).then((response) => {
      this.getCpu2006Datas = response.data.data
      //判断getCpu2006Datas是否有两组数据
      if (this.getCpu2006Datas[0].thread === '单线程') {
        this.singleThreaddata = this.getCpu2006Datas[0]
        this.MultiThreaddata = this.getCpu2006Datas[1]
      } else if (this.getCpu2006Datas[0].thread === '多线程') {
        this.MultiThreaddata = this.getCpu2006Datas[0]
        this.singleThreaddata = this.getCpu2006Datas[1]
      }
      this.other_list[0].second = this.singleThreaddata.execute_cmd
      this.other_list[1].second = this.singleThreaddata.modify_parameters
      console.log(this.singleThreaddata,111111)
      console.log(this.singleThreaddata.int_400_perlbench,222)
      console.log(this.singleThreaddata.fp_433_milc,222)
      this.cpu2006_datas.single_int_400_perlbench = this.singleThreaddata.int_400_perlbench
      this.cpu2006_datas.single_int_401_bzip2 = this.singleThreaddata.int_401_bzip2Precision
      this.cpu2006_datas.single_int_403_gcc = this.singleThreaddata.int_403_gcchroughput
      this.cpu2006_datas.single_int_429_mcf = this.singleThreaddata.int_429_mcf_1024
      this.cpu2006_datas.single_int_445_gobmk = this.singleThreaddata.int_445_gobmk256
      this.cpu2006_datas.single_int_456_hmmer = this.singleThreaddata.int_456_hmmer_4096
      this.cpu2006_datas.single_int_458_sjeng = this.singleThreaddata.int_458_sjengoughput
      this.cpu2006_datas.single_int_462_libquantum = this.singleThreaddata.int_462_libquantum
      this.cpu2006_datas.single_int_464_h264ref = this.singleThreaddata.int_464_h264ref_creation
      this.cpu2006_datas.single_int_471_omnetpp = this.singleThreaddata.int_471_omnetppripts_1
      this.cpu2006_datas.single_int_473_astar = this.singleThreaddata.int_473_astarripts_8
      this.cpu2006_datas.single_int_483_xalancbmk = this.singleThreaddata.int_483_xalancbmktem_call_overhead
      this.cpu2006_datas.single_int_SPECint_2006 = this.singleThreaddata.int_SPECint_2006
      this.cpu2006_datas.single_fp_410_bwaves = this.singleThreaddata.fp_410_bwaves
      this.cpu2006_datas.single_fp_416_gamess = this.singleThreaddata.fp_416_gamess_Precision
      this.cpu2006_datas.single_fp_433_milc = this.singleThreaddata.fp_433_milcthroughput
      this.cpu2006_datas.single_fp_434_zeusmp = this.singleThreaddata.fp_434_zeusmpy_1024
      this.cpu2006_datas.single_fp_435_gromacs = this.singleThreaddata.fp_435_gromacs_256
      this.cpu2006_datas.single_fp_436_cactusADM = this.singleThreaddata.fp_436_cactusADMy_4096
      this.cpu2006_datas.single_fp_437_leslie3d = this.singleThreaddata.fp_437_leslie3droughput
      this.cpu2006_datas.single_fp_444_namd = this.singleThreaddata.fp_444_namd
      this.cpu2006_datas.single_fp_447_dealII = this.singleThreaddata.fp_447_dealIIs_creation
      this.cpu2006_datas.single_fp_450_soplex = this.singleThreaddata.fp_450_soplexcripts_1
      this.cpu2006_datas.single_fp_453_povray = this.singleThreaddata.fp_453_povraycripts_8
      this.cpu2006_datas.single_fp_454_calculix = this.singleThreaddata.fp_454_calculixstem_call_overhead
      this.cpu2006_datas.single_fp_459_GemsFDTD = this.singleThreaddata.fp_459_GemsFDTD
      this.cpu2006_datas.single_fp_465_tonto = this.singleThreaddata.fp_465_tonto
      this.cpu2006_datas.single_fp_470_lbm = this.singleThreaddata.fp_470_lbm
      this.cpu2006_datas.single_fp_481_wrf = this.singleThreaddata.fp_481_wrf
      this.cpu2006_datas.single_fp_482_sphinx3 = this.singleThreaddata.fp_482_sphinx3
      this.cpu2006_datas.single_fp_SPECfp_2006 = this.singleThreaddata.fp_SPECfp_2006
      this.cpu2006_datas.multi_int_400_perlbench = this.MultiThreaddata.int_400_perlbench
      this.cpu2006_datas.multi_int_401_bzip2 = this.MultiThreaddata.int_401_bzip2
      this.cpu2006_datas.multi_int_403_gcc = this.MultiThreaddata.int_403_gcc
      this.cpu2006_datas.multi_int_429_mcf = this.MultiThreaddata.int_429_mcf
      this.cpu2006_datas.multi_int_445_gobmk = this.MultiThreaddata.int_445_gobmk
      this.cpu2006_datas.multi_int_456_hmmer = this.MultiThreaddata.int_456_hmmer
      this.cpu2006_datas.multi_int_458_sjeng = this.MultiThreaddata.int_458_sjeng
      this.cpu2006_datas.multi_int_462_libquantum = this.MultiThreaddata.int_462_libquantum
      this.cpu2006_datas.multi_int_464_h264ref = this.MultiThreaddata.int_464_h264ref
      this.cpu2006_datas.multi_int_471_omnetpp = this.MultiThreaddata.int_471_omnetpp
      this.cpu2006_datas.multi_int_473_astar = this.MultiThreaddata.int_473_astar
      this.cpu2006_datas.multi_int_483_xalancbmk = this.MultiThreaddata.int_483_xalancbmk
      this.cpu2006_datas.multi_int_SPECint_2006 = this.MultiThreaddata.int_SPECint_2006
      this.cpu2006_datas.multi_fp_410_bwaves = this.MultiThreaddata.fp_410_bwaves
      this.cpu2006_datas.multi_fp_416_gamess = this.MultiThreaddata.fp_416_gamess
      this.cpu2006_datas.multi_fp_433_milc = this.MultiThreaddata.fp_433_milc
      this.cpu2006_datas.multi_fp_434_zeusmp = this.MultiThreaddata.fp_434_zeusmp
      this.cpu2006_datas.multi_fp_435_gromacs = this.MultiThreaddata.fp_435_gromacs
      this.cpu2006_datas.multi_fp_436_cactusADM = this.MultiThreaddata.fp_436_cactusADM
      this.cpu2006_datas.multi_fp_437_leslie3d = this.MultiThreaddata.fp_437_leslie3d
      this.cpu2006_datas.multi_fp_444_namd = this.MultiThreaddata.fp_444_namd
      this.cpu2006_datas.multi_fp_447_dealII = this.MultiThreaddata.fp_447_dealII
      this.cpu2006_datas.multi_fp_450_soplex = this.MultiThreaddata.fp_450_soplex
      this.cpu2006_datas.multi_fp_453_povray = this.MultiThreaddata.fp_453_povray
      this.cpu2006_datas.multi_fp_454_calculix = this.MultiThreaddata.fp_454_calculix
      this.cpu2006_datas.multi_fp_459_GemsFDTD = this.MultiThreaddata.fp_459_GemsFDTD
      this.cpu2006_datas.multi_fp_465_tonto = this.MultiThreaddata.fp_465_tonto
      this.cpu2006_datas.multi_fp_470_lbm = this.MultiThreaddata.fp_470_lbm
      this.cpu2006_datas.multi_fp_481_wrf = this.MultiThreaddata.fp_481_wrf
      this.cpu2006_datas.multi_fp_482_sphinx3 = this.MultiThreaddata.fp_482_sphinx3
      this.cpu2006_datas.multi_fp_SPECfp_2006 = this.MultiThreaddata.fp_SPECfp_2006
    })
  },
  methods: {
    // 单元格的处理方法 当前行row、当前列column、当前行号rowIndex、当前列号columnIndex
    objectSpanMethod({rowIndex, columnIndex}) {
      //columnIndex 表示需要合并的列，多列时用 || 隔开
      if (columnIndex === 0 || columnIndex === 1) {
        const _row = this.filterData(this.tableDatas, columnIndex).one[rowIndex];
        const _col = _row > 0 ? 1 : 0;  // 为0是不执行合并。 为1是从当前单元格开始，执行合并1列
        return {
          rowspan: _row,
          colspan: _col,
        }
      }
    },
    filterData(arr, colIndex) {
      let spanOneArr = [];
      let concatOne = 0;
      arr.forEach((item, index) => {
        if (index === 0) {
          spanOneArr.push(1);
        } else {
          //first second 分别表示表格数据第一列和第二列对应的参数字段，根据实际参数修改
          if (colIndex === 0) {
            if (item['ThreadType'] === arr[index - 1]['ThreadType']) {
              spanOneArr[concatOne] += 1;
              spanOneArr.push(0);
            } else {
              spanOneArr.push(1);
              concatOne = index;
            }
          } else {
            if (item.second === arr[index - 1].second) {
              spanOneArr[concatOne] += 1;
              spanOneArr.push(0);
            } else {
              spanOneArr.push(1);
              concatOne = index;
            }
          }
        }
      });
      return {
        one: spanOneArr,
      };
    }
  }
};
</script>

<style>
@import url("//unpkg.com/element-ui@2.15.13/lib/theme-chalk/index.css");
</style>
