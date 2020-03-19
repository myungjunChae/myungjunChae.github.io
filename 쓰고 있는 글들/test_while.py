def solution(A):
    result=1
    A=sorted(A)
    while A:
      a = A.pop(0)
      if a==result:
        result+=1
    return result
