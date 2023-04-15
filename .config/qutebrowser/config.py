import os 

# Determines if your on mac or linux
if os.popen('echo $OSTYPE').read() == 'linux-gnu\n':
    user_dir = 'home'
else:
    user_dir = 'Users'


config.load_autoconfig(False)

# Other
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

# Colors
c.tabs.favicons.show = 'never'
c.url.default_page = f'file:///{user_dir}/haukur/.config/qutebrowser/default_page/index.html'
c.url.searchengines = {'DEFAULT': 'https://www.google.com/search?q={}'}
c.url.start_pages = f'file:///{user_dir}/haukur/.config/qutebrowser/default_page/index.html'
c.colors.completion.fg = ['gray', 'gray', 'gray']
c.colors.completion.odd.bg = '#0d0d0d'
c.colors.completion.even.bg = '#000000'
c.colors.completion.category.bg = '#000000'
c.colors.completion.item.selected.bg = '#ffffff'
c.colors.completion.item.selected.match.fg = '#000000'
c.colors.completion.match.fg = '#ffffff'
c.colors.keyhint.fg = '#ffffff'
c.colors.keyhint.suffix.fg = '#ffff00'
c.colors.statusbar.normal.fg = '#808080'
c.colors.statusbar.normal.bg = '#000000'
c.colors.statusbar.insert.fg = '#000000'
c.colors.statusbar.insert.bg = '#ffffff'
c.colors.statusbar.url.fg = '#808080'
c.colors.statusbar.url.hover.fg = '#0066ff'
c.colors.statusbar.url.success.http.fg = '#33ff00'
c.colors.statusbar.url.success.https.fg = '#33ff00'
c.colors.statusbar.url.warn.fg = '#ffff00'
c.colors.tabs.bar.bg = '#121212'
c.colors.tabs.odd.bg = '#242424'
c.colors.tabs.even.bg = '#242424'

# Darkmode
c.colors.webpage.darkmode.enabled = True
