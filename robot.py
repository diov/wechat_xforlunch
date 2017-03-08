# --coding:utf8--
import re
from enum import Enum

import requests
from werobot import WeRoBot
from lxml import html

robot = WeRoBot(token="x_forlunch", enable_session=True)
scale_pattern = re.compile(r"s\d+x\d+/")
cache_pattern = re.compile(r"\?ig_cache_key.*$")
type_xpath = "//meta[@property='og:type']/@content"


class InsType(Enum):
    video = "🎬"
    image = "🌁"


@robot.subscribe
def subscriber(message):
    return "愿你永远有一颗有趣的心~🙃️"


@robot.filter(re.compile(r".*?instagram.com/p.*?"))
def get_ins_pic(message):
    url = message.content
    req = requests.get(url)
    if req.status_code != 200:
        return "你输入的可能是假的 instagram 网址😝"

    tree = html.fromstring(req.text)
    ins_type = tree.xpath(type_xpath)[0]
    if ins_type == "":
        return "大哥没见过这种东西!🖕"

    url = tree.xpath("//meta[@property='og:{type}']/@content".format(type=ins_type))[0]
    if url and ins_type == "image":
        if scale_pattern.search(url):
            url = url.replace(scale_pattern.search(url).group(0), '')
        if cache_pattern.search(url):
            url = url.replace(cache_pattern.search(url).group(0), '')

    return "{type}:  {url}".format(type=InsType[ins_type], url=url)


@robot.handler
def hello(message, session):
    count = session.get("count", 0) + 1
    session["count"] = count
    return "🐶汪！汪汪汪~"
