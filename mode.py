def Mode(list):
  y={}
  for i in list:
    if not i in y:
      y[i]=1
    else:
        y[i]=y[i]+1
  return[g for g,l in y.items() if l==max(y.values())]