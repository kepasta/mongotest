import random

def pack():

    appname = ['Google Chrome', 'Mozilla Firefox', 'Opera', 'Internet Explorer', 'Safari']
    methname = ['try hard', 'die hard', 'go ahead', 'born to cry', "let's go", "what doesn't kill you", 'blahblahblah', 'purple cucumber']
    message = ['gimme money', 'go to outer space', 'slice you nice', 'rabbit hole', 'unicorns and magic', 'look at my horse',
           'cut my life into pieces', "i'm lovin' it", 'so good', 'collective unconsciousness', 'piglet', 'well done']
    probnumber = str(random.randrange(1000000))
    reqnumber = str(random.randrange(1000000000))
    strnumber = str(random.randrange(1000000))
    n = 0
    ipaddr = ''
    while n < 4:
        ipaddr += str(random.randrange(256)) + '.'
        n += 1
    ipaddr = ipaddr[:len(ipaddr) - 2]
    hour = random.randrange(24)
    minute = random.randrange(60)
    second = random.randrange(60)
    msecond = random.randrange(1000)
