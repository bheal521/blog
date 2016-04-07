#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ben Healy'
SITENAME = u'Ben Healy'
SITEURL = 'http://pbhealy.com'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = u'en'


THEME = "pelican-themes/pure-single"

ARTICLE_URL= 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

RESUME = "YES"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# from pure readme
COVER_IMG_URL = 'https://raw.githubusercontent.com/bheal521/bheal521.github.io/master/images/desk cover image.jpg'
PROFILE_IMG_URL = 'https://raw.githubusercontent.com/bheal521/bheal521.github.io/master/images/myAvatar.jpg'
FAVICON_URL = "https://raw.githubusercontent.com/bheal521/bheal521.github.io/master/images/favicon.ico"
TAGLINE = "Being a statistician means never having to say you're certain"



# Variables for the crowsfoot theme
Social = SOCIAL = (
      ('github', 'https://github.com/bheal521'),
      ('twitter', 'https://twitter.com/bheal521'),
	  ('envelope', 'mailto:peterbenjamin.healy@gmail.com?Subject=Howdy'),
	  ('linkedin-square', 'https://www.linkedin.com/in/pbhealy'),
	  ('spotify', 'https://play.spotify.com/user/bheal521')
)



READERS = {"html": None}

DEFAULT_PAGINATION = 10

FEED_RSS = "Ben's Feed"
SHOW_ARTICLE_AUTHOR = False
LICENSE_URL = 'http://creativecommons.org/licenses/by-sa/4.0/'
LICENSE_NAME = 'CC BY-SA'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-themes/pure-single"

#DISPLAY_CATEGORIES_ON_MENU = False

OUTPUT_PATH = '../bheal521.github.io'

GOOGLE_ANALYTICS = "UA-49434230-1"

DISQUS_SITENAME = "bheal521"
DISQUS_ON_PAGES = True

