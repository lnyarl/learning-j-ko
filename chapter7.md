# 7 장: 랭크

한 배열의 랭크가 차원의 갯수라는 것을 기억하는가? 스칼라는 랭크가 0이고 리스트는 랭크가 1, 테이블은 랭크가 2 인 식이다.

이 장의 주제는 랭크가 어떻게 함수에 인자로 사용되는지에 대한 것이다.

## 7.1 랭크 접속사

우선 몇가지 용어에 대해 알아보자. 배열은 셀로 나뉘어 있는데 이는 여러 방법으로 해석 할 수 있다. 다음과 같은 테이블을 보자. 

	   M =: 2 3 $ 'abcdef'
	   M
	abc
	def

이것은 랭크 0의 셀이 6개로 나뉘어져있다고 할수도 있고, 랭크 1의 두 셀로 나뉘어 있다고 할 수도 있고, 랭크 2의 셀 하나라고 볼 수도 있다. k의 랭크를 가지는 한 셀은 k-셀 이라고 부른다.

### 7.1.1 모나딕 동사

박스 동사(모나드 <)는 인자의 랭크가 무엇이든 전체를 하나의 박스로 만든다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L =: 2 3 4 </TT></TD>
<TD><TT>< L </TT></TD>
<TD><TT>M </TT></TD>
<TD><TT> < M</TT></TD>
<TR VALIGN=TOP>
<TD><TT>2 3 4</TT></TD>
<TD><TT>+-----+<BR>
|2 3 4|<BR>
+-----+</TT></TD>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>+---+<BR>
|abc|<BR>
|def|<BR>
+---+</TT></TD>
</TABLE>

하지만 박스로 만들 셀을 지정할 수도 이다. 접속사 `"`를 이용하면 된다.  `< " 0`라고 적으면 각 스칼라, 즉 0-셀을 박스에 담는다. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>M </TT></TD>
<TD><TT>< " 0 M </TT></TD>
<TD><TT>< " 1 M </TT></TD>
<TD><TT>< " 2 M</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>+-+-+-+<BR>
|a|b|c|<BR>
+-+-+-+<BR>
|d|e|f|<BR>
+-+-+-+</TT></TD>
<TD><TT>+---+---+<BR>
|abc|def|<BR>
+---+---+</TT></TD>
<TD><TT>+---+<BR>
|abc|<BR>
|def|<BR>
+---+</TT></TD>
</TABLE>

일반적인 구조는 `u " k y` 형태의 표현식으로, 모나딕 동사 `u`는 `y`의 각 `k`-cell에 적용된다.

배열에서 각 k-cell을 박스로 감싸서 확인해볼 수 있는 동사를 정의하자.

	   cells  =: 4 : '< " x y'

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>M   </TT></TD>
<TD><TT>0 cells M</TT></TD>
<TD><TT>1 cells M</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>+-+-+-+<BR>
|a|b|c|<BR>
+-+-+-+<BR>
|d|e|f|<BR>
+-+-+-+</TT></TD>
<TD><TT>+---+---+<BR>
|abc|def|<BR>
+---+---+</TT></TD>
</TABLE>

### 7.1.2 다이아딕 동사

주어진 테이블에서 어떻게 하면 각 행에 서로 다른 숫자를 곱할 수 있을까? 동사 `* " 1 0`을 이용하면 된다. 이 동사는 "1-cell들을 0-cell과 곱한다"라고 읽으면 된다. 아래의 예를 보자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X =: 2 2 $ 0 1 2 3</TT></TD>
<TD><TT>Y =: 2 3</TT></TD>
<TD><TT>X (* " 1 0) Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>0 1<BR>
2 3</TT></TD>
<TD><TT>2 3</TT></TD>
<TD><TT>0 2<BR>
6 9</TT></TD>
</TABLE>

일반적인 구조는 아래의 표현식과 같다.

	                X (u " (L,R)) Y 

이 식은 다이아드 `u`를 `X`의 L-cell 하나와 그와 관련된 `Y`의 R-cell 하나를 양쪽 인자로 하여 적용시킨다는 의미이다. 각 열을 서로 다른 숫자들과 곱하려면 `x`의 1-cell과 `y`의 독립된 1-cell을 결합한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X</TT></TD>
<TD><TT>Y</TT></TD>
<TD><TT>X (* " 1 1) Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>0 1<BR>
2 3</TT></TD>
<TD><TT>2 3</TT></TD>
<TD><TT>0 3<BR>
4 9</TT></TD>
</TABLE>

## 7.2 고유한 랭크

J에서 모든 동사는 자신이 받는 인자에 대해 고유하다고 할 수 있는 랭크가 있다. 아래에 예제를 준비했다. 첫 번째 예제를 보자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>  *: 2 </TT></TD>
<TD><TT>  *: 2 3 4 </TT></TD>
<TR VALIGN=TOP>
<TD><TT>4</TT></TD>
<TD><TT>4 9 16</TT></TD>
</TABLE>

여기 산술 함수인 "square"는 당연히 단일 숫자(0-cell)에 적용되었다. 랭크-1의 배열(리스트)이 인자로 들어온다면 이 함수는 인자의 각 0-cell에 따로 적용된다. 다른 말로 하자면 모나딕 `*:`의 고유한 랭크는 0이다 라고 한다. 다른 예로 내장 동사인 `#.`(hash dot. "Base Two"라고 한다)이 있다. 이 동사는 이진수를 나타내는 한 줄의 비트 스트링을 인자로 받는다. 그리고 이 숫자의 값을 계산해서 내놓는다. 예를 들어 `1 0 1`이 인자로 들어가면 결과로 `5`가 나온다.

	   #. 1 0 1
	5

동사 `#.`은 자연스럽게 비트의 리스트에 적용된다. 즉 1-cell에 적용된다. 만약 랭크가 2인 배열(즉, 테이블)이 인자로 들어오면 이 동사는 각 1-cell에 적용될 것이다. 즉 테이블의 각 행에 적용된다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>t =: 3 3 $ 1 0 1 0 0 1  0 1 1</TT></TD>
<TD><TT>#. t</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 0 1<BR>
0 0 1<BR>
0 1 1</TT></TD>
<TD><TT>5 1 3</TT></TD>
</TABLE>

따라서 모나딕 `#.`의 고유한 랭크는 `1`이다.

세 번째 예로, 이미 알고 있듯이, 모나딕 `<`은 인자의 랭크가 무엇이든 간에 인자 전체에 한 번 적용된다. 따라서 `<`의 고유한 랭크는 정의되지 않은 큰 수, 즉 무한대이다. 무한대는 _ 라고 쓴다. 이 예제들은 모나딕 동사의 경우만을 다뤘다. 모든 다이아딕 동사 또한 똑같이 양쪽 인자에 대해 두 개의 고유한 랭크를 가진다. 예를 들어 다이아딕 `+`의 고유한 랭크는 `0 0`이다. `+`는 왼쪽과 오른쪽의 인자에서 숫자 하나(rank-0)씩에 적용되기 때문이다. 일반적으로 동사는 모나딕과 다이아딕으로 사용할 수 있고 따라서 총 3개의 랭크를 가진다. 이것을 "고유한 랭크"라고 한다.

내장 부사인 `b.`(소문자 b dot, "Basic Characteristics"라고 한다.)를 이용해 동사의 고유한 랭크를 알아낼 수 있다. 임의의 동사 `u`에 대해서 표현식 `u b. 0`은 모나딕, 왼쪽, 오른쪽의 순서로 동사 `u`의 랭크를 보여준다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> *: b. 0</TT></TD>
<TD><TT>#. b. 0</TT></TD>
<TD><TT> < b. 0</TT></TD>
<TR VALIGN=TOP>
<TD><TT>0 0 0</TT></TD>
<TD><TT>1 1 1</TT></TD>
<TD><TT>_ 0 0</TT></TD>
</TABLE>

For convenience, the rank conjunction  `"` can accept a right argument consisting of a single rank (for a monad) or two ranks(for a dyad) or three ranks (for an ambivalent verb). 
편리함을 위해 랭크 접속사 `"`는 오른쪽 인자로 하나의 랭크(모나드)나 두 개(다이아드), 또는 세 개(두 경우 전부 동사)의 랭크를 가질 수 있다.
-----------------------이게 뭔말이

One rank or two are automatically expanded to three as shown by: 
하나 또는 두 개의 랭크는 자동으로 세 개로 늘어난다. 아래를 보자.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>(<"1) b. 0</TT></TD>
<TD><TT>(<"1 2) b. 0</TT></TD>
<TD><TT>(<"1 2 3) b. 0</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 1 1</TT></TD>
<TD><TT>2 1 2</TT></TD>
<TD><TT>1 2 3</TT></TD>
</TABLE>

## 7.3 프레임

`u`가 테이블의 모든 수를 더하는 동사라고 하자. 수를 더하는데 우선 열 들을 다 더하고 그 결과를 다시 하나의 수로 더한다. 아래에 모나딕 랭크 2를 가지는 `u`를 정의했다.

	   u =: (+/) @: (+/) " 2

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>w =: 4 5 $ 1</TT></TD>
<TD><TT>u w</TT></TD>
<TD><TT>u b. 0</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 1 1 1 1<BR>
1 1 1 1 1<BR>
1 1 1 1 1<BR>
1 1 1 1 1</TT></TD>
<TD><TT>20</TT></TD>
<TD><TT>2 2 2</TT></TD>
</TABLE>

`2 3 4 5`의 모양을 가진 4 차원 배열 `A`가 있다.

	   A =: 2 3 4 5 $  1  

`A`를 2-셀을 가진 2행 3열의 배열이고 각 셀은 4행 5열의 배열로 볼 수 있다. 이제 `u A`를 계산해보자. 동사 `u`는 랭크 2를 가지고 있다. 이 동사는 `A`의 각 셀에 따로 적용되고, 결과로 2행 3열의 배열을 내놓을 것이다.

각각의 결과는 스칼라이고(왜냐면 `u`가 스칼라를 만들기 때문이다) 따라서 전체 결과는 2행 3열의 스칼라 배열이다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>u A</TT></TD>
<TD><TT>$ u A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>20 20 20<BR>
20 20 20</TT></TD>
<TD><TT>2 3</TT></TD>
</TABLE>

모양 `2 3`을 `A`의 2-셀에 대한 "프레임" 또는 짧게 말해서 `A`의 2-프레임(2-frame) 이라고 한다. `A`의 k-프레임은 `A`의 모양에서 마지막 `k` 차원을 삭제해서 만든다. `A`의 `k`-셀의 배열의 모양으로 볼 수도 있다.

	   frame =: 4 : '$ x cells y'

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> $ A</TT></TD>
<TD><TT> 2 frame A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>2 3 4 5</TT></TD>
<TD><TT>2 3</TT></TD>
</TABLE>

일반적으로 동사 `u`는 `k`랭크를 가지고 있고, `s`의 모양의 각 k-셀들을 계산한다. (각 셀이 `s`와 같은 모양이라고 간주할 것이다.) 그럼 `u A`의 최종 결과의 모양은 `s`의 모양을 따르는 `A`의 k-프레임이다.

설명을 위해서 예를 하나 준비했다. 동사 `u`에서 첫번째 랭크(모나딕) `k`를 찾아내자.

	   k =: 0 { u b. 0

이제 `u`를 `A`의 k-셀에 적용해서 `s`를 계산할 수 있다.

	   s =: $ u  0 { > (, k cells A)

이 예에서는 `u`가 스칼라를 만들어내기 때문에 모양 `s`는 빈 리스트이다. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>k</TT></TD>
<TD><TT>s</TT></TD>
<TD><TT>kfr =: k frame A</TT></TD>
<TD><TT>kfr, s</TT></TD>
<TD><TT> $ u A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>2</TT></TD>
<TD><TT>&nbsp;</TT></TD>
<TD><TT>2 3</TT></TD>
<TD><TT>2 3</TT></TD>
<TD><TT>2 3</TT></TD>
</TABLE>

우리는 `u`가 인자의 각 셀에 대해서 계산 결과의 모양이 전부 같다고 가정했다. 아래에 나오는 "결과 재조립" 섹션에선 이 가정이 깨진다.

### 7.3.1 호응

다이아드는 고유한 랭크가 두개 있다. 하나는 왼쪽 인자, 또 하나는 오른쪽 인자를 위한 것이다. 이 각각을 동사 `u`의 랭크 `L`, `R`이라고 하자.

`u`를 `X`, `Y`에 적용 시킬 때, `u`는 `x`의 각 L-셀과 그와 관련된 `Y`의 R-셀에 적용된다. 예를 들어서 다이아드 `u`의 랭크가 `0 1`라고 하자. 이 동사는 `X`의 0-셀을 `Y`의 1-셀에 붙히는 연산을 한다.

	   u =: < @ ,  " 0 1
	   X =: 2  $ 'ab'
	   Y =: 2 3 $ 'ABCDEF'
	   

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X </TT></TD>
<TD><TT>Y</TT></TD>
<TD><TT>X u Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>ab</TT></TD>
<TD><TT>ABC<BR>
DEF</TT></TD>
<TD><TT>+----+----+<BR>
|aABC|bDEF|<BR>
+----+----+</TT></TD>
</TABLE>

중요한 것은 `X`의 0-프레임은 `Y`의 1-프레임과 같이 취급된다는 것이. 이 때, 두 프레임은 호응이 맞다 라고 한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X</TT></TD>
<TD><TT>Y</TT></TD>
<TD><TT>$X</TT></TD>
<TD><TT>$Y</TT></TD>
<TD><TT>0 frame X</TT></TD>
<TD><TT>1 frame Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>ab</TT></TD>
<TD><TT>ABC<BR>
DEF</TT></TD>
<TD><TT>2</TT></TD>
<TD><TT>2 3</TT></TD>
<TD><TT>2</TT></TD>
<TD><TT>2</TT></TD>
</TABLE>

이 두 프레임이 같지 않다면 무슨 일이 일어나는가? 그래도 여전히 하나가 다른 하나의 프리픽스가 될 것이다. 즉 한 프레임이 벡터 `f`이면 다른 프레임은 몇몇 `g`에 대해 `f,g`와 같은 프레임을 가질 수 있다. 아래에 예가 있다.

	   X =: 2 3 2 $ i. 12
	   Y =: 2     $ 0 1

and a dyad such as  `+`, with ranks  `(0 0)`,  we are interested in the 0-frame of  `X`and the 0-frame of  `Y`. 
랭크 `0 0`을 가지는 다이아드 `+`같은 동사는 `X`의 0-프레임과 `Y`의 0-프레임을 가져와 연산한다.

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X</TT></TD>
<TD><TT>Y</TT></TD>
<TD><TT>0 frame X</TT></TD>
<TD><TT>0 frame Y</TT></TD>
<TD><TT>X+Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT> 0&nbsp;&nbsp;1<BR>
 2&nbsp;&nbsp;3<BR>
 4&nbsp;&nbsp;5<BR>
<BR>
 6&nbsp;&nbsp;7<BR>
 8&nbsp;&nbsp;9<BR>
10 11</TT></TD>
<TD><TT>0 1</TT></TD>
<TD><TT>2 3 2</TT></TD>
<TD><TT>2</TT></TD>
<TD><TT> 0&nbsp;&nbsp;1<BR>
 2&nbsp;&nbsp;3<BR>
 4&nbsp;&nbsp;5<BR>
<BR>
 7&nbsp;&nbsp;8<BR>
 9 10<BR>
11 12</TT></TD>
</TABLE>

We see that the two frames are  `2` and  `2 3 2` and their difference  `g` is therefore  `3 2`. 

Here  `Y` has the shorter frame.  Then each cell of  `Y` corresponds to, not just a single cell of  `X`, but rather a  `3 2`-shaped array of cells. 

In such a case, a cell of  `Y` is automatically replicated to form a  `3 2`-shaped array of identical cells. In effect the shorter frame is made up to length,  so as to agree with the longer. Here is an example. The expression  `(3 2 & $) " 0 Y` means " a 3 by 2 replication of each 0-cell of  `Y`".  

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X</TT></TD>
<TD><TT>Y</TT></TD>
<TD><TT>YYY =: (3 2&$)"0 Y</TT></TD>
<TD><TT>X + YYY </TT></TD>
<TD><TT>X + Y </TT></TD>
<TR VALIGN=TOP>
<TD><TT> 0&nbsp;&nbsp;1<BR>
 2&nbsp;&nbsp;3<BR>
 4&nbsp;&nbsp;5<BR>
<BR>
 6&nbsp;&nbsp;7<BR>
 8&nbsp;&nbsp;9<BR>
10 11</TT></TD>
<TD><TT>0 1</TT></TD>
<TD><TT>0 0<BR>
0 0<BR>
0 0<BR>
<BR>
1 1<BR>
1 1<BR>
1 1</TT></TD>
<TD><TT> 0&nbsp;&nbsp;1<BR>
 2&nbsp;&nbsp;3<BR>
 4&nbsp;&nbsp;5<BR>
<BR>
 7&nbsp;&nbsp;8<BR>
 9 10<BR>
11 12</TT></TD>
<TD><TT> 0&nbsp;&nbsp;1<BR>
 2&nbsp;&nbsp;3<BR>
 4&nbsp;&nbsp;5<BR>
<BR>
 7&nbsp;&nbsp;8<BR>
 9 10<BR>
11 12</TT></TD>
</TABLE>

What we have seen is the way in which a low-rank argument is automaticallyreplicated to agree with a high-rank argument, which is possibleprovided one frame is a prefix of the other. Otherwisethere will be a length error. The frames in question are determined by the intrinsic dyadic ranks of the verb. 

The general scheme for automatically replicating one argument is: for arguments  `x` and  `y`,  if  `u` is a dyad with ranks  `L` and  `R`, and the L-frame of x is  `f,g` and the R-frame of  `y` is  `f` (supposing  `y` to have the shorter frame) 

then  `(x u y)` is computed as  `(x u (g& $)"R y)`

## 7.4 결과 재조립

We now look briefly at how the results of the computations on the separate cells are reassembled into the overall result.  

Suppose that the frame of application of a verb to its argument(s) is  `f`, say. Then we can visualise each individual result as being stuffed into its place in the  `f`-shaped framework of results. If each individual result-cell has the same shape,  `s` say, then the shape of the overall result will be  `(f,s)`. However, it is not necessarily the case that all the individual results are the same shape. For example,consider the following verb  `R`, which takes a scalar  `y` and produces a rank- `y` result. 

	   R =: (3 : '(y $ y) $ y') " 0
	   

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> R 1 </TT></TD>
<TD><TT> R 2 </TT></TD>
<TR VALIGN=TOP>
<TD><TT>1</TT></TD>
<TD><TT>2 2<BR>
2 2</TT></TD>
</TABLE>

When  `R` is applied to an array, the overall result may be explained by envisaging each separate result being stufffed into its appropriate box in an  `f`-shaped array of boxes.  Then everything is unboxed all together.Note that it is the unboxing which supplies padding and extra dimensions if necessary to bringall cells to the same shape. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> (R 1); (R 2)</TT></TD>
<TD><TT> > (R 1) ; (R 2) </TT></TD>
<TD><TT> R 1 2</TT></TD>
<TR VALIGN=TOP>
<TD><TT>+-+---+<BR>
|1|2 2|<BR>
| |2 2|<BR>
+-+---+</TT></TD>
<TD><TT>1 0<BR>
0 0<BR>
<BR>
2 2<BR>
2 2</TT></TD>
<TD><TT>1 0<BR>
0 0<BR>
<BR>
2 2<BR>
2 2</TT></TD>
</TABLE>

Consequently the shape of the overall result is given by  `(f, m`) where  `m` is the shape of the largestof the individual results. 

## 7.5 더 많은 랭크 접속사

### 7.5.1 상대적인 셀 랭크

The rank conjunction will accept a negative number for a rank.  Thus the expression  `(u " _1 y)` means thatu is to be applied to cells of rank 1 less than the rank of  `y`, that is, to the items of  `y`. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> X </TT></TD>
<TD><TT> $ X</TT></TD>
<TD><TT> < " _1 X</TT></TD>
<TD><TT> < " _2 X</TT></TD>
<TR VALIGN=TOP>
<TD><TT> 0&nbsp;&nbsp;1<BR>
 2&nbsp;&nbsp;3<BR>
 4&nbsp;&nbsp;5<BR>
<BR>
 6&nbsp;&nbsp;7<BR>
 8&nbsp;&nbsp;9<BR>
10 11</TT></TD>
<TD><TT>2 3 2</TT></TD>
<TD><TT>+---+-----+<BR>
|0 1| 6&nbsp;&nbsp;7|<BR>
|2 3| 8&nbsp;&nbsp;9|<BR>
|4 5|10 11|<BR>
+---+-----+</TT></TD>
<TD><TT>+---+---+-----+<BR>
|0 1|2 3|4 5&nbsp;&nbsp;|<BR>
+---+---+-----+<BR>
|6 7|8 9|10 11|<BR>
+---+---+-----+</TT></TD>
</TABLE>

### 7.5.2 사용자 정의 동사

The rank conjunction  `"` has a special significance for user-defined verbs.  The significance is that it allows us to define a verb considering only its "natural" rank: we ignore the possibility thatit may be applied to higher-rank arguments. In other words, we can write a definition assuming the verbwill be applied only to arguments of the natural rank. Afterwards, we can then put the finishing touch to our definition with the rank conjunction.  Here are two examples. 

The factorial of a number  `n` is the product of the numbers from  `1` to  `n`. Hence (disregarding for the moment J's built-in verb  `!`) we could define factorial straightforwardly as 

	      f =: */ @: >: @: i.

because  `i. n` gives the numbers  `0 1 ... (n-1)`, and  `>: i. n` gives  `1 2 ... n`. We see: 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>f 2 </TT></TD>
<TD><TT>f 3 </TT></TD>
<TD><TT>f 4</TT></TD>
<TD><TT>f 5</TT></TD>
<TR VALIGN=TOP>
<TD><TT>2</TT></TD>
<TD><TT>6</TT></TD>
<TD><TT>24</TT></TD>
<TD><TT>120</TT></TD>
</TABLE>

Will  `f` work as expected with a vector argument?  

	   f 2 3
	4 10 18

Evidently not. The reason is that  `(f 2 3)` begins by computing  `(i. 2 3)`, and  `(i. 2 3)` does NOT mean  `(i. 2)` followed by  `(i. 3)`. The remedy is to specify that  `f` applies separately to each scalar (rank-0 cell) in its argument:  

	   f  =: (*/ @: (>: @: i.)) " 0
	   
	   f 2 3 4 5
	2 6 24 120

For a second example of the significance of the rank-conjunction we look at explicitly defined verbs.The point being made here is, to repeat,  that it is useful to be able to write a definition on the assumption that the argument is a certain rank say, a scalar, and only later deal with extending to arguments of anyrank. 

Note that for any explicit verb, its intrinsic ranks are always assumed to be infinite.  This is because the J system does not look at the definition until the verb is executed.  Since the rank is infinite, the whole argument of an explicit verb is always treated as a singlecell (or pair of cells for a dyad) and there is no automatic extension to deal with multiple cells. 

For example, the absolute value of a number can be computed by the verb: 

	   abs =: 3 : 'if. y < 0 do. - y else. y end.'
	   

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>abs 3</TT></TD>
<TD><TT>abs _3</TT></TD>
<TR VALIGN=TOP>
<TD><TT>3</TT></TD>
<TD><TT>3</TT></TD>
</TABLE>

Since  `abs` is explicitly defined, we see that its monadic (first) rankis infinite: 

	   abs b. 0
	_ _ _

This means that if  `abs` is applied to an array  `y`, of any rank, it will be applied just once, and we can seefrom the definition that the result will be  `y` or  `-y`.  There are no other possibilities.   

It is indeed the case that if  `y` is a vector then   `(y &lt; 0)` yields a vector result, but the expression  `(if. y &lt; 0)` makes ONE decision. (This decision will in fact be based, not on the whole of  `y &lt; 0` but only on its first element. See   Chapter 12 for more details). Hence if the argument contains both positives and negatives, this decision must be wrong for some parts of the argument. 

	   abs 3 _3
	3 _3

Hence with  `abs` defined as above, it is important to say that it appliesseparately to each scalar in its argument.Thus a  better definition for  `abs` would be: 

	   abs =:(3 : 'if. y < 0 do. -y else. y end.') " 0
	   
	   abs 3 _3
	3 3
	   

This brings us to the end of Chapter 7.    