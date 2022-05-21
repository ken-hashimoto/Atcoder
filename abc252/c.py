#--------------------------------------------------------------
# input here
import sys
import io

_INPUT = """\
"""
sys.stdin = io.StringIO(_INPUT)
#--------------------------------------------------------------
# your code here
import sys
sys.setrecursionlimit(10**7)

def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]
def LL(n): return [list(input()) for i in range(n)]

N,M = MI()
graph = [[]]
#木構造において経路はただ一通りであることから1から一番遠いノードを求めてそこまでの最短経路を求める
