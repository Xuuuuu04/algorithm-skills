# CF-86D Powerful array

## 题面快照

## Description

An array of positive integers a1, a2, ..., an is given. Let us consider its arbitrary subarray al, al + 1..., ar, where 1 ≤ l ≤ r ≤ n. For every positive integer s denote by Ks the number of occurrences of s into the subarray. We call the power of the subarray the sum of products Ks·Ks·s for every positive integer s. The sum contains only finite number of nonzero summands as the number of different values in the array is indeed finite.

You should calculate the power of t given subarrays.

First line contains two integers n and t (1 ≤ n, t ≤ 200000) — the array length and the number of queries correspondingly.

Second line contains n positive integers ai (1 ≤ ai ≤ 106) — the elements of the array.

Next t lines contain two positive integers l, r (1 ≤ l ≤ r ≤ n) each — the indices of the left and the right ends of the corresponding subarray.

Output t lines, the i-th line of the output should contain single positive integer — the power of the i-th query subarray.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preferred to use cout stream (also you may use %I64d).

## Input

First line contains two integers n and t (1 ≤ n, t ≤ 200000) — the array length and the number of queries correspondingly.

Second line contains n positive integers ai (1 ≤ ai ≤ 106) — the elements of the array.

Next t lines contain two positive integers l, r (1 ≤ l ≤ r ≤ n) each — the indices of the left and the right ends of the corresponding subarray.

## Output

Output t lines, the i-th line of the output should contain single positive integer — the power of the i-th query subarray.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preferred to use cout stream (also you may use %I64d).

## Samples

```
3 2
1 2 1
1 2
1 3

```

```
3
6

```

```
8 3
1 1 2 2 1 3 1 1
2 7
1 6
2 7

```

```
20
20
20

```

## Note

Consider the following array (see the second sample) and its [2, 7] subarray (elements of the subarray are colored):
Then K1 = 3, K2 = 2, K3 = 1, so the power is equal to 32·1 + 22·2 + 12·3 = 20.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-86D |
| Contest | 86 |
| Index | D |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `data structures`、`implementation`、`math`、`two pointers` |
| 镜像标签 | `data structures`、`implementation`、`math`、`two pointers`、`*2200` |
| Codeforces 通过次数 | 16494 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/86/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/86/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P86D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

