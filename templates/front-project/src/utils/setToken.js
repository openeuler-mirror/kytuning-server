/*
 * Copyright (c) KylinSoft  Co., Ltd. 2024.All rights reserved.
 * PilotGo-plugin licensed under the Mulan Permissive Software License, Version 2. 
 * See LICENSE file for more details.
 * Author: wqz <wangqingzheng@kylinos.cn>
 * Date: Wed May 22 13:59:52 2024 +0800
 */
export function setToken(tokenKey, token) {
    return localStorage.setItem(tokenKey, token)
}

export function getToken(tokenKey) {
    return localStorage.getItem(tokenKey)
}

export function removeToken(tokenKey) {
    return localStorage.removeItem(tokenKey)
}