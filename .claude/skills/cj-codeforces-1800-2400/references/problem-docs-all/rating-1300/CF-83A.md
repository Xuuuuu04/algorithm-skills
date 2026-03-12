# CF-83A Magical Array

## 题面快照

## Description

Valery is very interested in magic. Magic attracts him so much that he sees it everywhere. He explains any strange and weird phenomenon through intervention of supernatural forces. But who would have thought that even in a regular array of numbers Valera manages to see something beautiful and magical.

Valera absolutely accidentally got a piece of ancient parchment on which an array of numbers was written. He immediately thought that the numbers in this array were not random. As a result of extensive research Valera worked out a wonderful property that a magical array should have: an array is defined as magic if its minimum and maximum coincide.

He decided to share this outstanding discovery with you, but he asks you for help in return. Despite the tremendous intelligence and wit, Valera counts very badly and so you will have to complete his work. All you have to do is count the number of magical subarrays of the original array of numbers, written on the parchment. Subarray is defined as non-empty sequence of consecutive elements.

## Input

Input

The first line of the input data contains an integer n (1 ≤ n ≤ 105). The second line contains an array of original integers a1, a2, ..., an ( - 109 ≤ ai ≤ 109).

## Output

Output

Print on the single line the answer to the problem: the amount of subarrays, which are magical.

Please do not use the %lld specificator to read or write 64-bit numbers in C++. It is recommended to use cin, cout streams (you can also use the %I64d specificator).

## Samples

### Sample 1

Input
```
4
2 1 1 4
```

Output
```
5
```

### Sample 2

Input
```
5
-2 -2 -2 0 1
```

Output
```
8
```

## Note

Note

Notes to sample tests:

Magical subarrays are shown with pairs of indices [a;b] of the beginning and the end.

In the first sample: [1;1], [2;2], [3;3], [4;4], [2;3].

In the second sample: [1;1], [2;2], [3;3], [4;4], [5;5], [1;2], [2;3], [1;3].

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-83A |
| Contest | 83 |
| Index | A |
| Rating | 1300 |
| Points | 500.0 |
| Codeforces 标签 | `math` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 6800 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 2 seconds |
| 内存限制 | 256 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/83/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/83/problem/A)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/83/A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

