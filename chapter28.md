# 28장 : 데이터 파일

일반적인 파일 핸들링의 주제와 어떻게 파일안에서 데이터가 구성되어있는가는 그것 자체로 주요 주제이다. 이 장에서는 J에서 제공하는 유용한 것들 중 몇 가지만을 다룬다. 

J에서 파일을 읽는 함수는 문자열 값을 리턴한다. 비슷하게 파일에 쓰는 함수는 문자열을 인자로 받는다. 만약 컴퓨터에 충분한 메모리가 있다면 파일에 쓰거나 읽을 전체 데이터를 하나의 문자열로 만들어 통째로 다루어도 된다.

이 장에선 우선 문자열을 읽고 쓰는 J함수 들에 대해 살펴볼 것이다. 그리고 문자열을 여러가지 데이터 포멧으로 다루는 예제를 보고 마지막으로 또 다른  파일 핸들링 방법인  mapped 파일에 대해 설명한다.

## 28.1  파일 읽고 쓰기

### 28.1.1  내장 동사

이후 나오는 파일 이름은 J 가 실행되고 있는 운영체제 내에서 올바른 파일 이름 포멧을 가진 문자열이다. 예를 들어 운영체제가 윈도우즈라면 파일 이름은 다음과 같다.(만약 유닉스 머신이라면 올바른 파일 이름은 다른 포멧일 것이다.)

	   F =: 'c:\temp\demofile.xyz'       NB. a filename

내장 동사 `1!:2`는 데이터를 파일에 쓴다. 파일 이름을 박스에 담아(<) 오른쪽 인자로 하고 왼쪽 인자는 파일에 쓸 데이터 문자열을 준다. 동사 실행 결과 만약 파일이 없으면 파일이 생성되고 파일 안의 데이터가 전부 입력된 데이터로 바뀐다.

	   'some data' 1!:2 < F    NB. write to file F

내장 동사인 `1!:1` 은 파일에서 데이터를 읽어온다. 오른쪽 인자는 박스에 담은 파일 이름이다. 동사를 수행하면 읽어들인 문자열을 반환한다.

	   data =: 1!:1 < F     NB.  read from file F

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>data</TT></TD>
<TD><TT>$ data</TT></TD>
<TR VALIGN=TOP>
<TD><TT>some data</TT></TD>
<TD><TT>9</TT></TD>
</TABLE>

### 28.1.2 파일로써의 화면과 키보드

화면과 키보드를 파일처럼 다루면, 프로그램과 사용자사이의 간단한 인터렉션을 구현할 수 있다. 

The expression  `x (1!:2) 2` writes the value of  `x` to "file 2",that is, to the screen. A verb to display to the screen can be written as 
표현식 `x (1!:2) 2`는 `x`의 값을 파일 "2"(즉, 화면)에 쓴다. 화면에 출력하는 동사는 다음과 같이 쓸 수 있다.

	   display =: (1!:2) & 2

For example, here is a verb to display the stages in the computation of least-common-denominator by Euclid'salgorithm. 

	   E =: 4 : 0
	display x , y
	if. y = 0 do. x else. (x | y) E x end.
	)
	   
	   12 E 15
	12 15
	3 12
	0 3
	3 0
	3

The value to be displayed by  `(1!:2) &2` is not limited to strings:in the example above a list of numbers was displayed. 

User-input can be requested from the keyboard by reading "file 1", that is,by evaluating   `(1!:1) 1`. The result is a character-string containing the user's keystrokes.For example, a function for user-interaction might be: 

	   ui =: 3 : 0
	display 'please type your name:' 
	n  =.  (1!:1) 1
	display 'thank you ', n
	''
	)

and then after executing 

	         ui ''

a dialogue appears on the screen,  like this: 

	       please type your name:

	       Waldo

	       thank you Waldo

### 28.1.3  Library Verbs

There are a number of useful verbs for file-handling in the "standard library" ( Chapter 26). Here is a brief summary of a selection: 

 write string s to file F read string from  file F append string s to file F  read slice from file F, starting at B, length L write text s to file F read text from file F true if file F exists delete file F <TABLE BORDER=1 CELLPADDING=4>
<TR><TD ALIGN=RIGHT><TT> s fwrite  F</TT> </TD>
    <TD> write string s to file F</TD></TR>
<TR><TD ALIGN=RIGHT><TT>   fread   F</TT></TD>
    <TD> read string from  file F</TD></TR>
<TR><TD ALIGN=RIGHT><TT> s fappend F</TT></TD >
    <TD> append string s to file F </TD></TR>
<TR><TD ALIGN=RIGHT><TT>   fread F;B,L</TT></TD>
    <TD> read slice from file F, starting at B, length L</TD></TR>
<TR><TD ALIGN=RIGHT><TT> s fwrites F </TT></TD>
    <TD> write text s to file F</TD></TR>
<TR><TD ALIGN=RIGHT><TT>   freads  F</TT></TD>
    <TD> read text from file F</TD></TR>
<TR><TD ALIGN=RIGHT><TT>   fexist  F</TT></TD> 
    <TD> true if file F exists</TD></TR>
<TR><TD ALIGN=RIGHT><TT>   ferase  F</TT></TD>
    <TD> delete file F</TD></TR>
</TABLE>

From now on we will use these library verbs for our file-handling. 

The library verb  `fwrite` writes data to a file. The right argument is a filename. The left argument is a character-string, the data to be written.The effect is that the file is created if it does not already exist, and the data becomes the whole content of the file. 

	   'some data' fwrite F    NB. file write
	9

The result shows the number of characters written.A result of  `_1` shows an error: either the left argument is not a string or the right argumentis not valid as a filename, orthe specified file exists but is read-only. 

	   (3;4) fwrite F
	_1

The library verb  `fread` reads data from  file. The argument is a filename and the resultis a character-string.  

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>z =: fread F</TT></TD>
<TD><TT>$z</TT></TD>
<TR VALIGN=TOP>
<TD><TT>some data</TT></TD>
<TD><TT>9</TT></TD>
</TABLE>

A result of  `_1` shows an error: the specifiedfile does not exist, or is locked. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>fread 'qwerty'</TT></TD>
<TD><TT>fexist 'qwerty'</TT></TD>
<TR VALIGN=TOP>
<TD><TT>_1</TT></TD>
<TD><TT>0</TT></TD>
</TABLE>

## 28.2  Large Files

For large files, the memory of the computer may not be sufficient to allow the fileto be treated as a single string. We look at this case very briefly.  

Write a file with some initial content: 

	   'abcdefgh' fwrite F
	8

We can append some data to the file with library verb  `fappend`. 

	   'MORE' fappend F
	4

To see the effect of  `fappend` (just for this demonstration, but not of course for a large file)we can read the whole file again : 

	   fread F
	abcdefghMORE

We can read a selected slice of the file, say 8 bytes starting from byte  `4`. In this casewe use  `fread` with a right argument of the form  `filename;start,size`. 

	   start =: 4
	   size  =: 8
	   fread F ; start, size
	efghMORE

## 28.3  Data Formats

We look now at a few examples of how data may be organized in a file, that is, represented by a string. Hence we look at converting between character strings, with various internal structures, and J variables.  

We take it that files are read and written for the purpose of exchanging data between programs. Two such programs we can call "writer" and "reader". Questions which ariseinclude:  Are writer and reader both to be J programs?     If so, then there is a convenient J-only format, the "binary representation" covered below.    If not, then we expect to work from a programming-language-independent description    of the data. 

 Are writer and reader to run on computers with the same architecture?     If not, then even in the J-to-J situation, some finesse may be needed.

Is the data organized entirely as a repetition of some structure     (for example, "fixed length records").    If so then we may usefully be able to treat it as one or more J arrays.     If not, we may need some ad-hoc programming.

### 28.3.1  The Binary Representation for J-0nly Files

Suppose we aim to handle certain files only in J programs, so that we are free to choose any file format convenient forthe J programmer. The "binary representation" is particularlyconvenient. 

For any array  `A`, 

	   A =:  'Thurs'; 19 4 2001 

the binary representation of  `A` is a character string.There are built-in verbs to convert betweenarrays and binary representations of arrays. 

	   arrbin  =: 3!:1   NB. array to binary rep.
	   binarr  =: 3!:2   NB. binary rep. to array

If  `B` is the binary representation of  `A`, we see that  `B` isa character string, with a certain length. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>$ B =: arrbin A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>+-----+---------+<BR>
|Thurs|19 4 2001|<BR>
+-----+---------+</TT></TD>
<TD><TT>88</TT></TD>
</TABLE>

We can write  `B` to a file, read it back, and do the inverse conversion to recover the value of  `A` : 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>B fwrite F </TT></TD>
<TD><TT>$ Z =: fread F</TT></TD>
<TD><TT>binarr Z</TT></TD>
<TR VALIGN=TOP>
<TD><TT>88</TT></TD>
<TD><TT>88</TT></TD>
<TD><TT>+-----+---------+<BR>
|Thurs|19 4 2001|<BR>
+-----+---------+</TT></TD>
</TABLE>

From J4.06 on, there are variationsof the binary representation verbs aboveto allow for different machine architectures: see the Dictionary under  `3!:1`. 

### 28.3.2  Text Files

The expression  `a.` (lower-case a dot)is a built-in noun, a character-string containing all 256 ASCII characters in sequence. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>65 66 67 { a.</TT></TD>
<TD><TT>$ a.</TT></TD>
<TR VALIGN=TOP>
<TD><TT>ABC</TT></TD>
<TD><TT>256</TT></TD>
</TABLE>

In the ASCII character set, that is, in  `a.`,  the character at position 0 is the null,at position 10 is line-feed and at position 13is carriage return . In J, the names  `CR` and  `LF` are predefined in the standard profile to meanthe carriage-return and linefeed characters. 

	   a. i. CR,LF
	13 10

We saw  `fread` and  `fwrite` used for reading and writingcharacter files. Text files are a special kindof character file, in that lines are delimited by  `CR` and/or  `LF` characters. 

On some systems the convention is thatlines of text are delimited by a single  `LF`and on other systems a  `CR,LF` pair is expected.Regardless of the system on which J is running, for J text variables, the convention is always followed of delimiting a linewith single  `LF` and no  `CR`.  

Here is an example of a text variable.  

	   t =: 0 : 0
	There is physics
	and there is 
	stamp-collecting.
	)

Evidently it is a string (that is, a 1-dimensional character list) with 3  `LF` characters and no  `CR` characters. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>$ t</TT></TD>
<TD><TT>+/t=LF</TT></TD>
<TD><TT>+/t=CR</TT></TD>
<TR VALIGN=TOP>
<TD><TT>49</TT></TD>
<TD><TT>3</TT></TD>
<TD><TT>0</TT></TD>
</TABLE>

If we aim to write this text variable  `t` toa text file, we must choose between the single- `LF` or  `CRLF` conventions. There are two useful library verbs,  `fwrites` and  `freads`to deal with this situation. 

Under Windows, `x fwrites y`  writes text-variable `x` to file `y`,in the process converting each `LF` in `x` to a `CRLF` pairin `y`. Under Linux, `x fwrites y` writes text-variable `x` to file `y`,with no conversion. Under Windows or Linux `z =: freads y`reads file `y`, converting any `CRLF`pair in `y` to a single `LF` in text-variable `z`.

For convenience in dealing with a text variable such as  `t`, we can cut it into lines. A verb for this purposeis  `cut` (described more fully in  Chapter 17 ).  

	   cut =: < ;. _2

`cut` produces a boxed list of lines, removing the  `LF` at the end of each line. 

	   lines =: cut t
	   lines
	+----------------+-------------+-----------------+
	|There is physics|and there is |stamp-collecting.|
	+----------------+-------------+-----------------+

The inverse of  `cut` we can call  `uncut`. It restores the  `LF`at the end of each box and then razes to make a string. 

	   uncut =: ; @: (,&LF &. >)
	   uncut lines
	There is physics
	and there is 
	stamp-collecting.
	

### 28.3.3  Fixed Length Records with Binary Data

Suppose our data is in two J variables: a table  `cnames`, of customer-names,and a list  `amts` in customer order with for each customer an amount, a balance say. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>cnames =: 'Mr Rochester' ,: 'Jane'</TT></TD>
<TD><TT>,. amts =: _10000 3</TT></TD>
<TR VALIGN=TOP>
<TD><TT>Mr Rochester<BR>
Jane</TT></TD>
<TD><TT>_10000<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3</TT></TD>
</TABLE>

Now suppose the aim is to write this data to a file, formatted in 16-byte records. Each record is to have two fields: customer-name in 12 bytesfollowed by amount in 4 bytes, as a signed integer. Here is a possible approach. 

The plan is to construct, from  `cnames` and  `amts`,an n-by-16 character table, to be called  `records`.For this example,  `n=2`, and  `records` will look like this: 

	Mr Rochester####
	Jane        ####
	   

where  `####` represents the 4 characters ofan integer in binary form. 

We build the  `records` table by stitching together side byside an n-by-12 table for the customer names field, and an n-by-4 table for the amounts field. 

For the customer-names field we already have  `cnames` which is suitable, since it is 12 bytes wide: 

	   $ cnames
	2 12

For the amounts field we convert  `amts` to characters, using  `ci4` from  Chapter 27. The result is a single string,which is reshaped to be n-by-4. 

	   ci4 =:  2 & (3!:4)  NB. integer to 4 char
	   
	   amtsfield =: ((# amts) , 4) $ ci4 amts

Now we build the n-by-16  `records` table by stitching togetherside-by-side the two "field" tables: 

	   records =: cnames ,. amtsfield

To inspect  `records`,here is a utility verb which shows a non-printingcharacter as  `#`

	   inspect =: 3 : ('A=.a.{~32+i.96';'(A i.y) { A,''#''')
	   

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>inspect records</TT></TD>
<TD><TT>$ records</TT></TD>
<TR VALIGN=TOP>
<TD><TT>Mr Rochester####<BR>
Jane&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;####</TT></TD>
<TD><TT>2 16</TT></TD>
</TABLE>

The outgoing string to be written to the file is the ravel of the records. 

	   (, records) fwrite F
	32

The inverse of the process is to recover J variables from the file. We read the file to get the incomingstring.  

	   instr =: fread F

Since the record-length is known to be 16, the number of records is 

	   NR =: (# instr) % 16

Reshape the incoming string to get the  `records` table. 

	   inspect records =: (NR,16) $ instr
	Mr Rochester####
	Jane        ####

and extract the data. The customer-names are obtained directly, as columns 0-11 of  `records`. 

	   cnames =: (i.12) {"1 records

For the amounts, we extract columns 12-15, ravel into a single string and convert to integers with  `c4i`. 

	   c4i =: _2 & (3!:4)  NB. 4 char  to integer
	   
	   amts   =: c4i  , (12+i.4) {"1  records

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>cnames </TT></TD>
<TD><TT>,. amts</TT></TD>
<TR VALIGN=TOP>
<TD><TT>Mr Rochester<BR>
Jane</TT></TD>
<TD><TT>_10000<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3</TT></TD>
</TABLE>

## 28.4  Mapped Files

A file is said to be mapped when the file is temporarily incorporatedinto the virtual-address-translation mechanism of an executing program. The data in a mapped file appears to the J programmer directly as the value of a J variable - an array. Changes to the value of the variable are changes to the data in the file.  

In such a case, we can say, for present purposes, that the file is mapped to the variable or, equivalently, that the variable is mapped to the file.  

Mapped files offer the followingadvantages:   Convenience. Data in a file is handled    just like data in any J array. There is no    reading or writing of the file.

 Persistent variables. A variable mapped to      a file lives in the file, and    can persist from one J session to another.

There are two cases.In the first case, any kind of existing file can be mapped to a variable. We take as given the structure of the datain the file, and then  the J programmust supply a description of the desired mapping.For example, a file with fixed-length recordscould be mapped to a character table.  

In the second case, a file can becreated in J in a special format (called "jmf")specifically for the purposeof mapping to a variable.  In this case,the description is automatically derivedfrom the variable and stored in the file along with thedata. Thus a "jmf" file is self-describing. 

We look first at creating jmf files, and then at mapping given files.. 

### 28.4.1   Library Script for Mapped Files

There is a library script,  `jmf.ijs`, for handling mapped files.For present purposes it is simplest to download it directly from theJ Application Library. Here is a   link to jmf.ijs . 

Assuming we have downloaded it into say, directory  `C:\temp` for example, we can load it into our J session with: 

	   load 'c:\temp\jmf.ijs'
	   

The script will load itself into the locale  `jmf` . 

### 28.4.2  jmf Files and Persistent Variables

Suppose we have constructed an array  `V` with somevaluable data, which from now on we aim to use and maintainover a number of J sessions. Perhaps  `V` is valuablenow, or perhaps it will become valuable over subsequentsessions as it is modified and added-to. 

Our valuable data  `V` can be an array of numbers,of characters, or of boxes.  For a simple example we start with  `V` as a table of numbers.  

	   ] V =:  2 2 $ 1 2 3 4
	1 2
	3 4

We can make a persistent variable from  `V` as follows. 

Step 1 is to estimate the size, in bytes,of a file required for the value of  `V`.Since we expect that over time `V` may grow from its present sizeultimately to, say, 64 KB,then our estimate  `S` is  

	   S =: 64000

If in doubt, allow plenty.The size must be given asa positive integer (not a float) and thereforeless than 2147483648 (2Gb) on a 32-bit machine. 

Step 2 is to choose a file-name and, for convenience, define a variable  `F` to hold the the file name as a string. For example:  

	   F =: 'c:\temp\persis.jmf'

Step 3 is to create file  `F` as a jmf file,large enough to hold  `S` bytes of data.  For this purpose the utility function  `createjmf` is available (in locale  `jmf`)so we can write:  

	   createjmf_jmf_ F;S

(On your system, with a different version of J, you may see a response different from what is shown here.) 

At this point, file  `F` exists.If we inspect it we see its actual size is  a little larger than  `S`, to accommodate a header record which makes the file self-describing. 

	   fdir F
	+----------+----------------+-----+---+------+
	|persis.jmf|2011 1 8 9 38 32|64284|rw-|-----a|
	+----------+----------------+-----+---+------+

The content of file  `F` is initially set by  `createjmf_jmf_` to represent a Jvalue, in fact a zero-length list. The important point isthat file  `F` now contains a definite value. 

Step 4 is to map the content of file  `F`to a new variable, for which we choose the name  `P`. 

	   map_jmf_ 'P'; F

This statement means, in effect: 

	               P =:  value-currently-in-file-F

and we can verify that  `P` is now an empty list: 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>P</TT></TD>
<TD><TT>$ P</TT></TD>
<TR VALIGN=TOP>
<TD><TT>&nbsp;</TT></TD>
<TD><TT>0</TT></TD>
</TABLE>

Notice particularly thatthe effect of mapping file  `F` to variable  `P`is to assign the value in  `F` to  `P` and not the other way around.Hence we avoided mapping file  `F` directlyonto our valuable array  `V` because  `V` would beoverwritten by the preset initial value in  `F`, and lost. 

Step 5  is to assign to  `P` the desired value, that of  `V`

	   P =: V

Variable  `P` is now a persistent variable, since it is mapped to file  `F`.  We can amend  `P`, for example by changing the valueat row 0 column 1 to  `99`. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>P</TT></TD>
<TD><TT>P =:  99 (<0 1) } P </TT></TD>
<TR VALIGN=TOP>
<TD><TT>1 2<BR>
3 4</TT></TD>
<TD><TT>1 99<BR>
3&nbsp;&nbsp;4</TT></TD>
</TABLE>

or by appending a new row: 

	   ] P =: P ,  0 0
	1 99
	3  4
	0  0

Step 6 is needed before we finish the current session.We  `unmap` variable  `P`, to ensure file  `F`  is closed.  

	   unmap_jmf_ 'P'
	0

The result of  `0` indicates success. The variable  `P` no longer exists:  

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>P</TT></TD>
<TD><TT>$ P</TT></TD>
<TR VALIGN=TOP>
<TD><TT>error</TT></TD>
<TD><TT>$ P</TT></TD>
</TABLE>

To demonstrate that the value of  `P` persists in file   `F` we repeatthe mapping, processing and unmapping in this or another session.The name  `P` we chose for our persistent variable isonly for this session. In another session,the persistent variable in file  `F` can be mapped to any name.  

This time we choose the name  `Q` for the persistent  variable. We map file  `F` to  `Q`:  

	   map_jmf_ 'Q' ; F
	   
	   Q
	1 99
	3  4
	0  0

modify  `Q`: 

	   ] Q =: Q , 7 8 
	1 99
	3  4
	0  0
	7  8

and unmap  `Q` to close file  `F`. 

	   unmap_jmf_ 'Q'
	0
	   

### 28.4.3  Mapped Files are of Fixed Size

Recall that we created file  `F` large enough for  `S`bytes of data.   

	   S
	64000
	   fdir F
	+----------+----------------+-----+---+------+
	|persis.jmf|2011 1 8 9 38 32|64284|rw-|-----a|
	+----------+----------------+-----+---+------+

The variable in file  `F`  is currently much smaller than this, and the unused trailing part of the fileis filled with junk.However, if we continue to modify  `Q` by appending to it,we reach a limit, by filling the file,  and encounter an error. To demonstrate, with a verb `fill` for the purpose: 

	   fill =: 3 : 0
	try.   while. 1 do. Q =: Q , 99 99 end.
	catch. 'full'
	end.
	)
	   
	   map_jmf_ 'Q'; F 
	   fill ''
	full
	   
	   

The amount of data now in  `Q` can be estimated as 4 bytes per integer (since  `Q`is integer) multiplied by the number of integers, that is, altogether  `4 * */$ Q`.This result for the final size of  `Q` accords with ouroriginal size estimate  `S`. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>4 * */ $ Q </TT></TD>
<TD><TT>S</TT></TD>
<TR VALIGN=TOP>
<TD><TT>64000</TT></TD>
<TD><TT>64000</TT></TD>
</TABLE>

	   unmap_jmf_ 'Q'
	0
	   

### 28.4.4  Given Files

Now we look at mapping ordinary data files (that is, filesother than the special jmf-format files we considered above). 

The way the data is laid out in the filewe take as given, and our task is specifyhow this layout is to be represented by the type, rank and shapeof a J variable, that is, to specify a suitable mapping.  

For example, suppose we aim to read a given file  `G` with its datalaid out in fixed-length records, each recordbeing 8 characters.  Suppose file  `G` was originally createdby, say:  

	        G =: 'c:\temp\data.xyz'

	   'ABCD0001EFGH0002IJKL0003MNOP0004' fwrite G
	32

The next step is to decide what kind ofa variable will be suitable for mapping the data infile  `G`.  We decide on an n-by-8 character table.The number of rows,  `n`,  will be determined by theamount of data in the file, so we do not specify  `n` in advance. 

It is convenient to start with a small example of an n-by-8 character table,which we call a prototype. The choice of  `n` is unimportant. 

	   prototype =: 1 8 $ 'a'

Now the mapping can be defined by:  

	   ] mapping =: ((3!:0) ; (}. @: $)) prototype
	+-+-+
	|2|8|
	+-+-+

We see that  `mapping` is a boxed list. The first item is the data-type. Here  `2`, meaning "character",  is producedby  `3!:0 prototype`.  The second item is the trailing dimensions(that is, all but the first) of the prototype. Here  `8` is all but the first of  `1 8`,  produced by `(}.@:$) prototype`.  Thus  `mapping` expresses orencodes "n-by-8 characters". 

Now  `mapping` is supplied as left argument to(dyadic)  `map_jmf_`. We map file  `G` onto a variable for whichwe choose the name  `W` thus: 

	   mapping map_jmf_ 'W'; G

We see that  `W` is now a variable. Its value is the data in the file. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>W</TT></TD>
<TD><TT>$ W</TT></TD>
<TR VALIGN=TOP>
<TD><TT>ABCD0001<BR>
EFGH0002<BR>
IJKL0003<BR>
MNOP0004</TT></TD>
<TD><TT>4 8</TT></TD>
</TABLE>

We can amend the data in the ususal way: 

	   ] W =: 'IJKL9999' 2 } W
	ABCD0001
	EFGH0002
	IJKL9999
	MNOP0004

What we cannot do is add another row to the data, because all the space in file  `G` is occupied by the data we already have. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>W</TT></TD>
<TD><TT>W =: W ,  'WXYZ0000'</TT></TD>
<TR VALIGN=TOP>
<TD><TT>ABCD0001<BR>
EFGH0002<BR>
IJKL9999<BR>
MNOP0004</TT></TD>
<TD><TT>error</TT></TD>
</TABLE>

We close file  `G` by unmapping variable  `W`:  

	   unmap_jmf_ 'W'
	0

### 28.4.5  Mapped Variables Are Special

Mapping files to variables offers the programmersignificant advantages in functionality and convenience. 

The price to be paid for these advantages isthat there are some considerations applying to mapped variables which do not apply to ordinary variables. The programmerneeds to be aware of, and to manage, these considerations.This is our topic in this section and the next. 

If  `A` is an ordinary variable, not mapped,then in the assignment  `B=: A` the value of  `A` is in effectcopied to  `B`. A subsequent change to  `A` does not affectthe value of  `B`. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A =: 1</TT></TD>
<TD><TT>B =: A</TT></TD>
<TD><TT>B</TT></TD>
<TD><TT>A =: 2</TT></TD>
<TD><TT>B</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1</TT></TD>
<TD><TT>1</TT></TD>
<TD><TT>1</TT></TD>
<TD><TT>2</TT></TD>
<TD><TT>1</TT></TD>
</TABLE>

By contrast, consider a variable mapped to a file.If the file is very large, there may not beenough space for another copy of the value.Hence copying is to be avoided.  

Compare the previous example with the case when `A` is a mapped variable.  

	   map_jmf_ 'A';F

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A =: 1</TT></TD>
<TD><TT>B =: A</TT></TD>
<TD><TT>B</TT></TD>
<TD><TT>A =: 2</TT></TD>
<TD><TT>B</TT></TD>
<TR VALIGN=TOP>
<TD><TT>1</TT></TD>
<TD><TT>1</TT></TD>
<TD><TT>1</TT></TD>
<TD><TT>2</TT></TD>
<TD><TT>2</TT></TD>
</TABLE>

We see that  `B` changes with changes to  `A`.In effect  `B =: A` means that  `B` isanother name for  `A`, not a copy of the value of  `A`. That is,both  `A` and  `B` refer to the same thing - the valuein the file. 

Hence it is also the case that  `A` changes with changes to  `B`.  

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>B =: 7</TT></TD>
<TD><TT>A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>2</TT></TD>
<TD><TT>7</TT></TD>
<TD><TT>7</TT></TD>
</TABLE>

Consider now an explicit verb applied to a mapped variable. Here  `y` becomes another name for the data in the file.Hence assignment to  `y` (even a local assignment)may cause an unintended change the mapped variable in the file.For example 

	   foo =: 3 : ' 3 * y =. y + 1'
	   
	   

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>foo 2</TT></TD>
<TD><TT>A</TT></TD>
<TD><TT>foo A</TT></TD>
<TD><TT>A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>9</TT></TD>
<TD><TT>7</TT></TD>
<TD><TT>24</TT></TD>
<TD><TT>8</TT></TD>
</TABLE>

### 28.4.6  Unmapping Revisited

The current status of mapped files and variablesis maintained by the J system in a "mapping table".   The mapping tablecan be displayed by entering the expression `showmap_jmf_ ''` but for present purposes here is a utility functionto display only selected columns. 

	   status =: 0 1 9 & {"1  @: showmap_jmf_
	   status ''
	+-------+------------------+----+
	|name   |fn                |refs|
	+-------+------------------+----+
	|A_base_|c:\temp\persis.jmf|3   |
	+-------+------------------+----+
	   

We see that currently variable  `A` in locale  `base` is mapped to file  `F` (persis.jmf).  

Under "refs", the value  `3` means that the datain file  `F` is the target of 3 references.One of these is variable  `A`, a second is the variable  `B` (which we know tobe another name for  `A`) and the third is for the system itself. 

Variables  `A` and  `B` are both in existence: 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>B</TT></TD>
<TR VALIGN=TOP>
<TD><TT>8</TT></TD>
<TD><TT>8</TT></TD>
</TABLE>

For the sake of simplicity, a recommended procedure for closing the file is first to erase all variables such as  `B` which are alternative names for the originally-mappedvariable  `A`

	   erase <'B' 
	1

The status shows the number of references is reduced. 

	   status ''
	+-------+------------------+----+
	|name   |fn                |refs|
	+-------+------------------+----+
	|A_base_|c:\temp\persis.jmf|2   |
	+-------+------------------+----+

Now we can unmap  `A`.   

	   unmap_jmf_ 'A'
	0

The result of  `0` means the file is closed and  `A` erased. The status table shows no entries, that is, that no files are mapped. 

	   status ''
	+----+--+----+
	|name|fn|refs|
	+----+--+----+
	   

Let us recreate the situation in which  `A` is mapped to  `F`and  `B` is another name for  `A`, so thereare 3 references to (the data in) file  `F`. 

	   map_jmf_ 'A'; F
	   B =: A
	   status ''
	+-------+------------------+----+
	|name   |fn                |refs|
	+-------+------------------+----+
	|A_base_|c:\temp\persis.jmf|3   |
	+-------+------------------+----+

What happens if we erase all the variables referring to  `F` ? 

	   erase 'A';'B'
	1 1
	   status ''
	+-------+------------------+----+
	|name   |fn                |refs|
	+-------+------------------+----+
	|A_base_|c:\temp\persis.jmf|1   |
	+-------+------------------+----+

We see there is still a single reference,under the name  `A` even though thereis no variable  `A`.  This singlereference reflects the fact that file  `F`is not yet unmapped.  

Thus when we saidearlier that file  `F` gets mapped tovariable  `A`, it would be more accurateto say that file  `F` gets mapped to the name  `A`, and a variable of that name iscreated.  Even though the variable is subsequently erased,the name  `A` still identifies the mapped file,and can be used as an argument to  `unmap`. 

	   unmap_jmf_ 'A'
	0
	   status ''
	+----+--+----+
	|name|fn|refs|
	+----+--+----+

For more information, see the "Mapped Files" lab. 

This is the end of Chapter 28    
