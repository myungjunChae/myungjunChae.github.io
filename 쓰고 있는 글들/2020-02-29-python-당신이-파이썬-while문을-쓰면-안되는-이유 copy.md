---
title: "Python - 내가 파이썬 while문을 쓰지 않게된 이유"
date: 2020-02-29 00:00:00 -0400
categories: python coding_test
---
오늘 다룰 소재는 프로젝트에 집중하느라 글쓰기를 잠정적으로 중단하고 있는 나에게 다시금 글을 쓰게한 엄청난 녀석이다. 제목이 다소 파격적이다. 실제로 while문 + α때문에 엄청난 시간적 소모를 겪었기에 이렇게 지을 수 밖에 없었다. 무슨 일을 겪었고 <b>앞으로 while문을 쓸 일은 없겠네.</b>라 생각한 필자의 경험을 구구절절이 설명하려한다.

# 문제의 시발점
---
최근에 카카오 경력직 코딩 테스트를 치뤘다. 문제는 hackerrank에서 총 3개의 문제가 출제됐으며, 난이도가 썩 높진 않아 푸는데에 1시간30분정도 걸렸던 것 같다. 그런데 최종적으로 내가 맞춘 문제는 두 문제가 전부였다. 이유는 마지막 문제의 시간복잡도를 남은 2시간 30분동안 해결해지 못한 것이 원인인데, 이 때까지만 해도 그냥 내 잘못인줄만 알았다. ~~아니 사실 내 잘못이지. 누굴 탓해.~~

이후에 카카오 최종면접에서 광탈한 후, 다시 코딩 테스트를 준비해야했기때문에 친구의 추천으로 codility에서 [문제]((https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/))를 풀고 있었다. 그리고 나는 다시 한 번 time complexity의 늪으로 빠져들었다.

<img width="300" alt="while_complexity" src="https://user-images.githubusercontent.com/10257454/75624307-89c9af00-5bf6-11ea-991f-63287c0185e2.png">
<br>
<br>
<img width="250" alt="while_complexity" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUQEhIVFRUVFRUVFRUXFRUVFRUVFRUWFhUVFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFQ8PFS0dFR0rLS0rKystKysrKy0rKy0tLSsrLS0tLSsrLTctKys3LSsrKys3LTcrLTctLSsrKy0rK//AABEIAK4BIgMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAADAQIEBQYABwj/xABBEAACAQIDBQYEAwUHAwUAAAABAgADEQQhMQUSQVFhBhMicYGRQqGx0TLB8BRSYoLhIzNykqKy8QdT0hUkQ2PC/8QAFwEBAQEBAAAAAAAAAAAAAAAAAAECA//EABwRAQEBAQACAwAAAAAAAAAAAAABEQIxURIhQf/aAAwDAQACEQMRAD8AslWFVZwEIBMsm7s4LCBY8JAGFjwseEhAkKYoj1SESnec7AfrhA5EhxTFtPXORFqyVQq3BXnp/iGn29YURUUwowl9DfpIRfOWGFc+2sIalPhaSadOSlphh15xFp2ymomHUUkpEjKSyUqwBhI8LCATt2XA0LF3Y8CP3YAt2NKQ9ohWQA3Im5D2nWgRikY1OS92MZYEFkgyklssGRKIxSJuQzRokAikEyySwg2SBEYQZkhkjDTgRyIloYpE3IArToTdnSYM4qwirHqkMtOQMVY8JCqkKtOAFacIqQwpwgpwAt4VJ85XVmkzGuRcHS2R5ef3kKoJGjFh1aBWFYadRf8AI/SUPvJlCtlbhr5yFSzIHMgfOEWpmTzJPzhWi2c98uPCTzSv5yhwNXMWmlptvKDEQynSh1SKBH2mmTd2JaEjGlCCOjLxymQOtOtOvELQOnRu9Gl5cDjGOYhaMqQAPUgWcxxE7uzIBR9JYRaMPTpwAGnGNTkwrGMsCEacGUkxlgmSBDZINlktlgnSAC06PtOgUqU4ZUhlpQq05AFacKtOFSnJCYeMEZKckU6F5KpYaTKVK0DCdosO+Gq/tFyaL5sijec1AirYDS26ga98rNznYeoo3KikGm1mU8LHO3kRp7cpfdsmRUps63UM5Iva47pxw85itkN3eDcn+6LMKIa19xvxAjQgNvD30krUX20admuNCLi2kjb+Ur9hVXNBHqcR/Z31KfCx9Pe1+MDsrFAlt38JdreV8jCrdGIzE5DFWnEUQLHBPmPf2zmqwLeD3mOoazU7OqgDdPH7WhFosfB09I4tNIUmDYzi0YYiFJnTrTrSjohMW04iAwRYqrF3ZQwxGivAVathIhwEeJXjFR4rQbE6PUSEtUyRSqRi6PaNKx94xngDZYJ1hGeCYyATrAvDMDBMkAM6P7udADTwxhhhpYJSj+6gV6UZKppCMk5RAUCFEZIm0torRXPNjoPzPSFV/bHCpUohXbdAa5tqVswYDlrrMSuBDqAxb9nUWp0ybk6eLe13dTY3uTfIZGyx696zvVdyHt4N6wWwt4SLMPK9h6yrxiV6YcMCUChqVQgBnBGeQyJDE+LLXjrM61FJtjaj0m/ZqedPd1JLMlyb0wSdLc+DSZsQAKeV8pCxWBuLakE58SeJPnFrvUVPAM+Vrn0mVayhVy1hA888fv2ps5quHAuqAkH1tb2kjs5iMSBesWtfK5zjRvhiAo3mIAGZJyHvKvHdv6aW3FLcjmC2fCwPMZm0JtHZBxNEKrEWIY8bjPIjzjKOwrsjVRfuxuiwsLXB4dReVHoex8YatJXItvAN7iTbyHsrNB5D8x+UsFSajNNtOtCbs7dlQy0daOtOgNtOIjhFMAaiOtOBiM4lHFZGxdC65QrVxBPVJgZ7NWzkqlWBh6tEE5yLUwnESueYmK8k0zylMGZdZY4KteFlTReOCR4EWGzO7iFYSIZABlgXEktAuJAC0WLadAsLRY0tGloCOYMNEqPI5aAu0Md3a3AuToPqZh9vYA4gs5q1AS29uhvCToBbUKOQI0vL/bFa7Bf3R9f0JWOb5cNT5cv1+czWmM2VtFqeIQYw8yFe63ZbEK3Bx+LMG2Wpvnqe0vaAVqN7J4ORsSrWUqL9d0/yzNbR2VVbEDwNVpO63C7u6qAglWp8cxrmfKGxOzKFNu9U7hBUd2SCpzC+FW0bO/WQhjVrNcaSRRIMj7TwjI5RxZlJB8xrbpGUGPrI0tO6UyPiVAtlHUGygsYTcEC45CBpOzNfIA+Xvp9Jd10G9u8ze2Y1+Xr0mI2VtK11KMOWk2dC7hXOTC2fDpLBe7Hp7oYHOxA+v3ljIOz3B37EXuLgHMXFxce8miajLjOixpaVC2nGDaqBBtVJhBi0G1WDCkx3dygTOTGBDxklFjrSgKUeceUyjrTiYEGoM4y0fV1jYDDTj6FCKIejCYfpwi955RXkaovISKkh5xMiBzzEd3w5wDkwLmNar0galU9IDt6LI2+eYnRgnPWgzXkVmiqZAUvBV6u6pbl9YQCVu1Kme7y185KsV1Vr3JgKjWB5n9fryhHMh4qpMqANurhWFRl3wLkgGxsAc/e0rdnYxRSbGCzVH8d+LMTe1/eM2lSRwLAlyQpJNwLm+Q4ZeeZkTH7oNkVVsLEgAFrc7a6mKKw7WqGoyVSam9eqtXMhw2oBOnA26wtPF8RKTbdOstOmLeA94yEHS1RznpY7qgjpbykXZ21rlUYFnJAG6Nb3zI+3OBtsLjAwhhixe1mPkjfa0ocHUv4kNweIPEcJc4WozZfORU/D1GNgtB+d2KqPXO81mA3ygDOLhlO6oyyvYFjmdemsz2Dwlx4mY9Lm00QqUsPh6lc//HSdwCfiH4QOpP1gZ3Ze16qYx65I3KlZ90KBdqabtO7Nx8NMZcCZ6LhNr03FwfMcR5j/AJnjvZutRFJKau7VlqliCSzuhB33VB+EAFGJGXhaa+jLqRvhWB0MjuxJmPqbQZWUqTcDPPrLDC7de43tLj2vnLOyxo1pQgWDo4gHLQ20+0MD1m9Zx1p06deUNWOjFjoHRrHrFjXPX2gQHfOJvSJjKtmglxokZ1YhpIoGU37cvOSsJjL6QatXPWRqtupjyx6CCc/xQ0H6TiT0jSfMxQv8MgYx6wbW5GSO7PSNen1lEX0nQvddTOgPWgTJVLDgQtpXbc25Rwib9aoqXyF9SeijNj0AkE+sVQFnYKo1JIAnnGK7XU6mMqLSUvh1QXri9g4tvH/Bn53F9JaUNp0toU6jKzMqNuHeUqCbKbAHUWYTJDsmqhkdjUp+I00BIVGIyO6xI5535ZTNqtXUcCVG0sWACb9BK3CJiqIWh3L1aYAAcNTBUWBtZnuQMx6C2UHtGkxNuV7ff1yk1QsJWLuwJ1sR6ZH6iHrYRrEgi/X+krqd0YOOBz8jrL2lUVxceo5feBku0+y2rMqJWLotxTDLuML21yAbQa+8yFbCVcO+5UVkYZjgRyII+oM9RxGGvIG0sB3tPumzUfhvqh/hPDy06QmMds6rW3yyGxOZLGwbT8QOvnNtTqPRp97XNJV3Q28lUMp8r2N+mcylbYNSnclRU5FDun1U/QEyDSwp3ssO+Wl0sPc5Qmt5S7Z0RkgeoRwSmx9yQAPeLWxtbHIocGjhi193JqtZkOgH4Qqm2eYvblK3Z3fVENJ7U0OoS2+38JbgOds+omw2FhVKsjKPDTJQ2AKlBcAH90i4t1EjXkPBYcJ/dr3Q47pO+w/iqanU5aZ5Wl/h6oVQCFso5DQcBK0eHOGpAtmdOULCld5r/ofr85IpUc1H8Q+tzFGQkrCLbxH0kAu0eOK9wlNXaqS7Dc3clyHiLZBbgcDppKbbXafHYJVephMO6EgbyYhsiRezjcO6fK4y4aTJ/wDU7alT9oFOnVZAKYuFYrvFicjbW1v9UzeDw6BSaqsrm24VsFtY3LXF+WnWVi16rsr/AKoqQDiMJVprp3iHvkHnkrcOAM3GyNsUMUneYeqtVdDunNTydTmp6EAz52x1buTub1/D4baFTndfrH7NxvdMlfD13p4i2bKAARc+E8HXjYgjPmJqVidPpJYt5muxvaUYukC+6tUDxgaEjUry106iaEv5zcutiQdR8tZ3p7xjjqPaUZ7aNXxSrqsZbY+lnK98OTwhhCDS72SZWjBGW+zKNoSLe3SO3D0igecIF6SNgCn1hAg6x+70jmNhckAczkIUPcHKI4sLmwHM5CVeP7QImSDfOl/hHD1lBjsa9U3dr9OA8hMXufjU5aM7Uof9z/SZ0yV50x8618I3G0sYtGlUrN+GmjOeoUE2HXKfPm0tp1MTUbEV23nbID4VvmEQcFH/ADPZv+oNRhgqgXMuaaf5qi3+U8i2dg6lVmSlhxVtkzbpIQ3vZXJCrfnyvNdemI2fYym1PBEgA79VmIvY5ALlwJ8GmXnC1MYAblXH8jN81BEkbFwzUcHTpuN1x3hYXBsWdmIuMvjkWtw8z+X2kaWWCxdwSqscuKlAOvjA58LyFXwm9mNbZ9ZJWsKdCpUOiLvHyCsx+kk9z4FqA3Vvy09xY+sIzuIwY0tB0sNu5j9feaFsOH01HzH5yNUobuUCtGes56UPXo8Rkf1qIym3A/r1lEDEYe8hvhONjbnL5qQJHAZXNr29oEUxp762kEbA4S0vMMm6PPKBw1GSh+jChFbn9ZSWmnlGU04QwW2sAtNL5nTgPvDmpaA7yAr1ciOh+QJgeQ9otod5jazN4gHAte34FAYA8MwZoNlbPO06aKGFLumtUqWyta4RObEbuuQ1OoviahL4uoFF2fE1Ao5lqpt6Zz1vY1NaFJaNP8KC3mTmzHqTcy1zWeyuy2CpboGHSoy6NVAqtfiRvZDP90CWr7Mwpa1fDUWpsRmaahqNQ5XVgAVVstCLN/iNodFjYMDfgenQy0pVCwscxbQ5ix1GfCI1iqrdk/2KsMXgmYoP7ygxJIX95GOZA4hrmxNjwm2pLcXubEX5ZGV2zatv7Js8rqTmSmhBPEi4HkR1lrhEsqryAHsLTUMd3fScU8oUxJrUVeIwtzAHDDlLWoJHdY1MV5oCSsNSikQ1LLM5AcTkIMG3esRiALk2HM5CVeO7QImVMbx5/D/WZ3G7QeobuxPTgPSZveeG5yv8dt6muVMb55/D/WUGNx71D42v00A9JEZ5U4rbtNN42ZglyxUCwtrmTrOV6tbkkWtQ3uPSCV7jPXj5jIyrwfaCnVKFQwWp+AsALngDYmxk4tZrc8/UWB/KRRrzoLeiyDYdrtnmtQFMaGpT3uihvEfaQjRWmgRFCqosANAJqMZTup9D7TP7QTPKdq5xVY8+Aev1H/jKar8Pl+Z+0uNpNw6D53J+sqKqaW5f/ozLQm1WAwVUnTccHy3APzknsZj0rYYUGYBxYC/NVC5HzWQO0eWAqdVPzZVmT2RX3L2OW+3+4yst4CQbaEZHpaPxNa673Wx89QfXP2lTh8fvZk3J484WpVhdOaNCRqteOLSDgttPaOpKQLf8/WEwlLvG3QQMic9Mhfh5QtbDlADcENexBuDbUecDqKZW+X3hjaRQ9oM4rPylNWC1d0Xyz4frhGNXJzkLvr8YjVYRLetaVWPxmRA4gj0I0iYrESoxdaQYzYVP/wB9Uc/A1Zx57+6P99/SehbLqHWef4MhMTUJJ8ZIHLPdb3ym/wBjjwekrMaPCPqOBH0zlvshgWAbTP5D+kz+GaWOGrbpBHMRrTQ4ivS3d9Qd5DvjrYEMuvFSw8yJZ0KoIDKbqZnywAD3Fjpnp0t0knY6sigEqQLgWN/ACdz1C7sso0Ai2kaliLZR/f8ASXUw2qYFjFrk6gX6CwJ6C+UqTtJKl03XRxqj2Dedr5jLWNXBMZtJE08R/wBI+8xuD7S1MW9ZKg3WpPu7gOVsxf3B+UtMadRMZiSKG0FqaLiFCnlvaf7hT/zmc7bWsxpi0GxiExpMy0ibYxBSjUcahGt52NvnaZrtBXp0MMaYN2dNxFGbNvCxY8eN78TNVVTeBU5gixHQyjwfZ+nSYuqq7fCzk3XgLCx98pcRBw+BZMLSpHJ/7MDo5YG3pf5Gaatz5G/3+V4CjhLN3jneYZDKyqD+6OfWSSZMUt50hkMMhUAHAchEgeu4pvCZnsUbm366yVidpCrTBpXa5zNiMh5iVdSqbMTkQD88vznWsYqNp1bm/O59z/SVlR8x0A+klY03Mg/FaZqpm3RfBsP/AKyfZyfynneExFj6k+5Jnom0Ke9hqi8TTcD/ACmeXUMjLGa1mGrWk9MTpKHBVMpLFSUXVOtDipKWnXkpMRJRYrVsQQbEG4M44si44Gx9tD9ZBFeBqVpBZGreMCjnlwHt9pCWvH9/NCdvwVbESC2JkWriYB8TWlXiq8WrWkOqbyCrr4J6j3pqS2WQ16ED5ZTabLcrTAYFSNQciDyMptindroev5z1Tt7sgvTXGU1zCjvQNSLZP6XsfTlGIzlCtpJq1SDY6yiwOOUoUbJgd5G5j4kP1HkecsqNXfAHxDIdRy8xw9uUipWNr6C+g+v/AAIPBbYekbg3HEHSQ8fWzP60yEqqmImG3o+y9v06pC7wVz8JOvlzlwtWeXhgmHL2G84WxOt2PhseBUXPoZM2R2wamQlXxr+98Q+/61m517THo/eQWIpq9t5QbG4JAJBGhB4GQMHtBKq7yMGHSSe8mkUW1UsxmM7ZYYtR31/FSYMDyDZE+hIb+WbrbC8ecz2Moh1Kt+FgVPkwtOd8tQHZ+JFWklUfGoNuR4j0Nx6Qxmc7F4k7tXDP+OjUb2YnT+YN7iaTyz8o/VCKxrmPcW1NvLM+8C9UDMWHUxoczcsup+0A7jz+ntIuIxyjjf6SBU2gWO6tzfgBILU1p0rBha//AGmiwPVO/g6pDCxF/OYraXbunSy7p2P8oH1lavbevWLCmqU7C9yC51sMridNRssXspWzU7p9xKjFYFkzIBHMH9GY1+0+KfWqR0WwECMW7HxMx8yTM6N6ma26GeWGnZiOWXtPRtlue5Uk3JF/rMdtTChKh8/rnKxUfDvYyb3kggQyNwlRJWrCrXlezRC8qrM4mCq4iV4qmMq1YFlTxU5sVKmnVhXeBMOJ6wb1pB3zHhoEg1IOo0aXj8NS3jcyIs9g4a7qx5j6z37DjwKP4FHyE8g7ObLNQbykDdI1vPXcPWDAAX0livOe3PYw074rCr4dalMarzZBy6cJldjYy7W6E+Vhee7Wnmnbfs0mGY4qjZRUBDJoA1wxZehtpJ1FjK4/FZypqV4mJc3Mg1GM5tJ9baTlVQuSqfhXIAZAXy1NgBc8PWRFxJ1J5/lItV/ORKmLsL2y3ra8xNDQ4DbFSi2/TYg8RwPmOM9G2D2pp1gqOQlQ5AXyYjXdP5TxUbQyuF05mDbadRiyXsoF7D0GuvGX7R9AbTzW/rM9VzuLzHYLt/3RWjUV3U+Em4LDO2RJzGfGautTY5rax0uSDnzsJmrmIVLZ9JKr1wCXcANmQtsvh9AZIq41QMyB0Ez22to1KZ3ch5X+sztfGVG1Yx5VrMZt1RkNfcyGTXqZ2FNT8VVgnsp8R9pl1rsv4WI6jI++sb3xvmSYwbXDYHDDOtXaqf3U8K++p+UucJtOjTyo0lX0z9znPOaOIIlhh8YYR6B/64ecSYwYsxY+1f/Z">
<br>
<b>N^2으로 푸셨네요 휴먼? 머리를 좀 더 써보시죠?</b> 라고 한다.

그런데 내가 제출한 코드는 다음과 같았다.

```
def solution(A):
    result=1
    A=sorted(A)
    while A:
      a = A.pop(0)
      if a==result:
        result+=1
    return result
```

???

눈을 비비고 읽어보았다. sorted는 o(nlogn), while은 o(n). 어렸을 적 배운 덧셈을 통해 더해보면 o(nlogn + n) 

~~알파고가 오답을 낸 순간을 목격했다~~

뭐 여튼 틀렸다고 하니까 새로운 답을 찾아나섰고 while문으로 계속 쉐도우복싱하다가 포기하고 인터넷에서 답안을 찾아보았다.

```
def solution(A):
    result=1
    A=sorted(A)
    for a in A:
      if a==result:
        result+=1
    return result
```

???

고작 다른 점은 while문에 for문으로 대체되었고, pop() 메소드가 새로 생긴 것뿐이였다. pop() 메소드는 python에서 O(1)로 동작한다고 알고 있었기에 사건은 점점 미궁으로 빠져들었다.
<br>
<br>

# 아니야 뭔가 다를거야 - 디스어셈블리
어딘가에 분명 문제가 존재했고 각각의 파이썬 코드의 bytecode를 디스어셈블리하였다. 어셈블리 변환에는 파이썬 내장 모듈 [dis](https://docs.python.org/3/library/dis.html)를 사용했다. 

### for문 
```
  6          18 SETUP_LOOP              39 (to 60)
             21 LOAD_FAST                0 (A)
             24 GET_ITER
        >>   25 FOR_ITER                31 (to 59)
             28 STORE_FAST               2 (a)
```

### while문

```
 14          18 SETUP_LOOP              50 (to 71)
        >>   21 LOAD_FAST                0 (A)
             24 POP_JUMP_IF_FALSE       70

 15          27 LOAD_FAST                0 (A)
             30 LOAD_ATTR                1 (pop)
             33 LOAD_CONST               2 (0)
             36 CALL_FUNCTION            1
             39 STORE_FAST               2 (a)
```

동일한 코드 부분은 생략한 어셈블리코드 모습이다. 간단히 첨언하자면 line 6는 for문의 동작으로 <b>iterator을 가져와서 next를 해가며 loop</b>을 하고, line14는 while의 동작으로 <b>정적인 iterator가 아닌 동적으로 매번 loop마다 조건을 체크</b>하는 것을 볼 수 있다.

그리고 line15는 A.pop(0)의 동작이다. 

### 별다른 특이점은 찾지 못했다.

# 아니야 뭔가 다를거야 - timer
별 다른 소득이 없었던 어셈블리코드를 제쳐두고 실제 어느 부분이 심각하게 동작에 영향을 미치는지 시간을 체크해봤다. 

### 함수 비교
지수적으로 배열의 길이를 증가시켜가며 for문으로 작성한 코드와 while문으로 작성한 코드의 시간소요를 체크해봤다. 배열 길이 리미트는 10,000,000으로 설정하였다. 결과는 충격적이다. 실제로 본 그래프 추출을 위한 러닝타임에 글을 전부 미리 다 써놓을 정도였다. 도대체 while문의 어디가 그렇게 잘못된 걸까. 

### 코드 블록 
내가 작성한 코드 내에서의 while문과 for문의 유일한 차이 A.pop(0)에 timer를 걸어보았다. 그리고 array size 1,000,000인 경우, 본 코드 블록에서 매 loop마다 80ms 정도의 시간을 소모하는 것을 확인했다. 

# 범인 검거
| Operation | Example | Complexity Class | Notes | 
| --- | --- | --- | ---| 
|Pop	      | l.pop()      | O(1)	     | same as l.pop(-1), popping at end
| Pop	| l.pop(i)  |  O(N)| O(N-i): l.pop(0):O(N) (see above)|

우리는 pop
실제 pop()는 o(1)로 동작하지만
실제 내부는 어떻게 동작하는지 확인하지 않았지만, 파라미터의 유무가 pop의 동작 시간에 차이를 발생시킨다.

# 결론
사실 while문을 탓할 건 아니였다. pop(0)에 대한 

만약 파이썬으로 알고리즘을 푸는 사람이라면 본인이 자주 사용하는 오퍼레이션에 대해서 시간복잡도를 숙지해놓을 필요가 있을 것 같다. 다음은 UC 어바인에서 정리한 
[파이썬 오퍼레이션 시간 복잡도](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)에 대한 글이다. 참고해보고 필자와 같은 실수를 하지 않았으면 좋겠다.