import json
import glob

fileList = glob.glob('./*.json')

allLogs = []

for fileDir in fileList:
    print('Merging ' + fileDir + '...')
    file = open(fileDir)
    data = json.load(file)
    for log in data:
        allLogs.append(log)
    file.close()

with open('allCombinedLogs.json', 'w') as f:
    json.dump(allLogs, f)
