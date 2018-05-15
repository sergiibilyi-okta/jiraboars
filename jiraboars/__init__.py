#!/usr/bin/python
import json
import re
import requests


URL = "https://mangarock.com/manga/mrs-serie-225627/"
def main():
    response = requests.get(URL)
    if response.status_code == 200:
        print 'SUCCESS'
        # print response.text
        m = re.search('<script>window.APP_STATE=(.*)</script><script data-cfasync="false" src="/javascript/material130.min.js">', response.text)
        val = m.group(1)
        chapters = json.loads(val)["currentManga"]["info"]["chapters"]
        amount = len(chapters)
        print chapters[amount -1]
        # p = re.compile('bigpay_(.*)-db_1')
    	# dbs = [db for db in text if p.match(db.name)]
    	# instances = []
    	# for db in dbs:
    else:
	    print 'FAILED'

if __name__ == "__main__":
	main()
