#!/usr/bin/env python

__all__ = ['downloads']

import os
import sys
import time
from common import *

def main():
	urls = sys.argv[1:]
	title = time.strftime("%Y%m%d%H%M%S", time.localtime())
	size = 1
	merge = True
	download_urls(urls, title, 'flv', total_size=size, refer=urls[0], merge=merge)

if __name__ == '__main__':
	main()

