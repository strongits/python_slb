import urllib.request as req


def price(stock):
	url= 'http://hq.sinajs.cn/list='+stock
	#print(url)
	with req.urlopen(url) as f:
		hq = f.read().decode('GBK')
		#print(hq)
		v=hq.split(',')
		name = v[0].split('"')[1]
		print( name+":" + v[1])
	
stocks=['gb_goog','gb_fb','gb_aapl','gb_bab']

for stock in stocks:
		price(stock)