# CF-63C Bulls and Cows

## 题面快照

## Description

The "Bulls and Cows" game needs two people to play. The thinker thinks of a number and the guesser tries to guess it.

The thinker thinks of a four-digit number in the decimal system. All the digits in the number are different and the number may have a leading zero. It can't have more than one leading zero, because all it's digits should be different. The guesser tries to guess the number. He makes a series of guesses, trying experimental numbers and receives answers from the first person in the format "x bulls y cows". x represents the number of digits in the experimental number that occupy the same positions as in the sought number. y represents the number of digits of the experimental number that present in the sought number, but occupy different positions. Naturally, the experimental numbers, as well as the sought number, are represented by four-digit numbers where all digits are different and a leading zero can be present.

For example, let's suppose that the thinker thought of the number 0123. Then the guessers' experimental number 1263 will receive a reply "1 bull 2 cows" (3 occupies the same positions in both numbers and 1 and 2 are present in both numbers but they occupy different positions). Also, the answer to number 8103 will be "2 bulls 1 cow" (analogically, 1 and 3 occupy the same positions and 0 occupies a different one).

When the guesser is answered "4 bulls 0 cows", the game is over.

Now the guesser has already made several guesses and wants to know whether his next guess can possibly be the last one.

The first input line contains an integer n (1 ≤ n ≤ 10) which represents the number of already made guesses. Then follow n lines in the form of "aibici", where ai is the i-th experimental number, bi is the number of bulls, ci is the number of cows (1 ≤ i ≤ n, 0 ≤ bi, ci, bi + ci ≤ 4). The experimental numbers are correct, i.e., each of them contains exactly four digits, in each of them all the four digits are different, and there can be a leading zero. All the experimental numbers are different. As the guesser hasn't guessed the number yet, the answer "4 bulls 0 cows" is not present.

If the input data is enough to determine the sought number, print the number with four digits on a single line. If it has less than four digits, add leading zero. If the data is not enough, print "Need more data" without the quotes. If the thinker happens to have made a mistake in his replies, print "Incorrect data" without the quotes.

## Input

The first input line contains an integer n (1 ≤ n ≤ 10) which represents the number of already made guesses. Then follow n lines in the form of "aibici", where ai is the i-th experimental number, bi is the number of bulls, ci is the number of cows (1 ≤ i ≤ n, 0 ≤ bi, ci, bi + ci ≤ 4). The experimental numbers are correct, i.e., each of them contains exactly four digits, in each of them all the four digits are different, and there can be a leading zero. All the experimental numbers are different. As the guesser hasn't guessed the number yet, the answer "4 bulls 0 cows" is not present.

## Output

If the input data is enough to determine the sought number, print the number with four digits on a single line. If it has less than four digits, add leading zero. If the data is not enough, print "Need more data" without the quotes. If the thinker happens to have made a mistake in his replies, print "Incorrect data" without the quotes.

## Samples

```
2
1263 1 2
8103 2 1

```

```
Need more data

```

```
2
1234 2 2
1256 0 2

```

```
2134

```

```
2
0123 1 1
4567 1 2

```

```
Incorrect data

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-63C |
| Contest | 63 |
| Index | C |
| Rating | 1700 |
| Points | 1500.0 |
| Codeforces 标签 | `brute force`、`implementation` |
| 镜像标签 | `brute force`、`implementation`、`*1700` |
| Codeforces 通过次数 | 1977 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/63/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/63/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P63C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

