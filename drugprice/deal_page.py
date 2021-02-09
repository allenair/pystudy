# -*- coding:utf-8 -*-
import re
import urllib.request as req
from bs4 import BeautifulSoup


def _getHtmlContent(url, encoding="utf-8"):
    """
    获取指定链接的全部网页内容的公共方法
    """
    headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/88.0.4324.150 Safari/537.36'}
    response = req.Request(url, headers=headers)
    htmlObj = req.urlopen(response)
    htmlContent = htmlObj.read().decode(encoding, errors='ignore')
    return htmlContent


def parseTiandiPage(url):
    htmlContent = _getHtmlContent(url)
    priceList = []
    soup = BeautifulSoup(htmlContent, 'html.parser')
    for tag in soup.select("ul[class='priceTableRows'] > li"):
        innerList = []
        for child in tag.children:
            val = child.string
            if val and len(val.strip()) > 0:
                innerList.append(val)
        priceList.append(innerList)

    return priceList
