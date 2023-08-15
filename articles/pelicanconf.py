# Site settings
SITENAME = "Wiktor's Blog"
AUTHOR = 'Wiktor Kaczor'
SITETITLE = AUTHOR
SITESUBTITLE = 'Software Engineer'
SITEURL = '/blog'
FAVICON = f'/static/favicon/favicon.ico'
SITELOGO = f'{SITEURL}/images/profile.jpg'
SITEDESCRIPTION = "Wiktor's blog about various technology topics and projects"

# Content settings
COPYRIGHT_YEAR = 2023

# Theme and menu settings
THEME = 'theme/'
MAIN_MENU = True # Show main menu
MENUITEMS = (
    ("Archives", f"{SITEURL}/archives.html"),
    ("Categories", f"{SITEURL}/categories.html"),
    ("Tags", f"{SITEURL}/tags.html"),
)
DEFAULT_PAGINATION = 10
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# Blogroll
LINKS = (('Résumé', 'https://wiktorkaczor.com/'),
         ('GitHub', 'https://github.com/wiktoraleksanderkaczor/'),
        ('LinkedIn', 'https://www.linkedin.com/in/wiktorkaczor/'))

# Output settings
PATH = 'content'
OUTPUT_PATH = '..' + SITEURL

# Internationalization
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True