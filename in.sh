# Specify day as command line argument
# ./util 1

py util/get_input.py $1
py util/open_page.py $1
# cp template.py $1.py
code $1.in
# code $1.py