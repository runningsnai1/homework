import requests

# 获取token
def test_token1():
    corpid = "ww7036f1b0e567408b"
    corpsecret = "vEzFRNazxj62Bc6aFCaRfSK7hjCLdA5_rTya3078zoE"
    r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return r.json()["access_token"]

# 查询已有部门
def test_getdepartment():
    r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token1()}")
    print(r.json())

# 创建子部门
def test_createdepartment():
    body={
        "name": "张三",
        "name_en": "zhangsan",
        "parentid": 1,
    }
    r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token1()}",
                    json=body
                    )
    print(r.json())

# 修改刚建的子部门名称
def test_updatedepartment():
    body={
        "name": "李四",
        "name_en": "lisi",
        "id":2
    }
    r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token1()}",
                    json=body
                    )
    print(r.json())
#
# 删除刚建的子部门
def test_deletedepartment():
    r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token1()}&id=2")
    print(r.json())