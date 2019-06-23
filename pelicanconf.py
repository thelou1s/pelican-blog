#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# import date

AUTHOR = 'thelou1s'
SITENAME = 'The Utopia'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

#DEFAULT_LANG = 'Chinese (Simplified)'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
# https://github.com/getpelican/pelican/issues/1103
RELATIVE_URLS = True

###############################################################################
# Theme
THEME = r'/Users/luis/PycharmProjects/pelican-blog/pelican/themes/pelican-clean-blog'

SOCIAL = (('twitter', 'https://twitter.com/myprofile'),
          ('github', 'https://github.com/myprofile'),
          ('facebook','https://facebook.com/myprofile'),
          ('flickr','https://www.flickr.com/myprofile/'),
          ('envelope','mailto:my@mail.address'))

# Theme
# THEME = r'E:\Python\pelican-blog\pelican\pelican\themes\pure'
# COVER_IMG_URL = 'static\home-bg.jpg'
# PROFILE_IMAGE_URL = 'static\home-bg.jpg'
# TAGLINE - Used for the page titles and some meta tags.
# DISQUS_SITENAME - Set this to enable disqus comments in articles.

# Theme
# https://github.com/gilsondev/pelican-clean-blog/tree/ea156f8f1741e473bc0ab848b7c8898112d6ffb5
# THEME = r'E:\Python\pelican-blog\pelican\pelican\themes\pelican-clean-blog'
# HEADER_COVER = r'static\home-bg.jpg'
# GITHUB_URL = 'http://github.com/myprofile'
# TWITTER_URL = 'http://twitter.com/myprofile'
# FACEBOOK_URL = 'http://facebook.com/myprofile'

# # NEST Template
# THEME = r'E:\Python\pelican-blog\pelican\pelican\themes\nest'
# # THEME = 'nest'
# SITESUBTITLE = u'My Awesome Blog'
# # Minified CSS
# NEST_CSS_MINIFY = True
# # Add items to top menu before pages
# MENUITEMS = [('Homepage', '/'),('Categories','/categories.html')]
# # Add header background image from content/images : 'background.jpg'
# NEST_HEADER_IMAGES = ''
# NEST_HEADER_LOGO = '/image/logo.png'
# # Footer
# NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
# NEST_SITEMAP_MENU = [('Archives', '/archives.html'),('Tags','/tags.html'), ('Authors','/authors.html')]
# NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
# NEST_SITEMAP_RSS_LINK = u'RSS Feed'
# NEST_SOCIAL_COLUMN_TITLE = u'Social'
# NEST_LINKS_COLUMN_TITLE = u'Links'
# NEST_COPYRIGHT = u'&copy; blogname 2015'
# # Footer optional
# NEST_FOOTER_HTML = ''
# # index.html
# NEST_INDEX_HEAD_TITLE = u'Homepage'
# NEST_INDEX_HEADER_TITLE = u'My Awesome Blog'
# NEST_INDEX_HEADER_SUBTITLE = u'Smashing The Stack For Fun And Profit'
# NEST_INDEX_CONTENT_TITLE = u'Last Posts'
# # archives.html
# NEST_ARCHIVES_HEAD_TITLE = u'Archives'
# NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
# NEST_ARCHIVES_HEADER_TITLE = u'Archives'
# NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives for all posts'
# NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# # article.html
# NEST_ARTICLE_HEADER_BY = u'By'
# NEST_ARTICLE_HEADER_MODIFIED = u'modified'
# NEST_ARTICLE_HEADER_IN = u'in category'
# # author.html
# NEST_AUTHOR_HEAD_TITLE = u'Posts by'
# NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
# NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
# NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# # authors.html
# NEST_AUTHORS_HEAD_TITLE = u'Author list'
# NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
# NEST_AUTHORS_HEADER_TITLE = u'Author list'
# NEST_AUTHORS_HEADER_SUBTITLE = u'Archives listed by author'
# # categories.html
# NEST_CATEGORIES_HEAD_TITLE = u'Categories'
# NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
# NEST_CATEGORIES_HEADER_TITLE = u'Categories'
# NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'
# # category.html
# NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
# NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
# NEST_CATEGORY_HEADER_TITLE = u'Category'
# NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'
# # pagination.html
# NEST_PAGINATION_PREVIOUS = u'Previous'
# NEST_PAGINATION_NEXT = u'Next'
# # period_archives.html
# NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
# NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
# NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
# NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
# NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# # tag.html
# NEST_TAG_HEAD_TITLE = u'Tag archives'
# NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
# NEST_TAG_HEADER_TITLE = u'Tag'
# NEST_TAG_HEADER_SUBTITLE = u'Tag archives'
# # tags.html
# NEST_TAGS_HEAD_TITLE = u'Tags'
# NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
# NEST_TAGS_HEADER_TITLE = u'Tags'
# NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
# NEST_TAGS_CONTENT_TITLE = u'Tags List'
# NEST_TAGS_CONTENT_LIST = u'tagged'
# # Static files
# STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg']
# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'},
#     'extra/logo.svg': {'path': 'logo.svg'}
# }

# # Theme customizations
# MINIMALXY_CUSTOM_CSS = 'static/custom.css'
# MINIMALXY_FAVICON = 'favicon.ico'
# MINIMALXY_START_YEAR = 2009
# # MINIMALXY_CURRENT_YEAR = date.today().year
#
# # Author
# AUTHOR_INTRO = u'Hello world! I’m John Doe.'
# AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I like coffee, birds and Python.'
# AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'
# AUTHOR_WEB = 'http://mypersonalsite.com'
#
# # Services
# GOOGLE_ANALYTICS = 'UA-12345678-9'
# DISQUS_SITENAME = 'johndoe'
#
# # Social
# SOCIAL = (
#    ('facebook', 'http://www.facebook.com/johndoe'),
#    ('twitter', 'http://twitter.com/johndoe'),
#    ('github', 'https://github.com/johndoe'),
#    ('linkedin', 'http://www.linkedin.com/in/johndoe'),
# )
#
# # Menu
# # MENUITEMS = (
# #    ('Categories', '/' + CATEGORIES_SAVE_AS),
# #    ('Archive', '/' + ARCHIVES_SAVE_AS),
# # )
