# CF-80A Panoramix's Prediction

## 题面快照

## Description

A prime number is a number which has exactly two distinct divisors: one and itself. For example, numbers 2, 7, 3 are prime, and 1, 6, 4 are not.

The next prime number after x is the smallest prime number greater than x. For example, the next prime number after 2 is 3, and the next prime number after 3 is 5. Note that there is exactly one next prime number after each number. So 5is not the next prime number for 2.

One cold April morning Panoramix predicted that soon Kakofonix will break free from his straitjacket, and this will be a black day for the residents of the Gallic countryside.

Panoramix's prophecy tells that if some day Asterix and Obelix beat exactly x Roman soldiers, where x is a prime number, and next day they beat exactly y Roman soldiers, where y is the next prime number after x, then it's time to wait for Armageddon, for nothing can shut Kakofonix up while he sings his infernal song.

Yesterday the Gauls beat n Roman soldiers and it turned out that the number n was prime! Today their victims were a troop of m Romans (m > n). Determine whether the Gauls should wait for the black day after today's victory of Asterix and Obelix?

The first and only input line contains two positive integers — n and m (2 ≤ n < m ≤ 50). It is guaranteed that n is prime.

Pretests contain all the cases with restrictions 2 ≤ n < m ≤ 4.

Print YES, if m is the next prime number after n, or NO otherwise.

## Input

The first and only input line contains two positive integers — n and m (2 ≤ n < m ≤ 50). It is guaranteed that n is prime.

Pretests contain all the cases with restrictions 2 ≤ n < m ≤ 4.

## Output

Print YES, if m is the next prime number after n, or NO otherwise.

## Samples

```
3 5

```

```
YES

```

```
7 11

```

```
YES

```

```
7 9

```

```
NO

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-80A |
| Contest | 80 |
| Index | A |
| Rating | 800 |
| Points | 500.0 |
| Codeforces 标签 | `brute force` |
| 镜像标签 | `brute force`、`*800` |
| Codeforces 通过次数 | 65207 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/80/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/80/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P80A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

