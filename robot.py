# --coding:utf8--
import re

import requests
from werobot import WeRoBot
from lxml import html

robot = WeRoBot(token='x_forlunch', enable_session=True)
scale_pattern = re.compile(r's\d+x\d+/')
cache_pattern = re.compile(r'\?ig_cache_key.*$')


@robot.subscribe
def subscriber(message):
    return '看个电影，听个歌，美滋滋~'


@robot.filter(re.compile(r".*?instagram.com/p.*?"))
def get_ins_pic(message):
    url = message.content
    req = requests.get(url)
    if req.status_code == 200:
        tree = html.fromstring(req.text)
        url = tree.xpath("//meta[@property='og:image']/@content")[0]
        if url:
            if scale_pattern.search(url):
                url = url.replace(scale_pattern.search(url).group(0), '')
            if cache_pattern.search(url):
                url = url.replace(cache_pattern.search(url).group(0), '')

            return url
        else:
            return 'There is no image return'


@robot.handler
def hello(message, session):
    count = session.get("count", 0) + 1
    session["count"] = count
    return '嘘~别说话~'
