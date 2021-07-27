import logging
from time import localtime, time,strftime

class LogInfo():
    def get_logtime(self):
        t1 = strftime('%Y_%m_%d_%H',localtime(time()))
        return t1
    def read_log(self):
        # 日志器
        log = logging.getLogger()
        # 日志等级为INFO
        log.setLevel(logging.INFO)

        # 设置日志位置
        sh = logging.StreamHandler()
        fh = logging.FileHandler('../Logger/mylogs/logs_{}.log'.format(self.get_logtime()), encoding='utf-8')

        # 设置日志输出格式及内容
        formation = logging.Formatter('%(levelname)s  %(asctime)s     %(filename)s   %(message)s')
        # 添加日志显示格式
        sh.setFormatter(formation)
        fh.setFormatter(formation)

        log.addHandler(sh)
        log.addHandler(fh)
        return log