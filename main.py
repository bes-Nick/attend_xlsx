import pandas as pd
import datetime

today = datetime.date.today()
today = today.strftime('%d-%m-%Y')
stud = []
df = pd.DataFrame()
df= pd.read_excel("attendance.xlsx")
for i,row in df.iterrows():
    stud.append(row['students'])

def attend(name):
    if name in stud:
        if today in df.columns:
            idx = df.index[df['students']==name]
            index = -1
            for i in idx:
                index = i;
            if index != -1:
                df.loc[index].at['23-11-2022'] = 'P'
        else:
            df.insert(loc=len(df.columns),column=today,value='A')
            idx = df.index[df['students']==name]
            index = -1
            for i in idx:
                index = i;
            if index != -1:
                df.loc[index].at['23-11-2022'] = 'P' 
        df.to_excel("attendance.xlsx", sheet_name='Sheet1', index=False)

print(stud)
attend('rahul')
attend('rahul')
attend('pankaj')
attend('sumit')
print(df)


