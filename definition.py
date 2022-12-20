import requests
import json
import os
import re
import argparse

try:
    if os.environ['MW_API_KEY']:
        MW_API_KEY = os.environ['MW_API_KEY']
except KeyError:
    print("set MW_API_KEY, idiot!")

try:
    parser = argparse.ArgumentParser(prog='definition.py',
                                     usage='%(prog)s [options]',
                                     description='search Merriam-Webster')
    parser.add_argument('searchterm', type=str, nargs=1,
                        help='the word you\'re looking for')
    args = parser.parse_args()
    searchterm = args.searchterm[0]

except SystemExit:
    print('definition requires one argument and no more')

mw_url = 'https://dictionaryapi.com/api/v3/references/collegiate/json/'

try:
    r = requests.get(mw_url+searchterm+"?key="+MW_API_KEY)

    text = r.text
    data = json.loads(text)
    raw_dt = data[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]
    raw_prs = data[0]['hwi']['prs'][0]['mw']
    dt = raw_dt.replace("{bc}", "")
    dt = dt.replace("{sx|", "see ")
    dt = dt.replace("||}", "")
    dt = re.sub('{dx_def}.*?{/dx_def} ', '', dt)
    dt = re.sub('{dx}.*?{/dx}', '', dt)
    dt = re.sub('{d_link', '', dt)
    dt = re.sub('}', '', dt)
    dt = re.sub('\|\w+\|', '', dt)

    print(f'{searchterm}: {raw_prs}: {dt}')

except NameError:
    print("Give us a search term!")
