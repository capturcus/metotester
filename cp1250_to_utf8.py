#!/usr/bin/python3

import sys

with open(sys.argv[1], "rt", encoding="cp1250") as f:
    with open(sys.argv[1].split(".")[0]+"_utf8.txt", "wt", encoding="utf-8") as g:
        g.write(f.read())