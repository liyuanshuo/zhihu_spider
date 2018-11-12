# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from copyheaders import headers_raw_to_dict

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

#数据库的设置
MONGODB_HOST = '192.168.43.131'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'zhihu'
MONGODB_DOCNAME = 'userinfor'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.5",
"Connection": "keep-alive",
"Cookie": '_zap=96303539-19e9-4bec-afbf-9a35cf8a3c2c; d_c0="ALAmfS0hYw6PToYbiV5ZQSQaqA7sbhEDfEg=|1539950643"; _xsrf=vad1TYalpVzoBf7hR5emKTScFfV7zk2C; capsion_ticket="2|1:0|10:1540042613|14:capsion_ticket|44:YWY0OTFhYTI5NzAyNDI5Mzk2ZDUxNTY4YzQ0Y2ExZjI=|677a4140b7cd7a5a3799061018556d009e566c28ec5a2759b5457a4db5876b71"; tgw_l7_route=ec452307db92a7f0fdb158e41da8e5d8',
"Host": "www.zhihu.com",
"origin": "https://www.zhihu.com",
"Referer": "https://www.zhihu.com/people/irons.du/followers?page=6",
"TE": "Trailers",
"x-ab-param": "se_entity=on;top_recall_core_interest=81;se_major_onebox=major;top_promo=1;se_gi=0;web_logoc=blue;top_newfollowans=0;top_nmt=0;top_retag=0;top_video_rew=0;web_ask_flow=exp_a;top_ntr=1;top_recall_follow_user=91;top_recall_tb_follow=71;top_universalebook=1;se_new_market_search=off;tp_ios_topic_write_pin_guide=1;se_consulting_price=n;top_billread=1;top_memberfree=1;se_ingress=off;top_feedre=1;top_tmt=0;tp_sft=a;se_rescore=0;tp_write_pin_guide=1;top_card=-1;top_root_few_topic=0;top_vds_alb_pos=0;top_video_score=1;ls_play_continuous_order=2;se_gemini_service=content;se_minor_onebox=d;top_follow_reason=0;top_mlt_model=0;top_raf=n;se_tf=1;top_billupdate1=2;tp_discussion_feed_card_type=0;top_nad=1;top_billab=0;top_ebook=0;pin_efs=orig;top_adpar=0;top_distinction=0;top_hca=0;top_multi_model=0;top_billpic=0;top_recommend_topic_card=0;top_video_fix_position=0;top_pfq=0;top_test_4_liguangyi=1;top_gr_auto_model=0;top_newfollow=0;se_relevant_query=old;top_30=0;top_gr_model=0;top_tag_isolation=0;top_billvideo=0;top_topic_feedre=21;top_free_content=-1;top_no_weighing=1;top_slot_ad_pos=1;top_tffrt=0;top_alt=0;top_cc_at=1;top_followtop=0;top_spec_promo=1;top_uit=0;top_feedre_itemcf=31;top_billboard_count=1;top_fqa=0;top_login_card=1;se_daxuechuisou=old;top_root_web=0;top_roundtable=1;top_videos_priority=-1;top_retagg=0;top_sjre=0;top_feedtopiccard=1;top_hweb=0;top_rank=0;se_consulting_switch=off;top_lowup=1;top_nucc=0;se_auto_syn=0;top_follow_question_hybrid=0;top_gr_topic_reweight=0;se_refactored_search_index=0;top_vd_op=0;top_tr=0;top_an=0;top_keyword=0;top_quality=0;se_correct_ab=0;top_dtmt=2;top_yhgc=0;top_nszt=0;top_recall=1;se_dt=1;top_new_user_gift=0;top_nuc=0;top_is_gr=0;top_nid=0;zr_ans_rec=gbrank;top_feedre_cpt=101;top_keywordab=0;se_merger=0;top_hqt=0;se_wiki_box=0;top_sj=2;top_vdio_rew=0;ls_new_video=0;top_f_r_nb=1;top_root_ac=1;top_manual_tag=1;top_recall_deep_user=1;top_user_gift=0;top_gif=0;top_recall_tb=1;top_root_mg=1;top_feedre_rtt=41;top_recall_tb_short=61;top_bill=0;top_recall_tb_long=51;top_v_album=1;top_yc=0;pin_ef=orig;top_root=0;top_vd_score_new=0;top_ad_slot=1;top_tagore=1",
"x-requested-with": "fetch",
"x-udid": "ALAmfS0hYw6PToYbiV5ZQSQaqA7sbhEDfEg=",
"x-zse-83": "3_1.1",
"x-zse-84": "h58kQ9olT_baKorlgg9k0SokNk8bQsAlj_rlK_ol8-8aPcNkhgrlS9_k9xuaRouk"
}

# '''
# Accept
# */*
# Accept-Encoding
# gzip, deflate, br
# Accept-Language
# en-US,en;q=0.5
# Connection
# keep-alive
# Cookie
# _zap=96303539-19e9-4bec-afbf-9…9f0a0115842464094a26115457122
# Host
# www.zhihu.com
# origin
# https://www.zhihu.com
# Referer
# https://www.zhihu.com/people/hubertuswi/followers?page=4
# TE
# Trailers
# User-Agent
# Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/62.0
# x-ab-param
# se_entity=on;se_ingress=off;tp…op_uit=0;top_universalebook=1
# x-requested-with
# fetch
# x-udid
# ALAmfS0hYw6PToYbiV5ZQSQaqA7sbhEDfEg=
# x-zse-83
# 3_1.1
# x-zse-84
# lobmNGokOoraKorlgg9k0O5wPceaN1…kKGom8lua7xrlzhAwO9KlTgNbRwAx
# '''

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhihu.middlewares.change_iproxy': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihu.pipelines.ZhihuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPERROR_ALLOWED_CODES = [403]

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
REDIS_HOST = "192.168.43.131"
REDIS_PORT = 6379