from datetime import datetime
import re
import pandas as pd
file = open('C:/Users/chaithu/Desktop/Anomization/input001.txt', 'r')
lines=[]
for line in file:
    #print(line)
    lines.append(line)
h=[]
h.append('T')
penul=[]
ki=[]
fg=[]
for i in range(len(lines)):
    g=lines[i].split()
    m=re.findall(r"[\/\d:\w.]+", lines[i])
    u=m[1]+m[4]
    #print(u)
    k=re.split(r':',u)
    c=re.split(r'/',u)
    #print(c)
    fg.append(k[1])
    fg.append(k[2])
    fg.append(c[5])
    fg.append(g[8])
    
    date_object = datetime.strptime(k[0], '%d/%b/%Y').strftime('%d-%m-%Y')
    
chunks = [fg[x:x+4] for x in range(0, len(fg),4)]    
ko_old='99'
ke_old='45'
hj='jajsj'
hu=pd.DataFrame(chunks)
ti=list(set(hu[0]))
tu=list(set(hu[1]))
ho=[]
for i in range(len(ti)):
    df_final=hu[hu[0].str.contains(ti[i])]
    for j in range(len(tu)):
        df_final1=df_final[df_final[1].str.contains(tu[j])]
        ho.append(df_final1)
hp=[]
for i in range(2,len(ho)-1):
    hp.append(ho[i])  
for i in range(len(hp)):
    g=len(hp[i][hp[i][3]!='500'])
    k=len(hp[i])
    hp[i][4]=((g/k)*100)
for i in range(len(hp)):
    del hp[i][2]
    del hp[i][3]
df_finale1=pd.concat(hp)    
df_finale=df_finale1.drop_duplicates()
hooki=[]
for i in range(len(lines)):
    g=lines[i].split()
    m=re.findall(r"[\/\d:\w.]+", lines[i])
    u=m[1]+m[4]
    k=re.split(r':',u)
    c=re.split(r'/',u)
    fg.append(k[1])
    fg.append(k[2])
    fg.append(c[5])
    fg.append(g[8])
    gp=df_finale[df_finale[0] == k[1]]
    gk=gp[gp[1] == k[2]]
    g[8]=gk[4].iloc[0]
    
    date_object = datetime.strptime(k[0], '%d/%b/%Y').strftime('%d-%m-%Y')
    hooki.append(date_object+'T'+k[1]+':'+k[2])
    hooki.append(m[4])
    hooki.append(g[8])
    pooki.append(hooki)
    hooki=[]
df_1=pd.DataFrame(pooki)   
df_2=df_1.drop_duplicates()
for i in range(len(df_2)):
    print(df_2[0].iloc[i],df_2[1].iloc[i],df_2[2].iloc[i])
