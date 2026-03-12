# CF-18E Flag 2

## 题面快照

## Description

According to a new ISO standard, a flag of every country should have, strangely enough, a chequered field n × m, each square should be wholly painted one of 26 colours. The following restrictions are set:

-  In each row at most two different colours can be used.

-  No two adjacent squares can be painted the same colour.

Pay attention, please, that in one column more than two different colours can be used.

Berland's government took a decision to introduce changes into their country's flag in accordance with the new standard, at the same time they want these changes to be minimal. By the given description of Berland's flag you should find out the minimum amount of squares that need to be painted different colour to make the flag meet the new ISO standard. You are as well to build one of the possible variants of the new Berland's flag.

The first input line contains 2 integers n and m (1 ≤ n, m ≤ 500) — amount of rows and columns in Berland's flag respectively. Then there follows the flag's description: each of the following n lines contains m characters. Each character is a letter from a to z, and it stands for the colour of the corresponding square.

In the first line output the minimum amount of squares that need to be repainted to make the flag meet the new ISO standard. The following n lines should contain one of the possible variants of the new flag. Don't forget that the variant of the flag, proposed by you, should be derived from the old flag with the minimum amount of repainted squares. If the answer isn't unique, output any.

## Input

The first input line contains 2 integers n and m (1 ≤ n, m ≤ 500) — amount of rows and columns in Berland's flag respectively. Then there follows the flag's description: each of the following n lines contains m characters. Each character is a letter from a to z, and it stands for the colour of the corresponding square.

## Output

In the first line output the minimum amount of squares that need to be repainted to make the flag meet the new ISO standard. The following n lines should contain one of the possible variants of the new flag. Don't forget that the variant of the flag, proposed by you, should be derived from the old flag with the minimum amount of repainted squares. If the answer isn't unique, output any.

## Samples

```
3 4
aaaa
bbbb
cccc

```

```
6
abab
baba
acac

```

```
3 3
aba
aba
zzz

```

```
4
aba
bab
zbz

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-18E |
| Contest | 18 |
| Index | E |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `dp` |
| 镜像标签 | `dp`、`*2000` |
| Codeforces 通过次数 | 1249 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 128MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/18/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/18/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P18E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

