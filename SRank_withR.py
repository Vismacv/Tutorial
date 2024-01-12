def rank(R1,R2):
  D=[];D1=[]
  sum=0
  n=len(R1)
  for i,j in zip(R1,R2):
    D.append(i-j)
  for i in D:
    D1.append(i*i)
  for i in D1:
    sum=sum+i
  r=1-(6*sum)/((n*n*n)-n)
  return(r)