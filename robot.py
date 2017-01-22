# --coding:utf8--
import re

import requests
from werobot import WeRoBot
from lxml import html

robot = WeRoBot(token='x_forlunch')
scale_pattern = re.compile(r's\d+x\d+/')
cache_pattern = re.compile(r'ig_cache_key.*$')

@robot.subscribe
def subscriber(message):
    return 'Hell O! My friend~'


@robot.filter(re.compile(".*?instagram.com\/p.*?"))
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
def hello(message):
    return '{source_message}, yeah, U are right!'.format(source_message=message.content)
