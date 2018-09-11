#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Damien Martin'
SITENAME = u'Stacked Turtles'
SITEURL = ''

# Themes I like:
# pelican-themes/elegant
# pelican-themes/chunk    (maybe a little too simple?)
# pelican-themes/medius   (need a lot of pictures to make articles work)
# pelican-themes/pelican-cait
# pelican-themes/syte     (doesn't work: encountered unknown tag assets)
# pelican-themes/html5-dopetrope
THEME = "pelican-themes/mydopetrope"  # A modification of html5-dopetrope
#THEME = "pelican-themes/pelican-cait"
PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# This is specific to html5-dopetrope
#MENUITEMS = [['Portfolio','portfolio.html'],
#             ['Posts','posts.html'],
#             ['Visualizations','visual.html'],
#             ['Calculators','calculators.html']];

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
LINKS = (('FiveThirtyEight: Data science and politics', 'https://fivethirtyeight.com'),
         ('Darkhorse analytics: data science and visualization', 'http://www.darkhorseanalytics.com/blog/'),
         ('Mike Bostock\'s D3 gallery', 'https://bl.ocks.org/'),
         ('Dataquest: getting started in data science', 'https://www.dataquest.io/blog/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MAIL = 'damien.j.martin@gmail.com'
FACEBOOK_USER = 'kiwidamien'
LINKEDIN_USER = '../in/damien-martin-91171724'

ABOUT_IMAGE = "theme/images/turtle.svg"
ABOUT_LINK  = "about.html"
ABOUT_TEXT  = "Stacked Turtles is a blog about gaining insights from data, and effecively communicating them"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup',
           'pelican_fontawesome', 'pelican_alias'
]
