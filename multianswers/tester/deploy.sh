#!/bin/bash
set -e
./pytania2ts.py
./build.sh $1
rm -rf ~/wdp/docs/$1
mv $1 ~/wdp/docs/$1

cd ~/wdp
git add --all && git commit -m"<automatic deploy>" && git push
