import sys
import os
import bs4,requests
if len(sys.argv)>1:
	name=' '.join(sys.argv[1:])
else:
	name='YOUR_USERNAME'
ini='https://www.codechef.com/users/'
print 'Loading Results...'
res=requests.get(ini+name)
res.raise_for_status()
soupobj=bs4.BeautifulSoup(res.text,'html.parser')
ranks=soupobj.select('hx')
print "RANKINGS FOR "+ str(name) +'\n'
if ranks[0].getText()=='NA':
	print('LONG CHALLENGE:'+ranks[0].getText())
else:
	print 'LONG CHALLENGE:'+ranks[0].getText()+'/'+ranks[1].getText()
if len(ranks)<3 or ranks[2].getText()=='NA':
	print 'SHORT CHALLENGE:'+"NA"
else:
	print 'SHORT CHALLENGE:'+ranks[2].getText()+'/'+ranks[3].getText()
if len(ranks)<4 or ranks[4].getText()=='NA':
	print 'LUNCHTIME:'+ "NA"
else:	
	print 'LUNCHTIME:'+ranks[4].getText()+'/'+ranks[5].getText()
print '**Global Rank/Country Rank'
