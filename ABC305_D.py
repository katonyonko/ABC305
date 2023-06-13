import io
import sys
import pdb
from bisect import bisect_left, bisect_right

_INPUT = """\
6
7
0 240 720 1320 1440 1800 2160
3
480 1920
720 1200
0 2160
21
0 20 62 192 284 310 323 324 352 374 409 452 486 512 523 594 677 814 838 946 1000
10
77 721
255 541
478 970
369 466
343 541
42 165
16 618
222 592
730 983
338 747
"""

def solve(test):
  N=int(input())
  A=list(map(int,input().split()))
  B=[0]
  for i in range(N-1):
    if i%2==0:
      B.append(B[-1])
    else:
      B.append(B[-1]+A[i+1]-A[i])
  def sleeping_time(x):
    y=bisect_right(A,x)-1
    res=B[y]
    if y%2==1: res+=x-A[y]
    return res
  Q=int(input())
  for _ in range(Q):
    l,r=map(int,input().split())
    print(sleeping_time(r)-sleeping_time(l))

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