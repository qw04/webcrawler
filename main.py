import re
import requests
import lxml
from bs4 import BeautifulSoup

def main():
	initialUrl = "https://www.amazon.co.uk/"
	soup = str(BeautifulSoup(requests.get(initialUrl).content,'lxml'))
	m = re.findall("a*a", soup)
	for i in range(len(m)):
		print(m[i])


if __name__ == '__main__':
	main()