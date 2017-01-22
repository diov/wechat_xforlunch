# --coding:utf8--

from werobot import WeRoBot

robot = WeRoBot(token='x_forlunch')


@robot.subscribe
def subscriber(message):
    return 'Hell O! My friend~'


@robot.handler
def hello(message):
    return '{source_message}, yeah, U are right!'.format(source_message=message.content)
