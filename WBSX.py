import webbrowser
def open_term(home_url, term):
  webbrowser.open_new_tab('%s/search?q=%s' % (home_url, term))
