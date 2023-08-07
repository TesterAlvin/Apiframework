import os
import yaml

#读取yaml的数据
def read_yaml(key):
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="r") as f:
        value = yaml.load(f,yaml.FullLoader)
        return value[key]

#写入yaml的数据
def write_yaml(data):
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)

#清空
def clear_yaml():
    with open(os.getcwd()+"/extract.yaml",encoding="utf-8",mode="w") as f:
        f.truncate()

if __name__ == '__main__':
    print(read_yaml())