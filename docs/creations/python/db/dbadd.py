#IMPORTANT:  Do NOT scrape websites or data with prohibiting items in Terms and Conditions.

import sqlite3

db_connect = sqlite3.connect("IOGENESIS.db")
cursor = connection.cursor()

# Create the items tuple


# Insert tuple items into the db
for iname, icat, idesc in itup:
    db_entry_command_one = """INSERT INTO items ({},{})""".format(iname,idesc)
    db_entry_command_two = """INSERT INTO item_categories ({})""".format(icat)
    cursor.execute(db_entry_command_one)
    cursor.execute(db_entry_command_two)

db_lookup_command = """SELECT * FROM items"""

cursor.execute(db_lookup_command)

lookup_answer = cursor.fetchall()

for x in lookup_answer:
    print(x)

#We want to compare the entry and lookup values to initiate an Error Statement if necessary.

#Save Changes
db_connect.commit()

db_connect.close()
