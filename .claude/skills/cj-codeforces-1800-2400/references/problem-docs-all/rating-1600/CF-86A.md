# CF-86A Reflection

## 题面快照

## Description

For each positive integer n consider the integer ψ(n) which is obtained from n by replacing every digit a in the decimal notation of n with the digit (9 - a). We say that ψ(n) is the reflection of n. For example, reflection of 192 equals 807. Note that leading zeros (if any) should be omitted. So reflection of 9 equals 0, reflection of 91 equals 8.

Let us call the weight of the number the product of the number and its reflection. Thus, the weight of the number 10 is equal to 10·89 = 890.

Your task is to find the maximum weight of the numbers in the given range [l, r] (boundaries are included).

Input contains two space-separated integers l and r (1 ≤ l ≤ r ≤ 109) — bounds of the range.

Output should contain single integer number: maximum value of the product n·ψ(n), where l ≤ n ≤ r.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preferred to use cout (also you may use %I64d).

## Input

Input contains two space-separated integers l and r (1 ≤ l ≤ r ≤ 109) — bounds of the range.

## Output

Output should contain single integer number: maximum value of the product n·ψ(n), where l ≤ n ≤ r.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preferred to use cout (also you may use %I64d).

## Samples

```
3 7

```

```
20

```

```
1 1

```

```
8

```

```
8 10

```

```
890

```

## Note

In the third sample weight of 8 equals 8·1 = 8, weight of 9 equals 9·0 = 0, weight of 10 equals 890.

Thus, maximum value of the product is equal to 890.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-86A |
| Contest | 86 |
| Index | A |
| Rating | 1600 |
| Points | 500.0 |
| Codeforces 标签 | `math` |
| 镜像标签 | `math`、`*1600` |
| Codeforces 通过次数 | 1641 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/86/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/86/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P86A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

