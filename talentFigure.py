import pyecharts
import requests
import simplejson as json
import matplotlib.pyplot as plt

# import json
from pyecharts.engine import create_default_environment

from WordImg import WordImg


class data(object):
    # class persona(object):
    realName = None,
    sex = None,
    birthDate = None,
    jobPosition = None,
    country = None,
    isAbroad = None,
    education = None,

    tax = None,
    applystatus = None,


def dic2obj(d):
    top = type('new', (object,), d)
    seqs = tuple, list, set, frozenset
    for i, j in d.items():
        if isinstance(j, dict):
            setattr(top, i, dic2obj(j))
        elif isinstance(j, seqs):
            setattr(top, i,
                    type(j)(dic2obj(sj) if isinstance(sj, dict) else sj for sj in j))
        else:
            setattr(top, i, j)
    return top


def list_all_dict(dict_a):
    if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
        for x in range(len(dict_a)):
            temp_key = dict_a.keys()[x]
            temp_value = dict_a[temp_key]
            print("%s : %s" % (temp_key, temp_value))
            list_all_dict(temp_value)  # 递归调用实现无限遍历


def http_request(url, headers):
    result = requests.get(url, headers=headers)
    return result


# TODO 实现泛型,自动匹配类变量,实现实体映射框架效果
# TODO 实现嵌套解析
def convert(dict_data):
    if dict_data is not None:
        country = dict_data.get('country', None)
        jobPosition = dict_data.get('jobPosition', None)
        education = dict_data.get('education', None)
        isAbroad = dict_data.get('isAbroad', None)
        birthDate = dict_data.get('birthDate', None)
        realName = dict_data.get('realName', None)
        sex = dict_data.get('sex', None)

    #
    # data.country = country
    # data.jobPosition = jobPosition
    # data.education = education
    # data.isAbroad = isAbroad
    # data.birthDate = birthDate
    # data.realName = realName
    # data.sex = sex
    data.country = '中国'
    data.jobPosition = '经理'
    data.education = '硕士'
    data.isAbroad = '留学'
    data.birthDate = '19960322'
    data.realName = 'Bruno Mars'
    data.sex = '男'

if __name__ == '__main__':
    url = 'http://10.0.0.15:8084/talent/v1/data/persona?id=1'
    headers = {'Auth-User-Id': '51', 'Auth-User-Token': 'eaa6ef8ad01d2f8fdfaa67ae927db57c78a61311',
               'Auth-User-Role': 'GOVERNMENT'}
    # result = http_request(url, headers)
    # print("获取json结果是:\n" + result.text)

    # jsondict = json.loads(result.text)
    # jsondict = json.loads()
    # dict_data = jsondict.get('data', None)
    #
    # # 输出所有的key的列表
    # print(dict_data.keys())
    # # 输出所有项的元组
    # print(dict_data.items())

    # convert(dict_data)
    convert(None)
    print(data.country)
    print(data.jobPosition)
    print(data.education)
    print(data.isAbroad)
    print(data.birthDate)
    print(data.realName)
    print(data.sex)
    # 背景图
    maskImg = plt.imread('./image/brunomars.jpeg')
    # plt.imshow(maskImg)
    # plt.show()
    list_data = [data.country, data.jobPosition, data.education, data.isAbroad, data.birthDate, data.realName, data.sex]
    value = [1, 1, 1, 1, 1, 1, 1]

    wc = WordImg.get_word(name=list_data, value=value)

    env = create_default_environment('html')
    # 为渲染创建一个默认配置环境
    # create_default_environment(filet_ype)
    # file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'

    env.render_chart_to_file(wc, path='1.html')
