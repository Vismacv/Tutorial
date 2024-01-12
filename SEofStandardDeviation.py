def SEofSD(x):
  N=5
  sum=0;sumx=0
  D=[];xsqur=[]
  for i in x:
    sum=sum+i
  mean=sum/N
  for i in x:
    Deviation=i-mean
    D.append(Deviation)
  for i in D:
    xsqure=i*i
    xsqur.append(xsqure)
  for i in xsqur:
    sumx=sumx+i
  SD=(sumx/(N-1))**0.5
  SE=SD/(2*N)**0.5
  return(SE)