

import re

parse_save = re.compile(
    r"(?P<addres>^\S+)[\s-]*\[(?P<datatime>.*)\]\s*\"(?P<resp>\w*)\s*(?P<file>[/\w]+)[^\"]+\"\s+(?P<code>\d+)\s+(?P<size>\d+)")
    # разрыв мозга и всего сопутсвующего
with open("./nginx_logs.txt", "r", encoding="utf-8") as file:
    print(*(tuple(x.groupdict().values())
            for line in file for x in parse_save.finditer(line)), sep="\n")