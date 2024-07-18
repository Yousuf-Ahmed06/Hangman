import sqlite3 as sql
conn = sql.connect('words.sqlite')
cur = conn.cursor()
# cur.executescript('''
# DROP TABLE IF EXISTS Words;
# CREATE TABLE Words (
#     id  INTEGER PRIMARY KEY,
#     word    TEXT UNIQUE
# );
# ''')
fhand = input("Please input file name: ")
if len(fhand) < 1:
    fhand = "FL notes.txt"
file = open(fhand)
for line in file:
    words = line.split(" ")
    word_list = [(word.strip().strip(".,()").lower(), ) for word in words if len(word) > 5]
    if len(word_list) > 0: 
        try: 
            cur.executemany('INSERT INTO Words (word) VALUES (?)', word_list)
            conn.commit()
        except: continue
    else: continue
print("end")
