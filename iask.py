#!/usr/bin/env python

__all__ = ['iask_download', 'iask_download_by_id']

import re
from common import *

def video_info(id):
    user_agent = r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
    headers = {'User-agent': user_agent}
    xml = get_decoded_html('http://v.iask.com/v_play.php?vid=%s' % id, headers)
    urls = re.findall(r'<url>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</url>', xml)
    name = r1(r'<vname>(?:<!\[CDATA\[)?(.+?)(?:\]\]>)?</vname>', xml)
    vstr = r1(r'<vstr>(?:<!\[CDATA\[)?(.+?)(?:\]\]>)?</vstr>', xml)
    return urls, name, vstr

def iask_download_by_id(id, title=None, merge=True):
    urls, name, vstr = video_info(id)
    title = title or name
    assert title
    download_urls(urls, title, 'flv', total_size=None, merge=merge)

def iask_download(url, merge=True):
    html = get_html(url)
    id = r1(r"""vid:'(\d+)'""", html)
    iask_download_by_id(id, merge=merge)

download = iask_download
download_playlist = playlist_not_supported('iask')

def main():
    script_main('iask', iask_download)

if __name__ == '__main__':
    main()

