# --coding:utf8--

from werobot import WeRoBot

robot = WeRoBot(token='x_forlunch')

@robot.handler
def hello(message):
    return 'Hello!'