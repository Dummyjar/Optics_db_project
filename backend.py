import sqlite3

def connect():
    conn= sqlite3.connect('optics.db')
    c=conn.cursor()
    c.execute("""
            CREATE TABLE IF NOT EXISTS students (
                fname text,
                lname text,
                reg text PRIMARY KEY,
                roll text,
                sex text,
                phone integer,
                year integer
                
            )  
    """)
    conn.commit()
    conn.close()

def entrydokha(fn,ln,reg,roll,sex,ph,year):
    conn= sqlite3.connect('optics.db')
    c=conn.cursor()
    c.execute("INSERT INTO students VALUES(?,?,?,?,?,?,?)",(fn,ln,reg,roll,sex,ph,year))
    conn.commit()
    conn.close()

def show():
    conn= sqlite3.connect('optics.db')
    c=conn.cursor()
    c.execute("SELECT * FROM students")
    items =c.fetchall()
    conn.commit()
    conn.close()
    return items

def Del(rg):
    conn=sqlite3.connect('optics.db')
    c=conn.cursor()
    c.execute("DELETE FROM students WHERE reg=(?)",(rg,))
    conn.commit()
    conn.close()
    

def edit(fn,ln,reg,roll,sex,ph,year):
    conn=sqlite3.connect('optics.db')
    c=conn.cursor()
    c.execute("UPDATE students SET fname=?,lname=?,roll=?,sex=?,phone=?,year=? WHERE reg=?",(fn,ln,roll,sex,ph,year,reg))
    conn.commit()
    conn.close()

def find(fn='',ln='',reg='',roll='',sex='',ph='',year=''):
    conn=sqlite3.connect('optics.db')
    c=conn.cursor()
    c.execute(""" SELECT * FROM students WHERE
    fname=? OR lname=? OR roll=? OR sex=? OR phone=? OR year=?  OR reg=?
    
    """,(fn,ln,roll,sex,ph,year,reg))
    row = c.fetchall()

    conn.commit()
    conn.close()
    return row



connect()

def run():
    pass

def check():
    if len(show())==0:
        return False
    else:
        return True

print(show())