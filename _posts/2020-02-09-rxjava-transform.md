---
title: "RxJava - Transfrom Operator편"
date: 2020-02-09 13:54:00 -0400
categories: android rxjava
---
# Transform Operator
변경 오퍼레이터는 RxJava의 오퍼레이터들 중에서 활용도가 가장 높다고 생각한다. 본 오퍼레이터들은 중첩된 비동기를 하나의 스트림으로 쉽게 구현할 수 있게 해주며, 다양한 방식으로 데이터를 조작할 수 있게한다.  

다양한 데이터 스트림(reactive source)가 존재하지만 여기서는 가장 근본이 되는 Observable로 치환하여 말하겠다.

# Map
---
✅Flowable, ✅Observable, ✅Maybe, ✅Single, ❌Completable

각 item에 함수를 적용하여 방출한다.

```
Observable.range(0,5)
    .map{x -> x*x}
    .subscribe{println(it)}

// 0
// 1
// 4
// 9
// 16 
```
<br>

# ConcatMap
---
✅Flowable, ✅Observable, ✅Maybe, ❌Single, ❌Completable

ConcatMap은 외부 Observable의 데이터를 순차적으로 처리할 수 있도록 보장한다. 내부 Observable이 먼저 결과를 방출할 수 있어도 방출하지 않고 기다린다.

```
Observable.range(0, 5)
    .concatMap { i  ->
        val delay = Math.round(Math.random() * 2)
        Observable.timer(delay, TimeUnit.SECONDS)
            .map { i }
    }
    .blockingSubscribe { println(it) }

// 0
// 1
// 2
// 3
// 4
```
<br>

# FlatMap
---
✅Flowable, ✅Observable, ✅Maybe, ✅Single, ❌Completable

FlatMap은 ConcatMap과 다르게 외부 Observable의 방출 순서와 상관없이 먼저 처리된 내부 Observable 방출한다.(인터리빙)
```
Observable.range(0, 5)
        .flatMap { i ->
            val delay = Math.round(Math.random() * 2)
            Observable.timer(delay, TimeUnit.SECONDS)
                .map { i }
        }
        .blockingSubscribe { println(it) }
    
// 0
// 2
// 4
// 1
// 3
```
<br>

# SwitchMap
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

SwitchMap은 ConcatMap과 FlatMap과는 다른 동작을 보인다. 내부 Observable의 방출이 끝나지 않았는데 외부 Observable이 방출을 해야한다면, 해당 내부 Observable의 동작을 중지한다.

```
Observable.range(0, 5)
    .switchMap {i ->
        Observable.timer(1, TimeUnit.SECONDS)
            .map { i }
    }
    .blockingSubscribe { println(it) }

// 4
```
<br>

# GroupBy
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

GroupBy는 사용자가 정한 key를 기준으로 Observable을 나눠 방출한다.
```
  Observable.range(0,10)
        .groupBy ({it%2})
        .concatMapSingle{it.toList()}
        .subscribe{println(it)}

// [0, 2, 4, 6, 8]
// [1, 3, 5, 7, 9]
```
<br>

# Scan
---
Scan은 이전에 방출된 값을 연속적으로 받아 function을 적용하여 방출한다.
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

```
Observable.just("b","c","d")
    .scan("a", {x,y -> x+y})
    .subscribe{println(it)}

// a
// ab
// abc
// abcd
```
<br>

# Buffer
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

방출에 대한 임계를 정하고, 넘으면 List<T>형태로 방출한다. 
```
val bufferObservable = Observable.range(0, 10)
    .buffer(2)
    .subscribe{ println(it) }

// [0, 1]
// [2, 3]
// [4, 5]
// [6, 7]
// [8, 9]
```
<br>

# Window
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

방출에 대한 임계값을 정하는 것은 Buffer와 똑같으나 각각의 window를 Observable로 방출한다.

```
Observable.range(0, 10)
    .window(2)
    .flatMapSingle { it.toList() }
    .subscribe { println(it) }
    
// [0, 1]
// [2, 3]
// [4, 5]
// [6, 7]
// [8, 9]
```
<br>
