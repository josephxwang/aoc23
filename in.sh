# Specify day as command line argument
# ./in.sh 1

py util/get_input.py $1
py util/open_page.py $1
code $1.in