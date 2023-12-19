import requests
import browser_cookie3
import sys

day = sys.argv[1]
cj = browser_cookie3.chrome() # Chrome must be closed for this

url = f'https://adventofcode.com/2023/day/{day}/input'
response = requests.get(url, cookies=cj)
content = response.text

with open(f'{day}.in','w') as file:
   file.write(content)