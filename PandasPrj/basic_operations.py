import numpy as np
import pandas as pd
from pandas import DataFrame


def header(msg):
    print('-'*50)
    print(msg)

datadf=pd.read_csv('..\Data\data.csv')

rulesdf=pd.read_csv("..\Data\\rules.csv")

rodf=pd.read_csv("..\Data\\rules_output.csv")

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
    dd["RULE_PRIORITY"] = str(r[4])
    output=output.append(dd)
    #print(dd)

header(output)

high_priority_rule=output.groupby(['emp'],as_index=False).max()
header(high_priority_rule)

header(rodf)

#print(rodf.lookup(rodf.index, rodf['RULE_RK']))

def func(df,k,f):
    #df[k]
    return(0)

for t in high_priority_rule.values:
    rule=t[1]
    key=t[0]
    query='RULE_RK =='+str(rule)
    n=rodf.query(query)
    #print(t["ATTR"].values[0])
    if n["ATTR"].values[0] not in high_priority_rule:
        high_priority_rule.insert(0, n["ATTR"].values[0], func(high_priority_rule,key,n["VALUE"].values[0]))
    print(high_priority_rule.where(query))

    #[n["ATTR"].values[0]])
    #print(high_priority_rule)
    #output[t["ATTR"].values]=0
    #print(t["ATTR"].values)


#print(high_priority_rule)
