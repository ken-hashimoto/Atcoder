N = int(input())
match = [list(map(int, input().split())) for _ in range(N)]
MOD = 10**9 + 7
#以下、問題文では1-indexedだが0-indexedで考える
#bit_Sを整数bitが表す女性の集合とする
#例えばbit = 5のときはbin(bit) = 0b101なのでビットが立っているところに注目して
#bit_S = {左から数えて0人目の女性,2人目の女性}となる。



dp = [0 for _ in range(1<<22)]
#dp[bit] = (左から[bit_S]人の男性と女性の集合Sでマッチングするときの場合の数)
#ただし集合Sに対して[S]はSに含まれる要素の数を表すものとする
#求めたいのはもちろんK = 11...1(1がN個)としたときのdp[K]  (実はK=(1<<N)-1)
dp[0] = 1

for bit in range(1,1<<N):#bitに対応する集合bit_Sで女性を選んでいるときを考える
  i = bin(bit).count('1')-1 #これが[S], 0-indexedに合わせておく
  for j in range(N):
    if (bit >> j) & 1: #もし選び方bit_Sの中にj人目の女性が含まれていたら
      dp[bit] += dp[bit - (1 << j)] * match[i][j]
      #dp[bit - (1 << j)]は bit_S - (j人目の女) が i-1 人目までの男の集合とマッチングするときの場合の数
      #もし男性iと女性jの相性が良いなら加える
      dp[bit] %= MOD
print(dp[(1<<N)-1]%MOD)