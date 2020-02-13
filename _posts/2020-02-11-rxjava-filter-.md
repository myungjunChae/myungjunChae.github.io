---
title: "RxJava - Filter Operator편"
date: 2020-02-11 16:04:00 -0400
categories: android rxjava
---
# Filter Operator
필터 오퍼레이터는 upstream의 데이터들 중, 특정 값들을 수신하지 않기 위해서 존재하는 오퍼레이터이다. 본 오퍼레이터들을 사용하면 사용자가 이벤트를 여러 번 발생시켰을 때, 특정 기준에 의해 이벤트를 최소의 이벤트만 송신하는 등의 기능을 구현할 수 있다.

다양한 데이터 스트림(reactive source)가 존재하지만 여기서는 가장 근본이 되는 Observable로 치환하여 말하겠다.

## point
- Debounce와 Throttle의 차이를 이해한다
- Throttle과 Sample의 차이를 이해한다 (아직 이해못함)

# Debounce
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

기본적으로 지연 방출이다. item의 방출 시간을 지정하고 방출 시간이 끝나기 전에 새로운 item이 방출되었을 경우, 이전 item의 방출을 중지한다.

```
val stream : Observable<String> = Observable.create{
        it.onNext("A") // A, 1초 지연방출
        Thread.sleep(1500) // 1.5초 sleep

        it.onNext("B") // B, 1초 지연방출
        Thread.sleep(500) // 0.5초 sleep

        it.onNext("C") // C, 1초 지연방출 (B드랍)
        Thread.sleep(250) // 0.25초 sleep

        it.onNext("D") // D, 1초 지연방출 (C드랍)
        Thread.sleep(2000) // 2초 sleep

        it.onNext("E") // E, 1초 지연방출 
        it.onComplete()
}

stream.subscribeOn(Schedulers.io())
        .debounce(1, TimeUnit.SECONDS)
        .blockingSubscribe{
                println(it)
        }

// A
// D
// E
```
<br>

# Distinct
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

이전에 방출된 item과 같은 값을 가진 item은 생략한다.


```
Observable.just(1)
.repeat(3)
.distinct()
.subscribe { println(it) }

// 1 
```
<br>

# ElementAt
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

지정한 index의 item만 방출한다.

```
Observable.range(1,5) // 1 - 2 - 3 - 4 - 5 방출 
.elementAt(2)
.subscribe { println(it) }

// 3
```
<br>

# Filter
---
✅Flowable, ✅Observable, ✅Maybe, ✅Single, ❌Completable

조건을 만족하는 item만 방출한다.

```
Observable.range(0,5) // 0 - 1 - 2 - 3 - 4 방출 
.filter { it%2 == 0 }
.subscribe { println(it) }

// 0
// 2 
// 4
```
<br>


# First(Element), Last(Element)
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

본 오퍼레이터들은 설명하기 무색한 기능을 제공한다. first는 맨앞의 item을 last는 맨뒤의 item만 방출한다. 여기서 각각의 element 오퍼레이터와 다른 점은 first와 last는 single을 반환하는 반면, element 오퍼레이터는 maybe를 반환한다는 점이다.

```
생략
```
<br>

# IgnoreElement
---
❌Flowable, ❌Observable, ✅Maybe, ✅Single, ❌Completable
Upstream의 Maybe와 Single을 Completable로 변환하여 방출한다.

```
Single.timer(1,TimeUnit.SECONDS)
        .ignoreElement()
        .doOnComplete{println("Done")}
        .blockingAwait()

// 1초 후
// Done
```
<br>

# IgnoreElements
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable
Upstream의 Flowable과 Observable을 Completable로 변환하여 방출한다.
```
Observable.intervalRange(1,5,1,1,TimeUnit.SECONDS)
        .ignoreElements()
        .doOnComplete{println("Done")}
        .blockingAwait()

//5초 후
//Done
```
<br>

# Sample
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

일정 주기동안 발생한 마지막 item만 방출한다.

```
 val stream : Observable<String> = Observable.create{
        it.onNext("A")

        Thread.sleep(500) // 누적 0.5초
        it.onNext("B")

        Thread.sleep(200) // 누적 0.7초
        it.onNext("C")

        //------Sampling 1초, C 방출-------

        Thread.sleep(800) // 누적 1.5초
        it.onNext("D")

        //------Sampling 2초, D 방출-------

        Thread.sleep(600) // 누적 2.1초
        it.onNext("E")
        it.onComplete()
    }

    stream.subscribeOn(Schedulers.io())
        .sample(1, TimeUnit.SECONDS)
        .blockingSubscribe{
            println(it)
        }

// C
// D
```
<br>

# Skip & SkipLast
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

지정한 갯수만큼 item을 drop하고 방출한다. (Last은 뒤에서부터 Skip)

```
// 생략
```
<br>

# Take & TakeLast
---
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

지정한 갯수만큼의 item만 방출한다. (Last은 뒤에서부터 Take)

```
// 생략
```
<br>

# throttleFirst & throttleLast
✅Flowable, ✅Observable, ❌Maybe, ❌Single, ❌Completable

> throttleLast와 sample의 차이는? 

일정 주기 중의 첫 item (first), 마지막 item (last)만 방출한다.

```
val stream : Observable<String> = Observable.create{
        it.onNext("A")

        Thread.sleep(500) // 누적 0.5초
        it.onNext("B")

        Thread.sleep(200) // 누적 0.7초
        it.onNext("C")

        //------Sampling 1초, A 방출-------

        Thread.sleep(800) // 누적 1.5초
        it.onNext("D")

        //------Sampling 2초, D 방출-------

        Thread.sleep(600) // 누적 2.1초
        it.onNext("E")
        it.onComplete()
    }

stream.subscribeOn(Schedulers.io())
        .throttleFirst(1, TimeUnit.SECONDS)
        .blockingSubscribe{
                println(it)
        }

//A
//D
```
<br>



# timeout
✅Flowable, ✅Observable, ✅Maybe, ✅Single, ✅Completable

일정 주기동안 item이 발행되지 않으면 timeout error를 발생시킨다.

```
val stream : Observable<String> = Observable.create{
        it.onNext("A")

        Thread.sleep(800)
        it.onNext("B")

        Thread.sleep(400)
        it.onNext("C")

        Thread.sleep(1200)
        //timeout

        it.onNext("D")
        it.onComplete()
}

stream.subscribeOn(Schedulers.io())
        .timeout(1, TimeUnit.SECONDS)
        .blockingSubscribe(
                {println(it)},
                {err->println(err)}
        )

//A
//B
//C
//io.reactivex.exceptions.UndeliverableException
```
