# 100 programs in 100 days
# 007 5/4/21
# stock ticker (from 003, repro on repl.it)

import requests, time

stocks = ["0700.hk", "1024.hk", "nvda", "tsm", "mrna", "crsp", "isrg", "tdoc", "1833.hk", "zm", "work", "sq", "shop", "tsla", "nio", "pltr"]

for s in stocks:
	p = stocks.index(s)
	if (p > 0) and (p % 5 == 0):
		print("waiting...")
		time.sleep(60)
	url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + s + "&apikey=MX0Z803PT2WLBB1I"
	data = requests.get(url).json()
	print(str(data["Global Quote"]["01. symbol"]), str(data["Global Quote"]["05. price"]))
