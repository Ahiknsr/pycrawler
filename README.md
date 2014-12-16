Pycrawler
=========

WebCrawler written in python using beautifulsoup and mechanize 

Usage
========

First install the required libraries using the command pip install -r requirements.txt

python webscraper.py -u http://www.iitbhu.ac.in -d 2  -s same  # follows links which belong to same domian 

python webscraper.py -u http://www.iitbhu.ac.in -d 2  -s diff -m # follow links to other sites and also search for emails  

Explanation about the arguments

-u is the url of webpage to start crawling
-d denotes the depth recommended value is 2 , maximum value is 4
-s takes either same or diff as arguments , use same if want you want to crawl only the links which belong to same site , diff you want to want follow links to other sites also
-m if used will search the webpages being crawled for emails 

The program will create files named levelx.txt , It will contains the links at which are found at depth x

If -m is used the emails found will be saved in emails.txt
