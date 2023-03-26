import pypyodbc as obdc
import pyodbc 
import pandas as pd

cnxn = pyodbc.connect(driver='{SQL Server}', host='LAPTOP-8B15A33V', database='eSchooling_RA',
                      trusted_connection='yes')


entities = '''
    SELECT * FROM Entities;
'''
result = cnxn.execute(entities).fetchall()


stdMov = ''' SELECT * FROM StudentMovements
'''
result1 =  cnxn.execute(stdMov).fetchall()



aseLevls = ''' SELECT * FROM AseLevels'''

result2 =  cnxn.execute(aseLevls).fetchall()



classes = ''' SELECT * FROM Classes'''

result3 =  cnxn.execute(classes).fetchall()



courses = ''' SELECT * FROM Courses'''

result4 =  cnxn.execute(courses).fetchall()



eduCG = ''' SELECT * FROM EducationCourseGrades'''

result5 =  cnxn.execute(eduCG).fetchall()


df = pd.DataFrame(result)
df.to_csv('teste')
print (df)
