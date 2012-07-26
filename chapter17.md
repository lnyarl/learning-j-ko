# Chapter 17: 어플리케이션 패턴

이 챕터에서는 배열에 함수를 적용시켜 배열의 엘리먼트를 선택하는 여러가지 방법에 대해 알아볼 것이다.

## 17.1 스캔(Scanning)

### 17.1.1 프리픽스 스캔(Prefix Scanning)

표현식 `f \ y` 연속적으로 y의 앞쪽 부분(프리픽스)을 점점 늘려가며 그 부분에 f를 적용시킨다. f로 박스 동사(`<`)를 쓰면 결과를 보기쉽게 가시화 할 수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>y =: 'abcde'</tt></td>
<td><tt>&lt; \ y</tt></td>
</tr><tr valign="TOP">
<td><tt>abcde</tt></td>
<td><tt>+-+--+---+----+-----+<br>
|a|ab|abc|abcd|abcde|<br>
+-+--+---+----+-----+</tt></td>
</tr></tbody></table>

숫자 벡터의 누적 합(Cumulative sums)도 계산할 수 있다.

      +/ \ 0 1 2 3
    0 1 3 6

비트 벡터를 스캐닝하면 다양한 효과를 낼 수 있다. 아래 예제는 "cumulative OR"이다. "cumulative OR"는 제일 처음 비트 다음의 모든 비트를 1로 세팅한다.

      +./\ 0 1 0 1 0
    0 1 1 1 1

### 17.1.2 인픽스 스캐닝(Infix Scanning)

표현식 `x f \ y`는 y를 연속적으로 길이 x로 잘라 각 부분에 f를 적용시킨다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>z =: 1 4 9 16</tt></td>
<td><tt>2 &lt; \ z</tt></td>
</tr><tr valign="TOP">
<td><tt>1 4 9 16</tt></td>
<td><tt>+---+---+----+<br>
|1 4|4 9|9 16|<br>
+---+---+----+</tt></td>
</tr></tbody></table>

만약 x가 음수라면 각 부분이 겹치지 않는다. 그리고 이 경우 마지막 섹션이 온전한 길이가 되지 않을 수도 있다. 아래 예제를 보자

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>z</tt></td>
<td><tt>_3 &lt; \ z</tt></td>
</tr><tr valign="TOP">
<td><tt>1 4 9 16</tt></td>
<td><tt>+-----+--+<br>
|1 4 9|16|<br>
+-----+--+</tt></td>
</tr></tbody></table>

잘리는 부분의 길이(`x`)를 2로 하고 각 부분에 동사(`f`) "두 번째 빼기 첫 번째",`{: - {.`,를 적용하면 연속된 아이템 사이의 차이도 구할 수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>smf =: {: - {.</tt></td>
<td><tt>smf 1 4</tt></td>
</tr><tr valign="TOP">
<td><tt>{: - {.</tt></td>
<td><tt>3</tt></td>
</tr></tbody></table>

      diff =: 2 & (smf\)

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>,. z</tt></td>
<td><tt>,. diff z</tt></td>
<td><tt>,. diff diff z</tt></td>
</tr><tr valign="TOP">
<td><tt> 1<br>
 4<br>
 9<br>
16</tt></td>
<td><tt>3<br>
5<br>
7</tt></td>
<td><tt>2<br>
2</tt></td>
</tr></tbody></table>

### 17.1.3 서픽스 스캔(Suffix Scanning)

표현식 `f \. y`는 y의 뒷 부분(Suffix)을 연속적으로 짧게 잘라 각 부분에 f를 적용시킨다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>y </tt></td>
<td><tt>&lt; \. y</tt></td>
</tr><tr valign="TOP">
<td><tt>abcde</tt></td>
<td><tt>+-----+----+---+--+-+<br>
|abcde|bcde|cde|de|e|<br>
+-----+----+---+--+-+</tt></td>
</tr></tbody></table>

### 17.1.4 아웃픽스(Outfix)

표현식 `x f \. y`는 y 전체에서 연속적으로 부분들은 제거하면서 f를 적용한다. 제거는 x의 길이 만큼 제거한다. 만약 x가 음수라면 제거하는 부분은 겹치지 않는다. 여기서도 마지막으로 제거되는 부분은 온전한 길이가 아닐 수 있다. 이해를 빠르게 하기 위해 예제를 보자.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>y  </tt></td>
<td><tt>2 &lt; \. y </tt></td>
<td><tt>_2 &lt; \. y    </tt></td>
</tr><tr valign="TOP">
<td><tt>abcde</tt></td>
<td><tt>+---+---+---+---+<br>
|cde|ade|abe|abc|<br>
+---+---+---+---+</tt></td>
<td><tt>+---+---+----+<br>
|cde|abe|abcd|<br>
+---+---+----+</tt></td>
</tr></tbody></table>

## 17.2 자르기(Cutting)

접속사 `;.`(semicolon dot)은 "Cut"이라고 한다. 만약 u가 동사이고 n이 작은 정수이면 `u ;. n`은 u를 n에 따라 다양한 패턴으로 적용하는 동사가 된다. n에는 _3 _2 _1 0 1 2 3이 가능하다. 이들 중 일부만 살펴보자.

### 17.2.1 역전(reversing)

표현식 `u ;. 0 y`은 y의 모든 축을 따라 역순으로 u를 적용시킨다. 아래 예제에서 우리는 u로 `[`를 선택했다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>M =: 3 3 $ 'abcdefghi' </tt></td>
<td><tt>[ ;. 0 M</tt></td>
</tr><tr valign="TOP">
<td><tt>abc<br>
def<br>
ghi</tt></td>
<td><tt>ihg<br>
fed<br>
cba</tt></td>
</tr></tbody></table>

### 17.2.2 블로킹(Blocking)

주어진 배열에서 더 작은 서브 배열을 꺼내어 그 서브 배열에 동사를 적용시킨다.
서브 배열은 2열의 테이블을 이용해 만들 수 있다. 첫 째 열은 서브 배열의 첫 번째 아이템을 가리키는 인덱스가 들어있고, 둘 째 열에는 서브 배열의 모양이 들어있다. 

예를 들어서 원래 배열의 1행 1열에서 시작하여 2 2 의 모양을 하고 있는 서브 배열은 아래와 같이 쓸 수 있다.

      spec =: 1 1 ,: 2 2

그럼 이제 다음 예제 처럼 identity 동사인 `[`를 특정 서브 배열에 적용할 수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>M   </tt></td>
<td><tt>spec</tt></td>
<td><tt>spec [ ;. 0 M</tt></td>
</tr><tr valign="TOP">
<td><tt>abc<br>
def<br>
ghi</tt></td>
<td><tt>1 1<br>
2 2</tt></td>
<td><tt>ef<br>
hi</tt></td>
</tr></tbody></table>

동사 u의 일반적인 구조는 표현식 `x u ;. 0 y`는 동사 u를 x에 의해 만들어진 y의 서브 배열에 적용하는 것 이다. 서브 배열을 만드는 x에서 두 번째 열인 모양 부분이 음수이면 M의 엘레먼트가 연관된 축을 따라 반전된다. 예들 들자면 아래와 같다.

      spec =: 1 1 ,: _2 2

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>M   </tt></td>
<td><tt>spec</tt></td>
<td><tt>spec [ ;. 0 M</tt></td>
</tr><tr valign="TOP">
<td><tt>abc<br>
def<br>
ghi</tt></td>
<td><tt> 1 1<br>
_2 2</tt></td>
<td><tt>hi<br>
ef</tt></td>
</tr></tbody></table>

### 17.2.3 플렛(Fretting)

한 줄의 텍스트를 단어 단위로 자른다고 해보자. 예제로 다음과 같은 문자열이 있다.

      y =: 'what can be said'

잠깐, 그 전에 공백문자로 끝나야 단어다 라고 정의하자. 위의 y에서 마지막 단어 'said'를 보면 공백 문자로 끝나지 않는다. 그래서 우선 제일 끝에 공백을 추가해주자.

      y =: y , ' '

이제 u가 동사이고 y가 공백으로 끝난다면 표현식 `u ;. _2 y`는 y를 공백을 기준으로 잘라 각각에 동사 u를 적용한다. 예를 들어서 y의 단어에 박스 함수인 `<,`를 적용할 수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>y  </tt></td>
<td><tt>&lt; ;. _2 y</tt></td>
</tr><tr valign="TOP">
<td><tt>what can be said </tt></td>
<td><tt>+----+---+--+----+<br>
|what|can|be|said|<br>
+----+---+--+----+</tt></td>
</tr></tbody></table>

또 동사 `#`를 이용해 각 단어의 글자수를 셀 수 도 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>y </tt></td>
<td><tt> # ;. _2 y</tt></td>
</tr><tr valign="TOP">
<td><tt>what can be said </tt></td>
<td><tt>4 3 2 4</tt></td>
</tr></tbody></table>

`;,`의 오른쪽 인자인 _2의 의미는 '단어는 y의 마지막 문자로 끝난다.(여기선 공백문자)'이다. 단어는 공백문자를 포함하지 않는다.

좀 더 일반적으로, "플랫(fret)"을 기준으로 반복적으로 리스트를 자른다고 할 수 있다. `;.`의 오른쪽 인자인 n은 플렛과 반복 주기를 정한다. 아래에 네 가지 경우가 있다.

 <table cellpadding="10" border="1"> 
<tbody><tr> <td> <tt>  n = 1 </tt></td> 
     <td>플랫으로 한 주기가 시작한다. <tt>y</tt>의 첫번째 아이템을 플랫으로 하고 다른 아이템들을 플랫을 기준으로 자른다. 
          <br/>각 주기는 플랫을 포함한다.
          </td> </tr>
<tr> <td> <tt>  n = _1  </tt> </td> 
     <td> <tt>n = 1</tt>이면 각 주기는 플랫을 포함하지 않는다.</td></tr>
<tr> <td> <tt>  n = 2  </tt> </td> 
     <td> 각 주기는 플랫을 뒤에 둔다. y의 가장 마지막 아이템이 플랫으로 결정되고 y는 플랫을 기준으로 잘린다.<br/>각 주기는 플랫을 포함한다.
<tr> <td> <tt>  n = _2  </tt> </td> 
     <td> <tt>n = 2 </tt>이면 각 주기가 플랫을 포함하지 않는다.</td> </tr>
</tbody></table>

예를 들어서 네 경우를 아래 문자열에 대입해보자.

      z =: 'abdacd' 
   
 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>z </tt></td>
<td><tt>&lt; ;. 1 z</tt></td>
<td><tt>&lt; ;. _1 z</tt></td>
<td><tt>&lt; ;. 2 z</tt></td>
<td><tt>&lt; ;. _2 z</tt></td>
</tr><tr valign="TOP">
<td><tt>abdacd</tt></td>
<td><tt>+---+---+<br>
|abd|acd|<br>
+---+---+</tt></td>
<td><tt>+--+--+<br>
|bd|cd|<br>
+--+--+</tt></td>
<td><tt>+---+---+<br>
|abd|acd|<br>
+---+---+</tt></td>
<td><tt>+--+--+<br>
|ab|ac|<br>
+--+--+</tt></td>
</tr></tbody></table>

다른 예로 테이블에 숫자를 넣는 방법에 대해서 보자. 우선 테이블에 `0 : 0`뒤에 한 행, 한 행 써서 숫자를 넣는다.

         T =: 0 : 0
     1   2  3
     4   5  6
    19  20 21
    )
   
T는 개행 문자가 3개인 문자열이다. 각 라인의 끝에 개행 문자가 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>$ T</tt></td>
<td><tt>+/ T = LF</tt></td>
</tr><tr valign="TOP">
<td><tt>30</tt></td>
<td><tt>3</tt></td>
</tr></tbody></table>

이제 T를 라인 단위로 자를 생각이다. 각 라인은 J 표현식로써의 문자열이다.(예를 들어 문자열 '1 2 3') 그런 문자열은 동사 `".`(double-auote dot, "Do"나 "Execute"라고 한다)를 이용해서 실제로 평가 할 수 있다. 그 결과, 각 라인이 숫자 3개를 포함하는 리스트가 나온다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>TABLE =: (". ;. _2) T</tt></td>
<td><tt>$ TABLE</tt></td>
</tr><tr valign="TOP">
<td><tt> 1&nbsp;&nbsp;2&nbsp;&nbsp;3<br>
 4&nbsp;&nbsp;5&nbsp;&nbsp;6<br>
19 20 21</tt></td>
<td><tt>3 3</tt></td>
</tr></tbody></table>

동사 `". ;. _2`는 챕터2에서 유틸리티 함수인 ArrayMaker로 한 번 소개되었었다.

### 17.2.4 구두점

단어를 공백 문자나 여러가지 구두점등으로 끝난다고 간주하면 텍스트 처리를 하기가 편하다. 플렛을 네 개의 문자로 이루어진 문자열이라고 해보자.

      frets =: ' ?!.'

우리는 어떤 문자열이 주어지면 그 문자열에서 플랫의 위치를 '참'으로 표시하는 비트 벡터를 구할 수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>t =: 'How are you?'</tt></td>
<td><tt>b =: t e. frets</tt></td>
</tr><tr valign="TOP">
<td><tt>How are you?</tt></td>
<td><tt>0 0 0 1 0 0 0 1 0 0 0 1</tt></td>
</tr></tbody></table>

내장 동사인 `e.`("Member")로 간단히 구했다. 표현식 `x e. y`는 만약 `x`가 리스트 `y`의 멤버일 때 참이다 라고 평가한다.

이제 비트 벡터 b를 문자열 t를 단어 단위로 자를 플랫으로 사용할 수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>t</tt></td>
<td><tt>b</tt></td>
<td><tt>b &lt; ;. _2 t</tt></td>
</tr><tr valign="TOP">
<td><tt>How are you?</tt></td>
<td><tt>0 0 0 1 0 0 0 1 0 0 0 1</tt></td>
<td><tt>+---+---+---+<br>
|How|are|you|<br>
+---+---+---+</tt></td>
</tr></tbody></table>

또다른 예로 순열을 오름차순을 한 주기로 자른다고 하자. 즉 한 아이템이 이전 아이템보다 작은 숫자면 새로운 주기가 시작되는 것이다. 아래 데이터가 있다.

      data =: 3 1 4 1 5 9

그럼 데이터를 길이가 2인 인픽스로 스캔을 하고 그 한 쌍의 아이템에 `>/`를 적용하면 비트벡터를 얻을 수 있다. 만약 결과가 1이면 한 쌍의 아이템에서 두번째 아이템이 새로운 주기의 시작점이 된다. 그 주기의 첫번째 아이템은 1이어야 한다.

        bv =: 1 , 2 >/ \ data 

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>data</tt></td>
<td><tt>data ,: bv</tt></td>
<td><tt>bv &lt; ;. 1 data</tt></td>
</tr><tr valign="TOP">
<td><tt>3 1 4 1 5 9</tt></td>
<td><tt>3 1 4 1 5 9<br>
1 1 0 1 0 0</tt></td>
<td><tt>+-+---+-----+<br>
|3|1 4|1 5 9|<br>
+-+---+-----+</tt></td>
</tr></tbody></table>

### 17.2.5 단어 형식화(Word Formation)

내장 함수로 `;:`(semicolon colon, "Word Formation"이라고 부름)라는 것이 있다. 이 함수는 문자열을 J 표현식으로 분석해서 표현식의 각 요소들을 나눠 박스에 담긴 문자열의 리스트로 보여준다.
예를 들자면 다음과 같다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>y =: 'z =: (p+q) - 1'</tt></td>
<td><tt>;: y</tt></td>
</tr><tr valign="TOP">
<td><tt>z =: (p+q) - 1</tt></td>
<td><tt>+-+--+-+-+-+-+-+-+-+<br>
|z|=:|(|p|+|q|)|-|1|<br>
+-+--+-+-+-+-+-+-+-+</tt></td>
</tr></tbody></table>

### 17.2.6 파일의 라인

아래 예제를 따라 파일을 하나 만들어보자. (파일 처리를 위한 함수에 대해 자세한 것을 알고 싶다면 26장을 보라)

      text =: 0 : 0
    What can be said
    at all
    can be said
    clearly.
    )
      
      text (1 !: 2) < 'foo.txt'
   
이제 파일을 라인 단위로 잘라보자. 그럼 우선 파일을 읽어서 문자열 변수에 넣고, 그 문자열을 잘라야 한다. 각 라인은 line-terminating 문자로 끝난다고 가정하면 파일의 마지막 문자를 플랫으로 쓸 수 있다. 아래에 예제가 있다.


      string =: (1 !: 1) < 'foo.txt'  NB. 파일을 읽는다.
      
      lines =: (< ;. _2) string          NB. 라인 단위로 자른다.
      
      lines
    +----------------+------+-----------+--------+
    |What can be said|at all|can be said|clearly.|
    +----------------+------+-----------+--------+
   
파일을 라인별로 자를때 알아두어야 할 것이 두 가지 있다.
첫째로 몇몇 시스템에선 줄의 끝에 라인-피드(line-feed, LF) 문자 하나가 있는가 하면, 또 다른 시스템에선 각 라인이 라인-피드 다음에 캐리지-리턴(carriage-return, CR)이 오는 형태로 두 문자가 있기도 한다.

J에서는 시스템에 관계없이 LF 문자 하나만 사용한다. 하지만 입력 데이터에 CR이 존재 할 수 있기 때문에 그에 대한 대비가 필요하다. 문자열에서 CR 문자를 없애려면 비트 벡터에 '문자열 notequal CR'을 사용할 수 있다. notequal은 내장 함수로 `~:`의 모양이다. 이는 아래와 같이 쓴다.

      string =: (string ~: CR) # string
   
둘째로 파일이 어떻게 만들어졌느냐에 따라 마지막 라인이 실제로 끝났는지 보장하지 못할 수 있다. 그래서 필요 하다면 LF 문자를 문자열의 마지막에 붙여서 사용해야한다.
플랫을 붙이고 CR문자를 없애 간단히 문자열을 정리하는건 아래와 같이 쓸 수 있다.

      tidy =: 3 : 0
    y =. y , (LF ~: {: y) # LF   NB. LF를 붙인다.
    (y ~: CR) # y                 NB. CR을 제거한다.
    )
      
      (< ;. _2) tidy string 
    +----------------+------+-----------+--------+
    |What can be said|at all|can be said|clearly.|
    +----------------+------+-----------+--------+
   
### 17.2.7 타일(Tiling)

표현식 `x u ;. 3 y`에서 동사 u는 y에서 탄생한 부분 배열들 각각에 적용된다. 그 부분 배열들은 타일이라 부른다. 타일의 크기와 배열은 x에 의해 정해진다. 아래 예제가 있다. y를 다음과 같다고 하자.

      y =: 4 4 $ 'abcdefghijklmnop'

그리고 우리가 만들 타일은 모양이 '2 2'이다. 각 타일은 각 축에 대해 바로 옆의 타일보다 2만큼 떨어져 있다.

      spec =: > 2 2 ; 2 2  NB.  오프셋, 모양

그리고 나서 보자

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>y </tt></td>
<td><tt>spec</tt></td>
<td><tt>spec &lt; ;. 3 y</tt></td>
</tr><tr valign="TOP">
<td><tt>abcd<br>
efgh<br>
ijkl<br>
mnop</tt></td>
<td><tt>2 2<br>
2 2</tt></td>
<td><tt>+--+--+<br>
|ab|cd|<br>
|ef|gh|<br>
+--+--+<br>
|ij|kl|<br>
|mn|op|<br>
+--+--+</tt></td>
</tr></tbody></table>

특정 타일은 가장자리에서 파편화 되 불완전한 조각이 될 수도 있다. 파편은 "Cut"의 오른쪽 인자에 3이나 _3을 주어서 결과에 포함하거나 제거할 수 있다.

      sp =: > 3 3 ; 3 3

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>y </tt></td>
<td><tt>sp</tt></td>
<td><tt>sp &lt; ;. 3 y</tt></td>
<td><tt>sp &lt; ;. _3 y</tt></td>
</tr><tr valign="TOP">
<td><tt>abcd<br>
efgh<br>
ijkl<br>
mnop</tt></td>
<td><tt>3 3<br>
3 3</tt></td>
<td><tt>+---+-+<br>
|abc|d|<br>
|efg|h|<br>
|ijk|l|<br>
+---+-+<br>
|mno|p|<br>
+---+-+</tt></td>
<td><tt>+---+<br>
|abc|<br>
|efg|<br>
|ijk|<br>
+---+</tt></td>
</tr></tbody></table>

17장이 끝났다.
