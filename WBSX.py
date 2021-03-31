import webbrowser
def open_term(home_url, term):
    '''Open a search term in the home_url'''
    if ' ' in term:
        new_term=term.replace(' ', '%20')
        webbrowser.open_new_tab('%s/search?q=%s' % (home_url, new_term))
    else:
        webbrowser.open_new_tab('%s/search?q=%s' % (home_url, term))
def wbsxcredits():
    '''Webbrowser-X credits'''
    print('''Webbrowser-X credits:
    https://docs.python.org/3/library/webbrowser.html
    Python webbrowser module''')
def wbsxlicense():
    '''Webbrowser-X license (licensed under MIT license)'''
    print('''MIT License

Copyright (c) 2021 ProgrammerTheProgrammer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''')
