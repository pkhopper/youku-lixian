#!/usr/bin/env python
# coding=utf-8

__all__ = ['downloads', 'merge']

import os
import sys
import time
from common import *

def downloads(fp, output_dir='/Users/pk/download/'):
    urls = []
    for url in open(fp, 'r').readlines():
        url = url.strip()
        if not url.startswith('#'):
            urls.append(url)
    if not urls[0].startswith("http:"):
        title = urls[0]
        urls = urls[1:]
    else:
        title = "%s-%s"%(time.strftime("%Y%m%d%H%M%S", time.localtime()), fp)
    output_dir = os.path.join(output_dir, title)
    if output_dir.endswith('.m3u'):
        output_dir = output_dir[:-4]
    if not os.path.isdir(output_dir):
        print output_dir
        os.mkdir(output_dir)

    ext = 'flv'
    if urls[0].startswith('mp4'):
        ext = 'mp4'

    size = 1024*1024*100
    merge = True
    download_urls(urls, title, ext, total_size=size,
                  output_dir=output_dir, refer=urls[0], merge=merge)
