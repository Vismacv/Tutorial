def correlation(x,y):
  x1=[];y1=[];x2=[];y2=[];z1=[]
  sum1=0;sum2=0;sum3=0;sum4=0;sum5=0
  for i in x:
    sum1=sum1+i
  mean1=sum1/len(x)
  for i in x:
    deviation1=i-mean1
    x1.append(deviation1)
    devsqu1=deviation1*deviation1
    x2.append(devsqu1)
  for i in x2:
    sum3=sum3+i
  for i in y:
    sum2=sum2+i
  mean2=sum2/len(y)
  for i in y:
    deviation2=i-mean2
    y1.append(deviation2)
    devsqu2=deviation2*deviation2
    y2.append(devsqu2)
  for i in y2:
    sum4=sum4+i
  for i,j in zip(x1,y1):
    z1.append(i*j)
  for i in z1:
    sum5=sum5+i
  r=sum5/(sum3*sum4)**0.5
  return(r)