#coding:utf-8

paraDict = {}
paraDict['user_query'] = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
paraDict['followees_query'] = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
paraDict['followers_query'] = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'


paraDict['headers'] = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'www.zhihu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    }

paraDict['cookies'] = {
        '__utma':'51854390.1452048966.1476520965.1480259118.1480602316.5',
        '__utmb':'51854390.2.10.1480602316',
        '__utmt':'1',
        '__utmv':'51854390.000--|3=entry_date=20151227=1',
        '__utmz':'51854390.1480602316.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
        '_xsrf': '69e0b57a38a855ab55876035b772c1c2',
        '_za': '14b67297-92b2-425c-8687-6ab5dd10e2dc',
        '_zap': '40eb5e6a-69fe-4c39-80ad-4807d6fe2573',
        'aliyungf_tc=':'AQAAAC8mzyDS5AEAXjgofRP9lSanx+2P',
        'acw_tc' : 'AQAAAK9fGwk6twQAXjgofehNJGCf26he',
        'cap_id': '"NzIwYWI2NzI2YmRhNDgzZjhjNzk3MDkyZGJjOTJjNmE=|1492961062|13d4b1d2ae33dfe4113329c41cc123baa6eeed4c"',
        'd_c0': '"AICAK95dtQmPTugBpUV2vX3CADki9IZdSXU=|1459570134"',
        'q_c1': 'd5d41462b25449aba9d53c2bf28d7f6b|1492358578000|1451225207000',
        'r_cap_id': '"MTMxYWQ5ZGRkOTI5NDk0YWI3ZmI0NTY0ZDRiYmM0Y2I=|1492961062|a784b0df5d3049532b94bb1dfca87cb7f215f87e"',
        'z_c0': 'Mi4wQUFDQXpfSWlBQUFBZ0lBcjNsMjFDUmNBQUFCaEFsVk5PVlFrV1FEZW51c3JUckJyUEF1WlpNd0lTbEVEWURCSHV3|1493018427|94ffd989e99396aba5a44c57860a72a74806231e',
        'l_n_c': '1'
    }