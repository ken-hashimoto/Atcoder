A,B,C,D,E,F,X = map(int,input().split())
Takahashi = 0
Aoki = 0
T_is_walking = ([True]*A + [False]*C)*100
A_is_walking = ([True]*D + [False]*F)*100
for i in range(X):
  if T_is_walking[i]:
    Takahashi += B
  if A_is_walking[i]:
    Aoki += E
if Takahashi > Aoki:
  print('Takahashi')
elif Takahashi < Aoki:
  print('Aoki')
else:
  print('Draw')