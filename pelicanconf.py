#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ben Healy'
SITENAME = u'Ben Healy'
SITESUBTITLE = "Being a statistician means never having to say you're certain"
SITEURL = 'http://bheaal521.github.io'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
TAG_FEED_ATOM = 'feeds/tags/%s.atom.xml'

# Blogroll
LINKS = False

# Social widget
#SOCIAL = False

# Variables for the crowsfoot theme
RESUME = "YES"
EMAIL_ADDRESS = 'peterbenjamin.healy@gmail.com'
GITHUB_ADDRESS = 'https://github.com/bheal521'
TWITTER_ADDRESS = 'https://twitter.com/bheal521'
LINKEDIN_ADDRESS = 'https://www.linkedin.com/in/pbhealy'
PROFILE_IMAGE_URL = 'https://raw.githubusercontent.com/bheal521/bheal521.github.io/master/images/myAvatar.jpg'
FEED_RSS = "Ben's Feed"
SHOW_ARTICLE_AUTHOR = False
LICENSE_URL = 'http://creativecommons.org/licenses/by-sa/4.0/'
LICENSE_NAME = 'CC BY-SA'


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pelican-themes/crowsfoot-master"

DISPLAY_CATEGORIES_ON_MENU = False

OUTPUT_PATH = '../bheal521.github.io'

GOOGLE_ANALYTICS = "UA-49434230-1"

DISQUS_SITENAME = "bheal521"

