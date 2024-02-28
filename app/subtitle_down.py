import requests
import app.global_var as gc

bvid = ""
pagelist_api = "https://api.bilibili.com/x/player/pagelist"
subtitle_api = "https://api.bilibili.com/x/player/v2"
headers = {
        'authority': 'api.bilibili.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'origin': 'https://www.bilibili.com',
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'cookie': '',
    }
    
def _get_player_list(bvid: str):
    response = requests.get(pagelist_api, params = {'bvid': bvid}, headers = headers)
    cid_list = [x['cid'] for x in response.json()['data']]
    return cid_list

def _get_subtitle_list(bvid: str, cid: str):
    headers['cookie'] = gc.return_var()
    response = requests.get(subtitle_api, params = (('bvid', bvid),('cid', cid)), headers = headers)
    print(headers)
    subtitle_list = response.json()['data']['subtitle']['subtitles']
    return subtitle_list

def _get_subtitle(cid: str):
    subtitles = _get_subtitle_list(cid)
    if subtitles:
        return _request_subtitle(subtitles[0])

def _request_subtitle(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        body = response.json()['body']
        return body

def _get_pagelist(bvid: str):
    response = requests.get(pagelist_api, params = {'bvid': bvid}, headers = headers)
    pagelist = len(response.json()['data'])
    return pagelist

def download_subtitle():
    page = _get_pagelist()
    subtitle_list = _get_subtitle(_get_player_list()[page])
    if subtitle_list:
        text_list = [x['content'] for x in subtitle_list]
        text = ' '.join(text_list)
        print("字幕获取成功\n")
        return text
    else:
        text = "该视频没有可供下载的字幕"
        return text