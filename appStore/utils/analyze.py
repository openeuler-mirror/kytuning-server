"""
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2.
 * See LICENSE file for more details.
 * Author: wangqingzheng <wangqingzheng@kylinos.cn>
 * Date: Fri Feb 23 11:15:41 2024 +0800
"""
#!/usr/bin/env python
# encoding: utf-8
"""
公共函数
@author: Wqz
@time: 10/5/24 3:45 PM
"""


def get_range(value_list):
    """
    :param value_list:原始分割列表
    :return: （大于5有几组数据，大于5的最小值，大于5的最大值，小于5有几组数据，小于5的最小值，小于5的最大值）
    """
    # 将数据转换为浮点数类型,列表中不能装%号类型，要么就会变成str类型，所以直接去除%处理。
    data = [float(value.replace('%', '')) if value is not None else 0.0 for value in value_list]

    # 大于5%的元素数量和范围
    greater_than_5 = [value for value in data if value >= 5]
    count_greater_than_5 = len(greater_than_5)
    min_greater_than_5 = "{:.2f}%".format(min(greater_than_5)) if greater_than_5 else None
    max_greater_than_5 = "{:.2f}%".format(max(greater_than_5)) if greater_than_5 else None

    # 小于-5%的元素数量和范围
    less_than_minus_5 = [value for value in data if value <= -5]
    count_less_than_minus_5 = len(less_than_minus_5)
    min_less_than_minus_5 = "{:.2f}%".format(-min(less_than_minus_5)) if less_than_minus_5 else None
    max_less_than_minus_5 = "{:.2f}%".format(-max(less_than_minus_5)) if less_than_minus_5 else None

    return (count_greater_than_5, min_greater_than_5, max_greater_than_5, count_less_than_minus_5, max_less_than_minus_5, min_less_than_minus_5)


def get_analyze_message(data, analyze):
    if data[0] == 1:
        analyze += '有1个单项性能提升%s，' % (data[1])
    elif data[0] > 1:
        analyze += '有%d个单项性能提升%s~%s，' % (data[0], data[1], data[2])
    if data[3] == 1:
        analyze += '有1个单项性能下降%s，' % (data[4])
    elif data[3] > 1:
        analyze += '有%d个单项性能下降%s~%s，' % (data[3], data[4], data[5])
    return analyze


def get_iozone_analyze_message(key, value, old_mark_name, number, analyze):
    name2 = key.split('-')[1].split('（')[0]
    name3 = ''
    if key.split('-')[0] == 'double':
        name1 = '两倍内存时：'
    elif key.split('-')[0] == 'full':
        name1 = '一倍内存时：'
    elif key.split('-')[0] == 'half':
        name1 = '内存一半时：'
    if value > 5:
        name3 = '提升'
    elif value < -5:
        name3 = '下降'
    if old_mark_name == name1 and name3:
        analyze += name2 + name3 + str(abs(value)) + '%，'
    elif name3 == '':
        # 数据基本持平情况
        pass
    else:
        number += 1
        old_mark_name = name1
        analyze = analyze[:-1] + ';'
        analyze += '\n%d.' % (number) + name1 + name2 + name3 + str(abs(value)) + '%，'
    return analyze, old_mark_name, number


def get_analyze_data(datas, test_type):
    """
    数据分析内容结果获取
    :param datas: 对比数据
    :param test_type: 测试类型
    :return: 数据分析结果
    """
    if test_type == 'stream':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            analyze = ''
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'
                for data in datas[4:]:
                    value = round(float(data[matching_key].strip('%')), 2)
                    if value >= 5:
                        analyze += str(data['column1']) + '的' + str(data['column2']) + '提升了' + str(value) + '%' + '\n'
                    elif value <= -5:
                        analyze += str(data['column1']) + '的' + str(data['column2']) + '提升了' + str(value) + '%' + '\n'
                if analyze == compar_name + '对比' + base_name + '\n':
                    analyze += '数据对比没有明显差距，相对持平状态。' + '\n'
                    all_analyze += analyze + '\n'
                else:
                    all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'lmbench':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            analyze = ''
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'

                # 全部的对比数据的值
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])

                Basic_system_list = compare_values[:5]
                Basic_system_value = get_range(Basic_system_list)
                if Basic_system_value[0] or Basic_system_value[3]:
                    analyze += '%d.大项Basic system parameters中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_system_value, analyze)
                    analyze += '\n'

                Processor_list = compare_values[5:16]
                Processor_value = get_range(Processor_list)
                if Processor_value[0] or Processor_value[3]:
                    analyze += '%d.大项Processor中' % (number)
                    number += 1
                    analyze = get_analyze_message(Processor_value, analyze)
                    analyze += '\n'

                Basic_integer_list = compare_values[16:21]
                Basic_integer_value = get_range(Basic_integer_list)
                if Basic_integer_value[0] or Basic_integer_value[3]:
                    analyze += '%d.大项Basic integer operations中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_integer_value, analyze)
                    analyze += '\n'

                Basic_uint64_list = compare_values[21:26]
                Basic_uint64_value = get_range(Basic_uint64_list)
                if Basic_uint64_value[0] or Basic_uint64_value[3]:
                    analyze += '%d.大项Basic uint64 operations中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_uint64_value, analyze)
                    analyze += '\n'

                Basic_float_list = compare_values[26:30]
                Basic_float_value = get_range(Basic_float_list)
                if Basic_float_value[0] or Basic_float_value[3]:
                    analyze += '%d.大项Basic float operations中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_float_value, analyze)
                    analyze += '\n'

                Basic_double_list = compare_values[30:34]
                Basic_double_value = get_range(Basic_double_list)
                if Basic_double_value[0] or Basic_double_value[3]:
                    analyze += '%d.大项Basic double operations中' % (number)
                    number += 1
                    analyze = get_analyze_message(Basic_double_value, analyze)
                    analyze += '\n'

                Context_switching_list = compare_values[34:41]
                Context_switching_value = get_range(Context_switching_list)
                if Context_switching_value[0] or Context_switching_value[3]:
                    analyze += '%d.大项Context switching中' % (number)
                    number += 1
                    analyze = get_analyze_message(Context_switching_value, analyze)
                    analyze += '\n'

                Communication_latencies_list = compare_values[41:49]
                Communication_latencies_value = get_range(Communication_latencies_list)
                if Communication_latencies_value[0] or Communication_latencies_value[3]:
                    analyze += '%d.大项*Local* Communication latencies中' % (number)
                    number += 1
                    analyze = get_analyze_message(Communication_latencies_value, analyze)
                    analyze += '\n'

                File_and_VM_list = compare_values[49:57]
                File_and_VM_value = get_range(File_and_VM_list)
                if File_and_VM_value[0] or File_and_VM_value[3]:
                    analyze += '%d.大项File & VM system latencies in microseconds中' % (number)
                    number += 1
                    analyze = get_analyze_message(File_and_VM_value, analyze)
                    analyze += '\n'

                Communication_bandwidths_list = compare_values[57:66]
                Communication_bandwidths_value = get_range(Communication_bandwidths_list)
                if Communication_bandwidths_value[0] or Communication_bandwidths_value[3]:
                    analyze += '%d.大项*Local* Communication bandwidths in MB/s - bigger is better中' % (number)
                    number += 1
                    analyze = get_analyze_message(Communication_bandwidths_value, analyze)
                    analyze += '\n'

                Memory_latencies_list = compare_values[66:71]
                Memory_latencies_value = get_range(Memory_latencies_list)
                if Memory_latencies_value[0] or Memory_latencies_value[3]:
                    analyze += '%d.大项Memory latencies in nanoseconds中' % (number)
                    number += 1
                    analyze = get_analyze_message(Memory_latencies_value, analyze)
                    analyze += '\n'
                all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'unixbench':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            analyze = ''
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'

                # 全部的对比数据的值
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])
                single_list = compare_values[:13]
                if single_list[-1]:
                    single_value = get_range(single_list[:-1])
                    if single_value[0] or single_value[3]:
                        analyze += '%d.单线程中' % (number)
                        number += 1
                        analyze = get_analyze_message(single_value, analyze)
                        single_score = float(single_list[-1].replace('%', '')) if single_list[-1] is not None else 0
                        if single_score > 2:
                            analyze += '总分提升%s%%;\n' % (single_score)
                        elif single_score < -2:
                            analyze += '总分下降%s%%;\n' % (-single_score)
                        else:
                            analyze += '总分基本持平;\n'
                    else:
                        analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.单线程总分获取失败;\n' % (number)

                multi_list = compare_values[13:26]
                if multi_list[-1]:
                    multi_value = get_range(multi_list[:-1])
                    if multi_value[0] or multi_value[3]:
                        analyze += '%d.多线程中' % (number)
                        number += 1
                        analyze = get_analyze_message(multi_value, analyze)
                        multi_score = float(multi_list[-1].replace('%', '')) if multi_list[-1] is not None else 0
                        if multi_score > 2:
                            analyze += '总分提升%s%%;\n' % (multi_score)
                        elif multi_score < -2:
                            analyze += '总分下降%s%%;\n' % (-multi_score)
                        else:
                            analyze += '总分基本持平;\n'
                    else:
                        analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.多线程总分获取失败;\n' % (number)
                all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'fio':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            analyze = ''
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'
                # 全部的对比数据的值
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])
                # compare_values[2::4]只要iops的数据
                fio_value = get_range(compare_values[2::4])
                analyze += '%d.总共测试%d项，' % (number, len(compare_values[2::4]))
                analyze = get_analyze_message(fio_value, analyze)
                analyze += '\n'
                all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'iozone':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            analyze = ''
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'
                # 全部的对比数据的名称和值
                compare_names = []
                compare_values = []
                number = 0
                old_mark_name = ''
                for data in datas[4:]:
                    compare_names.append(data['column1'])
                    compare_values.append(data[matching_key])
                compare_dict = dict(zip(compare_names, compare_values))
                for key, value in compare_dict.items():
                    value_ = float(value.replace('%', '')) if value is not None else 0.0
                    analyze, old_mark_name, number = get_iozone_analyze_message(key, value_, old_mark_name, number, analyze)
                number += 1
            all_analyze += analyze + '\n\n'
        return all_analyze
    elif test_type == 'jvm2008':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column3']
        all_analyze = ''
        for matching_key in matching_keys:
            analyze = ''
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'

                # 全部的对比数据的值
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])
                base_list = compare_values[:12]
                if base_list[-1]:
                    base_value = get_range(base_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        single_score = float(base_list[-1].replace('%', '')) if base_list[-1] is not None else 0
                        if single_score > 2:
                            analyze += '总分提升%s%%;\n' % (single_score)
                        elif single_score < -2:
                            analyze += '总分下降%s%%;\n' % (single_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base总分获取失败;\n' % (number)

                peak_list = compare_values[12:]
                if peak_list[-1]:
                    peak_value = get_range(peak_list[:-1])
                    if peak_value[0] or peak_value[3]:
                        analyze += '%d.peak' % (number)
                        number += 1
                        analyze = get_analyze_message(peak_value, analyze)
                        peak_score = float(peak_list[-1].replace('%', '')) if peak_list[-1] is not None else 0
                        if peak_score > 2:
                            analyze += '总分提升%s%%;\n' % (peak_score)
                        elif peak_score < -2:
                            analyze += '总分下降%s%%;\n' % (peak_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.peak总分获取失败;\n' % (number)
                all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'cpu2006':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column5']
        all_analyze = ''
        for matching_key in matching_keys:
            analyze = ''
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'

                # 全部的对比数据的值
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])

                base_sing_int_list = compare_values[:13]
                if base_sing_int_list[-1]:
                    base_value = get_range(base_sing_int_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base-单线程-int' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        int_score = float(base_sing_int_list[-1].replace('%', '')) if base_sing_int_list[-1] is not None else 0
                        if int_score > 2:
                            analyze += '总分提升%s%%;\n' % (int_score)
                        elif int_score < -2:
                            analyze += '总分下降%s%%;\n' % (int_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base-单线程-int总分获取失败;\n' % (number)

                base_sing_fp_list = compare_values[13:31]
                if base_sing_fp_list[-1]:
                    base_value = get_range(base_sing_fp_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base-单线程-fp' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        fp_score = float(base_sing_fp_list[-1].replace('%', '')) if base_sing_fp_list[-1] is not None else 0
                        if fp_score > 2:
                            analyze += '总分提升%s%%;\n' % (fp_score)
                        elif fp_score < -2:
                            analyze += '总分下降%s%%;\n' % (fp_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base-单线程-fp总分获取失败;\n' % (number)

                base_multi_int_list = compare_values[31:44]
                if base_multi_int_list[-1]:
                    base_value = get_range(base_multi_int_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base-多线程-int' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        int_score = float(base_multi_int_list[-1].replace('%', '')) if base_multi_int_list[-1] is not None else 0
                        if int_score > 2:
                            analyze += '总分提升%s%%;\n' % (int_score)
                        elif int_score < -2:
                            analyze += '总分下降%s%%;\n' % (int_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base-多线程-int总分获取失败;\n' % (number)

                base_multi_fp_list = compare_values[44:62]
                if base_multi_fp_list[-1]:
                    base_value = get_range(base_multi_fp_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base-多线程-fp' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        fp_score = float(base_multi_fp_list[-1].replace('%', '')) if base_multi_fp_list[-1] is not None else 0
                        if fp_score > 2:
                            analyze += '总分提升%s%%;\n' % (fp_score)
                        elif fp_score < -2:
                            analyze += '总分下降%s%%;\n' % (fp_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base-多线程-fp总分获取失败;\n' % (number)
                all_analyze += analyze + '\n'
        return all_analyze
    elif test_type == 'cpu2017':
        matching_keys = [key for key, value in datas[0].items() if value == '对比值']
        base_name = datas[1]['column6']
        all_analyze = ''
        for matching_key in matching_keys:
            analyze = ''
            compar_name = datas[1]['column' + str(int(matching_key.split('column')[-1]) - 1)]
            if compar_name:
                analyze = compar_name + '对比' + base_name + '\n'

                # 全部的对比数据的值
                compare_values = []
                number = 1
                for data in datas[4:]:
                    compare_values.append(data[matching_key])

                base_sing_int_list = compare_values[:11]
                if base_sing_int_list[-1]:
                    base_value = get_range(base_sing_int_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base-单线程-int' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        int_score = float(base_sing_int_list[-1].replace('%', '')) if base_sing_int_list[-1] is not None else 0
                        if int_score > 2:
                            analyze += '总分提升%s%%;\n' % (int_score)
                        elif int_score < -2:
                            analyze += '总分下降%s%%;\n' % (int_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base-单线程-int总分获取失败;\n' % (number)

                base_sing_fp_list = compare_values[11:25]
                if base_sing_fp_list[-1]:
                    base_value = get_range(base_sing_fp_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base-单线程-fp' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        fp_score = float(base_sing_fp_list[-1].replace('%', '')) if base_sing_fp_list[-1] is not None else 0
                        if fp_score > 2:
                            analyze += '总分提升%s%%;\n' % (fp_score)
                        elif fp_score < -2:
                            analyze += '总分下降%s%%;\n' % (fp_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base-单线程-fp总分获取失败;\n' % (number)

                base_multi_int_list = compare_values[25:36]
                if base_multi_int_list[-1]:
                    base_value = get_range(base_multi_int_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base-多线程-int' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        int_score = float(base_multi_int_list[-1].replace('%', '')) if base_multi_int_list[-1] is not None else 0
                        if int_score > 2:
                            analyze += '总分提升%s%%;\n' % (int_score)
                        elif int_score < -2:
                            analyze += '总分下降%s%%;\n' % (int_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base-多线程-int总分获取失败;\n' % (number)

                base_multi_fp_list = compare_values[36:50]
                if base_multi_fp_list[-1]:
                    base_value = get_range(base_multi_fp_list[:-1])
                    if base_value[0] or base_value[3]:
                        analyze += '%d.base-多线程-fp' % (number)
                        number += 1
                        analyze = get_analyze_message(base_value, analyze)
                        fp_score = float(base_multi_fp_list[-1].replace('%', '')) if base_multi_fp_list[-1] is not None else 0
                        if fp_score > 2:
                            analyze += '总分提升%s%%;\n' % (fp_score)
                        elif fp_score < -2:
                            analyze += '总分下降%s%%;\n' % (fp_score)
                        else:
                            analyze += '总分基本持平;\n'
                else:
                    analyze += '%d.base-多线程-fp总分获取失败;\n' % (number)
                all_analyze += analyze + '\n'
        return all_analyze
