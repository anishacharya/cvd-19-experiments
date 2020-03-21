#!/usr/bin/env bash
curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "$curr_dir"'/../COVID-19/' || exit
git pull
cd "$curr_dir" || exit

country=${1:-US}
plot_type=${2:-bar}

python3 driver.py --c "$country" --p "$plot_type"
