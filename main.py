#!/usr/bin/env python
import requests
from fake_useragent import UserAgent

#defining files
list_of_urls = 'inputfile.txt'
good_links = 'goodlinks.txt'
bad_links = 'badlinks.txt'
ignored_links = 'ignoredlinks.txt'

#defining 'browser' stuff
ua = UserAgent(fallback='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0')
#ua.update()
#user_agent = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
#xff_ip = "66.249.66.1"
#headers = {'User-Agent':user_agent,'X-Forwarded-For':xff_ip}
headers = {'User-Agent': str(ua.random)}

#defining urls to ignore
archive_url = ["https://archive.", "http://archive.", "https://web.archive.org/", "http://web.archive.org/"]
ignore_url = ["aspi.org.au"]

#opens all the files
with open(list_of_urls, 'r', encoding='utf8') as inputfile, open(good_links, 'w+') as goodfile, open(bad_links, 'w+') as badfile, open(ignored_links, 'w+') as ignoredfile:
    #read in the urls one by one
    for url in inputfile.readlines():
        #strip the \n from the line
        url = url.strip()
        if any(x in url for x in archive_url):
            ignoredfile.write('archived: ' + url + '\n')
            print('skipped - archived')
        elif any(x in url for x in ignore_url):
            ignoredfile.write('ignored: ' + url + '\n')
            print('skipped - ignored')
        else:

            #try getting the url and seeing if the status code is 200. If it's not, tell me what the
            #response code is that you get. If the request fails for whatever reason otherwise, for example,
            #DNS error, then mark it bad.
            try:
                request = requests.get(url, headers=headers)
                if request.status_code == 200:
                    print(url + ' - good')
                    goodfile.write(url + '\n')
                else:
                    badfile.write(url + " - bad - returned response code: {code}\n".format(code=request.status_code))
                    print(url + " - bad - returned response code: {code}".format(code=request.status_code))
            except:
                print(url + ' - bad - possibly domain does not exist')
                badfile.write(url + ' - bad - possibly domain does not exist\n')
