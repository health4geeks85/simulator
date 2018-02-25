import time
import random
import base64
import datetime
import sys


nowFormat = '%Y-%m-%dT%H:%M:%S.%fZ'
dateFormat = '%Y-%m-%d'
timeFormat = '%H:%M:%S'


def display(path):
    with open(path, 'rb') as f:
        content = f.read()
    lines = base64.b64decode(content).decode()
    buf = list(lines.split('\n'))
    while True:
        if not buf:
            buf = list(lines.split('\n'))
        time.sleep(random.randint(0, 9)/10)
        # time.sleep(1)
        now = datetime.datetime.now()
        line = buf.pop()
        # print(line)
        print(line.format(now=now.strftime(nowFormat),
                          date=now.strftime(dateFormat),
                          time=now.strftime(timeFormat)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'orderer':
            display('orderer.bin')
        else:
            display('peer.bin')
    else:
        display('orderer.bin')
