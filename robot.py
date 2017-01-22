# --coding:utf8--
import requests
from werobot import WeRoBot
from lxml import html

robot = WeRoBot(token='x_forlunch')


@robot.subscribe
def subscriber(message):
    return 'Hell O! My friend~'


@robot.handler
def hello(message):
    return '{source_message}, yeah, U are right!'.format(source_message=message.content)


@robot.filter('www.instagram.com/p')
def get_ins_pic(message):
    url = message.content
    req = requests.get(url)
    if req.status_code == 200:
        tree = html.fromstring(req.text)
        if tree.xpath("//meta[@property='og:image']/@content")[0]:
            return tree.xpath("//meta[@property='og:image']/@content")[0]
        else:
            return 'There is no image return'
