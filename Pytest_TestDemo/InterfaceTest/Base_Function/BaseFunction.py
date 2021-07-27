from InterfaceTest.Logger.Get_log import LogInfo
import requests
from jsonpath import jsonpath
import json


class Base_f():
    log = LogInfo().read_log()
    # def do_get(self,url=None, heander=None, **kwargs):
    #     try:
    #         log.info('正在对接口{}进行GET测试'.format(url))
    #         return requests.get(url, heander, **kwargs)
    #     except Exception as e:
    #         return log.error(e)
    #
    # def do_post(self,url, data, **kwargs):
    #     try:
    #         log.info('正在对接口{}进行POST测试')
    #         return requests.post(url, data, **kwargs)
    #     except Exception as e:
    #             return log.error(e)

    def get_text(self, info,key):
            if info :
                infos = json.loads(info)
                mes =jsonpath(infos,"$..{}".format(key))
                if len(mes) == 1:
                    return mes[0]
                return mes

    def request(self,url,methond, data=None, **kwargs):
        self.log.info('-------接口请求测试开始------')
        if methond.upper() in ('GET','POST'):
            try:
                self.log.info('正在对接口 {} 发送 {} 请求测试'.format(url, methond))
                request = getattr(requests,methond)(url, data, **kwargs)
                # -------------------------------------------
                rems = self.get_text(request.text,'reason')
                self.log.info('正在发送数据{}'.format(data))
                # -----------------------------------------------
                self.log.info('接口实际返回数据为reason: {}'.format(rems))
            except Exception as e :
                return self.log.error(e)
        else:
            print('接口请求类型错误，没有该请求方式')
        self.log.info('-------接口请求测试结束------')
        return request