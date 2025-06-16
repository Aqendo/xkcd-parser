# XKCD Parser
A program that parses all comics' json from [xkcd.com](https://xkcd.com)
## Automatic deployment
You can generate JSON dump by yourself and you can download `parsed.json` file from `gh_pages` repo. This repository has CI/CD configured to automatically update that file periodically.
## Help message
```
usage: ./parser.py already_data.json result_data.json

A program to parse xkcd.com's json api for direct links of comics.

positional arguments:
  already_data  The JSON file of already parsed XKCD comics
  result_data   The JSON file that will be created. It will contain data that
                was already parsed + newly parsed comics info

options:
  -h, --help    show this help message and exit

Try not to overload xkcd.com servers by overusing this script. Please!
```