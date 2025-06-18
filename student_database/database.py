import sqlite3

con=sqlite3.connect('form_database.db')

cursor=con.cursor()

cursor.execute('''
   create table if not exists student_reg(
   roll_no integer PRIMARY KEY NOT NULL,
   name text NOT NULL,
   email text,
   dept text,
   studing_year integer,
   doj text
   )
''')

#sample data

cursor.execute('''insert into student_reg (roll_no,name,email,dept,studing_year,doj) values(?,?,?,?,?,?) ''',(1036,'Arun MC','arun@gmail.com','CSE',2,13-9-2023))

con.commit()
con.close()

print("Database and table created sucessfully")