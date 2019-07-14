from xbmcswift2 import Plugin, xbmcgui
from resources.lib import theatheistexperience-podcast

plugin = Plugin()

URL = "https://www.spreaker.com/show/3254896/episodes/feed"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/759ffa12e832b60f7779066e7b874dba.jpg"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/759ffa12e832b60f7779066e7b874dba.jpg"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = theatheistexperience-podcast.get_soup(URL)
    
    playable_podcast = theatheistexperience-podcast.get_playable_podcast(soup)
    
    items = theatheistexperience-podcast.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = theatheistexperience-podcast.get_soup(URL)
    
    playable_podcast1 = theatheistexperience-podcast.get_playable_podcast1(soup)
    
    items = theatheistexperience-podcast.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
