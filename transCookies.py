# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = 'd_c0="AFBAdndwgQqPTrHSrrQTeeu2SiSh7ZsyS2k=|1473265217"; _za=aa02a2b6-53d1-42ed-95bf-ffdb2eb9ad10; _zap=93f17464-0d39-4bc0-adee-51b2a0a74bc7; q_c1=fa67bc696d7b42a6ab498067f2a1bdef|1492358197000|1473265217000; capsion_ticket="2|1:0|10:1492358378|14:capsion_ticket|44:MzcwOTQ2MThkNTlkNDdiZjljYmQ5OGNhYjhlMThlNjg=|6822c284a9dc3896b4726c8f0f86d1c9e5029fc878c808ff682a4a3bdbb336bd"; aliyungf_tc=AQAAAMk0PAR31gAAeTgofV9kUPgirQ53; _xsrf=5e0d4a351caa73ed28431284614a0f72; acw_tc=AQAAABvAng4oTQwAXjgofZqLwJ/9RSYd; r_cap_id="YTU2NTlhNmIzZGFkNGQzZWExZjgwZjNhOThlNDNmNTg=|1492826545|45a2bd2bccf4803991b0101910477957ab1d1b1b"; cap_id="YmI3NTM4OWU0OWVmNDk1ZGFlMjgwN2UxNzI2ODFkMGQ=|1492826545|b38636a20bbac2b0798e7426a334dce6249758d9"; l_n_c=1; z_c0=Mi4wQUFDQXpfSWlBQUFBVUVCMmQzQ0JDaGNBQUFCaEFsVk53MFlpV1FENk9VSEpmUk9ZN1RXR0xKbE9Ddjg1VDVnTTVR|1492873987|74118f536c62e9f53c43747706f734cf7f3df8fc'
    trans = transCookie(cookie)
    print(trans.stringToDict())