#!/usr/bin/env python

from lxml import html
import requests
import string
import unidecode

page = requests.get('http://www.bestplaces.net/find/state.aspx?state=IL')
tree = html.fromstring(page.content)

rows = tree.xpath('//div[@class="8u"]/section/div[@class="row"]/div[@class="4u"]/a/text()')


def getStates():
    page = requests.get('http://www.bestplaces.net/find/')
    tree = html.fromstring(page.content)
    name = tree.xpath('//div[@class="row 0%"]/div/a/node()')
    id = tree.xpath('//div[@class="row 0%"]/div/a/@title')

    node_num = len(name) - 1
    return id

 #   i = 0
 #   while i <= node_num:
 #       print state_name[i], " : ", state_id[i]
 #       i = i + 1
    
def getMetroURL(id):
    url = "http://www.bestplaces.net/find/metro.aspx?st=" + id
    page = requests.get(url)
    tree = html.fromstring(page.content)                                            
    rows = tree.xpath('//div[@class="8u"]/section/div[@class="row"]/div[@class="4u"]/a/@*')
    parsed_urls = []
    for i in rows:
        p_url = string.replace(i, "../", "http://www.bestplaces.net/")
        parsed_urls.append(p_url)
    return parsed_urls


def getMetroStats(url):
    page = requests.get(url)                                                    
    tree = html.fromstring(page.content)
    rows = tree.xpath('//div//ul/li/span[@class="bignum"]/text()')
 # rows contains these feilds   
 # Population, Married Population, Unemployment Rate, Average Commute Time, Median Age 
 # Household Size, Median Home Price, Real Estate
    return "Pop : " + rows[0] + " Unemployment : " + rows[2] + " Home Cost : " + rows[6] 



#statelist = getStates()
#for i in statelist:
#    url = getMetroURL(i)
#    for x in url: 
#        print getMetroStats(x) + " " + x


#print state_rows

#print alaska
#for i in state_rows:
#    print i


def getHousing():
    page = requests.get('http://www.bestplaces.net/housing/metro/indiana/columbus')
    tree = html.fromstring(page.content)
    name = tree.xpath('//table[@id="mainContent_dgHousing"]//tr/td/text()')
    for i in name:
      i = unidecode.unidecode(i)
      print i

print getHousing()
