import os 

# Determines if your on mac or linux
if os.popen('echo $OSTYPE').read() == 'linux-gnu\n':
    user_dir = 'home'
else:
    user_dir = 'Users'

# load_autoconfig
config.load_autoconfig(False)

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')
config.set('content.notifications.enabled', False, 'https://filmora.wondershare.com')
config.set('content.notifications.enabled', False, 'https://www.youtube.com')
config.set('content.notifications.enabled', False, 'https://www.reddit.com')

# start_pages
c.url.default_page = f'file:///{user_dir}/haukur/.config/qutebrowser/default_page/index.html'
c.url.start_pages = f'file:///{user_dir}/haukur/.config/qutebrowser/default_page/index.html'

# searchengine
c.url.searchengines = {'DEFAULT': 'https://www.google.com/search?q={}'}


# Colors
c.colors.completion.odd.bg = '#0d0d0d'
c.colors.completion.even.bg = '#000000'
c.colors.completion.category.bg = '#000000'
c.colors.completion.item.selected.bg = '#ffffff'
c.colors.completion.item.selected.match.fg = '#ff0000'
c.colors.completion.match.fg = '#ff0000'
c.colors.statusbar.normal.fg = '#808080'
c.colors.statusbar.normal.bg = '#000000'
c.colors.statusbar.insert.fg = '#000000'
c.colors.statusbar.insert.bg = '#ffffff'
c.colors.statusbar.url.fg = '#808080'
c.colors.statusbar.url.hover.fg = '#0066ff'
c.colors.statusbar.url.success.http.fg = '#33ff00'
c.colors.statusbar.url.success.https.fg = '#33ff00'
c.colors.statusbar.url.warn.fg = '#ffff00'
c.colors.webpage.darkmode.enabled = True
