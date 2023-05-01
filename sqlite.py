import sqlite3
import time

con = sqlite3.connect('db.sqlite3', timeout=10)   # db 연결
cursor_db = con.cursor()   # db를 연다
# cursor_db.execute('DROP TABLE accounts_test')

con.commit()  # 저장한다
con.close()   # db 닫기
