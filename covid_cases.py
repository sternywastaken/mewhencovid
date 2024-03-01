from bs4 import BeautifulSoup
import requests

source_bahrain = requests.get('https://www.worldometers.info/coronavirus/country/bahrain/').text
source_ww = requests.get('https://www.worldometers.info/coronavirus/').text
source_india = requests.get('https://www.worldometers.info/coronavirus/country/india/').text

soup = BeautifulSoup(source_bahrain, 'lxml')
soup_ww = BeautifulSoup(source_ww, 'lxml')
soup_india = BeautifulSoup(source_india, 'lxml')


def bahrain():
	article = soup.find('div', class_='content-inner')

	print('Covid cases in Bahrain: ')

	cases = article.span.text
	print(cases)

	print()


def world_wide():
	article_ww = soup_ww.find('div', class_='content-inner')

	print('Covid cases world wide: ')

	cases_ww = article_ww.span.text
	print(cases_ww)

	print()

def india():
	article_india = soup_india.find('div', class_='content-inner')

	print('Covid cases in India: ')

	cases_india = article_india.span.text
	print(cases_india)

	print()

world_wide()
india()
bahrain()
