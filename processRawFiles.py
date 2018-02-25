import datetime
import base64
import sys
if len(sys.argv) > 0:
    mode = sys.argv[1]
else:
    mode = 'orderer'

if mode == 'orderer':
    rawFile = 'orderer.txt'
    processedFile = 'orderer.bin'
else:
    rawFile = 'peer.txt'
    processedFile = 'peer.bin'

if mode == 'orderer':
    nowIdx = 7
    dateIdx = 8
    timeIdx = 9
else:
    nowIdx = 10
    dateIdx = 11
    timeIdx = 12

with open(rawFile, 'r') as f:
    lines = f.readlines()

currentTime = datetime.datetime.now().strftime('%y-%m-%dT%H:%M:%S.%fZ')

newLines = []
for line in lines:
    line = line.replace('{', '{{')
    line = line.replace('}', '}}')
    parts = line.split(' ')
    # print(parts)
    if len(parts) > nowIdx and '2018-02-01' in parts[nowIdx]:
        parts[nowIdx] = '{now}'
    if len(parts) > timeIdx:
        if '2018-02-01' in parts[dateIdx] and 'UTC' in parts[timeIdx+1]:
            parts[dateIdx] = parts[dateIdx].replace('2018-02-01', '{date}')
            parts[timeIdx] = '{time}'
    # print(parts)
    newLines.append(' '.join(parts))


with open(processedFile, 'wb') as f:
    f.write(base64.b64encode(''.join(newLines).encode()))




