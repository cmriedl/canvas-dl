#!/usr/bin/env python3

#    canvas-dl.py
#
#    Copyright (C) 2019 cmr@informatik.wtf
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
from collections import namedtuple
import json
from pathlib import Path
import re
import sys
from urllib.request import urlretrieve


MODULE_REGEX = re.compile('(Module [0-9]+)(?:Topic)?:')


Video = namedtuple('Video', ['title', 'url'])


def make_unix_compat(string):
    return string.lower().replace(' ', '_').replace('&amp;', '_and_')


def get_videos(canvasjson):
        videos = []

        stuff = list(canvasjson['playlistResult'].values())[0]
        items = stuff['items']

        for item in items:
            videos.append(Video(item['name'], item['downloadUrl']))

        module_name = MODULE_REGEX.match(stuff['name']).group(1)
        return module_name, videos


def download_videos(videos, module_name): 
    outdir = Path(__file__).resolve().parent
    outdir = outdir / Path(make_unix_compat(module_name))
    outdir.mkdir(parents=True, exist_ok=True)

    print(f'downloading videos into {str(outdir)}/')
    for video in videos:
        fpath = outdir / f'{Path(make_unix_compat(video.title))}.mp4'
        urlretrieve(video.url, fpath)
        print('... still working ...')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('jsonfile',
                        type=lambda x: Path(x).resolve(strict=True))
    parser.add_argument('--video', action='store_true', default=False)
    parser.add_argument('--caption', action='store_true', default=False)
    args = parser.parse_args()

    with open(args.jsonfile) as f:
        canvasjson = json.loads(f.read())

        if args.video:
            module_name, videos = get_videos(canvasjson)
            download_videos(videos, module_name)
        elif args.caption:
            print('not implemented')
            exit(-1)


if __name__ == '__main__':
    main()
