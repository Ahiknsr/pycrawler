from BeautifulSoup import BeautifulSoup, SoupStrainer
from urlparse import urljoin,urlparse
import re

def get_links(html,url):
	""" This function will return all the urls from html , if urls in html are relative they will be converted to absolute """
	urls=[]
	for link in BeautifulSoup(html, parseOnlyThese=SoupStrainer('a')):
		if link.has_key('href'):
			if link['href']=='':
				continue
			link['href']=link['href'].strip(' ')
			urls.append(urljoin(url,link['href']))

	return urls


def get_links_domain(html,url):
	""" This function will return all the urls from a webpage which point to same domain  """
	urls=[]
	dom=urlparse(url).hostname
	for link in BeautifulSoup(html, parseOnlyThese=SoupStrainer('a')):
		if link.has_key('href'):
			
			if link['href']==' ':
				continue
			
			link['href']=link['href'].strip(' ')
			
			newurl=urljoin(url,link['href'])
			udom=urlparse(newurl).hostname
			if udom == dom :
				urls.append(newurl)

	return urls
			

def get_files(html,url,exten):
	""" This function will search the webpage for given file extensions """
	file_urls=[]
	if exten[0]!='.':
		exten='.'+exten
	for link in BeautifulSoup(html,parseOnlyThese=SoupStrainer('a')):
		if link.has_key('href'):
			absurl=urljoin(url, link['href'])
			if absurl[-len(exten):]==exten:
				file_urls.append(absurl)

	return file_urls


def get_emails(html):
	""" search for emails using regex expressions """
	emails=[]
	for mail in  re.findall(r"[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",html):
		emails.append(mail)

	return emails



