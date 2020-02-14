import requests
import re

def getHTMLText(url):
    try:
        header = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'sec-fetch-user': '?1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'referer': 'https://s.taobao.com/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'cna=2Sh2FGYHhnUCAQWXXmjJaxlm; t=44109dae7e21638f0c3f3f5adac81b9a; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; sgcookie=QxTKqjM3Lpd42n5t7xU1; uc3=vt3=F8dBxdzykYdC5OQPCy8%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UUpgQEHKbVNdIg%3D%3D&nk2=0vR3gffPetHtWerxBXA%3D; lgc=%5Cu5317%5Cu51B0%5Cu6D0B%5Cu5947%5Cu5E7B%5Cu4E4B%5Cu65C5; uc4=nk4=0%400EUBqcx3rmHeUWLc9DWTRcMb1kqD66C5PA%3D%3D&id4=0%40U2gqz64BUI13CEYT3cLf0bC4ypki; tracknick=%5Cu5317%5Cu51B0%5Cu6D0B%5Cu5947%5Cu5E7B%5Cu4E4B%5Cu65C5; _cc_=VFC%2FuZ9ajQ%3D%3D; tg=0; enc=JsxP%2FFDXm0RVYvD%2BbLzcKH2KNbJcfcrFICk2DImGlF7V5Dv63wz%2Fzocm4S3oRlpp7p5iPEMWPh%2BLltfM5CyP6g%3D%3D; birthday_displayed=1; mt=ci=6_1; uc1=cookie14=UoTUO8YItgzuHw%3D%3D; v=0; cookie2=107f4a126d27559ffe1034eac27440f3; _tb_token_=7eb563bd99898; JSESSIONID=D0BCF26D8027964B888BE198A6A83092; isg=BI-P0i_UDcAclQk89Mo2n5dOHiOZtOPWlLjVqqGcK_4FcK9yqYRzJo1idqBOE7tO; l=cBETqU4eQU3v2j1DBOCanurza77OSIRYYuPzaNbMi_5dy6Ts9E_Oo7uoDF96VjWd9WLB4Tn8Nrv9-etkZgIzgz--g3fP.',
        }

        #r = requests.get(url,timeout=20)
        r = requests.get(url,headers = header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.request.url)
        return r.text
    except:
        print("Web crawler error 爬虫失败")
        return ""

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        #print(plt)
        #print(len(plt),len(tlt))
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    #print(ilt)
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = "书包"
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

main()
