#!/bin/bash
set -e
#npm run build --base-href "/wdp/$1/" --deploy-url "/wdp/$1/"
ng build --prod --base-href "/wdp/$1/" --deploy-url "/wdp/$1/"
# sed -i'' 's/href="\/"/href="\/wdp\/"/' docs/index.html
mv dist $1

