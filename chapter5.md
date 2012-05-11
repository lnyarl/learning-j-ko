# 챕터 5: 배열 만들기

이 챕터에선 배열을 만드는 것을 다룬다. 우선 리스트로 배열을 만드는 것을 해보고 더 큰 배열을 만들기 위해 배열들을 여러 방법으로 연결해볼 것이다.

## 5.1 모양을 이용해 배열 만들기

### 5.1.1 복습

챕터 2에서 "아이템"이라고 했던 것이 무엇이었는지 떠올려보자. 숫자 리스트의 아이템은 숫자이다. 테이블의 아이템은 행이다. 3차원 배열의 아이템은 평면이다.

`x $ y`가 y의 아이템를 x의 모양으로 늘어놓아 배열을 만든다는 것도 상기하자. 예를 들자면 다음과 같다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>2 2 $ 0 1 2 3</tt></td>
<td><tt>2 3 $ 'ABCDEF'</tt></td>
</tr><tr valign="TOP">
<td><tt>0 1<br>
2 3</tt></td>
<td><tt>ABC<br>
DEF</tt></td>
</tr></tbody></table>

만약 새 배열을 만드는데에 리스트 y에 필요한 만큼의 아이템이 없다면 다시 y의 첫 번째 아이템부터 가져와서 배열을 만든다. 이러한 특징에 의해 배열 간단한 패턴을 보일 수 있다.(예를 들어 모든 엘리먼트가 같다거나 할 수 있다.)

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>2 3 $ 'ABCD'</tt></td>
<td><tt>2 2 $ 1</tt></td>
<td><tt>3 3 $ 1 0 0 0</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DAB</tt></td>
<td><tt>1 1<br>
1 1</tt></td>
<td><tt>1 0 0<br>
0 1 0<br>
0 0 1</tt></td>
</tr></tbody></table>

"Shape" 동사인 다이아딕 `$`와 짝을 이루는 동사인 "ShapeOf"(모나딕 `$`)가 있다. "ShapeOf"는 차원의 리스트, 즉 인자의 모양을 알려준다. 예를 들자면 다음과 같다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>A =: 2 3 $ 'ABCDEF'</tt></td>
<td><tt>$ A</tt></td>
<td><tt>a =: 'pqr'</tt></td>
<td><tt>$ a</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>2 3</tt></td>
<td><tt>pqr</tt></td>
<td><tt>3</tt></td>
</tr></tbody></table>

임의의 배열 A에 대해서 차원의 리스트인 `$ A`는 1차원 리스트(A의 모양)이다. 따라서 `$ $ A`는 아이템이 1개인 리스트(A의 랭크)이다. 따라서 `$ $ $ A`는 항상 숫자 1만 가진 리스트이다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>A</tt></td>
<td><tt>$ A</tt></td>
<td><tt>$ $ A</tt></td>
<td><tt>$ $ $ A</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>2 3</tt></td>
<td><tt>2</tt></td>
<td><tt>1</tt></td>
</tr></tbody></table>

### 5.1.2 빈 배열

몇 차원의 배열이든 길이가 0이 가능하다. 길이가 0 또는 빈 리스트를 만들려면 차원 리스트를 0으로 쓰고 아이템의 값으로는 아무 값이나(뭐든 간에) 쓴다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>E =: 0 $ 99</tt></td>
<td><tt>$ E</tt></td>
</tr><tr valign="TOP">
<td><tt>&nbsp;</tt></td>
<td><tt>0</tt></td>
</tr></tbody></table>

만약 `E`가 비어있다면 이 배열은 아이템이 없다는 뜻이다. 아이템 하나를 여기에 추가하면 `E`는 아이템이 하나인 배열이 된다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>E</tt></td>
<td><tt>$ E </tt></td>
<td><tt>w =: E ,98</tt></td>
<td><tt>$ w</tt></td>
</tr><tr valign="TOP">
<td><tt>&nbsp;</tt></td>
<td><tt>0</tt></td>
<td><tt>98</tt></td>
<td><tt>1</tt></td>
</tr></tbody></table>

비슷하게 만약 `ET`가 0행 3열인 빈 테이블일 때, 한 행을 추가하면 `ET`는 행이 하나인 테이블이 된다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>ET =: 0 3 $ 'x' </tt></td>
<td><tt>$ ET</tt></td>
<td><tt> $ ET , 'pqr' </tt></td>
</tr><tr valign="TOP">
<td><tt>&nbsp;</tt></td>
<td><tt>0 3</tt></td>
<td><tt>1 3</tt></td>
</tr></tbody></table>

### 5.1.3 스칼라 만들기

이젠 스칼라를 만들어보자. 스칼라는 차원이 없다. 즉 차원 리스트가 비어있다. `$`의 왼쪽 인자로 빈 리스트를 주어서 스칼라를 만들 수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>S =: (0$0) $ 17</tt></td>
<td><tt>$ S</tt></td>
<td><tt>$ $ S</tt></td>
</tr><tr valign="TOP">
<td><tt>17</tt></td>
<td><tt>&nbsp;</tt></td>
<td><tt>0</tt></td>
</tr></tbody></table>

### 5.1.4 더 일반적으로 모양잡기

`x $ y`는 y의 아이템을 가진 x 모양의 배열을 만든다. 일반적으로 말해서 `x $ y`의 모양은 그냥 x라기 보단 y가 가진 아이템의 모양을 따르는 x라고 할 수 있다.

만약 y가 테이블이라면 y의 아이템은 행(즉, 리스트)이다. 아래 예제에서는 Y가 가진 아이템 하나의 모양은 Y의 행의 길이이다. (여기선 4이다.)

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>X =: 2</tt></td>
<td><tt>Y =: 3 4 $ 'A'</tt></td>
<td><tt>Z =: X $ Y</tt></td>
<td><tt>$ Z</tt></td>
</tr><tr valign="TOP">
<td><tt>2</tt></td>
<td><tt>AAAA<br>
AAAA<br>
AAAA</tt></td>
<td><tt>AAAA<br>
AAAA</tt></td>
<td><tt>2 4</tt></td>
</tr></tbody></table>

다음 섹션에선 우리가 만들었던 배열들을 연결해서 새로운 배열을 만드는 것을 해볼것이다.

## 5.2 추가하기 또는 끝끼리 연결하기

모든 배열은 아이템의 리스트로 간주할 수 있다. 예를 들어 테이블의 아이템은 행이다. 동사 `,`(comma)는 "Append"라고 부른다. 표현식 `x,y`는 x의 아이템 리스트 뒤에 y의 아이템 리스트가 온다는 뜻이다.

	   B =: 2 3 $ 'UVWXYZ'
	   b =:   3 $ 'uvw'
   
 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>a</tt></td>
<td><tt>b</tt></td>
<td><tt>a , b</tt></td>
<td><tt>A</tt></td>
<td><tt>B</tt></td>
<td><tt>A , B</tt></td>
</tr><tr valign="TOP">
<td><tt>pqr</tt></td>
<td><tt>uvw</tt></td>
<td><tt>pqruvw</tt></td>
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>UVW<br>
XYZ</tt></td>
<td><tt>ABC<br>
DEF<br>
UVW<br>
XYZ</tt></td>
</tr></tbody></table>

위에 나오는 예제에서 `A,B`에서 A의 아이템은 길이가 3인 리스트이고 B도 마찬가지이다. A의 아이템이 B의 아이템처럼 랭크가 같고 길이가 같은 것과 호환되기 때문이다. 그렇지 않은 경우는? 그럴땐 "Append"동사는 인자 하나를 늘려서 다른 것에 맞춘다거나 같은 랭크로 만들거나 길이를 맞추기 위해 값들을 덧댄다. 이에 대한건 다음 예제에서 볼 수 있다.

### 5.2.1 같은 랭크로 만들기

테이블에 행을 추가한다고 해보자. 예를 들어 위에 나왔던 2행 3열의 테이블인 `A`에 문자 3개의 리스트인 `b`를 새로운 행으로 붙이려고 한다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>A </tt></td>
<td><tt>b </tt></td>
<td><tt>A , b</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>uvw</tt></td>
<td><tt>ABC<br>
DEF<br>
uvw</tt></td>
</tr></tbody></table>

우리가 원했던건 `A`의 두 아이템 다음에 `b`가 가진 하나의 아이템이 붙는 것이었다. 하지만 `b`는 아이템이 1개가 아니다. `b`의 모양을 1행 3열의 테이블로 바꾸면 가능하다. 즉 `b`의 랭크를 올리는 것이다. 하지만 사실 그렇게 할 필요는 없다. 왜냐면 우리가 봤듯이 "Append" 동사는 자동으로 낮은 랭크의 인자를 1개의 아이템을 가진 배열로 만든다.

  <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>A</tt></td>
<td><tt>b</tt></td>
<td><tt>A , (1 3 $ b)</tt></td>
<td><tt>A , b</tt></td>
<td><tt>b , A</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>uvw</tt></td>
<td><tt>ABC<br>
DEF<br>
uvw</tt></td>
<td><tt>ABC<br>
DEF<br>
uvw</tt></td>
<td><tt>uvw<br>
ABC<br>
DEF</tt></td>
</tr></tbody></table>

### 5.2.2 길이 맞추기

한 인자의 아이템이 다른 쪽의 아이템보다 더 짧다면 길이를 더 늘려서 맞춘다. 문자 배열은 빈 문자로 채우고 숫자 배열은 0으로 채운다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>A</tt></td>
<td><tt>A , 'XY'</tt></td>
<td><tt>(2 3 $ 1) , 9 9</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>ABC<br>
DEF<br>
XY</tt></td>
<td><tt>1 1 1<br>
1 1 1<br>
9 9 0</tt></td>
</tr></tbody></table>

### 5.2.3 스칼라 복제하기(Replicating)

"Append"의 스칼라 인자는 다른 인자와 맞추기 위해서 복제된다. 아래 예제는 어떻게 스칼라 `'*'`가 복제되는지에 대한 것이다. 벡터 `1 $ '*'`가 늘어나는 것이 아니다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>A</tt></td>
<td><tt>A , '*'</tt></td>
<td><tt>A , 1 $ '*'</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>ABC<br>
DEF<br>
***</tt></td>
<td><tt>ABC<br>
DEF<br>
*</tt></td>
</tr></tbody></table>

## 5.3 꿰메기 또는 옆으로 연결하기

다이아딕 동사 `,.`(comma dot)은 "Stiich"라고 부른다. 표현식 `x ,. y`는 x의 각 아이템은 매핑되는 y의 아이템을 연결한다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>a</tt></td>
<td><tt>b</tt></td>
<td><tt>a ,. b</tt></td>
<td><tt>A</tt></td>
<td><tt>B</tt></td>
<td><tt>A ,. B</tt></td>
</tr><tr valign="TOP">
<td><tt>pqr</tt></td>
<td><tt>uvw</tt></td>
<td><tt>pu<br>
qv<br>
rw</tt></td>
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>UVW<br>
XYZ</tt></td>
<td><tt>ABCUVW<br>
DEFXYZ</tt></td>
</tr></tbody></table>

## 5.4 라미네이팅(Laminating) 또는 그대로 붙이기

동사 `,:`(comma colon)은 "Laminate"라고 부른다. `x ,: y`의 결과는 언제나 아이템이 2개인 배열이다. 두 아이템 중 첫 번째는 x이고 두 번째는 y이다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>a</tt></td>
<td><tt>b</tt></td>
<td><tt>a ,: b</tt></td>
</tr><tr valign="TOP">
<td><tt>pqr</tt></td>
<td><tt>uvw</tt></td>
<td><tt>pqr<br>
uvw</tt></td>
</tr></tbody></table>

만약 x와 y가 테이블이면 두 테이블이 차곡히 쌓여 3차원 배열 형태(첫 번째 차원은 길이가 2)의 결과가 나올 것이다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>A</tt></td>
<td><tt>B</tt></td>
<td><tt>A ,: B</tt></td>
<td><tt>$ A ,: B</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>UVW<br>
XYZ</tt></td>
<td><tt>ABC<br>
DEF<br>
<br>
UVW<br>
XYZ</tt></td>
<td><tt>2 2 3</tt></td>
</tr></tbody></table>

## 5.5 링크하기

동사 `;`(semicolon)은 "Link"라고 부른다. 이 동사를 쓰면 편하게 박스 리스트를 만들수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>'good' ; 'morning'</tt></td>
<td><tt>5 ; 12 ; 1995</tt></td>
</tr><tr valign="TOP">
<td><tt>+----+-------+<br>
|good|morning|<br>
+----+-------+</tt></td>
<td><tt>+-+--+----+<br>
|5|12|1995|<br>
+-+--+----+</tt></td>
</tr></tbody></table>

`x;y`가 항상 `< x, < y`와 같지 않다는 것을 예제 `5;12;1995`로 알 수 있다. "Link"가 박스의 리스트를 만들려고 할때 오른쪽 인자가 이미 박스의 리스트라면 그걸 알아챈다. `< x, < y`를 아래와 같이 정의 해놓고,

	   foo =: 4 : '(< x) , (< y)'

이 두 개를 비교해보자.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>1 ; 2 ; 3</tt></td>
<td><tt>1 foo 2 foo 3</tt></td>
</tr><tr valign="TOP">
<td><tt>+-+-+-+<br>
|1|2|3|<br>
+-+-+-+</tt></td>
<td><tt>+-+-----+<br>
|1|+-+-+|<br>
| ||2|3||<br>
| |+-+-+|<br>
+-+-----+</tt></td>
</tr></tbody></table>

## 5.6 배열 해체하기

여태 4가지 다이아딕 동사 - "Append"(`,`), "Stitch"(`,.`), "Laminate"(`,:`), "Link"(`;`) - 를 봤다. 각각은 모나딕으로도 쓰일 수 있다. 다음을 보자.

### 5.6.1 부수기

모나딕 `;`은 "Raze"라고 부른다. 이 동사는 인자의 엘리먼트를 언박싱해서 하나의 리스트로 만든다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>B =: 2 2 $ 1;2;3;4</tt></td>
<td><tt>; B</tt></td>
<td><tt>$ ; B</tt></td>
</tr><tr valign="TOP">
<td><tt>+-+-+<br>
|1|2|<br>
+-+-+<br>
|3|4|<br>
+-+-+</tt></td>
<td><tt>1 2 3 4</tt></td>
<td><tt>4</tt></td>
</tr></tbody></table>

### 5.6.2 풀기

모나딕 `,`은 "Ravel"이라고 부른다. 이 동사는 인자의 엘리먼트를 조립해서 하나의 리스트로 만든다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>B</tt></td>
<td><tt>, B</tt></td>
<td><tt> $ , B</tt></td>
</tr><tr valign="TOP">
<td><tt>+-+-+<br>
|1|2|<br>
+-+-+<br>
|3|4|<br>
+-+-+</tt></td>
<td><tt>+-+-+-+-+<br>
|1|2|3|4|<br>
+-+-+-+-+</tt></td>
<td><tt>4</tt></td>
</tr></tbody></table>

### 5.6.3 아이템 풀기

모나딕 `,.`은 "Ravel Items"라고 부른다. 이 동사는 인자의 각 아이템을 따로 풀어서 테이블의 형태로 만든다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>k =: 2 2 3 $ i. 12</tt></td>
<td><tt>,. k</tt></td>
</tr><tr valign="TOP">
<td><tt>0&nbsp;&nbsp;1&nbsp;&nbsp;2<br>
3&nbsp;&nbsp;4&nbsp;&nbsp;5<br>
<br>
6&nbsp;&nbsp;7&nbsp;&nbsp;8<br>
9 10 11</tt></td>
<td><tt>0 1 2 3&nbsp;&nbsp;4&nbsp;&nbsp;5<br>
6 7 8 9 10 11</tt></td>
</tr></tbody></table>

"Ravel Items"는 하나의 리스트를 1열의 테이블로 만들기에 좋다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>b   </tt></td>
<td><tt>,. b</tt></td>
</tr><tr valign="TOP">
<td><tt>uvw</tt></td>
<td><tt>u<br>
v<br>
w</tt></td>
</tr></tbody></table>

### 5.6.4 아이템화

모나딕 `,:`은 "Itemize"라고 한다. 이 동사는 차원을 하나 추가해서 어떤 배열이든 아이템이 1개인 배열로 만든다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>A </tt></td>
<td><tt>,: A</tt></td>
<td><tt>$ ,: A</tt></td>
</tr><tr valign="TOP">
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>ABC<br>
DEF</tt></td>
<td><tt>1 2 3</tt></td>
</tr></tbody></table>

## 5.7 큰 배열과 작은 배열

우리가 본 바와 같이 배열은 동사 `$`로 만들 수 있다.

	   3 2 $ 1 2 3 4 5 6
	1 2
	3 4
	5 6

그 내용을 한 줄로 표현할 수 있는 작은 배열은 `$`대신 차원 수를 명시하지 않아도 되는 다른 방법이 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt> &gt; 1 2 ; 3 4 ; 5 6</tt></td>
<td><tt> 1 2 , 3 4 ,: 5 6</tt></td>
</tr><tr valign="TOP">
<td><tt>1 2<br>
3 4<br>
5 6</tt></td>
<td><tt>1 2<br>
3 4<br>
5 6</tt></td>
</tr></tbody></table>

큰 테이블을 만드는 것은 아래 나오는 방법을 쓰면 편하다. 우선 우선 "utility" 동사가 있다.(이는 유용하긴 하지만 지금 당장에 이 정의에 대해서 다루진 않겠다.)

	   ArrayMaker =: ". ;. _2

ArrayMaker는 스크립트를 입력받아 각 라인을 행으로 해서 숫자 테이블로 만든다.

	   table =: ArrayMaker 0 : 0
	1 2 3
	4 5 6
	7 8 9
	)

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>table</tt></td>
<td><tt>$ table</tt></td>
</tr><tr valign="TOP">
<td><tt>1 2 3<br>
4 5 6<br>
7 8 9</tt></td>
<td><tt>3 3</tt></td>
</tr></tbody></table>

(챕터17에 ArrayMaker의 동작에 대한 설명이 있다) 박스 배열도 똑같이 스크립트로 적어놓는다.

	   X =:  ArrayMaker  0 : 0
	'hello' ; 1 2 3 ; 8
	'Waldo' ; 4 5 6 ; 9
	)

<table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>X</tt></td>
<td><tt>$ X</tt></td>
</tr><tr valign="TOP">
<td><tt>+-----+-----+-+<br>
|hello|1 2 3|8|<br>
+-----+-----+-+<br>
|Waldo|4 5 6|9|<br>
+-----+-----+-+</tt></td>
<td><tt>2 3</tt></td>
</tr></tbody></table>

챕터 5가 끝났다.
