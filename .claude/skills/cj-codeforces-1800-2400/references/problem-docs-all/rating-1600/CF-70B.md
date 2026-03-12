# CF-70B Text Messaging

## 题面快照

## Description

Fangy the little walrus, as all the modern walruses, loves to communicate via text messaging. One day he faced the following problem: When he sends large texts, they are split into parts each containing n characters (which is the size of one text message). Thus, whole sentences and words get split!

Fangy did not like it, so he faced the task of breaking the text into minimal messages on his own so that no sentence were broken into pieces when it is sent and the number of text messages to be sent would be minimal. If two consecutive sentences are in different messages, the space between them can be ignored (Fangy does not write this space).

The little walrus's text looks in the following manner:

```
TEXT ::= SENTENCE | SENTENCE SPACE TEXT
SENTENCE ::= WORD SPACE SENTENCE | WORD END
END ::= {'.', '?', '!'}
WORD ::= LETTER | LETTER WORD
LETTER ::= {'a'..'z', 'A'..'Z'}
SPACE ::= ' '

```

SPACE stands for the symbol of a space.

So, how many messages did Fangy send?

The first line contains an integer n, which is the size of one message (2 ≤ n ≤ 255). The second line contains the text. The length of the text does not exceed 104 characters. It is guaranteed that the text satisfies the above described format. Specifically, this implies that the text is not empty.

On the first and only line print the number of text messages Fangy will need. If it is impossible to split the text, print "Impossible" without the quotes.

## Input

The first line contains an integer n, which is the size of one message (2 ≤ n ≤ 255). The second line contains the text. The length of the text does not exceed 104 characters. It is guaranteed that the text satisfies the above described format. Specifically, this implies that the text is not empty.

## Output

On the first and only line print the number of text messages Fangy will need. If it is impossible to split the text, print "Impossible" without the quotes.

## Samples

```
25
Hello. I am a little walrus.

```

```
2

```

```
2
How are you?

```

```
Impossible

```

```
19
Hello! Do you like fish? Why?

```

```
3

```

## Note

Let's take a look at the third sample. The text will be split into three messages: "Hello!", "Do you like fish?" and "Why?".

-  登录后递交

-

-  讨论 (0)

-  题解 (0)

-  文件

-  统计

-

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-70B |
| Contest | 70 |
| Index | B |
| Rating | 1600 |
| Points | 1000.0 |
| Codeforces 标签 | `expression parsing`、`greedy`、`strings` |
| 镜像标签 | `expression parsing`、`greedy`、`strings`、`*1600` |
| Codeforces 通过次数 | 2086 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/70/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/70/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P70B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

