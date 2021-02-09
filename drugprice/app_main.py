# -*- coding: utf-8 -*-
import drugprice.deal_page as dp
import time


def dealTiandi(url, pageNum=1):
    """
    处理天地网的中药价格抓取
    """
    head = ['品名', '规格', '产地', '近期价格', '走势', '周涨跌', '月涨跌', '年涨跌']
    priceList = []
    for i in range(1, pageNum + 1):
        tmpUrl = url
        if i > 1:
            tmpUrl = tmpUrl.replace('.html', '-{}.html'.format(i))
        priceList.extend(dp.parseTiandiPage(tmpUrl))
        print("page {} is finished!".format(i))

    _saveFile(head, priceList, "d:/tiandi-{}.csv".format(time.strftime('%Y-%m-%d')))


def dealKangmei(url, pageNum=1):
    """
    处理康美中药网的价格抓取
    """
    head = ["品名", "规格", "产地", "亳州", "安国", "成都", "玉林", "廉桥", "普宁"]
    priceList = []
    for i in range(1, pageNum + 1):
        tmpUrl = url + "?pageNum={}".format(i)
        priceList.extend(dp.parseKangmeiPage(tmpUrl))
        print("page {} is finished!".format(i))

    _saveFile(head, priceList, "d:/kangmei-{}.csv".format(time.strftime('%Y-%m-%d')))


def _saveFile(head, rowList, fileName):
    """
    存储抓取结果为csv文件的公共方法
    """
    with open(fileName, mode='w', encoding="utf-8") as fin:
        fin.write(','.join(head) + '\n')
        for row in rowList:
            fin.write(','.join(row) + '\n')


if __name__ == '__main__':
    dealTiandi('https://www.zyctd.com/jiage/8-0-0.html', 28)
    dealKangmei('https://www.kmzyw.com.cn/jiage/today_price.html', 56)
    print('{}Finished!{}'.format('=' * 10, '=' * 10))
