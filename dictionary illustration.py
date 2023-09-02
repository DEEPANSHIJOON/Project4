lst=[1,2,3,4,6,-1,-2,-3,-4]
# lst1=[]
# lst2=[]
# dict={}
dict={'pos':[],'neg':[]}
for x in lst:
    if x>=0:
        dict['pos'].append(x)
    else :
        dict['neg'].append(x)
# dict['pos']=lst1
# dict['zero']=0
# dict['neg']=lst2
dict['pos']=1
print(dict)
