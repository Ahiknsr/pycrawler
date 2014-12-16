import mechanize
import cookielib


br=mechanize.Browser()
cookie_jar=cookielib.CookieJar()
br.set_cookiejar(cookie_jar)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0')]
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_equiv(True)
#br.set_handle_gzip(True)#experimental feature 
br.set_handle_redirect(True)
br.set_handle_referer(True)
