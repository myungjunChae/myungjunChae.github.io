import dis
import time
import matplotlib.pyplot as plt

def for_testing(A):
    result=1
    A=sorted(A)
    for a in A:
      if a==result:
        result+=1
    return result

def while_testing(A):
    result=1
    A=sorted(A)
    while A:
      a = A.pop(0)
      if a==result:
        result+=1
    return result

def while_mutation_testing(A):
    result=1
    count = 0
    A=sorted(A)
    while True:
      if len(A) == count+1:
        break
      a=A[count]
      count+=1
      if a==result:
        result+=1
    return result

def pop_first(A):
  return A.pop(0)

def pop_last(A):
  return A.pop()


def timer(func, value):
  start = int(round(time.time() * 1000))
  func(value)
  end = int(round(time.time() * 1000))
  return end - start

if __name__ == "__main__":
  #print(dis.dis(for_testing))
  #print(dis.dis(while_mutation_testing))

  x=1
  count=0
  while x < 10000000:
    t1=timer(for_testing,[1]*x)
    t2=timer(while_testing,[1]*x)
    x*=2

    # evenly sampled time at 200ms intervals

    # red dashes, blue squares and green triangles
    plt.plot(count,t1, 'ro', count,t2, 'bs')
    count+=1
  
  plt.show()

  #print(dis.dis(pop_first))
  #print(dis.dis(pop_last))
  #timer(pop_first, [1]*1000000000)
  #timer(pop_last, [1]*1000000000)
