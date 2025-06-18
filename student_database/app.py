import sqlite3
from flask import Flask, render_template,request, redirect

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_data')
def add_data():
    return render_template('form_and_table.html')
 
@app.route('/back')
def back():
    return redirect('/')

@app.route('/submit',methods=['POST'])
def submit():
    roll_no=request.form['roll_no']#syntax for post method

    name=request.form['name'].lower()
    
    email=request.form['email'].lower()
    
    dept=request.form['dept'].lower()
    
    studing_year=request.form['studing_year']
    
    doj=request.form['doj']


    con=sqlite3.connect('form_database.db')
    cursor=con.cursor()
    if roll_no !=None:
      cursor.execute('insert into student_reg (roll_no,name,email,dept,studing_year,doj) values (?,?,?,?,?,?)',(roll_no,name,email,dept,studing_year,doj))

      con.commit()
      con.close()
      print("******data loaded sucessfully*****")
      return redirect('/add_data')
   

@app.route('/view_data',methods=['GET'])
def view_data():
    con=sqlite3.connect('form_database.db')
    cursor=con.cursor()
    search_col=request.args.get('find')#syntax for the gt method
    searching_data=request.args.get('search',' ').lower()
    
    operation_data=request.args.get('operation')

    print(search_col)
    print(searching_data)
    if(operation_data=='view'):
      if(search_col=='all'):
        cursor.execute('select * from student_reg order by name asc ')
      elif search_col in ['roll_no','name','dept','studing_year','DOJ','email']:
        query = f"SELECT * FROM student_reg WHERE {search_col} = ? ORDER BY name ASC"
        cursor.execute(query, [searching_data])
      
       #the above is retriveing the data , we using like this because '?' only for values/ content but not for the column names thats why search_vol can't replace with ?; if i do this it will consider column name was replaces with the data in search_col variable
       #   
    elif(operation_data=='delete'):
       if(search_col=='all'):
        cursor.execute('delete from student_reg')
       elif search_col in ['roll_no','name','dept','studing_year','DOJ','email']:
        query = f"delete from student_reg where {search_col} = ?"
        cursor.execute(query, (searching_data,))
       con.commit()
       print("deleted")
    else:
         return render_template('view_db.html')    


    
    data=cursor.fetchall() 
         
    cursor.close()

   
 
    return render_template('view_db.html',datas=data)

    #for this function con.commit is for updation or modification in hte db and not for viewing the db and also fetchall() also works for viewing the db and not for updation or modification the db

if __name__ == '__main__':
    app.run(debug=True)   
