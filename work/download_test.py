# -*- coding: utf-8 -*-

import requests
import urllib.request

url = """
http://ysting.ysxs8.com:81/%E6%81%90%E6%80%96%E6%82%AC%E7%96%91/%E3%80%8A%E5%8F%A4%E8%91%A3%E5%B1%80%E4%B8%AD%E5%B1%802%E6%B8%85%E6%98%8E%E4%B8%8A%E6%B2%B3%E5%9B%BE%E4%B9%8B%E8%B0%9C%E3%80%8B/%E3%80%8A%E5%8F%A4%E8%91%A3%E5%B1%80%E4%B8%AD%E5%B1%80%E4%B9%8B%E6%B8%85%E6%98%8E%E4%B8%8A%E6%B2%B3%E5%9B%BE%E3%80%8B012--%E6%9C%89%E5%A3%B0%E5%B0%8F%E8%AF%B4%E5%90%A7[www.ysxs8.com].mp3.mp3
"""

res = requests.get(url)



with open('e:/03.mp3', "wb") as fw:
    with requests.get(url, stream=True) as r:
      # 此时只有响应头被下载
      # print(r.headers)
      print("下载文件基本信息:")
      print('-' * 30)
      print("文件类型:", r.headers["Content-Type"])
      filesize = r.headers["Content-Length"]
      print("文件大小:", filesize, "bytes")
      print("下载地址:", url)
      print('-' * 30)
      print("开始下载")
 
      chunk_size = 128
      times = int(filesize) // chunk_size
      show = 1 / times
      show2 = 1 / times
      start = 1
      for chunk in r.iter_content(chunk_size):
        fw.write(chunk)
      print("\n结束下载")

