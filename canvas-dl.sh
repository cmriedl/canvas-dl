#!/bin/bash -eu

#    canvas-dl.sh
#
#    Copyright (C) 2019 cmr@informatik.wtf harrylane3@gmail.com
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

trap 'echo "uh-oh something went wrong..."' ERR

stuff=$(curl -si "$1" | grep 'window.kalturaIframePackageData = ' \
        | sed -nr 's/.*window\.kalturaIframePackageData = (.*)/\1/p' \
        | sed '$ s/;$//' \
	| python3 -m json.tool)

echo "$stuff" > canvas-dl.json

python3 canvas-dl.py canvas-dl.json --video
