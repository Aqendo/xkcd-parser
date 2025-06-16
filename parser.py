#!/usr/bin/env python3
# XKCD Parser - A program to parse all comics' JSON from XKCD.COM
# Copyright (C) 2025 Sergey Sitnikov
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import json
import multiprocessing

import requests

AMOUNT_POOL = 50


def check_path_already_data(path: str) -> None:
    f = open(path, "r")
    f.close()


def check_path_result_data(path: str) -> None:
    f = open(path, "w")
    f.close()


def get_latest_comic_num() -> int:
    req = requests.get("https://xkcd.com/info.0.json")
    try:
        json_data = req.json()
        if not "num" in json_data or not isinstance(json_data["num"], int):
            print(
                f"ERROR: could not receive adequeate json data from xkcd! Received: {json.dumps(json_data)}"
            )
            exit(1)
        return json_data["num"]
    except Exception as e:
        print(f"ERROR: could not get lastest comic number! {e}")
        exit(1)


def save_to_file(path: str, data: list) -> None:
    with open(path, "w+") as f:
        json.dump(data, f)


def get_json(num: int) -> dict | list:
    req = requests.get(f"https://xkcd.com/{num}/info.0.json")
    json_answer = req.json()
    if not "num" in json_answer:
        print(f"WARNING: no parameter `num` in {num}'s comic JSON! Skipping.")
        return []
    print(f"INFO: Successfully parsed {num} comic", flush=True)
    return json_answer


def main(already_data: str, result_data: str) -> None:
    check_path_already_data(already_data)
    with open(already_data, "r") as f:
        already_data_text = f.read()
    try:
        already_data_json = json.loads(already_data_text)
        if not isinstance(already_data_json, list):
            print("WARNING: Wrong JSON file passed. Fallbacked to an empty list.")
            already_data_json = []
    except json.decoder.JSONDecodeError:
        print("WARNING: Wrong JSON file passed. Fallbacked to an empty list.")
        already_data_json = []
    check_path_result_data(result_data)
    already = set()
    for i in already_data_json:
        already.add(i["num"])
    latest_comic_num = get_latest_comic_num()
    if latest_comic_num in already:
        save_to_file(result_data, already_data_json)
        return
    need_to_parse = [
        i for i in range(1, latest_comic_num + 1) if i != 404 and i not in already
    ]
    print(len(need_to_parse))
    with multiprocessing.Pool(AMOUNT_POOL) as p:
        results = p.map(get_json, need_to_parse)
        already_data_json += [i for i in results if isinstance(i, dict)]
    already_data_json.sort(key=lambda x: x["num"])
    save_to_file(result_data, already_data_json)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="XKCD Parser",
        usage="./parser.py already_data.json result_data.json",
        description="A program to parse xkcd.com's json api for direct links of comics.",
        epilog="Try not to overload xkcd.com servers by overusing this script. Please!",
    )
    parser.add_argument(
        "already_data", help="The JSON file of already parsed XKCD comics"
    )
    parser.add_argument(
        "result_data",
        help="The JSON file that will be created. It will contain data that was already parsed + newly parsed comics info",
    )
    args = parser.parse_args()
    main(args.already_data, args.result_data)
