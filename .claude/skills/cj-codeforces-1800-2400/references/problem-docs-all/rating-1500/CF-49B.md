# CF-49B Sum

## 题面快照

## Description

Vasya studies positional numeral systems. Unfortunately, he often forgets to write the base of notation in which the expression is written. Once he saw a note in his notebook saying a + b = ?, and that the base of the positional notation wasn’t written anywhere. Now Vasya has to choose a base p and regard the expression as written in the base p positional notation. Vasya understood that he can get different results with different bases, and some bases are even invalid. For example, expression 78 + 87 in the base 16 positional notation is equal to FF16, in the base 15 positional notation it is equal to 11015, in the base 10 one — to 16510, in the base 9 one — to 1769, and in the base 8 or lesser-based positional notations the expression is invalid as all the numbers should be strictly less than the positional notation base. Vasya got interested in what is the length of the longest possible expression value. Help him to find this length.

The length of a number should be understood as the number of numeric characters in it. For example, the length of the longest answer for 78 + 87 = ? is 3. It is calculated like that in the base 15 (11015), base 10 (16510), base 9 (1769) positional notations, for example, and in some other ones.

## Input

Input

The first letter contains two space-separated numbers a and b (1 ≤ a, b ≤ 1000) which represent the given summands.

## Output

Output

Print a single number — the length of the longest answer.

## Samples

### Sample 1

Input
```
78 87
```

Output
```
3
```

### Sample 2

Input
```
1 1
```

Output
```
2
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-49B |
| Contest | 49 |
| Index | B |
| Rating | 1500 |
| Points | 1000.0 |
| Codeforces 标签 | `math` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 2764 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 2 seconds |
| 内存限制 | 256 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/49/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/49/problem/B)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/49/B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

