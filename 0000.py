# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:04:33 2017

@author: k_Jas
"""

import re
import requests
from bs4 import BeautifulSoup


#requests 返回请求
def get_html(url, headers):
    try:
        r = requests.get(url, headers = headers, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        
        return r.text
    except:
        return 'error'



'''
通过歌手页信息 遍历标签（哪个？）
得到每首歌的链接号，歌名
返回一个字典
'''
def get_songs_number(url, headers):
    html = get_html(url, headers )
    soup = BeautifulSoup(html, 'lxml')
    
    #找到热门50首tag
    r = soup.find('ul', {'class':'f-hide'} ).find_all('a')
    #print (r)
    music_ids = []
    for song in r:
        music_ids.append(song.attrs["href"][9:])
    return music_ids


'''
通过每首歌的url
向文件中写入歌词 
'''    
def get_lyric(url, headers):
    html = get_html(url, headers = headers).replace('\\n','\n')

    f = open('g:/123.txt', 'a', encoding = 'utf-8')
    f.write(html)
    f.write("\n\n\n\n\n")
    f.close
    
    

def main():
    #id=xxxx是某歌手的编号 
    url_artist = 'http://music.163.com/artist?id=9944' 
    #http://music.163.com/#/artist?id=1007170 是假链接
    url_song_front = 'http://music.163.com/api/song/lyric?' + 'id=' 
    url_song_back = '&lv=1'

    headers = {
        'Referer' : 'http://music.163.com/',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host':'music.163.com'
            }
    
    music_ids = get_songs_number(url_artist, headers)
    #print(music_ids)
    
    for music_id in music_ids:
        get_lyric(url_song_front + str(music_id) + url_song_back , headers)
    

if __name__ == '__main__':
    main()
