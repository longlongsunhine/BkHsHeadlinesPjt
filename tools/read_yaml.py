import os
from config import BASE_PATH
import yaml
# 定义函数
def read_yaml(filename):
    # os.sep：自动获取”/“
    file_path=os.path.join(BASE_PATH,"data",filename)
    # 定义空列表 组装测试数据
    arr=[]
    # 获取文件流
    with open(file_path,"r",encoding="utf-8") as f:
        # 遍历 调用 yaml.safe_load(f).values() 方法
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))  #将数据组装成元组
            # arr.append(list(datas.values())) #将数据组装成列表
    # 返回结果
    return arr

if __name__ == '__main__':
    filename="mp_login.yaml"
    file_path=os.path.join(BASE_PATH,"data",filename)
    # print(file_path)
    print(read_yaml(filename))
