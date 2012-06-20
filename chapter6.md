# 제 6장: 인덱싱

Indexing is the name given to selecting of elements of arrays by position. This topic includes selecting elements, rearranging selected elements to form new arrays, and amending, or updating, selected elements of arrays. 

## 6.1  Selecting

The verb `{` (left-brace) is called "From".  The expression `(x { y)` selects elements from `y` according to positions given by `x`.  For example, recall from Chapter 02 that if `L` is a list, then the positions of items of `L` are numbered 0 1 and so on.  The expression `(0 { L)` gives the value of the first item of `L` and `1 { L` gives the second item.   

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

The left argument of `{` is called the "index".

### 6.1.1  Common Patterns of Selection.

Several items may be selected together:  

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L </TT></TD>
<TD><TT>0 2 4 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>ace</TT></TD>
</TABLE>

Items selected from `L` may be replicated and re-ordered:

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L </TT></TD>
<TD><TT>5 4 4 3 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>feed</TT></TD>
</TABLE>

An index value may be negative: a value of `_1` selects the last item, `_2` selects the next-to-last item and so on. Positive and negative indices may be mixed.

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

A single element of a table at, say, row 1 column 2is selected with an index `(&lt; 1 ; 2)`.

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

We can select from a table all elements in specified rows and columns, to produce a smaller table (called a subarray).  To select a subarray consisting of, for example rows `1` and `2` and columns `0` and `1`, we use an index `(&lt; 1 2; 0 1)`

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

A complete row or rows may be selected from a table. Recall that a table is a list of items, each item being a row. Thus selecting rows from tables is just like selecting items from lists. 

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

To select a complete column or columns,a straightforward way isto select all the rows:

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

but there are other possibilities: see below.

### 6.1.2  Take, Drop, Head, Behead, Tail, Curtail

Next we look at a group of verbs providing some convenient short forms of indexing.There is a built-in verb `{.` (left brace dot,  called "Take"). The first `n` items of list `L` are selected by `(n {. L)`

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>2 {. L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>ab</TT></TD>
</TABLE>

If we take `n` items from `L` with`(n {. L)`,and `n` is greater than the length of `L`,the result is padded to length `n`, with zeros, spaces or empty boxes as appropriate. 

For example, supposewe require to make a string of exactly 8 charactersfrom a given string, a description of some kind, which maybe longer or shorter than 8. If longer, we shorten. If shorter we pad with spaces.

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

There is a built-in verb `}.` (right-brace dot, called "Drop").All but the first `n` items of `L` are selected by`(n }. L)`. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L</TT></TD>
<TD><TT>2 }. L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>cdef</TT></TD>
</TABLE>

The last `n` items of `L` are selected by `(-n) {. L`. All but the last `n` are selected by `(-n) }. L`

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

There are abbreviations of Take and Drop inthe special case where `n=1`. The first item of a list is selected by monadic `{.`(left-brace dot, called "Head").  All but the firstare selected by `}.` (right-brace dot, called "Behead").

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

The last item of a list is selected by monadic `{:`(left-brace colon, called "Tail").  All but the lastare selected by `}:` (right-brace colon, called "Curtail".

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

## 6.2  General Treatment of Selection

It will help to have some terminology.  In general we will have an n-dimensional array, but consider a 3-dimensional array.  A single element is picked out by giving a plane-number, a row-number and a column-number.  We say that the planes are laid out in order along the first axis, and similarly the rows along the second axis, and the columns along the third. 

There is no special notation for indexing; rather the left argument of `{` is a data structure which expresses, or encodes, selections and rearrangements. This data structure can be built in any way convenient. What follows is an explanation of how to build it.

### 6.2.1  Independent Selections

The general expression for indexing is of the form `index { array`. Here `index`is an array of scalars. Each scalar in `index` gives rise to a separateindependent selection, and the results are assembled together. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>L </TT></TD>
<TD><TT> 0 1 { L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>ab</TT></TD>
</TABLE>

### 6.2.2  Shape of Index

The shape of the results depends on the shape of `index`. 

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

The indices must lie within the range `-#L` to `(#L)-1`:

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

### 6.2.3  Scalars

Each scalar in `index` is either a single number or a box (and of course if one is a box, all are.)If the scalar is a single number it selects an item from `array`. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A =: 2 3 $ 'abcdef'</TT></TD>
<TD><TT>1 { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>def</TT></TD>
</TABLE>

If the scalar in `index` is a box however then it contains a list of selectors which are applied to successive axes.To show where a box is used for this purpose, we can use the name `SuAx`, say, for the box function.

	   SuAx =: <

The following example selects from `A` the element at row 1, column 0. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx 1 0) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>d</TT></TD>
</TABLE>

### 6.2.4  Selections on One Axis

In a list of selectors for successive axes, of the form `(SuAx p , r, c)` say,each of `p`, `r` and `c` is a scalar. This scalar is either a number or a box (and if one is boxed, all are).A number selects one thing on its axis: one plane, row or column as appropriate, as in the last example.

However, if the selector is a box it contains a list of selections all applicable to the sameaxis. To show where a box is used for this purpose we can use the name `Sel`, say, for the box function.

	   Sel =: <

For example, to select from `A` elements at row 1, columns 0 2:

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 1), (Sel 0 2)) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>df</TT></TD>
</TABLE>

### 6.2.5  Excluding Things

Instead of selecting things on a particular axis, we can exclude things, by supplying a list ofthing-numbers enclosed in yet another level of boxing.To show where a box is used for this purpose we can use the name `Excl`, say, for the box function.

	   Excl =: <

For example, to select from `A` elements at row 0, all columns excluding column 1:

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 0), (Sel (Excl 1))) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>ac</TT></TD>
</TABLE>

We can select all things on a particular axis by excluding nothing, that is, giving an emptylist `(0$0)` as a list of thing-numbers to exclude.For example, to select from `A` elements at row 1, all columns:

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 1),(Sel (Excl 0$0))) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>def</TT></TD>
</TABLE>

### 6.2.6  Simplifications

The expression `(Excl 0$0)` denotes a boxed emptylist. There is a built-in J abbreviation for this,namely `(a:)` (letter-a colon, called "Ace"), which in this context we can think of as meaning "all".

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>A</TT></TD>
<TD><TT>(SuAx (Sel 1),(Sel a:)) { A</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abc<BR>
def</TT></TD>
<TD><TT>def</TT></TD>
</TABLE>

If in any index of the form `(SuAx p,q,..., z)`, the last selector `z` is the "all" form, `(Sel (Excl 0$0))` or `(Sel a:)`, then it can be omitted.

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

If in any index of the form `(SuAx (Sel p),(Sel q),...)`, the "all" form is entirely absent,then the index can be abbreviated to `(SuAx p;q;...)`. For example, to select elements atrow 1, columns 0 and 2:

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

Finally, as we have already seen, if selecting only one thing on each axis, a simple unboxed list is sufficient. For example to select  the element at row 1, column 2:

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

### 6.2.7  Shape of the Result

Suppose that `B` is a 3-dimensional array:

	   B =: 10 + i. 3 3 3

and we define `p` to select planes along the first axis of `B`,and `r` to select rows along the second axis, and `c` to select columns along the third axis:

	   p =: 1 2
	   r =: 1 2
	   c =: 0 1

We see that, selecting with `p;r;c`, the shape of the result`R` is the concatenation of the shapes of `p`, `r` and `c`

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

In this last example, `r` is a scalar, so the shape of `r` is an empty list, and so the axis corresponding to `r`has disappeared, and so the result `T` is 2-dimensional.

## 6.3  Amending (or Updating)  Arrays

Sometimes we need to compute an array which is the same as an existing array except for new values at a comparatively small number of positions. We may speak of 'updating' or 'amending' an array at selected positions.  The J function for amending arrays is `}` (right brace, called "Amend"). 

### 6.3.1  Amending with an Index

To amend an array we need three things: the original array a specification of the position(s) at which the original is to be amended. This can be an index exactly like the index we have seen above for selection with `{`. new values to replace existing elements at specified positions.Consequently the J expression to perform an amendment may have the general form:

	        newvalues index } original

For example:  to amend list `L` to replace the first item (at index `0`) with '*':

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

`}` is an adverb, which takes `index` as its argument to yield the dyadic amending verb `(index })`. 

	   ReplaceFirst =: 0 }
	   '*' ReplaceFirst L
	*bcdef

`(index })` is a verb like any other, dyadic and yielding a value in the usual way. Therefore to change an array by amending needs the whole of the result to be reassigned to the old name.  Thus amendment often takes place on the pattern:

	                 A  =:  new index } A 

The J system ensures that this is an efficient computation with nounnecessary movement of data.

To amend a table at row 1 column 2, for example:

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

To amend multiple elements, a list of new values can be supplied, and they are taken in turn to replace a list of values selected by an index

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT> L</TT></TD>
<TD><TT> '*#' 1 2 } L</TT></TD>
<TR VALIGN=TOP>
<TD><TT>abcdef</TT></TD>
<TD><TT>a*#def</TT></TD>
</TABLE>

### 6.3.2  Amending with a Verb

Suppose that `Y` is a list of numbers, and we wish to amend it so that all numbers exceedinga given value `X` are replaced by `X`. (For the sake of thisexample, we here disregard the built-in J verb  `(&lt;.)` for this function.)

The indices at which `Y` is to be amended must be computed from `X` and `Y`.  Here is a function `f` to compute the indices:

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

The amending is done, in the way we have seen above, by supplying indices of `(X f Y)`:

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>Y</TT></TD>
<TD><TT>X (X f Y) } Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>98 102 101 99</TT></TD>
<TD><TT>98 100 100 99</TT></TD>
</TABLE>

The "Amend" adverb `}` allows the expression `(X (X f Y) } Y)`to be abbreviated as `(X f } Y)`. 

 <TABLE CELLPADDING=10 BORDER=1>
<TR  VALIGN=TOP>
<TD><TT>X (X f Y) } Y</TT></TD>
<TD><TT>X f } Y</TT></TD>
<TR VALIGN=TOP>
<TD><TT>98 100 100 99</TT></TD>
<TD><TT>98 100 100 99</TT></TD>
</TABLE>

Since `}` is an adverb, it can acceptas argument either the indices `(X f Y)` or the verb `f`.

	   cap =: f }
	   
	   10 cap 8 9 10 11
	8 9 10 10

Note that if verb `f` is to be supplied as argumentto adverb `}`, then `f` must be a dyad, althoughit may ignore `X` or `Y`. 

### 6.3.3  Linear Indices

We have just looked at amending lists with a verb. The purpose of the verb is to find the places at which to amend, that is, to compute from the values in a list the indices at which to amend. With a table rather than a list, the indices would have to be  2-dimensional, and the task of the verb in constructing the indices would be correspondingly more difficult.  It would be easier to flatten a table into a linear list,  amend it as a list, and rebuild the list into a table again.  

For example, suppose we have a table:

	   M =: 2 2 $ 13 52 51 14

Then, using our index-finding verb `f`, the flattening, amending and rebuilding is shown by:

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

However, there is a better way.First note that our index-finding verb `f` takes as argument, not `M`but `(LL =: , M)`. Thus information about the original shape of `M`is not available to the index-finder `f`. In this example, this does not matter, but in generalwe may want the index-finding to depend upon both the shape and the values in `M`. It would be betterif `f` took the whole of `M` as argument.In this case `f` must do its own flattening.Thus we redefine `f`:

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

Now the index finder `f` takes an array as argument,and delivers indices into the flattened array, so-called "linear indices".The amending process, with this new `f`, is shown by:

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

Finally, provided `f` delivers linear indices, then `(})` allowsthe last expression to be abbreviated as:

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

## 6.4  Tree Indexing

So far we have looked at indexing into rectangular arrays.There is also a form of indexing into boxed structures,which we can picture as "trees" having branches and leaves.For example:

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

Then data can be fetched from the tree by specifying a path from the root. The path is a sequence of choices,given as left argument to the verb `{::` (left-brace colon colon,called "Fetch")The path `0` will fetch the first branch, whilethe path `0;1` fetches the second leaf of the first branch:

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

The monadic form `{:: tree` is called the "Map" of `tree`.it has the same boxed structure as `tree` and shows the path to each leaf.

	   {:: tree
	+-------------+-------------------+
	|+-----+-----+|+-----+-----+-----+|
	||+-+-+|+-+-+|||+-+-+|+-+-+|+-+-+||
	|||0|0|||0|1|||||1|0|||1|1|||1|2|||
	||+-+-+|+-+-+|||+-+-+|+-+-+|+-+-+||
	|+-----+-----+|+-----+-----+-----+|
	+-------------+-------------------+

This is the end of Chapter 6.   