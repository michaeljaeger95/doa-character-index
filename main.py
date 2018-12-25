import urllib.request
import pandas as pd
from tabulate import tabulate
from bs4 import BeautifulSoup


def single(l):
	return pd.Series({
		t: int(BeautifulSoup(
			urllib.request.urlopen("http://www.dumbingofage.com/tag/{}/".format(t)).read(),
			"html.parser"
		).select("div.archiveresults")[0].text.split(' ')[0])
		for t in l})


def double(l):
	res = pd.DataFrame(columns=l, index=l)
	for i in range(len(l)):
		t1 = l[i]
		for j in range(i + 1, len(l)):
			t2 = l[j]
			a = BeautifulSoup(
				urllib.request.urlopen("http://www.dumbingofage.com/tag/{}+{}/".format(t1, t2)).read(),
				"html.parser"
			).select("div.archiveresults")
			res[t2][t1] = int(a[0].text.split(' ')[0]) if a else 0
	return res


with open("list.txt") as f:
	names = f.readlines()  # [:5]
	names = [x.strip() for x in names]
	print(tabulate(single(names).to_frame(), tablefmt="markdown"))
	print(tabulate(double(names), tablefmt="markdown"))
