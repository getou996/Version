import yaml


def read_data():
    file = open('../data/interface.yaml', encoding='utf-8')
    # 读取yaml中的数据，并且以数组list的形式返回
    interface_data = yaml.load(file, yaml.FullLoader)

    # [{'url': 'http://apis.juhe.cn/simpleWeather/query', 'data': {'city': '福州', 'key': 'ignore'}}]
    # for k,v in interface_data[0].items():
    #     print(k,v)
    # print(interface_data)
    # print(type(interface_data))
    return interface_data
# file = open('../data/interface.yaml', encoding='utf-8')
# #     # 读取yaml中的数据，并且以数组list的形式返回
# interface_data = yaml.load(file, yaml.FullLoader)
#     print(url,data,text)
