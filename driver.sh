#!/usr/bin/env bash
curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "$curr_dir"'/../COVID-19/' || exit
git pull
cd "$curr_dir" || exit

python3 read_data.py