import requests
import lxml
from bs4 import BeautifulSoup


def main():
	initialUrl = "https://www.dell.com/en-uk/shop/laptop-computers-2-in-1-pcs/sr/laptops/inspiron-laptops?~ck=bt"
	# initialUrl = str(input())
	f = requests.get(initialUrl)
	soup = BeautifulSoup(f.content,'lxml')
	print(soup)

if __name__ == '__main__':
	main()