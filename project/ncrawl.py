import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('crawler.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Pages
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, tag TEXT,
     title TEXT, error INTEGER)''')

# cur.execute('''CREATE TABLE IF NOT EXISTS Links
#     (from_id INTEGER, to_id INTEGER)''')

# cur.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')

fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'links.txt'
fhand = open(fname)

read_count = 0
retrieve_count = 0 
first = True

for line in fhand:
    if read_count > 213 :
        print('')
        print('Retrieved 214 locations, restart to retrieve more')
        break

    url = line.rstrip()
    #print(len(url))
    #print(type(url))
    #print(memoryview(url.encode())

    #print('')
    cur.execute("SELECT title FROM pages WHERE url= ?",
        (memoryview(url.encode()), ))

    try:
        data = cur.fetchone()[0]
        if first:
            #print("Found in database ",url)
            print("Restarting...")
            first = False
        continue
    except:
        pass

    read_count += 1
    print('')
    print("Retreiving:",url)
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break
    except:
        print('Error Retrieving')
        continue

    retrieve_count += 1
    soup = BeautifulSoup(html, 'html.parser')
    html = soup.find('title')

    tag = str(html)
    title = soup.title.text

    # Retrieve the title tag
    print('Tag:       ',tag) # Prints the tag
    print('Title:     ',title) # Prints the tag string content

    #print(type(title))
    #print(type(title.string))

    cur.execute('INSERT OR IGNORE INTO Pages (url, tag, title) VALUES ( ?, ?, ? )', ( memoryview(url.encode()), tag, title) )
    conn.commit()

print('')
print('Links Read:',read_count)
print('Links Retrieved:',retrieve_count)