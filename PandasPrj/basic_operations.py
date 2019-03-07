import numpy as np
import pandas as pd
from pandas import DataFrame


def header(msg):
    print('-'*50)
    print(msg)

datadf=pd.read_csv('C:\Data\PythonCode\Data\data.csv')

rulesdf=pd.read_csv("C:\Data\PythonCode\Data\\rules.csv")

rulesdf.sort_values('RULE_RK',ascending=True, inplace=True)

output=datadf.query('emp==-1')

for r in rulesdf.values:
    if r[2]=='=':
        query=str(r[1])+' == ' + str(r[3])
        header(query)
    elif r[2]=='!=':
        query=str(r[1])+' != ' + str(r[3])
    dd=datadf.query(query)
    dd["RULE_RK"]=str(r[0])
    output=output.append(dd)
    #print(dd)

header(output)
