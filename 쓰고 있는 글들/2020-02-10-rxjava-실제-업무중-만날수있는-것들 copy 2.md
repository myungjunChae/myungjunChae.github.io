---
title: "RxJava - 실제 안드로이드 업무에 적용할 수 있는 것들"
date: 2020-02-12 00:00:00 -0400
categories: android rxjava
---
> 본 글은 https://github.com/kaushikgopal/RxJava-Android-Samples 의 내용 중 필요한 부분만 발췌하여 번역한 것이므로 오역이 있을 수 있습니다. 

본 글은 실제 RxJava의 요소들이 안드로이드 어플리케이션 내의 어떤 부분에서 적용될 수 있을지를 다룬 내용이다. 처음 Rx을 접하면 어떠한 방식으로 어플리케이션 내에서 응용이 가능한 지 가늠하기 어렵다.(현재 그런 상태이다..) 본 글을 정리하므로서 좀 더 Rx를 잘 활용할 수 있게 되기를 기대한다. 

# 백그라운드 작업과 동시성 (scheduler 사용하기)
---
보통 긴 I/O 작업은 백그라운드 스레드에서 작업한 후, 해당 결과를 메인스레드(UI 쓰레드)에 전달한다. 
 
The long operation is simulated by a blocking Thread.sleep call (since this is done in a background thread, our UI is never interrupted).

To really see this example shine. Hit the button multiple times and see how the button click (which is a UI operation) is never blocked because the long operation only runs in the background.

# Observable 구성하기 : 병렬 네트워크 Call 병합하기 (flatmap, zip 사용하기)

The below ascii diagram expresses the intention of our next example with panache. f1,f2,f3,f4,f5 are essentially network calls that when made, give back a result that's needed for a future calculation.

         (flatmap)
f1 ___________________ f3 _______
         (flatmap)               |    (zip)
f2 ___________________ f4 _______| ___________  final output
        \                        |
         \____________ f5 _______|

The code for this example has already been written by one Mr.skehlet in the interwebs. Head over to the gist for the code. It's written in pure Java (6) so it's pretty comprehensible if you've understood the previous examples. I'll flush it out here again when time permits or I've run out of other compelling examples.

# Pseudo caching : 캐시에서 데이터를 검색한 후, 네트워크에 요청하기 (concat, concatEager, merge or publish 사용하기)
---
disk cache observable, network call observable 

일반적으로 디스크 observable은 네트워크 observable보다 빠르다. 하지만 본 예제에서는 operator들의 동작을 보기 위해서 느린 디스크 observable을 사용한다.

본 예제는 다음의 4가지 테크닉에 대해서 다룬다.

concat
concatEager
merge
publish selector + merge + takeUntil

마지막 테크닉은 아마 당신이 최종적으로 사용하고자하는 것일 것이다. 하지만 기술이 어떻게 발전해왔는지를 이해하기 위해 위의 3가지 테크닉을 더 다룬다.

concat 

concat is great. It retrieves information from the first Observable (disk cache in our case) and then the subsequent network Observable. Since the disk cache is presumably faster, all appears well and the disk cache is loaded up fast, and once the network call finishes we swap out the "fresh" results.

The problem with concat is that the subsequent observable doesn't even start until the first Observable completes. That can be a problem. We want all observables to start simultaneously but produce the results in a way we expect. Thankfully RxJava introduced concatEager which does exactly that. It starts both observables but buffers the result from the latter one until the former Observable finishes. This is a completely viable option.

Sometimes though, you just want to start showing the results immediately. Assuming the first observable (for some strange reason) takes really long to run through all its items, even if the first few items from the second observable have come down the wire it will forcibly be queued. You don't necessarily want to "wait" on any Observable. In these situations, we could use the merge operator. It interleaves items as they are emitted. This works great and starts to spit out the results as soon as they're shown.

Similar to the concat operator, if your first Observable is always faster than the second Observable you won't run into any problems. However the problem with merge is: if for some strange reason an item is emitted by the cache or slower observable after the newer/fresher observable, it will overwrite the newer content. Click the "MERGE (SLOWER DISK)" button in the example to see this problem in action. @JakeWharton and @swankjesse contributions go to 0! In the real world this could be bad, as it would mean the fresh data would get overridden by stale disk data.

To solve this problem you can use merge in combination with the super nifty publish operator which takes in a "selector". I wrote about this usage in a blog post but I have Jedi JW to thank for reminding of this technique. We publish the network observable and provide it a selector which starts emitting from the disk cache, up until the point that the network observable starts emitting. Once the network observable starts emitting, it ignores all results from the disk observable. This is perfect and handles any problems we might have.

Previously, I was using the merge operator but overcoming the problem of results being overwritten by monitoring the "resultAge". See the old PseudoCacheMergeFragment example if you're curious to see this old implementation.

# Rx를 사용한 페이징 (Subjects 사용하기)

I leverage the simple use of a Subject here. Honestly, if you don't have your items coming down via an Observable already (like through Retrofit or a network request), there's no good reason to use Rx and complicate things.

This example basically sends the page number to a Subject, and the subject handles adding the items. Notice the use of concatMap and the return of an Observable<List> from _itemsFromNetworkCall.

For kicks, I've also included a PaginationAutoFragment example, this "auto-paginates" without us requiring to hit a button. It should be simple to follow if you got how the previous example works.

Here are some other fancy implementations (while i enjoyed reading them, i didn't land up using them for my real world app cause personally i don't think it's necessary):

Matthias example of an Rx based pager
Eugene's very comprehensive Pagination sample
Recursive Paging example

# RxBus : RxJava를 이용한 EventBus (RxRelay - 절대 멈추지 않는 Subjects, debouncedBuffer 사용하기)

Implementing an event bus with RxJava
DebouncedBuffer used for the fancier variant of the demo

share/publish/refcount








# 이벤트 누적하기 (buffer 사용하기)
---
본 예제는 Buffer를 사용하여 이벤트를 누적하는 방법을 다룬다. 버튼이 하나 제공되며 해당 버튼을 클릭하면 이벤트가 누적된다. 누적된 클릭은 일정 시간 이후에 마지막 결과로 나오게 된다.

만약 당신이 버튼을 한 번 클릭했다면 1회 클릭에 대한 로그 메세지가 발생될 것이고, 당신이 2초 안에 버튼을 다섯 번 클릭했다면 5회 클릭에 대한 하나의 로그 메세지가 출력될 것이다. (이는 다섯 번의 로그 메세지가 출력되는 것과는 엄연히 다르다.)

# 즉시/자동 검색 텍스트 리스너 (Subject, debounce 사용하기)
---
이 데모는 어떻게 중간에 발생하는 이벤트를 무시한 채, 오로지 마지막의 이벤트를 처리할 수 있는지에 대해 다룬다. 전형적인 예제는 자동검색 결과창이다. 당신이 Bruce Lee를 검색할 때 B, Br, Bru, Bruce, Bruce L... 등의 결과는 실행하길 원치 않을 것이다. 차라리 조금 기다리고 유저가 단어를 타이핑 완료한 후, 단 한 번의 요청만들 하는 것이 낫다.
우리는 이것은 RxJava의 debounce/throttleWithTimeout을 통해 구현할 수 있다.

# 텍스트뷰 양방향 데이터 바인딩 (publishSubject 사용하기)
---
데이터 바인딩이란?
> 뷰의 데이터 갱신을 프로그래매틱 방식으로 하는 것이 아닌 선언적으로 UI에 기록하여 데이터의 변경이 즉각적으로 뷰에 반영될 수 있게하는 것

본 예제에서의 양방향 데이터 바인딩을 사용하면 당신은 잠재적으로 아주 쉽게 MVP 패턴을 사용할 수 있다. Publish Subject를 통해 양방향 바인딩을 좀 더 심도있게 사용하는 법에 대해서 다루겠다.

# Form 유효성 확인 (combineLatest 사용하기)
combineLatest는 여러개의 observable의 상태를 한번에 파악할 수 있게 한다.
본 예제는 combineLatest를 이용하여 기본 form의 유효성을 확인하는 법을 다룬다. 예제에는 3개의 form이 있으며, 해당 form들의 값이 유효하면 파란색 밑줄, 그렇지 않으면 에러를 랜딩한다.

3개의 독립적인 Observable이 form의 변화를 트랙킹한다. (RxAndroid의 WidgetObservabled을 사용하면 text 변화를 손쉽게 모니터링할 수 있다.)

유효성을 검증하는 Func3는 3개의 form이 모두 text change event를 받을 후에 동작합니다.

이러한 테크닉은 input field가 더 많아져, 유효성을 검증하기 위해 input field만큼의 boolean을 선언해야하고 코드가 읽기 힘들어질 때, 더욱 빛을 발합니다.

# 간단한 타이머 (using timer, interval and delay)

본 예제는 특정한 interval을 가지고 task를 실행하는 여러 케이스를 timer와 interval 그리고 delay operator들을 통해 다룬다. (Android TimerTasks 쓰지마라!) 

시연은 다음과 같다.

run a single task after a delay of 2s, then complete
run a task constantly every 1s (there's a delay of 1s before the first task fires off)

run a task constantly every 1s (same as above but there's no delay before the first task fires off)
run a task constantly every 3s, but after running it 5 times, terminate automatically

run a task A, pause for sometime, then execute Task B, then 

# Activity가 회전될 때, 데이터 유지하기 (Subjects, retained Fragments 사용하기)

RxJava를 안드로이드에서 사용하면 다음과 같은 질문들은 많이 한다.

> "어떻게하면 액티비티가 Rotating되거나, 언어가 변경되었을 때 Observable의 task를 유지할 수 있을까?"

본 예제는 retained Fragment(with setRetainInstance(true))를 사용하는 전략을 제시한다.

시작 버튼을 누른 후, 화면을 회전시켜도 Observable이 중단된 시점부터 다시 시작하는 것을 볼 수 있을 것이다.

Hot Observable과 결합해서 사용한듯?

다른 방법을 통해서 또 쓴거같은데?
I have since rewritten this example using an alternative approach. While the ConnectedObservable approach worked it enters the lands of "multicasting" which can be tricky (thread-safety, .refcount etc.). Subjects on the other hand are far more simple. You can see it rewritten using a Subject here.

# 간단한 Timeout 예제 (timeout 사용하기)
버튼1은 timeout 전에 실행된다. 하지만 버튼2는 강제적으로 timeout이 발생한다.
본 예제는 어떻게 timeout Exception에 대해 대처하는 Custom Observable을 만들 수 있는지 다룬다.






# 리소스 셋업과 해제 (using 이용하기)
본 Operator은 상대적으로 잘 알려지지 않았고, 사용하기 어렵기로 악명높다. Using은 리소스 셋업과 해제를 도와주는 API이다.
이 Operator의 장점은 잠재적으로 비용이 드는 리소스를 엄밀한 범위 내에서 사용할 수 있게 한다(?)in a tightly scoped manner.  
DB connections (like Realm instances), socket connections, thread locks 등등에 적용할 수 있다.

# Multicast Playground
Multicasting in Rx is like a dark art. Not too many folks know how to pull it off without concern. This example condiers two subscribers (in the forms of buttons) and allows you to add/remove subscribers at different points of time and see how the different operators behave under those circumstances.

The source observale is a timer (interval) observable and the reason this was chosen was to intentionally pick a non-terminating observable, so you can test/confirm if your multicast experiment will leak.

I also gave a talk about Multicasting in detail at 360|Andev. If you have the inclination and time, I highly suggest watching that talk first (specifically the Multicast operator permutation segment) and then messing around with the example here.