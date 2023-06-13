import io
import sys
import pdb

_INPUT = """\
6
5 6
......
..#.#.
..###.
..###.
......
3 2
#.
##
##
6 6
..####
..##.#
..####
..####
..####
......
"""

def solve(test):
  H,W=map(int,input().split())
  S=[input() for _ in range(H)]
  a,b,c,d=10**20,0,10**20,0
  for i in range(H):
    for j in range(W):
      if S[i][j]=='#':
        a=min(a,i)
        b=max(b,i)
        c=min(c,j)
        d=max(d,j)
  for i in range(H):
    for j in range(W):
      if a<=i<=b and c<=j<=d and S[i][j]=='.':
        p,q= i+1,j+1
  print(p,q)

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