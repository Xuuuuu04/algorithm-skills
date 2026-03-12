# CF-44E Anfisa the Monkey

## 题面快照

## Description

Anfisa the monkey learns to type. She is yet unfamiliar with the "space" key and can only type in lower-case Latin letters. Having typed for a fairly long line, Anfisa understood that it would be great to divide what she has written into k lines not shorter than a and not longer than b, for the text to resemble human speech more. Help Anfisa.

## Input

Input

The first line contains three integers k, a and b (1 ≤ k ≤ 200, 1 ≤ a ≤ b ≤ 200). The second line contains a sequence of lowercase Latin letters — the text typed by Anfisa. It is guaranteed that the given line is not empty and its length does not exceed 200 symbols.

## Output

Output

Print k lines, each of which contains no less than a and no more than b symbols — Anfisa's text divided into lines. It is not allowed to perform any changes in the text, such as: deleting or adding symbols, changing their order, etc. If the solution is not unique, print any of them. If there is no solution, print "No solution" (without quotes).

## Samples

### Sample 1

Input
```
3 2 5
abrakadabra
```

Output
```
ab
rakad
abra
```

### Sample 2

Input
```
4 1 2
abrakadabra
```

Output
```
No solution
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-44E |
| Contest | 44 |
| Index | E |
| Rating | 1400 |
| Points | - |
| Codeforces 标签 | `dp` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 6050 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 2 seconds |
| 内存限制 | 256 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/44/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/44/problem/E)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/44/E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

