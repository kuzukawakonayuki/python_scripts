#coding: utf-8

import sqlite3#SQLite3インポート

print("DBtest |1--TableCreate|2--RecordCreate|3--RecordPrint|")
test = int(raw_input())
test2 = int(0)
con = sqlite3.connect('./sample.db')
cur = con.cursor()

if test == 1:
    class DBc:
        sql = "create table fruits(name,price);"
        cur.execute(sql)
        con.close()

elif test == 2:
    class Tc:
        sql = "insert into fruits values('apple','100yen')"
        cur.executemany("insert into fruits values(?,?)",[('orange','150yen'),('banana','200yen')])
        cur.execute(sql)
        con.commit()
        con.close()



else:
    class DBp:
        sql = "select * from fruits"
        c = cur.execute(sql)

        while test2 < 3:
            row = c.fetchone()
            print row[0],row[1]
            test2 += 1

        con.close()