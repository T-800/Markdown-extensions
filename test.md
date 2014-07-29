[TOC]



# Test 1
%
\begin{align*}
(a+b)^3 &= (a+b)^2(a+b)\\
&=(a^2+2ab+b^2)(a+b)\\
&=(a^3+2a^2b+ab^2)+(a^2b+2ab^2+b^3)\\
&=a^3+3a^2b+3ab^2+b^3
\end{align*}
%
<dot>
digraph a {
    graph [rankdir=LR]
    0 -> 1 -> 4 -> 3 -> 2 -> 0 [label="b"]
    0 -> 2 [style=bold,label="a"]
    1 -> 2 [label="c"]
    2 -> 3 [label="d"]
    3 -> 0 [label="e"]
    4 -> 4

    0 [color=blue]
    4 [color=red]
}
</dot>


test inline $$\sqrt{2} \sin x$$, $$\sqrt{2}\,\sin x$$ fin test

test Block

$$
\int_0^\infty e^{-x^2} dx=\frac{\sqrt{\pi}}{2}
$$

fin test

    public static void main(String[] args){
        System.out.println("Hello");
    }



1. a
1. b
1. c

# test 2

The HTML specification
is maintained by the W3C.

## Test sub 1

$$
F(x,y)=0 ~~\mbox{and}~~
\left| \begin{array}{ccc}
  F''_{xx} & F''_{xy} &  F'_x \\
  F''_{yx} & F''_{yy} &  F'_y \\
  F'_x     & F'_y     & 0
  \end{array}\right| = 0
$$


    \begin{eqnarray}
    && \int 1 = x + C \nonumber\\
    && \int x = \frac{x^2}{2} + C \nonumber\\
    && \int x^2 = \frac{x^3}{3} + C \label{eq:xdef}
    \end{eqnarray}



First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

    ficIn = open("test.md", 'r')
    txt = ficIn.read()
    ficIn.close()
    ficOut = open("test.html", 'w')

$$\setlength{\unitlength}{0.75mm}
\begin{picture}(60,40)
\put(30,20){\vector(1,0){30}}
\put(30,20){\vector(4,1){20}}
\put(30,20){\vector(3,1){25}}
\put(30,20){\vector(2,1){30}}
\put(30,20){\vector(1,2){10}}
\thicklines
\put(30,20){\vector(-4,1){30}}
\put(30,20){\vector(-1,4){5}}
\thinlines
\put(30,20){\vector(-1,-1){5}}
\put(30,20){\vector(-1,-4){5}}
\end{picture}$$


This is some text above a graph.

<dot>
digraph a {
    nodesep=1.0;
    rankdir=LR;
    a -> b -> c ->d;
}
</dot>

Some other text between two graphs.


This is also some text below a graph.

$$
\setlength{\unitlength}{0.8cm}
\begin{picture}(6,4)
\linethickness{0.075mm}
\multiput(0,0)(1,0){7}
{\line(0,1){4}}
\multiput(0,0)(0,1){5}
{\line(1,0){6}}
\thicklines
\put(0.5,0.5){\line(1,5){0.5}}
\put(1,3){\line(4,1){2}}
\qbezier(0.5,0.5)(1,3)(3,3.5)
\thinlines
\put(2.5,2){\line(2,-1){3}}
\put(5.5,0.5){\line(-1,5){0.5}}
\linethickness{1mm}
\qbezier(2.5,2)(5.5,0.5)(5,3)
\thinlines
\qbezier(4,2)(4,3)(3,3)
\qbezier(3,3)(2,3)(2,2)
\qbezier(2,2)(2,1)(3,1)
\qbezier(3,1)(4,1)(4,2)
\end{picture}
$$

$$
\setlength{\unitlength}{0.8cm}
\begin{picture}(6,5)
\thicklines
\put(1,0.5){\line(2,1){3}}
\put(4,2){\line(-2,1){2}}
\put(2,3){\line(-2,-5){1}}
\put(0.7,0.3){$A$}
\put(4.05,1.9){$B$}
\put(1.7,2.95){$C$}
\put(3.1,2.5){$a$}
\put(1.3,1.7){$b$}
\put(2.5,1.05){$c$}
\put(0.3,4){$F=
\sqrt{s(s-a)(s-b)(s-c)}$}
\put(3.5,0.4){$\displaystyle
s:=\frac{a+b+c}{2}$}
\end{picture}
$$


%\begin{equation}
\Re{z} =\frac{n\pi \dfrac{\theta +\psi}{2}}{
\left(\dfrac{\theta +\psi}{2}\right)^2 + \left( \dfrac{1}{2}
\log \left\lvert\dfrac{B}{A}\right\rvert\right)^2}.
\end{equation}

\begin{equation}
\boxed{\eta \leq C(\delta(\eta) +\Lambda_M(0,\delta))}
\end{equation}

\begin{equation}\label{first}
a=b+c
\end{equation}

\begin{subequations}\label{grp}
\begin{align}
a&=b+c\label{second}\\
d&=e+f+g\label{third}\\
h&=i+j\label{fourth}
\end{align}
\end{subequations}%
