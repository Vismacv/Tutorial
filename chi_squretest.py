def chi_squre(O,E):
  D=[]
  sum=0
  n=6
  TV=11.07
  for i,j in zip(O,E):
    D.append((i-j)**2/j)
  for i in D:
    sum=sum+i
  df=n-1
  if sum<TV:print("Accept")
  else:print("Reject")
  return(sum)