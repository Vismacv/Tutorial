def Rank(x,y):
  x1=[];y1=[];D=[];D1=[]
  sum=0
  n=len(x)
  rank1=[sorted(x,reverse=True).index(i)+1 for i in x]
  x1.append(rank1)
  rank2=[sorted(y,reverse=True).index(i)+1 for i in y]
  y1.append(rank2)
  for i,j in zip(x1[0],y1[0]):
    D.append(i-j)
  for i in D:
    D1.append(i*i)
  for i in D1:
    sum=sum+i
  r=1-(6*sum)/((n*n*n)-n)
  return(r)