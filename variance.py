def Variance(L,dof=0):
  sum=0;sumd=0;sumds=0
  d1=[];d2=[]
  N=len(L)
  for i in L:
    sum=sum+i
  mean=sum/len(L)
  for i in L:
    deviation=i-mean
    d1.append(deviation)
    devsqure=deviation*deviation
    d2.append(devsqure)
  for i in d1:
      sumd=sumd+i
  for i in d2:
   sumds=sumds+i
  var=sumds/(N-dof)
  return(var)