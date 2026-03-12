# CF-83D Numbers

## 题面快照

## Description

One quite ordinary day Valera went to school (there's nowhere else he should go on a week day). In a maths lesson his favorite teacher Ms. Evans told students about divisors. Despite the fact that Valera loved math, he didn't find this particular topic interesting. Even more, it seemed so boring that he fell asleep in the middle of a lesson. And only a loud ringing of a school bell could interrupt his sweet dream.

Of course, the valuable material and the teacher's explanations were lost. However, Valera will one way or another have to do the homework. As he does not know the new material absolutely, he cannot do the job himself. That's why he asked you to help. You're his best friend after all, you just cannot refuse to help.

Valera's home task has only one problem, which, though formulated in a very simple way, has not a trivial solution. Its statement looks as follows: if we consider all positive integers in the interval [a;b] then it is required to count the amount of such numbers in this interval that their smallest divisor will be a certain integer k(you do not have to consider divisor equal to one). In other words, you should count the amount of such numbers from the interval [a;b], that are not divisible by any number between 2 and k - 1 and yet are divisible by k.

The first and only line contains three positive integers a, b, k (1 ≤ a ≤ b ≤ 2·109, 2 ≤ k ≤ 2·109).

Print on a single line the answer to the given problem.

## Input

The first and only line contains three positive integers a, b, k (1 ≤ a ≤ b ≤ 2·109, 2 ≤ k ≤ 2·109).

## Output

Print on a single line the answer to the given problem.

## Samples

```
1 10 2

```

```
5

```

```
12 23 3

```

```
2

```

```
6 19 5

```

```
0

```

## Note

Comments to the samples from the statement:

In the first sample the answer is numbers 2, 4, 6, 8, 10.

In the second one — 15, 21

In the third one there are no such numbers.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-83D |
| Contest | 83 |
| Index | D |
| Rating | 2400 |
| Points | - |
| Codeforces 标签 | `dp`、`math`、`number theory` |
| 镜像标签 | `dp`、`math`、`number theory`、`*2400` |
| Codeforces 通过次数 | 1022 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/83/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/83/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P83D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

