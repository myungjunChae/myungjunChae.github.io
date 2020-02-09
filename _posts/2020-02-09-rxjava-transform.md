---
title: "RxJava Transfrom Operator편"
date: 2020-02-09 13:54:00 -0400
categories: android rxjava
---
# Transform Operator
변경 오퍼레이터는 RxJava의 오퍼레이터들 중에서 활용도가 가장 높다고 생각한다. 본 오퍼레이터들은 중첩된 비동기를 하나의 스트림으로 쉽게 구현할 수 있게 해주며, 다양한 방식으로 데이터를 조작할 수 있게한다.  

### Buffer
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

Observable의 item들을 일정 주기를 기점으로 bundle에 담아 한번에 배출합니다.
> periodically gather items from an Observable into bundles and emit these bundles rather than emitting the items one at a time

```
val bufferObservable = Observable.range(0, 10)
    .buffer(2)
    .subscribe(
        { println("Next : ${it}") },
        { println("error") },
        { println("finish") }
    )

// Next : [2, 3]
// Next : [4, 5]
// Next : [6, 7]
// Next : [8, 9]
// finish

```
### FlatMap
> transform the items emitted by an Observable into Observables, then flatten the emissions from those into a single Observable

### GroupBy
> divide an Observable into a set of Observables that each emit a different group of items from the original Observable, organized by key

### Map
> transform the items emitted by an Observable by applying a function to each item

### Scan
> apply a function to each item emitted by an Observable, sequentially, and emit each successive value

### Winodw 
> periodically subdivide items from an Observable into Observable windows and emit these windows rather than emitting the items one at a time

| FlatMap | Observable에서 배출된 item 하나하나를 Observable로 감싸고, 각 item을 다시 한번 배출합니다.|
| GroupBy | 기존의 Observable을 key에 의해 재조직된 Obeservable들로 묶어 배출한다. |
| Map | 각 item에 사용자가 정의한 function을 적용하여 배출한다. |
| Scan | 이전에 방출된 값과 다음의 item을 같이 function에 전달한다. |
| Window | 일정 주기를 기점으로 Observable의 item들을 나누어 Observable window에 담고, 해당 window를 한 번에 배출합니다. |
