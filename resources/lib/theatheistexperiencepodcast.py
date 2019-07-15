import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup)
    return soup

get_soup("https://www.spreaker.com/show/3254896/episodes/feed")

def get_soup2(url2):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    
    print "type: ", type(soup2)
    return soup2

get_soup2("http://atheist-experience.com/archive/?full=1")


def get_playable_podcast(soup):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup.find_all('item'):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('description')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast(playable_podcast):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_playable_podcast1(soup):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup.find_all('item', limit=1):
        
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link

            title = content.find('title')
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail,
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
    items = []

    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items


def get_playable_podcast2(soup2):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup2.find_all('tr'):
        
        try:        
            link = content.find('a type="audio/mpeg')
            link = link.get('href')
            print "\n\nLink: ", link

            title = content.find('td','td valign=top')
            title = title.get_text()

#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/759ffa12e832b60f7779066e7b874dba.jpg"
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast2(playable_podcast2):
    """
    @para: list containing dict of key/values pairs for playable podcasts

    """
    items = []

    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })

    return items
