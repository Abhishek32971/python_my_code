import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE Ages(
             name VARCHAR(128),
             age INTEGER
             )"""
         )
def add_people(sName, iAge):
    with conn:
        c.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':sName, 'age':iAge})

# dPeople = {'Oz': 25, 'Noor': 31, 'Praise': 22, 'Kerris': 26, 'Louise': 19, 'Ismaeel': 17 }
# for keyName, valueAge in dPeople.items():
#     add_people(keyName, valueAge)

lPeople = [('Oz', 25), ('Noor', 31), ('Praise', 22), ('Kerris', 26), ('Louise', 19), ('Ismaeel', 17)]
for tItem in lPeople:
    sName, iAge = tItem
    add_people(sName, iAge)

c.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")
print(c.fetchall())

conn.commit()
conn.close()

conn = sqlite3.connect('emaildb2.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
list_1 =[]
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    dom = email.find('@')
    org = email[dom+1:len(email)]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()