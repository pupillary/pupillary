# Scrapy settings for che project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'che2'

SPIDER_MODULES = ['che2.spiders']
NEWSPIDER_MODULE = 'che2.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = "WARNING"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3  # 汽车之家案例。 必须加上这个。
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False  # 这个要打开。 否则下面的cookie无效的

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    "Cookie": "fvlid=1642167433528aCtTRzzJxa5w; sessionid=25e76ed4-ac76-4c18-86ef-9f05f56e5f71; area=110114; che_sessionid=01720F78-6018-468C-A3E8-35235321AF81%7C%7C2022-01-14+21%3A37%3A13.520%7C%7C0; listuserarea=110100; sessionip=221.218.212.121; Hm_lvt_d381ec2f88158113b9b76f14c497ed48=1652356283; sessionvisit=3d18f224-a438-45a4-849d-531c3f4587d8; sessionvisitInfo=25e76ed4-ac76-4c18-86ef-9f05f56e5f71|www.autohome.com.cn|100533; che_sessionvid=4B36F1DE-CAF9-47AF-B6E6-A4BA52B82875; userarea=110100; ahpvno=5; UsedCarBrowseHistory=0%3A43581488; Hm_lpvt_d381ec2f88158113b9b76f14c497ed48=1652357364; ahuuid=1A75FF15-842E-4369-8720-FD12B13EEB5E; showNum=8; sessionuid=25e76ed4-ac76-4c18-86ef-9f05f56e5f71; v_no=7; visit_info_ad=01720F78-6018-468C-A3E8-35235321AF81||4B36F1DE-CAF9-47AF-B6E6-A4BA52B82875||-1||-1||7; che_ref=www.autohome.com.cn%7C0%7C100533%7C0%7C2022-05-12+20%3A09%3A19.594%7C2022-05-12+20%3A05%3A10.988; carDownPrice=1"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'che.middlewares.CheSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'che.middlewares.CheDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'che.pipelines.ChePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
