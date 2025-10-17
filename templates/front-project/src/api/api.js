// 项目中我们大多数时候都会把对应的接口请求封装成api来调用
import service from '../service.js'

//data 一般适用于POST、PUT请求
//params 一般适用于GET请求

// 登录接口
export function login(data) {
    return service({
        method: 'post',
        url: '/api-token-auth/',
        data
    })
}


// 测试管理列表，因为这个get请求不需要参数所以可以
export function test_case(type,data) {
    return service({
        method: type,
        url: '/test_case/',
        data
    })
}

//测试日志导出
export function down_message(params) {
    return service({
        method: 'get',
        url: '/down_message/',
        responseType: 'blob',
        params
    })
}

//发起测试
export function do_test_case(data) {
    return service({
        method: 'post',
        url: '/do_test_case/',
        data
    })
}

//配置管理
export function user_config(type, paramsOrData) {
  const commonConfig = {
    method: type,
    url: '/user_config/',
  };
  if (type === 'get') {
    commonConfig.params = paramsOrData;
  } else {
    commonConfig.data = paramsOrData;
  }
  return service(commonConfig);
}

//配置管理
export function project(type, paramsOrData) {
  const commonConfig = {
    method: type,
    url: '/project/',
  };
  if (type === 'get') {
    commonConfig.params = paramsOrData;
  } else {
    commonConfig.data = paramsOrData;
  }
  return service(commonConfig);
}


// // 获取指定的project组
// export function get_project(params) {
//     return service({
//         method: 'get',
//         url: '/project/',
//         params
//     })
// }

// // project
// export function project(type, data) {
//     return service({
//         method: type,
//         url: '/project/',
//         data
//     })
// }

// project 合并数据接口
export function mergeData(data) {
    return service({
        method: 'post',
        url: '/merge_data/',
        data
    })
}

// 筛选字段接口
export function getFilterName() {
    return service({
        method: 'get',
        url: '/get_filter_name/',
    })
}

// env
export function env(params) {
    return service({
        method: 'get',
        url: '/env/',
        params
    })
}

// // stream
// export function stream(params) {
//     return service({
//         method: 'get',
//         url: '/stream/',
//         params,
//     })
// }
//修改stream数据
export function get_modify_stream(params) {
    return service({
        method: 'get',
        url: '/get_modify_stream/',
        params,
    })
}


//修改stream数据
export function stream(type, paramsOrData) {
  const commonConfig = {
    method: type,
    url: '/stream/',
  };
  if (type === 'get') {
    commonConfig.params = paramsOrData;
  } else {
    commonConfig.data = paramsOrData;
  }
  return service(commonConfig);
}


// lmbench
export function lmbench(params) {
    return service({
        method: 'get',
        url: '/lmbench/',
        params
    })
}

// unixbench
export function unixbench(params) {
    return service({
        method: 'get',
        url: '/unixbench/',
        params
    })
}

// fio
export function fio(params) {
    return service({
        method: 'get',
        url: '/fio/',
        params
    })
}

// iozone
export function iozone(params) {
    return service({
        method: 'get',
        url: '/iozone/',
        params
    })
}

// jvm2008
export function jvm2008(params) {
    return service({
        method: 'get',
        url: '/jvm2008/',
        params
    })
}

// cpu2006
export function cpu2006(params) {
    return service({
        method: 'get',
        url: '/cpu2006/',
        params
    })
}

// cpu2017
export function cpu2017(params) {
    return service({
        method: 'get',
        url: '/cpu2017/',
        params
    })
}

// 下载excel表格接口
export function download_excel(params) {
    return service({
        method: 'get',
        url: '/download_excel/',
        responseType: 'blob',
        params
    })
}

//错误数据管理
export function error_list(type, paramsOrData) {
  const commonConfig = {
    method: type,
    url: '/error_list/',
  };
  if (type === 'get') {
    commonConfig.params = paramsOrData;
  } else {
    commonConfig.data = paramsOrData;
  }
  return service(commonConfig);
}

//设备管理
export function machine_list(type, paramsOrData) {
  const commonConfig = {
    method: type,
    url: '/machine_list/',
  };
  if (type === 'get') {
    commonConfig.params = paramsOrData;
  } else {
    commonConfig.data = paramsOrData;
  }
  return service(commonConfig);
}

//修改服务器系统信息
export function modify_server(data) {
    return service({
        method: 'post',
        url: '/modify_server/',
        data
    })
}

//机器使用完成
export function finished_using(data) {
    return service({
        method: 'post',
        url: '/finished_using/',
        data
    })
}

//申请使用设备
export function apply_use_machine(data) {
    return service({
        method: 'post',
        url: '/apply_use_machine/',
        data
    })
}
//取消申请使用设备
export function cancel_apply_use_machine(data) {
    return service({
        method: 'post',
        url: '/cancel_apply_use_machine/',
        data
    })
}





