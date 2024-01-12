def ANOVA(T1,T2,T3):
  sumt1=0;sumt2=0;sumt3=0;sumt4=0;sumt5=0;sumt6=0;
  n1=len(T1)
  n2=len(T2)
  n3=len(T3)
  N=n1+n2+n3
  t1=[];t2=[];t3=[];t4=[]
  for i in T1:
    sumt1=sumt1+i
  mean1=sumt1/n1
  s1=sumt1*mean1
  for i in T2:
    sumt2=sumt2+i
  mean2=sumt2/n2
  s2=sumt2*mean2
  for i in T3:
    sumt3=sumt3+i
  mean3=sumt3/n3
  s3=sumt3*mean3
  T=sumt1+sumt2+sumt3
  Xbar=T/N
  for i in T1:
    t1.append(i*i)
  for i in t1:
    sumt4=sumt4+i
  for i in T2:
    t2.append(i*i)
  for i in t2:
    sumt5=sumt5+i
  for i in T3:
    t3.append(i*i)
  for i in t3:
    sumt6=sumt6+i
  sum33=sumt4+sumt5+sumt6
  correction=(T*T)/N
  TSS=sum33-correction
  SSBG=((sumt1*sumt1)/n1)+((sumt2*sumt2)/n2)+((sumt3*sumt3)/n3)-correction
  SSWG=TSS-SSBG
  DFtss=N-1
  DFbg=3-1
  DFWG=DFtss-DFbg
  VBG=SSBG/DFbg
  VWG=SSWG/DFWG
  varianceRatio=VBG/VWG
  return(varianceRatio)