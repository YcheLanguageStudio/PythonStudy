f=open('./ip.data','r')
d=f.read()
f.close()
a={}
for i in range(0,len(d),5):
    t=ord(d[i+2])*256+ord(d[i+3])
    if a.has_key(t):
        a[t]+=256
    else:
        a[t]=256
