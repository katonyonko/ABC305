import io
import sys
import pdb

_INPUT = """\
6
4 5
2 2 3
3 1 3 4
3 1 2 4
5 4
2 2 4
2 1 3
1 2
2 1 3
2 2 4
2 1 5
5 5
2 2 4
3 1 3 4
1 2
3 1 3 4
3 1 2 5
"""

def solve(test):
  N,M=map(int,input().split())
  now=0
  used=[0]*N
  used[0]=1
  path=[0]
  while now!=N-1:
    l=list(map(lambda x:int(x)-1,input().split()))
    k=l[0]+1
    l=l[1:]
    flg=0
    for i in range(k):
      if used[l[i]]==0:
        now=l[i]
        path.append(now)
        print(now+1)
        used[now]=1
        flg=1
        break
    if flg==0:
      x=path.pop()
      if x==now: x=path[-1]
      now=x
      print(now+1)

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