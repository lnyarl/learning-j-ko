# 8 장 : 동사 합성

이 챕터는 두 동사를 합쳐 새로운 합성 동사를 만드는 것을 목표로 한다.

## 8.1 모나드와 모나드 합성하기

3 장에서 나왔던 합성 접속사인 `@:`(at colon, "At"이라고 한다.)를 상기하자. `sum`과 `square`라는 동사를 이용해서 새로운 합성 동사인 제곱의 합을 만들수 있다.

	   sum    =: +/
	   square =: *:

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>sumsq =: sum @: square</TT></TD>
<TD><TT>sumsq 3 4</TT></TD>
<TR VALIGN=TOP>
<TD><TT>sum@:square</TT></TD>
<TD><TT>25</TT></TD>
</TABLE>

일반적인 구조는 다음과 같다. 모나드 동사 `f`, `g`가 있다면

	               (f @: g) y    는   f (g y)   이다.

특이한 것은 `f`는 `g y`의 결과 전체에 적용된다는 것이다. 예를 들어 `g`가 어떤 테이블의 각 행에 따로 적용된다고 해보자. 

	   g =: sum " 1 
	   f =: <

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>y =: 2 2 $ 1 2 3 4</TT></TD>
<TD><TT>g y</TT></TD>
<TD><TT>f g y</TT></TD>
<TD><TT>(f @: g) y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 2<BR>
3 4</TT></TD>
<TD><TT>3 7</TT></TD>
<TD><TT>+---+<BR>
|3 7|<BR>
+---+</TT></TD>
<TD><TT>+---+<BR>
|3 7|<BR>
+---+</TT></TD>
</TABLE>

가장 간단한 형태의 합성을 보았다. 이제 좀 더 다양한 변형을 보자.

## 8.2 합성하기: 모나드와 다이아드

만약 `f`가 모나드이고 `g`가  다이아드이면 `f @: g`는 아래와 같은 의미를 가지는 다이아딕 동사가 된다.

	           x (f @: g) y    는    f (x g y)   이다.

예제를 보자. 두 벡터 `x`와 `y`의 곱의 합은 "스칼라 곱"이라고 한다.

	   sp =: +/ @: *

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>x =: 1 2</TT></TD>
<TD><TT>y =: 2 3</TT></TD>
<TD><TT>x * y</TT></TD>
<TD><TT>+/(x * y) </TT></TD>
<TD><TT>x sp y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 2</TT></TD>
<TD><TT>2 3</TT></TD>
<TD><TT>2 6</TT></TD>
<TD><TT>8</TT></TD>
<TD><TT>8</TT></TD>
</TABLE>

표현식 `x (f @: g) y`에서 동사 `f`가 `x g y`의 결과 전체에 한 번 적용 되었음을 마지막 예제에서 알 수 있다.

## 8.3  합성하기: 다이아드와 모나드

접속사 `&:`(mpersand colon, "Appose"라고 읽는다.)는 다이아드인 `f`와 모나드인 `g`를 합성한다. 구조는 다음과 같다.

	               x (f &: g) y   는   (g x) f (g y)  이다

예를 들어 두 리스트가 같은 길이인지 알아보고자 할 땐 `= &: #`를 쓴다.

	   eqlen =: = &: #

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> x </TT></TD>
<TD><TT> y </TT></TD>
<TD><TT>#x</TT></TD>
<TD><TT>#y</TT></TD>
<TD><TT>(#x) = (#y)</TT></TD>
<TD><TT>x eqlen y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 2</TT></TD>
<TD><TT>2 3</TT></TD>
<TD><TT>2</TT></TD>
<TD><TT>2</TT></TD>
<TD><TT>1</TT></TD>
<TD><TT>1</TT></TD>
</TABLE>

`f`가 `g x`와 `g y`에 적용 되었음을 알 수 있다.

## 8.4  이중 합성

복습을 잠깐 하자. 우리는 세 가지 합성 방법을 배웠다.

	              (f @: g) y    =    f (g y)

	            x (f @: g) y    =    f (x g y)

	            x (f &: g) y    =    (g x) f (g y)

으리고 이번엔 네 번째 합성 방법이다. 

	              (f &: g) y    =    f (g y) 

이 방법은 분명 첫 번째 방법과 똑같다. 이런 명백한 중복은 모나딕과 다이아딕 케이스 두 경우를 다 정의하는 이중적인 정의를 할 때에 유용하게 쓰인다.

우선 첫 번째와 두 번째 방법에서 만약 `g`가 이중적이라면 그의 합성인 `f @: g`또한 이중적이다. 예를 들어 `g`가 불안정한 내장 동사인 `|.`라고 해보자. `|. y`는 `y`의 순서를 반대로 바꾸는 것이고 `x |. y`는 `y`를 `x`의 순서로 바꾸는 것이다.	

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> y =: 'abcdef' </TT></TD>
<TD><TT>(< @: |.) y </TT></TD>
<TD><TT>  1 (< @: |.) y </TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>+------+<BR>
|fedcba|<BR>
+------+</TT></TD>
<TD><TT>+------+<BR>
|bcdefa|<BR>
+------+</TT></TD>
</TABLE>

위의 세 번째와 네 번째 합성 방법은 만약 `f`가 이중적이면 `f &: g`또한 이중적이다. 예를 들어서 `f`가 `%`(역원 또는 나누기)이고 `g`가 `*:`(제곱)라고 해보자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>% *: 2</TT></TD>
<TD><TT>(% &: *:) 2</TT></TD>
<TD><TT>(*: 3) % (*: 2)</TT></TD>
<TD><TT>3 (% &: *:) 2 </TT></TD>
<TR VALIGN=TOP>
<TD><TT>0.25</TT></TD>
<TD><TT>0.25</TT></TD>
<TD><TT>2.25</TT></TD>
<TD><TT>2.25</TT></TD>
</TABLE>

## 8.5 합성: 모나드를 따라가는 모나드

"Atop"이라고 부르는 접속사 `@`가 있다. 이 녀석은 접속사 `@:`의 변형중 하나이다. 아래는 ` f @: g`와 `f @ g`의 차이에 대해 설명하는 예제이다.

	   y =: 2 2 $ 0 1 2 3

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>y</TT></TD>
<TD><TT>f</TT></TD>
<TD><TT>g</TT></TD>
<TD><TT>(f @: g) y</TT></TD>
<TD><TT>(f @ g) y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>0 1<BR>
2 3</TT></TD>
<TD><TT><</TT></TD>
<TD><TT>sum"1</TT></TD>
<TD><TT>+---+<BR>
|1 5|<BR>
+---+</TT></TD>
<TD><TT>+-+-+<BR>
|1|5|<BR>
+-+-+</TT></TD>
</TABLE>

`f @: g`에서 `f`는 딱 한 번만 적용된다. 하지만 `f @ g`에서는 `g`가 적용되는 것마다 그에 상응하는 것에 `f`가 적용된다. 이것을 `f`의 적용이 `g`의 적용을 따라간다 라고 말한다.

일반적으로 동사는 세 가지 랭크(모나딕, 왼쪽, 오른쪽)아 있고 동사 `f`의 랭크들을 알아보기 위해서는 표현식 `f b. 0`을 쓰면 된다고 7장에서 말했었다. 간단히 예제를 보자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>g</TT></TD>
<TD><TT>g b. 0</TT></TD>
<TR VALIGN=TOP>
<TD><TT>sum"1</TT></TD>
<TD><TT>1 1 1</TT></TD>
</TABLE>

동사 `g`의 모나딕 랭크가 `G`라고 해보자.

	   G =: 0 { (g b. 0)

그럼 `f @ g`은 `f @: g`가 각각의 `G`-셀에 적용된다. 즉 `f @: g"G`이다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>(f @ g) y</TT></TD>
<TD><TT>(f @: g)"G y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>+-+-+<BR>
|1|5|<BR>
+-+-+</TT></TD>
<TD><TT>+-+-+<BR>
|1|5|<BR>
+-+-+</TT></TD>
</TABLE>

그리고 일반적인 구조는 다음과 같다.

	             (f @ g) y    는     (f @: g) " G y   이다

## 8.6  합성: 다이아드를 따르는 모나드

다음으로 `g`가 다이아드인 `f @ g`합성을 볼 것이다. `f`와 `g`가 다음과 같다고 해보자.

	   f =: <
	   g =: |. " 0 1  NB. 다이아딕

그럼 `x g y`는 `y`의 벡터를 그와 연관된 `x`의 스칼라에 따라 회전시킨다는 의미가 된다. 예제를 보자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>x=: 1 2</TT></TD>
<TD><TT>y=: 2 3 $ 'abcdef'</TT></TD>
<TD><TT>x g y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 2</TT></TD>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>bca<BR>
fde</TT></TD>
</TABLE>

여기서 이제 `f @: g`와 `f @ g`의 차이가 드러난다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>f (x g y)</TT></TD>
<TD><TT>x (f @: g) y </TT></TD>
<TD><TT>x (f @ g) y </TT></TD>
<TR VALIGN=TOP>
<TD><TT>+---+<BR>
|bca|<BR>
|fde|<BR>
+---+</TT></TD>
<TD><TT>+---+<BR>
|bca|<BR>
|fde|<BR>
+---+</TT></TD>
<TD><TT>+---+---+<BR>
|bca|fde|<BR>
+---+---+</TT></TD>
</TABLE>

`f @: g`에서는 동사 `f`가 한 번만 적용됨을 알 수 있다. 하지만 `f @ g`에서는 각각의 `g`적용에 `f`가 다시 각각 적용된다.

`g`의 왼쪽과 오른쪽의 랭크를 각각 `L`과 `R`이라고 해보자 그러면 `f @ g`는 `x`의 `L`-셀과 그와 관계된 `y`의 `R`-셀에 따로 `f @: g`이 적용되는 것과 같다. 득 `f @ g`는 `(f @: g)"G`이다. 여기서 `G = L,R`이다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>G =: 1 2 { (g b. 0)</TT></TD>
<TD><TT>x (f @:g)" G y</TT></TD>
<TD><TT>x (f @ g) y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>0 1</TT></TD>
<TD><TT>+---+---+<BR>
|bca|fde|<BR>
+---+---+</TT></TD>
<TD><TT>+---+---+<BR>
|bca|fde|<BR>
+---+---+</TT></TD>
</TABLE>

이에 대한 구조는 아래와 같다. 

	              x (f@g) y =  x (f@:g) " G y

## 8.7  합성: 모나드를 따르는 다이아드

접속사 `&`가 연산자들을 붙인다고 챕터 3에서 배웠다. 명사 하나와 다이아딕 동사를 하나를 인자로 받아 모나드를 만든다. 예를 들어서 `+&6`은 인자에 `6`을 더하는 모나드이다.

만약 `&`의 양쪽 인자가 모두 동사이면 `&`는 다르게 작동한다. 이 경우에는 연산자들을 합성한다. (그리고 이 경우 "Compose"라고 읽는다.) 이제 `f`가 다이아딕인 `f & g` 합성에 대해서 보자

`g`가 "Square" 함수이고 `f`가 두개의 리스트를 잇는 "comma" 함수라고 하자.

	   f =: ,
	   g =: *: 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>x =: 1 2</TT></TD>
<TD><TT>y =: 3 4</TT></TD>
<TD><TT>g x</TT></TD>
<TD><TT>g y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 2</TT></TD>
<TD><TT>3 4</TT></TD>
<TD><TT>1 4</TT></TD>
<TD><TT>9 16</TT></TD>
</TABLE>

아래의 예제에서 `f &: g`와 `f & g`의 차이를 볼 수 있다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>(g x) f (g y)</TT></TD>
<TD><TT>x (f &: g) y</TT></TD>
<TD><TT>x (f & g) y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 4 9 16</TT></TD>
<TD><TT>1 4 9 16</TT></TD>
<TD><TT>1&nbsp;&nbsp;9<BR>
4 16</TT></TD>
</TABLE>

`f &: g`에서 동사 `f`는 한 번만 적용되어 `1 4 , 9 16`를 수행함을 알 수 있다. 반면 `f & g`에서는 `f`가 각각 두번 적용 되었다. 처음에 한번 적용되어 `1,9`가 나오고 그 다음에 적용되어 `4,16`이 나왔다.

구조는 다음과 같다.

	              x (f & g) y  는  (g x) (f " G,G) (g y)   이다.

`G`가 `g`의 모나딕 랭크라면 `f`는 `x`의 `G`-셀들과 그에 연관된 `y`의 `G`-셀들에 따로 적용된다. 아래에 예제가 있다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>G =: 0 { (g b. 0)</TT></TD>
<TD><TT>(g x)(f " (G,G))(g y) </TT></TD>
<TD><TT> x (f & g) y </TT></TD>
<TR VALIGN=TOP>
<TD><TT>0</TT></TD>
<TD><TT>1&nbsp;&nbsp;9<BR>
4 16</TT></TD>
<TD><TT>1&nbsp;&nbsp;9<BR>
4 16</TT></TD>
</TABLE>

## 8.8 다시 이중성

`f & g`합성은 이중적이다. 다이아딕 `x f&g y`의 경우는 위에서 다뤘다. 모나딕 `f&g y`은 `f@g y`와 같다.

	   f =: <
	   g =: *:

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>f&g 1 2 3</TT></TD>
<TD><TT>f@g 1 2 3</TT></TD>
<TR VALIGN=TOP>
<TD><TT>+-+-+-+<BR>
|1|4|9|<BR>
+-+-+-+</TT></TD>
<TD><TT>+-+-+-+<BR>
|1|4|9|<BR>
+-+-+-+</TT></TD>
</TABLE>

## 8.9  요약

아래에 위에서 봐왔던 8개의 경우를 요약해놨다.

	         @:       (f @: g) y  =  f (g y)

	         @:     x (f @: g) y  =  f (x g y)

	         

	         &:       (f &: g) y  =  f (g y) 

	         &:     x (f &: g) y  =  (g x) f (g y)

	       

	         @        (f @ g)  y  =  (f @: g) " G  y

	         @      x (f @ g)  y  =  x (f @: g) " LR y

	       

	         &        (f & g)  y  =  (f @: g) " G  y

	         &      x (f & g)  y  =  (g x) (f " (G,G)) (g y)

`G`는 `g`의 모나딕 랭크이고 `LR`은 `g`의 오른쪽, 왼쪽 랭크의 벡터이다. 

## 8.10 역(Inverses)

"Square"(제곱) 동사인 `*:`는 "Square-root"(제곱근) 동사인 `%:`의 역이라고 할 수 있다. 역수를 만드는 동사는 자신이 자신의 역이다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>*: 2 </TT></TD>
<TD><TT>%: 4</TT></TD>
<TD><TT>% 4</TT></TD>
<TD><TT>% 0.25</TT></TD>
<TR VALIGN=TOP>
<TD><TT>4</TT></TD>
<TD><TT>2</TT></TD>
<TD><TT>0.25</TT></TD>
<TD><TT>4</TT></TD>
</TABLE>

J의 많은 동사들은 역을 가지고 있다. 내장 접속사 `^:`(caret colon, "Power"라고 한다.)는 표현식 `f ^: _1`을 이용해서 동사 `f`의 역을 구한다. (이건 관례적으로 역함수를 f<sup>-1</sup>으로 쓰는 것과 비슷하다)

예를 들어서 제곱의 역함수는 제곱근이다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> sqrt =: *: ^: _1</TT></TD>
<TD><TT>sqrt 16</TT></TD>
<TR VALIGN=TOP>
<TD><TT>*:^:_1</TT></TD>
<TD><TT>4</TT></TD>
</TABLE>

`^:`는 내장 동사뿐만이 아니라 사용자 정의 동사들 까지도 자동으로 역을 찾는다. 예를 들어 "제곱근 곱하기 2"의 역은 "절반의 제곱"이 된다.

	   foo    =: (2&*) @: %:
	   fooINV =: foo ^: _1
	   

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>foo 16</TT></TD>
<TD><TT>fooINV 8</TT></TD>
<TD><TT>foo fooINV 36</TT></TD>
<TR VALIGN=TOP>
<TD><TT>8</TT></TD>
<TD><TT>16</TT></TD>
<TD><TT>36</TT></TD>
</TABLE>

## 8.11 합성: 동사 아래 동사(Verb Under Verb)

이제 접속사 `&.`(ampersand dot. "Under"라고 한다.)로 합성하는 방법에 대해 알아보자. 합성 "`f` Under `g`"는 `g`를 적용하고 그 다음에 `f`를 적용하고 `g`의 역을 적용한다라는 의미이다.

예제를 보자. 어떤 숫자의 제곱근은 로그를 구하고 그것을 반으로 나눈 다음 진수(antilog)를 구하면 된다. 즉 "halving under logarithm"이다. 절반으로 나누는 동사는 `-:`이고 로그는 `^.`이다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>SQRT =: -: &. ^.</TT></TD>
<TD><TT>SQRT 16</TT></TD>
<TR VALIGN=TOP>
<TD><TT>-:&.^.</TT></TD>
<TD><TT>4</TT></TD>
</TABLE>

일반적인 구조는 다음과 같다.

	             (f &. g) y   는  (g ^: _1) f g y   이다.

8장이 끝났다.