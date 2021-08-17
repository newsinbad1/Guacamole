import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=somvs065.som.ucsf.edu,2433;'
                      'Database=SOMEduDataHub;'
                      'Trusted_Connection=yes;')
conn2 = pyodbc.connect('Driver={SQL Server};'
                    'Server=somvs065.som.ucsf.edu,2433;'
                    'Database=SOMEduDataHub;'
                    'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor_insert = conn2.cursor()


#CREATE TABLE SOMEduDataHub.dbo.zkat_test (id varchar(255), item varchar(255));


cursor.execute("SELECT TOP 3 clerkshipID, clerkship_name FROM SOMEduDataHub.dbo.i_clerkships WHERE clerkship_name LIKE '%110%'")

# for row in cursor:
#     print(row)

for row in cursor:
    insert_row = "INSERT INTO SOMEduDataHub.dbo.zkat_test (id,item) VALUES (?,?)"
    cursor_insert.execute(insert_row, (row[0],row[1]))

conn.commit()

conn2.commit()
conn2.close()

cursor.execute("SELECT * FROM SOMEduDataHub.dbo.zkat_test")
for row in cursor:
    print(row)

conn.commit()
conn.close()
