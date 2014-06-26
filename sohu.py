#!/usr/bin/env python

__all__ = ['sohu_download']

from common import *

def real_url(host, prot, file, new):
    url = 'http://%s/?prot=%s&file=%s&new=%s' % (host, prot, file, new)
    html = get_html(url)
    print html
    start, _, host, key, _, _, _, _, _ = html.split('|')
    return '%s%s?key=%s' % (start[:-1], new, key)

def sohu_download(url, merge=True, format=None):
    f = ["norVid", "highVid", "superVid", "oriVid"]
    if url.find('#') > 0:
        format = url.split('#')[1]
        url = url.split('#')[0]
    vid_page = get_html(url)
    vid = r1('vid="(\d+)"', vid_page)
    if not vid:
        vid = r1('vid:\s*\'(\d+)\'', vid_page)
    assert vid
    import json
    data = json.loads(get_decoded_html('http://hot.vrs.sohu.com/vrs_flash.action?vid=%s' % vid))
    if format:
        vid = data['data'][format]
        data = json.loads(get_decoded_html('http://hot.vrs.sohu.com/vrs_flash.action?vid=%s' % vid))
    host = data['allot']
    prot = data['prot']
    urls = []
    data = data['data']
    title = data['tvName']
    size = sum(data['clipsBytes'])
    assert len(data['clipsURL']) == len(data['clipsBytes']) == len(data['su'])
    for file, new in zip(data['clipsURL'], data['su']):
        urls.append(real_url(host, prot, file, new))
    assert data['clipsURL'][0].endswith('.mp4')
    download_urls(urls, title, 'mp4', total_size=size, refer=url, merge=merge)

download = sohu_download
download_playlist = playlist_not_supported('sohu')

def main():
    script_main('sohu', sohu_download)

if __name__ == '__main__':
    main()

