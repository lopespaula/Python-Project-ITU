
"""
	i). CREATE DATABASE LOGIN_APP;
 
	ii). CREATE TABLE LOG_DETAILS(NAME VARCHAR(20), USERNAME VARCHAR(20), PASSWORD VARCHAR(20), AVATAR VARCHAR(20));
 
	iii). DESC LOG_DETAILS;
"""
import sqlite3 as sql
mydb =   sql.connect('login_app.db')
 

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE LOG_DETAILS(NAME VARCHAR(20), USERNAME VARCHAR(20), PASSWORD VARCHAR(20), AVATAR VARCHAR(20))")

# mycursor.execute('''INSERT INTO LOG_DETAILS (NAME, USERNAME,PASSWORD)VALUES("Shipra","Shipra","Shipra")''')
mycursor.execute('select * from LOG_DETAILS')
result = mycursor.fetchall()
for row in result:

    print(f'{row[0]:2}{row[1]}{row[2]}' )
            
# mydb.commit()
mydb.close()


