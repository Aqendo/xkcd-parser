# XKCD Parser
A program that parses all comics' json from [xkcd.com](https://xkcd.com)

## Download dump
https://aqendo.github.io/xkcd-parser/parsed.json
## Automatic deployment
You can generate JSON dump by yourself and you can download `parsed.json` file from `gh_pages` repo or directly from [Github Pages Link](https://aqendo.github.io/xkcd-parser/parsed.json). This repository has CI/CD configured to automatically update that file periodically.
## Help message
```
usage: ./parser.py parsed.json

A program to parse all comics' JSON from XKCD.COM

positional arguments:
  json_file   The JSON file of already scraped comics' info. If exists, will be updated with new comics (if any)

options:
  -h, --help  show this help message and exit

Try not to overload xkcd.com servers by overusing this script. Please!
```
## License
```
XKCD Parser - A program to parse all comics' JSON from XKCD.COM
Copyright (C) 2025 Sergey Sitnikov
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
