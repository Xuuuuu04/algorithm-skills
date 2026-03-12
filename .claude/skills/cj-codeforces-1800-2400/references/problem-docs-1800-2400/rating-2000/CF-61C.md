# CF-61C Capture Valerian

## 题面快照

## Description

It's now 260 AD. Shapur, being extremely smart, became the King of Persia. He is now called Shapur, His majesty King of kings of Iran and Aniran.

Recently the Romans declared war on Persia. They dreamed to occupy Armenia. In the recent war, the Romans were badly defeated. Now their senior army general, Philip is captured by Shapur and Shapur is now going to capture Valerian, the Roman emperor.

Being defeated, the cowardly Valerian hid in a room at the top of one of his castles. To capture him, Shapur has to open many doors. Fortunately Valerian was too scared to make impenetrable locks for the doors.

Each door has 4 parts. The first part is an integer number a. The second part is either an integer number b or some really odd sign which looks like R. The third one is an integer c and the fourth part is empty! As if it was laid for writing something. Being extremely gifted, after opening the first few doors, Shapur found out the secret behind the locks.

c is an integer written in base a, to open the door we should write it in base b. The only bad news is that this R is some sort of special numbering system that is used only in Roman empire, so opening the doors is not just a piece of cake!

Here's an explanation of this really weird number system that even doesn't have zero:

Roman numerals are based on seven symbols: a stroke (identified with the letter I) for a unit, a chevron (identified with the letter V) for a five, a cross-stroke (identified with the letter X) for a ten, a C (identified as an abbreviation of Centum) for a hundred, etc.:

- I=1

- V=5

- X=10

- L=50

- C=100

- D=500

- M=1000

Symbols are iterated to produce multiples of the decimal (1, 10, 100, 1, 000) values, with V, L, D substituted for a multiple of five, and the iteration continuing: I1, II2, III3, V5, VI6, VII7, etc., and the same for other bases: X10, XX20, XXX30, L50, LXXX80; CC200, DCC700, etc. At the fourth and ninth iteration, a subtractive principle must be employed, with the base placed before the higher base: IV4, IX9, XL40, XC90, CD400, CM900.

Also in bases greater than 10 we use A for 10, B for 11, etc.

Help Shapur capture Valerian and bring peace back to Persia, especially Armenia.

The first line contains two integers a and b (2 ≤ a, b ≤ 25). Only b may be replaced by an R which indicates Roman numbering system.

The next line contains a single non-negative integer c in base a which may contain leading zeros but its length doesn't exceed 103.

It is guaranteed that if we have Roman numerals included the number would be less than or equal to 300010 and it won't be 0. In any other case the number won't be greater than 101510.

Write a single line that contains integer c in base b. You must omit leading zeros.

## Input

The first line contains two integers a and b (2 ≤ a, b ≤ 25). Only b may be replaced by an R which indicates Roman numbering system.

The next line contains a single non-negative integer c in base a which may contain leading zeros but its length doesn't exceed 103.

It is guaranteed that if we have Roman numerals included the number would be less than or equal to 300010 and it won't be 0. In any other case the number won't be greater than 101510.

## Output

Write a single line that contains integer c in base b. You must omit leading zeros.

## Samples

```
10 2
1

```

```
1

```

```
16 R
5

```

```
V

```

```
5 R
4

```

```
IV

```

```
2 2
1111001

```

```
1111001

```

```
12 13
A

```

```
A

```

## Note

You can find more information about roman numerals here: http://en.wikipedia.org/wiki/Roman_numerals

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-61C |
| Contest | 61 |
| Index | C |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `math` |
| 镜像标签 | `math`、`*2000` |
| Codeforces 通过次数 | 840 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/61/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/61/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P61C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

