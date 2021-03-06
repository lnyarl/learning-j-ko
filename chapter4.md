# J언어 배우기 - 제 4장: 스크립트와 명시적인 함수

필요할 때 다시 실행할 수 있는 J코드 라인의 시퀀스를 "스크립트"라고 한다. 이 챕터의 테마는 스크립트와 스크립트에 정의된 함수, 그리고 파일에 저장된 스크립트이다.

## 4.1 텍스트

아래에 `txt`라는 변수에 값을 할당하는 코드가 있다.

	   txt =: 0 : 0
	What is called a "script" is
	a sequence of lines of J.
	)

`0 : 0`이란 표현식은 "다음과 같이"라는 의미이다. 즉 `0 : 0`은 인자를 취해서 그 것이 무엇이든 간에 결과를 변수에 할당한다. 인자는 여러 라인이 될 수 있고 마지막 줄은 닫는 괄호만 적는다.

`txt`의 값은 위에서 보듯 두 줄로 이루어진 하나의 문자열이다. 저 문자열은 개행 문자(line-feed, LF)를 포함하고 있다. 개행문자는 `txt`를 출력할 때에 같이 화면에 출력된다. `txt`는 랭크가 1이고 특정 길이를 가진다. 다시 말해 2개의 개행문자를 가지고 있는 그냥 리스트라는 말이다.

	   txt
	What is called a "script" is
	a sequence of lines of J.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>$ txt</tt></td>
<td><tt># $ txt</tt></td>
<td><tt>+/ txt = LF</tt></td>
</tr><tr valign="TOP">
<td><tt>55</tt></td>
<td><tt>1</tt></td>
<td><tt>2</tt></td>
</tr></tbody></table>

이제 `txt`를 “텍스트”변수라고 하자. 텍스트는 0 이상의 개행문자를 가진 문자열이다.

## 4.2 프로시저용 스크립트

아래의 프로시저에 있는 계산 과정을 하나하나 밟아 나가보자. 굉장히 간단한 예제로 화씨-섭씨 변환기는 두 단계로 표현할 수 있다. 화씨를 나타내는 변수 T에 온도 값을 넣는다.

	   T =: 212

첫 번째 단계는 32를 빼는 것이다. 그 결과를 t라고 하자.

	   t =: T - 32

두 번째 단계는 t에 `5%9`를 곱해서 섭씨를 구하는 것이다.

	   t * 5 % 9
	100

자 이제 우리가 이 계산을 T의 값을 바꿔가면서 몇 번 더 하고 싶다고 해보자. 두 줄의 프로시저를 스크립트로 작성함으로써 필요 할 때마다 불러서 쓸 수 있다. 아래와 같이 J코드로 작성된 스크립트는 텍스트 변수에 담긴다.

	   script =: 0 : 0
	t =: T - 32
	t * 5 % 9
	)

이런 스크립트는 내장 함수인 `0 ! :111`를 이용해 실행할 수 있다. 이 함수는 `do`라고 부른다.

	   do =: 0 !: 111
	   
	       do  script

그럼 이제 아래의 문자들이 키보드로 친 것처럼 화면에 나올 것이다.

   t =: T - 32
   t * 5 % 9
100

그리고 T의 값을 바꿔서 다시 스크립트를 돌려볼 수도 있다.

   T =: 32
   do script
   t =: T - 32
   t * 5 % 9
0

## 4.3 명시적으로 정의된 함수

스크립트로는 함수도 정의할 수 있다. 아래는 화씨-섭씨 변환 동사에 대한 예제이다.

	   Celsius =: 3 : 0
	t =: y - 32
	t * 5 % 9
	)

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>Celsius 32 212</tt></td>
<td><tt>1 + Celsius 32 212</tt></td>
</tr><tr valign="TOP">
<td><tt>0 100</tt></td>
<td><tt>1 101</tt></td>
</tr></tbody></table>

이 정의문에 대해 더 자세히 살펴보자

### 4.3.1 헤딩(Heading)

함수는 `3 : 0`이란 표현 식으로 시작한다. 이 표현 식의 의미는 "다음은 동사이다"라는 뜻이다. (반면 위에서 보았던 `0 : 0`은 "다음은 문자열이다" 라는 뜻이다) 

`3 : 0`에 있는 콜론(colon)은 접속사이다. 왼쪽 인자인 3은 "동사"를 뜻하고 오른쪽 인자인 0은 "다음에 따라오는 것은"이라는 의미이다. 더 자세한 사항은 챕터 12를 참고하라. 이런 식으로 함수를 만드는 방법을 "명시적인 정의"나 "명시하다"라고 표현한다.

### 4.3.2 의미(Meaning)

표현식 `Celsius 32 212`는 동사 `Celsius`에 인자 `32 212`를 적용한 것이다. 이 동사는 이미 작성된 대로 작동한다. 아래처럼 말이다.

   y =: 32 212
   t =: y - 32
   t * 5 % 9
0 100

첫 번째 줄 다음부터는 스크립트에 작성되어 있는 내용이다.

### 4.3.3 인자 변수

인자 `32 212`는 스크립트에서 y라는 이름의 변수로 받을 수 이다. 모나딕 함수에서 이 y를  "인자 변수"라고 한다. (다이아딕 함수의 경우는 뒤에 다룰 것이다. 간단히 이야기 하자면 왼쪽 인자는 x, 오른쪽 인자는 y라는 이름을 가진다.)

### 4.3.4 지역 변수

아래에 다시 `Celsius`의 정의를 적어놨다.

	   Celsius =: 3 : 0
	t =: y - 32
	t * 5 % 9
	)

우리는 여기서 변수 t에 값을 할당하는 것을 볼 수 있다. 이 변수는 `Celsius`를 실행하는 동안에만 사용한다. 불행히도 이 할당문은 `Celsius`밖에서 정의 된 또다른 t라는 변수와 충돌한다. 예를 들자면 다음과 같다.

	   t =: 'hello' 
	   
	   Celsius 212
	100
	   
	   t
	180

원래 `'hello'`라는 값을 가지고 있었던 변수 t는 `Celsius` 실행 후 값이 바뀌었다. 이런 현상을 피하기 위해서 `Celsius`안에 있는 변수 t를 확실하게 `Celsius`만 사용하는 변수(private)로 만들어 t라는 이름의 다른 변수와 분리 시킨다. `=.`(equal dot)이라는 심볼이 그런 일을 하는 또 다른 종류의 할당문이다. 그럼 함수를 다음과 같이 새로 정의 할 수 있다.

	   Celsius =: 3 : 0
	t =. y - 32
	t * 5 % 9
	)

`Celsius`안의 변수 t를 우리는 지역 변수라고 부르거나 t는 `Celsius`에서 지역적이다 라고 한다. 반면 함수 밖에서 정의 된 변수는 전역 변수이다. 이제 `Celsius`안에서 지역 변수 t에 할당하는 행위가 전역 변수 t에 아무런 영향을 주지 않는 것을 볼 수 있다.

	   t =: 'hello'
	    
	   Celsius 212
	100
	   
	   t
	hello

인자 변수 y도 지역 변수다. 이젠 `Celsius 32 212`를 보다를 정확하게 계산할 수 있다.

	   y =. 32 212
	   t  =. y - 32
	   t * 5 % 9
	0 100

### 4.3.5 다이아딕 동사

`Celsius`는 모나딕 동사이다. 모나딕 동사는 `3 : 0`으로 시작해 인자로 y하나만 받도록 정의한다.  그런데 다이아딕 동사는 `4 : 0`으로 시작한다. 왼쪽 인자와 오른쪽 인자는 항상 각각 x와 y라는 이름으로 정의되어있다. 아래에 예제가 있다. 주어진 두 수의 "양의 차이(positive difference)"는 큰 수에서 작은 수를 뺀 것이다.

	   posdiff =: 4 : 0
	larger  =. x >. y
	smaller =. x <. y
	larger - smaller 
	)

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>3 posdiff 4</tt></td>
<td><tt>4 posdiff 3</tt></td>
</tr><tr valign="TOP">
<td><tt>1</tt></td>
<td><tt>1</tt></td>
</tr></tbody></table>

### 4.3.6 한 줄 코드

한 줄 스크립트는 문자열로 나타낼 수 있다. 그리고 그걸 콜론 접속사의 오른쪽 인자로 준다.

	   PosDiff =: 4 : '(x >. y) - (x <. y)'
	   4 PosDiff 3
	1

### 4.3.7 제어 구조

위에서 봤던 스크립트로 정의된 함수에 대한 예제들에서는 제일 처음 줄이 실행되고 그다음 줄이 실행되고 그렇게 마지막 줄까지 차례대로 실행된다.
그렇게 쭉 실행되는 것 말고도 다음 실행될 표현식을 선택하는 것도 된다.

예를 들어, 가로, 세로, 높이를 입력받아 부피를 계산하는 함수가 있다고 하자. 이 함수는 입력으로 들어온 인자가 아이템이 3개인 리스트인지 검사한다. 만약 입력 값이 올바르면 부피를 계산하고 아니면 'ERROR'이라는 문자열을 출력한다고 하자. 그럼 함수는 다음과 같이 작성할 수 있고

	   volume =: 3 : 0
	if.   3 = # y
	do.   * / y
	else. 'ERROR'
	end.
	)

아래와 같은 결과를 볼 수 있다.

 <table cellpadding="10" border="1">
<tbody><tr valign="TOP">
<td><tt>volume 2 3 4</tt></td>
<td><tt>volume 2 3</tt></td>
</tr><tr valign="TOP">
<td><tt>24</tt></td>
<td><tt>ERROR</tt></td>
</tr></tbody></table>

`if.`에서 `end.`까지의 전부를 통털어 그러한 양식을 "제어 구조"라고 부른다. 그리고 `if.` `do.` `else.` `end.`는 "제어 단어"라고 한다. 챕터 12에서 제어 구조에 대해 더 다룬다.

## 4.4 암묵적 스타일과 명시적 스타일의 비교

이제껏 우리는 함수를 정의하는 두 가지 방법을 봤다. 이번 챕터에서 다룬 명시적인 스타일은 인자들이 내부에서 명시적으로 변수로서 사용되기 때문에 그렇게 부른다. 따라서 위의 부피를 구하는 예제에서 변수 y는 인자의 명시적인 사용이다.

반면 이전 챕터에서 봤던 스타일은 "암묵적인 스타일"이라고 한다. 그 정의안에 인자에 대한 언급이 없기 때문이다. 예를 들어 "양의 차이"를 구하는 함수의 명시적인 정의와 암묵적인 정의를 비교해보자.

	   epd =: 4 : '(x >. y) - (x <. y)'
	   
	   tpd =: >. - <.

암묵적인 스타일로 작성된 많은 함수들은 명시적으로 정의할 수 있다. 물론 반대의 경우도 마찬가지다. 어떤 스타일을 선호하는가 라는 문제는 함수가 어떻게 정의 되어야 한다 라는 우리 생각에 비추어보아 어떤게 더 자연스럽게 보이는가에 달려있다. 둘 중에 하나를 선택하면 된다. 한 쪽은 문제를 더 작은 단계로 나누어 차례대로 해결하는 것이고, 다른 한쪽은 작은 함수들의 모임이다.

암묵적인 스타일은 짧게 정의할 수 있다. 그래서 암묵적인 스타일의 함수는 체계적인 분석과 변환을 하기에 좋다. 실제로 대부분의 암묵적인 함수들에 대해 J 시스템은 자동적으로 그런 역함수나 파생등의 변환을 자동으로 해준다.

## 4.5 값으로써의 함수

함수는 값이다. 그리고 값은 표현식을 입력하면 화면에 표시된다. 표현식은 간단히 이름으로 표현될 수 있다. 아래는 암묵적, 명시적 함수들의 값이다.

	   - & 32
	+-+-+--+
	|-|&|32|
	+-+-+--+
	   
	   epd
	+-+-+-------------------+
	|4|:|(x >. y) - (x <. y)|
	+-+-+-------------------+
	   
	   Celsius
	+-+-+-----------+
	|3|:|t =. y - 32|
	| | |t * 5 % 9  |
	+-+-+-----------+

각 함수의 값은 박스 구조로 표시된다. 기본적으로는 그렇지만 다르게 표현할 방법도 몇 가지 있다. 이는 챕터 27을 참고하라. 여기에서는 "선형 표현" 방법만 다룰 예정이다. 이 방법은 함수를 다시 화면에 타이핑 한 것 처럼 문자의 나열로 표현하는 방법이다. 다음 함수를 써서 현재 세션의 함수 값 표현 방법을 선형 표현으로 바꿀 수 있다.

	   (9!:3) 5

그리고나선 아래와 예제 같이 보인다.

	   epd
	4 : '(x >. y) - (x <. y)'

이 다음 챕터 부터는 함수의 값이 종종 선형 표현으로 표현될 것이다.

## 4.6 스크립트 파일

지금까진 텍스트 변수나 함수등의 변수 하나를 정의하는 J 코드 스크립트를 봐왔다. 반면 J 코드를 텍스트로 담고 있는 파일은 많은 정의를 저장할 수 있다. 그런 파일을 스크립트 파일이라고 한다. 스크립트 파일은 파일을 읽으면 그 안의 정의가 모두 실행되기 때문에 유용하다고 할 수 있다.

아래에 예제가 있다. 마음에 드는 텍스트 에디터를 이용해서 파일을 만들고 아래 두 줄을 써넣자.

	squareroot =: %:
	z =: 1 , (2+2) , (4+5)

J 스크립트 파일은 확장자를 ".ijs"로 한다. 그래서 예를 들어 방금 만들어진 파일의 전체 경로는 "c:\temp\myscript.ijs" 라고 하자.

그럼 J 세션에서 변수 F를 정의하고 문자열로 표현한 이 파일 이름을 변수 F에 담아 편하게 파일을 참조 할 수 있다.

	   F =: 'c:\temp\myscript.ijs'   
   
아래와 같이 입력 하면 그 두 줄을 저장하고 있는 파일을 실행할 수 있다.

	       0!:1 < F

그럼 파일에 있는 라인이 키보드로 친 듯이 화면에 나올 것이다.

	   squareroot =: %:
	   z =: 1 ,(2+2), (4+5)

이제 파일에서 로드된 이 정의들을 사용 할 수 있다.

	   z
	1 4 9
	   
	   squareroot z
	1 2 3

J 세션의 액티비티는 전통적으로 "스크립트 파일 편집", "스크립트 파일안의 정의들을 로딩/리로딩" 그리고 "키보드로 입력 받은 것을 계산"하는 것들을 다 합쳐놓은 것이다. 한 세션에서 다른 세션으로 이어질 수 있는 것은 스크립트 파일 뿐이다. 세션이 끝날 때 J 시스템 상태나 메모리는 세션이 유지되는 동안 입력되었던 모든 정의들과 함께 없어진다. 따라서 스크립트 파일에는 변하지 않는 정의들이 있기 때문에, J 세션이 끝나기 전에는 모든 스크립트 파일이 변경되지 않는게 좋다.

세션이 시작 될때 J 시스템은 특정한 스크립트 파일을 자동으로 로드한다. 이 스크립트 파일을 "profile" 이라고 한다.(더 자세한 사항은 챕터 26을 보라) profile은 사용자가 편집할 수 있다. 따라서 일반적으로 쓸만한 정의 들을 기록해놓기에 좋다. 우린 이제 챕터4의 끝이자 파트1의 끝에 다다랐다. 다음 챕터는 파트1에서 다뤘던 테마를 좀 더 깊게 다루도록 하겠다.
