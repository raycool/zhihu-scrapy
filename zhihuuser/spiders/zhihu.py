# -*- coding: utf-8 -*-
import json
import time
import os

import matplotlib.pyplot as plt
import scrapy
from PIL import Image
from scrapy.http import Request, FormRequest
from zhihuuser.items import ZhihuuserItem

from zhihuuser.const import *

class ZhihuSpider(scrapy.Spider):  #类变量与类实例变量
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    #登录地址
    login_url = 'https://www.zhihu.com/login/email'
    #用户信息获取地址
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    # 我关注的人
    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&amp;offset={offset}&amp;limit={limit}'
    # 关注我的人
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&amp;offset={offset}&amp;limit={limit}'
    #起始搜索用户
    start_user = 'ren-sheng-san-le-shi'
    #变量，用户信息获取地址及关注的人的必要参数
    user_query = paraDict['user_query']
    followees_query = paraDict['followees_query']
    followers_query = paraDict['followers_query']
    #http header头和cookies，cookies免登录使用
    headers = paraDict['headers']
    cookies = paraDict['cookies']

    def start_requests(self):
        # 返回值必须是一个序列，只调用一次
        #上面这个Request采用验证码的方式进行登录，登录之后获取cookies，然后可以保存到const下面
        #按格式整理好后，就可以直接利用cookies登录，cookies可以采用浏览器抓包的方式来获取，此处未添加自动保存cookies的函数

        yield Request('http://www.zhihu.com/#signin', headers=self.headers, callback=self.login, meta={'cookiejar': 1})
        #此方法为采用cookies直接进行登录，省去每次的登录步骤。
        #yield Request(self.user_url.format(user=self.start_user, include=self.user_query), headers = self.headers,cookies=self.cookies, callback=self.parse_user)
    # 获取xsrf值
    def get_xsrf(self, response):
        _xsrf = response.xpath(".//*[@id='sign-form-1']/input[2]/@value").extract()[0]
        # print(_xsrf)
        return _xsrf

    # 获取验证码的类型，en为四位英文验证码，cn为中文验证码
    def get_captcha_type(self, response):
        print(response.xpath("//div[@class='Captcha input-wrapper']").extract())
        captcha_type = response.xpath("//div[@class='Captcha input-wrapper']/@data-type").extract()
        if not captcha_type:
            captcha_type = response.xpath("//div[@class='input-wrapper captcha-module']/@data-type").extract()
        # print(captcha_type[0])
        return captcha_type[0]

    # 开始登录操作，提取登录需要的参数
    def login(self, response):
        self._xsrf = self.get_xsrf(response)
        self.captcha_lang = self.get_captcha_type(response)

        t = str(int(time.time()) * 1000)
        captcha_en_url = 'http://www.zhihu.com/captcha.gif?r=' + t + '&type=login'
        captcha_cn_url = 'http://www.zhihu.com/captcha.gif?r=' + t + '&type=login&lang=cn'
        if self.captcha_lang == 'en':
            captcha_url = captcha_en_url
        else:
            captcha_url = captcha_cn_url
        # 下载验证码图片，得到验证码后登录
        yield scrapy.Request(captcha_url, headers=self.headers, callback=self.post_login)

        # 获取中文验证码的坐标，使用ginput函数
    def get_captcha_cn(self, path):
        image = plt.imread(path)
        plt.imshow(image)
        pos = plt.ginput(0, 0)
        def change(l):
            k = []
            for i in l:
                i = list(i)
                i[0] = int(i[0]) // 2 + 0.29
                i[1] = int(i[1]) // 2 + 0.45
                k.append(i)
            return k
        input_points = change(pos)
        return input_points

    def post_login(self, response):
        #得到上层目录
        path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
        imagePath = path + '/captcha.gif'
        with open(imagePath, 'wb+') as fp:
            fp.write(response.body)
        postdata = {
            '_xsrf': self._xsrf,
            #输入帐号密码，采用邮箱登录方式
            'password': 'xxxxxxx',
            'email': 'xxxxxxxxx'
        }

        if self.captcha_lang == 'en':
            im = Image.open(imagePath)
            im.show()
            im.close()
            captcha = input('请输入验证码:')
            postdata['captcha'] = captcha

        else:
            input_points = self.get_captcha_cn(imagePath)
            captcha = {}
            captcha["img_size"] = [200, 44]
            captcha["input_points"] = input_points

            # 上送字段必须为双引号表示,注意。
            captcha = str(captcha).replace('\'', '\"')
            postdata['captcha'] = captcha
            postdata['captcha_type'] = self.captcha_lang
        yield FormRequest(url=self.login_url, formdata=postdata, method='POST', headers=self.headers,
                          callback=self.check_login)

    def check_login(self, response):
        return_str = response.body.decode()
        # print(type(return_str))
        returnmsg = json.loads(return_str)
        # print(type(returnmsg))
        ret_code = returnmsg.get('r', 1)
        if ret_code == 0:
            print('successful')
            # 登录成功，开始从第一个用户爬取数据
            yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
            #获取我关注的人的列表
            # yield Request(self.followees_url.format(user=self.start_user, include=self.followees_query, limit=20, offset=0),
            #               self.parse_followees)
            #获取关注我的人的列表
            # yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, limit=20, offset=0),
            #               self.parse_followers)
        else:
            print('failed')
            return

    def parse_user_test(self, response):
        print(response.text)

    def parse_user(self, response):
        result = json.loads(response.text)
        #print(result)
        item = ZhihuuserItem()
        #print(item.fields)
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield Request(self.followees_url.format(user=result.get('url_token'),
                      include=self.followees_query, limit=20, offset=0),self.parse_followees)
        yield Request(self.followers_url.format(user=result.get('url_token'),
                      include=self.followers_query, limit=20, offset=0),self.parse_followers)

    def parse_followees(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_followees)

    def parse_followers(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_followers)