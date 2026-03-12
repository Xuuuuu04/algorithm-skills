# CF-56A Bar

## 题面快照

## Description

According to Berland laws it is only allowed to sell alcohol to people not younger than 18 years. Vasya's job is to monitor the law's enforcement. Tonight he entered a bar and saw n people sitting there. For every one of them Vasya happened to determine either the age or the drink the person is having. Vasya can check any person, i.e. learn his age and the drink he is having at the same time. What minimal number of people should Vasya check additionally to make sure that there are no clients under 18 having alcohol drinks?

The list of all alcohol drinks in Berland is: ABSINTH, BEER, BRANDY, CHAMPAGNE, GIN, RUM, SAKE, TEQUILA, VODKA, WHISKEY, WINE

The first line contains an integer n (1 ≤ n ≤ 100) which is the number of the bar's clients. Then follow n lines, each describing one visitor. A line either contains his age (an integer from 0 to 1000) or his drink (a string of capital Latin letters from 1 to 100 in length). It is guaranteed that the input data does not contain spaces and other unnecessary separators.

Only the drinks from the list given above should be considered alcohol.

Print a single number which is the number of people Vasya should check to guarantee the law enforcement.

## Input

The first line contains an integer n (1 ≤ n ≤ 100) which is the number of the bar's clients. Then follow n lines, each describing one visitor. A line either contains his age (an integer from 0 to 1000) or his drink (a string of capital Latin letters from 1 to 100 in length). It is guaranteed that the input data does not contain spaces and other unnecessary separators.

Only the drinks from the list given above should be considered alcohol.

## Output

Print a single number which is the number of people Vasya should check to guarantee the law enforcement.

## Samples

```
5
18
VODKA
COKE
19
17

```

```
2

```

## Note

In the sample test the second and fifth clients should be checked.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-56A |
| Contest | 56 |
| Index | A |
| Rating | 1000 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1000` |
| Codeforces 通过次数 | 9534 |
| 镜像尝试 / 通过 | 2 / 2 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/56/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/56/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P56A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

