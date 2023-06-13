import io
import sys
import pdb
from heapq import heappop,heappush

_INPUT = """\
6
5 5 2
1 2
2 3
2 4
3 5
1 5
1 1
5 2
3 0 1
2 3
10 10 2
2 1
5 1
6 1
2 4
2 5
2 10
8 5
8 6
9 6
7 9
3 4
8 2
"""

#Dijkstra
def Dijkstra(G,C,h):
  done=[False]*len(G)
  inf=10**20
  while h:
    x,y=heappop(h)
    if done[y]:
      continue
    done[y]=True
    for v in G[y]:
      if C[v[1]]>C[y]+v[0]:
        C[v[1]]=C[y]+v[0]
        heappush(h,(C[v[1]],v[1]))

def solve(test):
  N,M,K=map(int,input().split())
  G=[[] for _ in range(N)]
  for _ in range(M):
    a,b=map(lambda x:int(x)-1,input().split())
    G[a].append((1,b))
    G[b].append((1,a))
  inf=10**20
  C=[inf]*N
  heap=[]
  for _ in range(K):
    p,h=map(int,input().split())
    p-=1
    C[p]=-h
    heappush(heap,(-h,p))
  Dijkstra(G,C,heap)
  print(len([i for i in range(N) if C[i]<=0]))
  print(*[i+1 for i in range(N) if C[i]<=0])

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)