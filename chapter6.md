# 제 6장: 인덱싱

인덱싱은 위치를 가지고 배열의 여러 요소들을 선택하는 것이다. 이 장에선 요소 선택, 선택된 요소를 새로운 배열로 재정리, 선택한 요소의 수정 또는 갱신을 다룬다.

## 6.1  선택하기

동사 `{`는 "From"이라고 부른다. 표현식 `x { y`는 `y`에서 `x`가 가르키는 위치의 요소들을 선택한다. 예를 들어보자. 그 전에 제 2장에서`L`이 리스트라면 `L`의 아이템의 위치는 0 1 2 .. 이렇게 매긴다고 했던 것을 기억하고 있어야한다. 그러면 표현식 `0 { L`은 `L`의 첫 번째 아이템을 반환한다. `1 { L`은 두 번째 아이템을 반환한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L =: 'abcdef'</TT></TD>
<TD><TT> 0 { L</TT></TD>
<TD><TT> 1 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>a</TT></TD>
<TD><TT>b</TT></TD>
</TABLE>

`{`의 왼쪽 인자는 "index"(인덱스)라고 부른다.

### 6.1.1 선택하기의 일반적인 패턴

몇몇 아이템들을 한꺼번에 선택 할 수도 있다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L </TT></TD>
<TD><TT>0 2 4 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>ace</TT></TD>
</TABLE>

`L`에서 선택한 아이템들을 한 번 더 뽑거나 재 정렬할 수도 있다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L </TT></TD>
<TD><TT>5 4 4 3 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>feed</TT></TD>
</TABLE>

인덱스는 음수도 가능하다. `_1`은 마지막 아이템을, `_2`는 마지막 바로 전 아이템을 선택한다. 양수, 음수 인덱스를 같이 사용해도 된다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L </TT></TD>
<TD><TT> _1 { L</TT></TD>
<TD><TT> _2 1 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>f</TT></TD>
<TD><TT>eb</TT></TD>
</TABLE>

테이블의 단일 요소인 두 번째 행, 세 번째 열은 인덱스 `< 1 ; 2`로 선택한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>T =: 3 3 $ 'abcdefghi'</TT></TD>
<TD><TT> (< 1 ; 2) { T</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def<BR>
ghi</TT></TD>
<TD><TT>f</TT></TD>
</TABLE>

아니면 좀 더 작은 테이블(subarray라고 한다)을 만들기 위해 특정 행과 열의 모든 엘리먼트를 일괄 선택할 수도 있다. 예를 들어 주어진 테이블의 1행과 2행, 0열과 1열을 선택해 subarray를 만들고자 한다면 인덱스 `<; 1 2; 0 1`를 사용한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>T</TT></TD>
<TD><TT>(< 1 2;0 1) { T</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def<BR>
ghi</TT></TD>
<TD><TT>de<BR>
gh</TT></TD>
</TABLE>

테이블에서 온전한 행을 선택할 수도 있다. 테이블이 각 아이템이 하나의 행을 이루는 아이템들의 리스트인 것을 기억하고 있을것이다. 따라서 테이블에서 행을 선택하는 것은 그냥 리스트에서 아이템을 선택하는 것과 같다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>T </TT></TD>
<TD><TT>1 { T</TT></TD>
<TD><TT>2 1 { T</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def<BR>
ghi</TT></TD>
<TD><TT>def</TT></TD>
<TD><TT>ghi<BR>
def</TT></TD>
</TABLE>

온전한 열을 선택하는 방법 중 금방 떠오르는 방법은 모든 행의 특정 아이템을 선택하는 것이다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>T </TT></TD>
<TD><TT>(< 0 1 2 ; 1 ){ T</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def<BR>
ghi</TT></TD>
<TD><TT>beh</TT></TD>
</TABLE>

하지만 다르게도 할 수 있다. 아래를 보자

### 6.1.2  Take, Drop, Head, Behead, Tail, Curtail

이번엔 인덱싱을 하는데에 편리한 간단한 동사들을 소개한다. 우선 내장 동사인 `{.`(left brace dot이고 "Take"라고 읽는다.)를 보자. `n {. L`은 리스트 `L`에서 처음 `n`개의 아이템을 선택한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>2 {. L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>ab</TT></TD>
</TABLE>

만약 `n {. L`을 이용해서 L에서 n개의 아이템을 가져오고 L의 길이보다 n이 크다면, `n {. L`의 결과는 n만큼 늘어나고 남는 부분은 0(zero)나 빈 문자나 빈 박스로 채워진다.

예를 들어서 어떤 문자열에서 정확히 문자 8자로 만들어야 한다고 해보자. 주어지는 문자열은 8보자 길거나 짧을 수 있다. 만약 길다면 짧게 해야하고, 짧다면 스페이스를 보충해서 늘려야 한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>s =: 'pasta'</TT></TD>
<TD><TT># s</TT></TD>
<TD><TT>z =: 8 {. s</TT></TD>
<TD><TT># z</TT></TD>
<TR VALIGN=TOP>
<TD><TT>pasta</TT></TD>
<TD><TT>5</TT></TD>
<TD><TT>pasta&nbsp;&nbsp;&nbsp;</TT></TD>
<TD><TT>8</TT></TD>
</TABLE>

내장 동사인 `}.`(right-brace dot이라고 하고 "Drop"이라고 읽는다)를 보자. 이 함수를 사용하면 `n }. L`이고 리스트 `L`에서 처음 `n`개의 아이템을 빼고 선택한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>2 }. L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>cdef</TT></TD>
</TABLE>

`L`에서 마지막 `n`개의 아이템을 선택하는 것은 `(-n) {. L`이라고 쓴다. 그럼 마지막 `n`개의 아이템을 빼고 선택하는 것은 어떻게 쓸까. `(-n) }. L`이다

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>_2 {. L</TT></TD>
<TD><TT>_2 }. L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>ef</TT></TD>
<TD><TT>abcd</TT></TD>
</TABLE>

"Take"와 "Drop"동사는 `n = 1`일 때의 특별한 케이스에 대한 약어가 있다. 리스트의 가장 처음 아이템을 선택하는 것은 `{.`("Head")를 모나딕으로 사용한다. 첫 번째 아이템을 제외하고 선택하는 것은 `}.`("Behead")을 모나딕으로 사용한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>{. L</TT></TD>
<TD><TT>}. L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>a</TT></TD>
<TD><TT>bcdef</TT></TD>
</TABLE>

리스트의 마지막 아이템은 `{:`(left-brace colon으로 쓰고 "Tail"이라고 읽는다.)를 모나딕으로 사용한다. 마지막 아이템만 제외하는 것은 `}:`(right-brace colon이라고 쓰고 "Curtail"라고 읽는다.)

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>{: L</TT></TD>
<TD><TT>}: L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>f</TT></TD>
<TD><TT>abcde</TT></TD>
</TABLE>

## 6.2  일반적인 선택 방법

앞으로 편하려면 몇 가지 용어에 대해 정하고 가자. 일반적으로 우리는 n-차원의 배열을 다룰 수 있지만 그냥 3차원의 배열만 생각하자. 하나의 요소는 판 번호, 행 번호, 열 번호를 이용해 선택한다. 판 번호란 첫 번째 축을 따라 늘어서 있는 숫자 중 하나이다. 비슷하게 행 번호는 두 번째 축, 열 번호는 세 번째 축을 따라 늘어서있다.

인덱싱을 하는데에 특별한 표기법은 없다. `{`의 왼쪽 인자는 표현식이나 부호화된 무언가, 또는 선택이나 재정렬을 하기 위한 데이터가 온다. 이런 데이터는 편한 방법으로 만들면 된다. 이제부터 이 데이터를 어떻게 만드는지 알아보자.


### 6.2.1 독립적인 선택

인덱싱을 하는 일반적인 표현식은 `index { array`의 형태이다. `index`는 스칼라의 배열이다. `index`를 이루는 각 스칼라는 각각 독립적인 선택을 수행하고 선택된 값들을 전부 합쳐서 결과를 낸다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L </TT></TD>
<TD><TT> 0 1 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>ab</TT></TD>
</TABLE>

### 6.2.2  인덱스의 모양

리스트에서 아이템을 선택한 결과의 모양은 `index`의 모양에 의해 정해진다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>index =: 2 2 $ 2 0 3 1</TT></TD>
<TD><TT>index { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>2 0<BR>
3 1</TT></TD>
<TD><TT>ca<BR>
db</TT></TD>
</TABLE>

인덱스의 범위는 반드시 `-#L`에서 `(#L)-1`사이에 있어야 한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> L</TT></TD>
<TD><TT>#L</TT></TD>
<TD><TT>_7 { L</TT></TD>
<TD><TT>6 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>6</TT></TD>
<TD><TT>error</TT></TD>
<TD><TT>error</TT></TD>
</TABLE>

### 6.2.3  스칼라

`index`의 각 스칼라는 그냥 숫자이거나 박스이다(그리고 당연히 하나가 박스면 나머지 인덱스도 전부 박스이다.) 만약 스칼라가 단일 숫자이면 `array`에서 아이템 하나 만을 선택한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A =: 2 3 $ 'abcdef'</TT></TD>
<TD><TT>1 { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>def</TT></TD>
</TABLE>

만약 `index`의 스칼라가 박스라면 박스 안에는 연속되는 축에 적용할 셀렉터의 리스트가 있다. 박스가 이런 용도로 쓰이는 것을 한번 보자. 우선 박스 함수로 `SuAx`라는 함수를 만들었다.

	   SuAx =: <

아래의 예제에서는 `A`에서 1행 0열의 요소를 선택한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx 1 0) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>d</TT></TD>
</TABLE>

### 6.2.4 하나의 축에서 선택하기

`SuAx p, r, c`와 같은 형태의 연속된 축에 적용할 셀렉터의 리스트에서 `p`, `r`, `c`는 스칼라이다. 이 스칼라는 숫자이거나 박스이다(그리고 만약 하나가 박스면 다른 것도 다 박스이다.) 한 숫자는 축에서 하나를 선택한다. 위에서 나온 예처럼 하나의 판이나 열 또는 행이 될 수 있다.

하지만 만약 셀렉터가 박스라면 그 박스는 같은 축에 적용할 셀렉터의 리스트를 담고 있다. 이런 용도로 박스를 사용하는 것을 보기위해서 `Sel`이라는 이름의 박스 함수를 만들자.

	   Sel =: <

예를 들어서 `A`에서 1행 0열, 1행 2열의 요소를 선택하려면 아래와 같이 쓴다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 1), (Sel 0 2)) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>df</TT></TD>
</TABLE>

### 6.2.5 제외하기

특정한 축에서 무언가를 선택하는 대신 다른 레벨로 박싱된 숫자의 리스트를 이용해 어떤 것을 제외할 수 있다. 박스를 이 용도로 사용하기 위해서 `Excl`라는 함수를 정의하자.

	   Excl =: <

`A`의 0번째 행에서 1열의 요소만 제외하고 나머지를 선택하려면 아래 예제처럼 한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 0), (Sel (Excl 1))) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>ac</TT></TD>
</TABLE>

아무것도 제외하지 않는 행동을 해서 특정 축의 모든 요소를 선택할 수도 있다. 즉 제외에 사용할 인덱스로 빈 리스트인 `0$0`를 사용한다. 예를들어 `A`의 1행의 모든 열을 선택하려면 아래 처럼 하자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 1),(Sel (Excl 0$0))) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>def</TT></TD>
</TABLE>

### 6.2.6  단순화

표현식 `Excl 0$0`는 박싱된 빈 배열이다. J에는 이것에 대한 내장된 약어가 있다. `a:`(letter-a colon이라고 하고 "Ace"라고 읽는다)가 그것이다. 이 동사는 이 장에선 "all"이라는 의미가 되겠다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 1),(Sel a:)) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>def</TT></TD>
</TABLE>

만약 `(SuAx p,q,..., z)`의 형태의 인덱스에서 마지막 셀렉터인 `z`가 "all"의 형태(`Sel (Excl 0$0)`이나 `Sel a:`)라면 이 셀렉터는 무시된다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 1),(Sel a:)) {A</TT></TD>
<TD><TT>(SuAx (Sel 1)) {A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>def</TT></TD>
<TD><TT>def</TT></TD>
</TABLE>

`SuAx (Sel p),(Sel q),...`의 형태의 인덱스에 "all" 형태가 하나도 없다면 이 인덱스는 `SuAx p;q;...`의 형태로 단축할 수 있다. 예를 들어 만약 1행 0열, 1행 2열의 요소를 선택하려면 다음과 같이 한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 1),(Sel 0 2)) {A</TT></TD>
<TD><TT>(SuAx 1;0 2) {A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>df</TT></TD>
<TD><TT>df</TT></TD>
</TABLE>

마지막으로 위에서 봤듯이 만약 각 축에서 하나씩만 선택한다면 간단한 언박싱된 리스트만으로도 충분하다. 예를 들어서 1행, 2열에서 요소를 선택한다면 다음과 같이 한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A </TT></TD>
<TD><TT>(SuAx 1;2) { A</TT></TD>
<TD><TT>(SuAx 1 2) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>f</TT></TD>
<TD><TT>f</TT></TD>
</TABLE>

### 6.2.7  결과의 모양

3차원 배열 `B`가 있다.

	   B =: 10 + i. 3 3 3

그리고 `p`는 `B`의 첫 번째 축에 있는 판을 선택하는 인덱스로, `r`은 두 번째 축을 따라 행을 선택하는 인덱스, 'c'는 세 번째 축을 따라 열을 선택하는 인덱스로 정의하자.

	   p =: 1 2
	   r =: 1 2
	   c =: 0 1

이제 `p;r;c`로  선택을 하면 그 결과인 `R`의 모양은 `p`, `r`, `c`의 결과를 이은(concatenation) 모양이 될 것이다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>B</TT></TD>
<TD><TT>R =: (< p;r;c) { B</TT></TD>
<TD><TT>$ R</TT></TD>
<TD><TT>($p),($r),($c)</TT></TD>
<TR VALIGN=TOP>
<TD><TT>10 11 12<BR>
13 14 15<BR>
16 17 18<BR>
<BR>
19 20 21<BR>
22 23 24<BR>
25 26 27<BR>
<BR>
28 29 30<BR>
31 32 33<BR>
34 35 36</TT></TD>
<TD><TT>22 23<BR>
25 26<BR>
<BR>
31 32<BR>
34 35</TT></TD>
<TD><TT>2 2 2</TT></TD>
<TD><TT>2 2 2</TT></TD>
</TABLE>

`B` is 3-dimensional, and so is `R`. As we would expect, this concatenation-of-shapes holds when a selector (`r`, say) is a list of length one:
`B`는 3차원이고 `R`도 3차원이다. 예상대로 모양의 연결은 셀렉터가 길이가 1인 리스트일때 가능하다.------------------

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>r =: 1 $ 1</TT></TD>
<TD><TT>S =: (< p;r;c){B</TT></TD>
<TD><TT>$ S</TT></TD>
<TD><TT>($p),($r),($c)</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1</TT></TD>
<TD><TT>22 23<BR>
<BR>
31 32</TT></TD>
<TD><TT>2 1 2</TT></TD>
<TD><TT>2 1 2</TT></TD>
</TABLE>

and the concatenation-of-shapes holds when selector `r` is a scalar:
그리고 모양의 연결은 셀렉터 `r`이 스칼라인것을 잡는다.-------------

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>r =: 1</TT></TD>
<TD><TT>T =: (< p;r;c){B</TT></TD>
<TD><TT>$ T</TT></TD>
<TD><TT>($p),($r),($c)</TT></TD>
<TD><TT>$ r</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1</TT></TD>
<TD><TT>22 23<BR>
31 32</TT></TD>
<TD><TT>2 2</TT></TD>
<TD><TT>2 2</TT></TD>
<TD><TT>&nbsp;</TT></TD>
</TABLE>

마지막 예제에서 `r`은 스칼라이다. 따라서 `r`의 모양은 빈 리스트이다. 그래서 `r`의 축은 아무것도 표시되지 않는다. 그래서 `T`는 2차원이다.

## 6.3  배열 수정(갱신)하기

배열의 앞 쪽을 새로운 값으로 배꿔야 할 때가 종종 있다. 그것을 선택된 위치를 '갱신' 또는 '수정'한다고 한다. 배열을 수정 하기 위한 J함수는 `}`(right brace라고 하고 "Amend"라고 부른다.)이다.

### 6.3.1 인덱스로 수정하기

배열을 수정하기 위해선 세 가지가 필요하다.

- 원본 배열
- 원본 배열에서 수정해야 할 특정한 위치. 이 위치는 위에서 봤듯이다 `{`로 선택 할 수 있는 인덱스이다.
- 특정 위치의 값을 대체할 새로운 값

결과적으로 수정하기 위한 J 표현식의 일반적인 형태는 다음과 같다.

	        newvalues index } original

리스트 `L`의 첫 번째 아이템(인덱스가 `0`인 곳)을 '*'로 치환하는 예를 보자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>new=:'*'</TT></TD>
<TD><TT>index=:0</TT></TD>
<TD><TT>new index } L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>*</TT></TD>
<TD><TT>0</TT></TD>
<TD><TT>*bcdef</TT></TD>
</TABLE>

`}`는 `index`를 취해서 수정용 다이아딕 동사인 `index }`를 만드는 부사이다.

	   ReplaceFirst =: 0 }
	   '*' ReplaceFirst L
	*bcdef

`index }`는 다른 동사와 마찬가지로 다이아딕도 있고 값을 내놓기도한다. 그러므로 배열을 수정하기 위해선 전체 결과를 이전 이름에 재할당해야한다. 따라서 보통 수정은 아래와 같은 패턴을 가진다.

	                 A  =:  new index } A 

J 시스템은 데이터의 불필요한 이동을 없애서 효과적으로 계산하도록 되어있다.

예로 테이블의 1행 2열을 수정해보자

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT> '*' (< 1 2) } A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>abc<BR>
de*</TT></TD>
</TABLE>

여러 요소들을 수정하려면 새로운 값들이 리스트로 입력되어야 한다. 그러면 인덱스에 의해 선택된 값의 리스트를 새로운 값으로 치환한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> L</TT></TD>
<TD><TT> '*#' 1 2 } L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>a*#def</TT></TD>
</TABLE>

### 6.3.2 동사로 수정하기

`Y`를 숫자의 리스트라고 하자. 이 리스트에서 `X`를 넘어가는 값은 전부 `X`로 바꾸려 한다. (이 예제에서는 `<.`를 사용하지 않기로 한다.)

`Y`를 수정하기 위한 인덱스들은 `X`를 이용해 계산되어야만 한다. 아래에 이 인덱스를 계산하는 함수 `f`가 있다.

	   f =: 4 : '(y > x) # (i. # y)'
	   

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X =: 100</TT></TD>
<TD><TT>Y =: 98 102 101 99</TT></TD>
<TD><TT>Y > X</TT></TD>
<TD><TT>X f Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>100</TT></TD>
<TD><TT>98 102 101 99</TT></TD>
<TD><TT>0 1 1 0</TT></TD>
<TD><TT>1 2</TT></TD>
</TABLE>

이제 다음 예제를 보면 `X f Y`를 수행해서 뽑아낸 인덱스로 수정을 마쳤다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>Y</TT></TD>
<TD><TT>X (X f Y) } Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>98 102 101 99</TT></TD>
<TD><TT>98 100 100 99</TT></TD>
</TABLE>

부사 `}`인 "Amend"는 표현식 `X (X f Y) } Y`를 짧게 `X f } Y`로 쓸 수 있다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X (X f Y) } Y</TT></TD>
<TD><TT>X f } Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>98 100 100 99</TT></TD>
<TD><TT>98 100 100 99</TT></TD>
</TABLE>

Since `}` is an adverb, it can acceptas argument either the indices `(X f Y)` or the verb `f`.
`}`가 부사이기 때문에, 인자로 인덱스인 `X f Y`나 함수 `f`를 다 취할 수 있다.

	   cap =: f }
	   
	   10 cap 8 9 10 11
	8 9 10 10

만약 동사 `f`를 `}`의 인자로 사용한다면 `X`나 `Y`가 없더라도 `f`는 다이아드로 이용된다. 

### 6.3.3 선형 인덱스
 
지금까지는 동사로 수정하는 방법을 봐왔다. 동사는 수정할 위치를 찾아내기 위해 쓰였다. 즉 인덱스 리스트의 값을 계산해서 수정할 곳의 위치를 계산했다. 리스트가 아닌 테이블을 수정한다면 인덱스는 2차원이 된다. 그리고 동사로 인덱스를 만들기는 좀 더 어려워 진다. 테이블을 선형 리스트로 만들어 리스트로 수정하는 방법이 있다. 그리고 수정한 리스트를 다시 테이블로 만든다.

예를 들어 아래와 같은 테이블을 가지고 있다고 하자.

	   M =: 2 2 $ 13 52 51 14

그럼 우리의 친구 인덱스를 찾는 동사 `f`를 이용해서 평평하게 펴고, 수정한 다음에 다시 테이블로 만드는 것을 해보자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>M</TT></TD>
<TD><TT>LL =: ,M</TT></TD>
<TD><TT>Z =: 50 f } LL</TT></TD>
<TD><TT> ($M) $ Z</TT></TD>
<TR VALIGN=TOP>
<TD><TT>13 52<BR>
51 14</TT></TD>
<TD><TT>13 52 51 14</TT></TD>
<TD><TT>13 50 50 14</TT></TD>
<TD><TT>13 50<BR>
50 14</TT></TD>
</TABLE>

하지만 더 좋은 방법이 있다. 우선 동사 `f`가 `M`이 아니라 `LL =: , M`을 인자로 받았다는 것에 주목하자. 따라서 `f`은 `M`의 원래 모양에 대한 정보를 알 수 없다. 이 예제에서 그건 문제가 안된다. 하지만 일반적으로 `M`의 모양과 값에 맞는 인덱스를 찾기 원한다. 그럼 `f`가 `M`을 고스란히 인자로 받으면 되겠다. 이 경우에 `f`는 알아서 평평하게 펴줘야 한다. 따라서 `f`를 재정의 할 필요가 있다.

	   f =: 4 : 0
	y =. , y
	(y > x) # (i. # y)
	)
	   
 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>M</TT></TD>
<TD><TT>50 f M</TT></TD>
<TR VALIGN=TOP>
<TD><TT>13 52<BR>
51 14</TT></TD>
<TD><TT>1 2</TT></TD>
</TABLE>

이제 인덱스를 찾는 동사 `f`는 인자로 하나의 배열을 받고 인덱스들을 평평한 배열(이걸 "선형 인덱스"라고 한다)에 넣는다. 프로세스를 수정해서 새로운 `f`를 만들자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>M</TT></TD>
<TD><TT>($M) $ 50 (50 f M) } (, M)</TT></TD>
<TR VALIGN=TOP>
<TD><TT>13 52<BR>
51 14</TT></TD>
<TD><TT>13 50<BR>
50 14</TT></TD>
</TABLE>

최종적으로 `f`는 선형 인덱스를 만들고 `}`을 이용해 위의 마지막 표현식을 다음과 같이 짧게 표현할 수 있다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>M</TT></TD>
<TD><TT>50 f } M</TT></TD>
<TR VALIGN=TOP>
<TD><TT>13 52<BR>
51 14</TT></TD>
<TD><TT>13 50<BR>
50 14</TT></TD>
</TABLE>

## 6.4 트리 인덱스

지금까지는 사각형의 배열을 인덱싱해왔다. 이제 부터는 "트리"로 추상화 할 수 있는 박스 구조를 인덱싱 해보자. 트리는 가지와 잎으로 이루어져있다. 아래 예제를 보자.

	   branch =: <
	   leaf   =: <
	   
	   branch0 =: branch (leaf 'J S'),(leaf 'Bach')
	   branch1 =: branch (leaf 1), (leaf 2), (leaf 1777)
	   tree    =: branch0,branch1
	   tree
	+----------+----------+
	|+---+----+|+-+-+----+|
	||J S|Bach|||1|2|1777||
	|+---+----+|+-+-+----+|
	+----------+----------+

루트에서 부터의 특정 경로를 이용하면 트리에서 데이터를 꺼낼 수 있다. 동사 `{::`(left-brace colon colon, "Fetch"라고 한다.)의 왼쪽에 오는 인자는 경로로 선택의 시퀀스라고 할 수 있다. 경로 `0`은 첫 번째 가지를 꺼내온다. `0;1`은 첫 번째 가지의 두 번째 잎을 꺼내온다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>0 {:: tree</TT></TD>
<TD><TT>(0;1) {:: tree</TT></TD>
<TR VALIGN=TOP>
<TD><TT>+---+----+<BR>
|J S|Bach|<BR>
+---+----+</TT></TD>
<TD><TT>Bach</TT></TD>
</TABLE>

모나딕 형태인 `{:: tree`는 `tree`의 "Map"이라고 부른다. 이 표현식은 `tree`와 같은 형태의 박스 구조를 반환하고 반환된 값은 각 잎을 선택하는 경로를 담고 있다.

	   {:: tree
	+-------------+-------------------+
	|+-----+-----+|+-----+-----+-----+|
	||+-+-+|+-+-+|||+-+-+|+-+-+|+-+-+||
	|||0|0|||0|1|||||1|0|||1|1|||1|2|||
	||+-+-+|+-+-+|||+-+-+|+-+-+|+-+-+||
	|+-----+-----+|+-----+-----+-----+|
	+-------------+-------------------+

챕터 6이 끝났다.