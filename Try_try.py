import string
import random
import os
import zipfile

def chuangjian(myaname):
    wenname = []
    k = 1
    while (k <= 10):
        def shouzimu(size=1, chars=string.ascii_uppercase):
            return ''.join(random.choice(chars) for _ in range(size))

        def wenjianname(size=random.randrange(4, 15), chars=string.ascii_uppercase):
            return ''.join(random.choice(chars) for _ in range(size))

        name = wenjianname()
        name = str(name)
        name = name.lower()
        tou = shouzimu()
        curPath = os.getcwd()
        targetPath = curPath + os.path.sep

        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        fileName = tou + name + myaname + '.lua'
        wenname.append(fileName)
        filePath = targetPath + os.path.sep + fileName

        with open(filePath, 'a') as f:
            for i in range(1, 800):
                def neirong(size=random.randrange(60, 90), chars=string.ascii_uppercase + string.digits):
                    return ''.join(random.choice(chars) for _ in range(size))

                def bianliang(size=random.randrange(4, 15), chars=string.ascii_uppercase):
                    return ''.join(random.choice(chars) for _ in range(size))

                nrong = neirong()
                name1 = bianliang()
                name2 = bianliang()
                name3 = bianliang()
                f.write('local' + ' ' + name1 + '=' + '\'' + nrong + '\'' + ';' + '\n')
                if i % 8 == 0:
                    f.write('function' + ' ' + name2 + '()' + 'end' + '\n')
                if i % 5 == 0:
                    f.write('print' + '(' + '\'' + name3 + '\'' + ')' + '\n')
        k = k + 1
    wenjianname = 'jilu' + '.txt'
    wenjianpath = targetPath + os.path.sep + wenjianname
    with open(wenjianpath, 'a') as h:
        for _ in wenname:
            h.write(_ + ',')

def shanchu():
    curPath_s = os.getcwd()
    path111 = curPath_s  + '\\' + 'jilu.txt'
    with open(path111, 'r') as m:
        list=m.read().split(',')
        l=0
        while(l<(len(list)-1)):
            shanwenjian=curPath_s+'\\'+list[l]
            os.remove(shanwenjian)
            l=l+1
    os.remove(path111)

def yasuo(name_yasuo):
    name = name_yasuo + '.zip'
    azip = zipfile.ZipFile(name, 'w')
    curPath_s = os.getcwd()
    for filesname in os.walk(curPath_s):
        for file in filesname[len(filesname) - 1]:
            list = file.split('.')
            if len(list) == 2 and list[1] == "lua":
                azip.write(file)
    azip.close()

tils = []
strttt = str(input('输入名字（多个名字用空格间隔，不输入则生成默认的文件）：'))
if len(strttt) == 0:
    tils = ['Service', 'Model', 'Entity', 'Command', 'Controller']
else:
    tils = strttt.split(' ')

for it in tils:
    chuangjian(it)
    yasuo(it)

key = int(input('输入1删除创建的文件并结束，输入其他不删除！请输入：'))
if key == 1:
    shanchu()
else:
    print('over')