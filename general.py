import pandas as pd


file = r'file.log'

cols=['host','1','userid','date','tz','endpoint','status','data','referer','user_agent']
df=pd.read_csv(file,delim_whitespace=True,names=cols).drop('1',1)

print (df.head())


unique_ip=df.host.unique()
print(unique_ip)


total = df['data'].sum()
print('the server traffic is :',(total))


status_freq = pd.DataFrame(columns=['status', 'Frequency'])


status_freq['Frequency'] = df.groupby('status').size()

status_freq['status']=df.groupby('status').agg({'status':lambda x:list(x).__getitem__(1)})

ap = status_freq[status_freq['status']>=500].sum()

print ('the requests generated requests a 5xx server error :',(ap['Frequency']))

print('distring ips visited server :',len(unique_ip))