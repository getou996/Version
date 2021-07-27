from InterfaceTest.Base_Function.BaseFunction import Base_f
from InterfaceTest.data.read_yaml import read_data
from InterfaceTest.Logger.Get_log import LogInfo
import pytest
r = Base_f()

class Test_WeatherInterface():
    @pytest.mark.parametrize('userdata',read_data())
# [{'url': 'http://apis.juhe.cn/simpleWeather/query','data': {'city': '福州', 'key': 'ignore'}}]
    def test_01(self, userdata):
        self.method = userdata['methond']
        self.url = userdata['url']
        self.data = userdata['data']
        res = r.request(self.url, self.method, self.data)
        # res = r.do_get(self.url, self.data)
        # assert 200 == res.json()['resultcode']
        # print(res.json())
        assert r.get_text(res.text,'city') == self.data['city']


        # print(self.method)

if __name__ == '__main__':
    pytest.main()
