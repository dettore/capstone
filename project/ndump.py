import sqlite3
import time
import re
import zlib
from datetime import datetime, timedelta

# Open the main content (Read only)
conn = sqlite3.connect('file:crawler.sqlite?mode=ro', uri=True)
cur = conn.cursor()

# Title:      If coronavirus hits London, your boss might ask you to stay at home | CBC News

#allsenders = list()
titles = 0
#cur.execute('''SELECT title FROM Pages''')
cur.execute('''SELECT url, tag, title FROM Pages''')
for title_row in cur :
    #sender = fixsender(message_row[0])
    #if sender is None : continue
    #if 'gmane.org' in sender : continue
    #if sender in allsenders: continue
    #allsenders.append(sender)
    titles +=1
    print('')
    print('Retrieved:',title_row[0].decode())
    print('Tag:      ',title_row[1])
    print('Title:    ',title_row[2])
    #print(title_row[0])

#print("Loaded allsenders",len(allsenders),"and mapping",len(mapping),"dns mapping",len(dnsmapping))
print('')
print("Loaded titles:",titles)

cur.close()
