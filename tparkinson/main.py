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


def getHousing(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    headers = tree.xpath('//table[@id="mainContent_dgHousing"]//tr//td[1]//font/text()')
    data = tree.xpath('//table[@id="mainContent_dgHousing"]//tr//td[not(@bgcolor="#000000")]/text()')
    
    json_data = {}
    count = 0
    for i in data:
        if isinstance(i, unicode):
            i = unidecode.unidecode(i).strip()
        else:
            i.strip()
        if count == 0:
            k = i
            count = count + 1
        elif count == 1:
            v1 = i
            json_data.update({k : v1})
            count = count + 1
        elif count == 2:
            count = 0
    return json_data


output = getHousing('http://www.bestplaces.net/housing/metro/indiana/columbus')
print output

