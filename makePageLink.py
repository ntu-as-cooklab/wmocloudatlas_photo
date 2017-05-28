from os import listdir, getcwd
from os.path import isfile, join
import json

DIC_PATH = getcwd() + "/rawHtmlData"
files = [f for f in listdir(DIC_PATH) if isfile(join(DIC_PATH, f))]
files = [f for f in files if f.endswith(".txt")]

listJson = {}

for file in files:
    FILE_PATH = DIC_PATH + '/%s' % file
    print FILE_PATH
    with open(FILE_PATH, 'r') as input_stream:
        lines = input_stream.readlines()
        lines = [x for x in lines if x != '\n']
        linkSet = []
        for line in lines:
            linkSet.append(
                "https://www.wmocloudatlas.org/imgviewer-" + line.split(';')[0] + ".html")
        listJson[file.split('.')[0]]= linkSet

print listJson

fout=open(getcwd() + '/pageLink.json', 'w')
fout.write(json.dumps(listJson))
fout.close()
