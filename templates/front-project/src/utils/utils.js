/*
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Wed May 22 14:08:49 2024 +0800
 */
import {ElMessage} from 'element-plus';
import {down_message} from "@/api/api";

export default {
    data() {
        return {
            currentPage: 1, //当前页数
            pageSize: 10, // 每页显示条数
            total: 0, // 总条数
            itemKey: 0, //更新数据后生成随机数从而刷新页面数据
        };
    },
    computed: {
        //分页展示当前页面
        showData() {
            return this.allDatas.slice(
                (this.currentPage - 1) * this.pageSize,
                this.currentPage * this.pageSize
            );
        },
        //数据详情页面的展示全部数据和展示平均数据
        displayTableData() {
            if (this.showAllData) {
                return this.tableDatas;
            } else {
                let count = 1;
                const modifiedTableData = JSON.parse(JSON.stringify(this.tableDatas)); // 深拷贝原始数据
                modifiedTableData.forEach(row => {
                    Object.entries(row).forEach(([key, value]) => {
                        if (typeof value === 'string' && key.startsWith('column') && value.startsWith('平均值')) {
                            row[key] = value + this.dataName.charAt(0).toUpperCase() + this.dataName.slice(1) + "#" + `${count}`; // 将"平均值"替换为"this.dataName#"
                            count++;
                        }
                    });
                });
                return modifiedTableData;
            }
        }
    },
    methods: {
        //分页
        handleSizeChange(val) {
            this.pageSize = val;
            this.currentPage = 1;
        },
        //分页
        handleCurrentChange(val) {
            this.currentPage = val;
        },
        //下载日志
        downLog(row) {
            down_message({result_log_name: row.result_log_name}).then((response) => {
                const url = window.URL.createObjectURL(new Blob([response.data]))
                const link = document.createElement('a')
                link.href = url
                link.setAttribute('download', 'log.tar')
                document.body.appendChild(link)
                link.click()
            }).catch(error => {
                if (error.code === "ERR_BAD_REQUEST") {
                    ElMessage({message: "下载失败没有找到对应日志", type: 'warning'})
                }
                console.log(error)
            }).finally(() => {
                // excelDisabled 将被设置为 true，然后立即被设置为 false,禁用的时间非常短，不足以被用户察觉到。
                this.excelDisabled = false;
            });
        },
        //处理展示的数据
        handleDataLoaded(value) {
            this.showAllData = value;
            // 在这里处理子组件的数据
        },
        //对比数据的样式和颜色
        getCellClassName(row, key) {
            let value = row[key];
            if (typeof value === 'string' && value.endsWith('%')) {
                // 去除百分比符号 "%"
                value = value.replace('%', '');
                // 将百分比转换为小数
                value = parseFloat(value);
                if (value >= 5) {
                    return 'green-cell';
                } else if (value < -5) {
                    return 'red-cell';
                }
            }
            return '';
        },
        // 单元格合并 当前行row、当前列column、当前行号rowIndex、当前列号columnIndex
        objectSpanMethod({rowIndex, columnIndex}) {
            //columnIndex 表示需要合并的列，多列时用 || 隔开
            if (columnIndex === 0) {
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
                        if (item.column1 === arr[index - 1].column1) {
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
        },
    },
};