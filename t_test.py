def t_Test(x1,x2):
  sum1=0;sum2=0;sumx1=0;sumx2=0
  n1=len(x1);n2=len(x2)
  r=0.50
  TV=2.552
  X1=[];X12=[];X2=[];X22=[]
  for i in x1:
    sum1=sum1+i
  mean1=sum1/n1
  for i in x1:
    x1=i-mean1
    X1.append(x1)
  for i in X1:
    x1sqr=i*i
    X12.append(x1sqr)
  for i in X12:
    sumx1=sumx1+i
  for i in x2:
    sum2=sum2+i
  mean2=sum2/n2
  for i in x2:
    x2=i-mean2
    X2.append(x2)
  for i in X2:
    x2sqr=i*i
    X22.append(x2sqr)
  for i in X22:
    sumx2=sumx2+i
  SD1=(sumx1/(n1-1))**0.5
  SD2=(sumx2/(n2-1))**0.5
  SEk1=SD1/(n1)**0.5
  SEk2=SD2/(n2)**0.5
  SEd=((SEk1*SEk1)+(SEk2*SEk2)-2*r*SEk1*SEk2)**0.5
  t=(mean1-mean2)/SEd
  df=n1+n2-2
  if t>TV:print("Accept Null Hypothesis")
  else:print("Reject Null Hypthesis")
  return(t)