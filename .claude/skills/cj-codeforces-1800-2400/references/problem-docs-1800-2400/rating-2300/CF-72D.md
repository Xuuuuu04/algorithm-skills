# CF-72D Perse-script

## 题面快照

## Description

Two good friends were trying to make a new programming language called Perse-script.

The most important part of this language is strings. A string in Perse-script is put between characters "

So for example "Hello" is a string. But Hello is a variable name or a keyword, which are not considered in this problem.

Perse-script is function-based. So there are no operators in this language. For example for summing two numbers you have to write sum(a,b) and not a+b.

There are several functions for working on strings. These include:

- concat(x,y) is a function which gets two strings x and y and puts y at the end of x and returns the result. For example concat("Hello","World") returns "HelloWorld".

- reverse(x) gets a single string x and reverses it. For example reverse("Hello") returns "olleH".

- substr(x,a,b) gets a string x and two integers a and b (1 ≤ a ≤ b ≤ n, where n is the length of x). And returns the substring of x between indexes a and b, inclusive. For example substr("Hello",2,4) returns "ell".

- substr(x,a,b,c) is another version of substr which works just like the last one but c is the step of adding. c is positive. For example substr("HelloWorld",1,10,2) returns "Hlool". This substr means that you put the ath character , and then every cth character until you reach b.

You're going to manipulate the string part of Perse-script. Given a string expression, you should print its result. It is guaranteed that the expression contains only strings shown by characters " and the above functions.

Commands in Perse-script are case-insensitive. So to call substr function you can write SUBsTr(). But you can't print as the result "hElLo" instead of printing "Hello".

See the samples for more information.

A single line containing the correct expression. It is guaranteed that the total length of this expression does not exceed 103 and that all the integers used in it are less than or equal to 100 by absolute value. The given string is non-empty.

All strings in the input which are placed between "s consist of uppercase and lowercase Latin letters only.

Print in single line the resulting string. It is guaranteed that an answer exists and that the length of the answer does not exceed 104. It is guaranteed that the answer is non-empty.

## Input

A single line containing the correct expression. It is guaranteed that the total length of this expression does not exceed 103 and that all the integers used in it are less than or equal to 100 by absolute value. The given string is non-empty.

All strings in the input which are placed between "s consist of uppercase and lowercase Latin letters only.

## Output

Print in single line the resulting string. It is guaranteed that an answer exists and that the length of the answer does not exceed 104. It is guaranteed that the answer is non-empty.

## Samples

```
"HelloWorld"

```

```
"HelloWorld"

```

```
REVerse(substr("helloworld",1,5))

```

```
"olleh"

```

```
conCAT(rEveRSE("olleh"),"world")

```

```
"helloworld"

```

```
reversE(concAT(substr("hello",1,2),sUbstr("world",1,5,1)))

```

```
"dlroweh"

```

```
suBstr("Noruz",1,4,2)

```

```
"Nr"

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-72D |
| Contest | 72 |
| Index | D |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `*special`、`expression parsing` |
| 镜像标签 | `*special problem`、`expression parsing`、`*2300` |
| Codeforces 通过次数 | 83 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 7000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/72/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/72/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P72D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

