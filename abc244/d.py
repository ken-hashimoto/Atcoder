S1,S2,S3 = input()
T1,T2,T3 = input()
if (S1,S2,S3) == (T1,T3,T2):
  print('No')
elif (S1,S2,S3) == (T3,T2,T1):
  print('No')
elif (S1,S2,S3) == (T2,T1,T3):
  print('No')
else:
  print('Yes')