# -*- coding: utf-8 -*-
import scrapy
import json
import re
from zhihu.items import ZhihuItem
from scrapy_redis.spiders import RedisCrawlSpider

class UserinforSpider(RedisCrawlSpider):
    name = 'userinfor'
    redis_key = "myspider:start_urls"
    allowed_domains = ['zhihu.com']
    # start_urls = ['https://www.zhihu.com/api/v4/members/excited-vczh/followers?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=20&limit=20']

    def parse(self, response):

        # print(response.body.decode("utf-8", "ignore"))
        print(response.body.decode("utf-8", "ignore"))
        response_data = json.loads(response.body.decode("utf-8", "ignore"))["data"]
        # print(len(response_data))
        # print('**'*20)
        count = len(response_data)
        if count < 20:
            pass
        else:
            page_offset = int(re.findall("&offset=(.*?)&", response.url)[0])
            new_page_offset = page_offset + 20
            next_page_url = response.url.replace("&offset=" + str(page_offset)+"&", "&offset="+str(new_page_offset)+"&")
            yield scrapy.Request(url=next_page_url, callback=self.parse)

        for eve_user in response_data:
            item = ZhihuItem()
            item["name"] = eve_user["name"]
            item["is_advertiser"] = eve_user["is_advertiser"]
            item["avatar_url_template"] = eve_user["avatar_url_template"]
            item["user_type"] = eve_user["user_type"]
            item["answer_count"] = eve_user["answer_count"]
            item["type"] = eve_user["type"]
            item["url_token"] = eve_user["url_token"]
            item["user_id"] = eve_user["id"]
            item["articles_count"] = eve_user["articles_count"]
            item["url"] = eve_user["url"]
            item["gender"] = eve_user["gender"]
            item["headline"] = eve_user["headline"]
            item["avatar_url"] = eve_user["avatar_url"]
            item["is_org"] = eve_user["is_org"]
            item["follower_count"] = eve_user["follower_count"]

            #去重
            with open("userinfor.txt") as f:
                user_list = f.read()

            if eve_user["url_token"] not in user_list:
                with open("userinfor.txt", "a") as f:
                    f.writable()
                    f.write(eve_user["url_token"] + "----")


            yield item

            new_url = "https://www.zhihu.com/api/v4/members/" + eve_user["url_token"] + "/followers?include=data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=20&limit=20"
            yield scrapy.Request(url=new_url, callback=self.parse)
            # print(eve_user)





