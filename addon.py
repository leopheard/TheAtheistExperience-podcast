from xbmcswift2 import Plugin, xbmcgui
from resources.lib import theatheistexperiencepodcast

plugin = Plugin()

URL = "https://www.spreaker.com/show/3254896/episodes/feed"
URL2 = "http://atheist-experience.com/archive/?full=1"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/759ffa12e832b60f7779066e7b874dba.jpg"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/759ffa12e832b60f7779066e7b874dba.jpg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('all_episodes2'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_rss_itunes_square_1400/images.spreaker.com/original/759ffa12e832b60f7779066e7b874dba.jpg"},
    ]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = theatheistexperiencepodcast.get_soup(URL)
    
    playable_podcast = theatheistexperiencepodcast.get_playable_podcast(soup)
    
    items = theatheistexperiencepodcast.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = theatheistexperiencepodcast.get_soup(URL)
    
    playable_podcast1 = theatheistexperiencepodcast.get_playable_podcast1(soup)
    
    items = theatheistexperiencepodcast.compile_playable_podcast1(playable_podcast1)

    return items

@plugin.route('/all_episodes2/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup2 = theatheistexperiencepodcast.get_soup(URL2)
    
    playable_podcast2 = theatheistexperiencepodcast.get_playable_podcast1(soup2)
    
    items = theatheistexperiencepodcast.compile_playable_podcast2(playable_podcast2)

    return items


if __name__ == '__main__':
    plugin.run()
