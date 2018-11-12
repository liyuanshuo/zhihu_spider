# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
from ast import literal_eval


class ZhihuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhihuDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class change_iproxy(object):
    '''
    思考：
    1）什么时候切换IP
        本身的IP不能用的时候,也就是被ban了
    2）切换IP是否需要花钱
        使用qiyeboy的开源项目IPProxy来爬取免费的代理IP(效果可能不怎么好)
    3）如何更好的更换IP
        IPProxy默认每半个小时爬取一次免费IP
    '''

    def __init__(self):
        self.get_ip_url = "http://127.0.0.1:8000/?types=0&count=100&country=%E5%9B%BD%E5%86%85"
        self.test_ip_url = "http://www.ip111.cn/"
        self.ip_list = []
        #IP的数量， 默认100个IP
        self.ip_count = 0
        #每个IP的使用次数,每个IP使用40次
        self.each_ip_use_count = 0
        # self.get_ip_data()


    def get_ip_data(self):
        self.ip_list.clear()
        tmp_ip_data_list = literal_eval(requests.get(url=self.get_ip_url).text)
        for i in range(len(tmp_ip_data_list)):
            self.ip_list.append({"ip": tmp_ip_data_list[i][0], "port": tmp_ip_data_list[i][1]})


    def change_proxy(self, request):
        print("http://" + str(self.ip_list[self.ip_count-1]["ip"]) + ":" + str(self.ip_list[self.ip_count-1]["port"]))
        request.meta["proxy"] = "http://" + str(self.ip_list[self.ip_count-1]["ip"]) + ":" + str(self.ip_list[self.ip_count-1]["port"])

    def check_ip_useful(self):
        requests.get(url=self.test_ip_url, proxies={"http": str(self.ip_list[self.ip_count-1]["ip"]) + ":" + str(self.ip_list[self.ip_count-1]["port"])}, timeout=5)


    def if_ip_used(self, request):
        try:
            self.change_proxy(request)
            self.check_ip_useful()
        except:
            if self.ip_count == 0 or self.ip_count == 100:
                self.get_ip_data()
                self.ip_count = 1
                self.each_ip_use_count = 0
            self.ip_count += 1
            self.if_ip_used(request)



    def process_request(self, request, spider):
        if self.ip_count == 0 or self.ip_count == 100:
            self.get_ip_data()
            self.ip_count = 2
        if self.each_ip_use_count == 4000:
            self.ip_count = self.ip_count + 1
            self.each_ip_use_count = 0
            # self.change_proxy(request)
        else:
            # self.change_proxy(request)
            self.each_ip_use_count = self.each_ip_use_count + 1

        self.if_ip_used(request)
        # self.change_proxy(request)
        # tmp_ip = "115.159.31.195"
        # tmp_port = "8080"
        # request.meta["proxy"] = "http://" + tmp_ip + ":" + tmp_port
