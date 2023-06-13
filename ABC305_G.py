import io
import sys
import pdb

_INPUT = """\
6
4 3
aab
bbab
abab
20 1
aa
1000000007 28
bbabba
bbbbaa
aabbab
bbbaba
baaabb
babaab
bbaaba
aabaaa
aaaaaa
aabbaa
bbaaaa
bbaabb
bbabab
aababa
baaaba
ababab
abbaba
aabaab
ababaa
abbbba
baabaa
aabbbb
abbbab
baaaab
baabbb
ababbb
baabba
abaaaa
"""

class MatMul:
  def __init__(self, N, mod):
    self.N = N
    self.mod = mod
  def idx(self,i,j): return i*self.N+j
  def mult(self,A,B):
    res=[]
    for i in range(self.N):
      for j in range(self.N):
        res.append(sum([A[self.idx(i,k)]*B[self.idx(k,j)]%self.mod for k in range(self.N)])%self.mod)
    return res
  def pow_mat(self,A,n):
    tmp=[A]
    m=n
    while m>1:
      tmp.append(self.mult(tmp[-1],tmp[-1]))
      m//=2
    res=[0]*self.N**2
    for i in range(self.N):
      res[self.idx(i,i)]=1
    for i in range(len(tmp)):
      if (n>>i)&1==1:
        res=self.mult(res,tmp[i])
    return res
  
def solve(test):
  mod=998244353
  N,M=map(int,input().split())
  S=[input() for _ in range(M)]
  if N<=6:
    ans=0
    for i in range(1<<N):
      x=''.join(['a' if (i>>j)&1==0 else 'b' for j in range(N)])
      flg=0
      for j in range(M):
        if S[j] in x: flg=1
      if flg==0: ans+=1
  else:
    def idx(i,j): return i*(1<<6)+j
    mat=[0]*((1<<6)**2)
    init=[0]*(1<<6)
    for i in range(1<<6):
      mat[idx(i,(i<<1)&((1<<6)-1))]=1
      mat[idx(i,((i<<1)&((1<<6)-1))+1)]=1
    for i in range(1<<6):
      x=''.join(['a' if (i>>j)&1==0 else 'b' for j in range(6)])
      flg=0
      for j in range(M):
        if S[j] in x: flg=1
      if flg==1:
        for j in range(1<<6):
          mat[idx(i,j)]=0
      else:
        init[i]=1
    matmul=MatMul(1<<6,mod)
    res=matmul.pow_mat(mat,N-6)
    ans=sum([sum([init[j]*res[idx(i,j)] for j in range(1<<6)])%mod for i in range(1<<6)])%mod
  print(ans)

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