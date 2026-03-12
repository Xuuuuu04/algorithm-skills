# CF-93D Flags

## 题面快照

## Description

When Igor K. was a freshman, his professor strictly urged him, as well as all other freshmen, to solve programming Olympiads. One day a problem called "Flags" from a website called Timmy's Online Judge caught his attention. In the problem one had to find the number of three-colored flags that would satisfy the condition... actually, it doesn't matter. Igor K. quickly found the formula and got the so passionately desired Accepted.

However, the professor wasn't very much impressed. He decided that the problem represented on Timmy's Online Judge was very dull and simple: it only had three possible colors of flag stripes and only two limitations. He suggested a complicated task to Igor K. and the fellow failed to solve it. Of course, we won't tell anybody that the professor couldn't solve it as well.

And how about you? Can you solve the problem?

The flags consist of one or several parallel stripes of similar width. The stripes can be one of the following colors: white, black, red or yellow. You should find the number of different flags with the number of stripes from L to R, if:

-  a flag cannot have adjacent stripes of one color;

-  a flag cannot have adjacent white and yellow stripes;

-  a flag cannot have adjacent red and black stripes;

-  a flag cannot have the combination of black, white and red stripes following one after another in this or reverse order;

-  symmetrical flags (as, for example, a WB and a BW flag, where W and B stand for the white and black colors) are considered the same.

The only line contains two integers L and R (1 ≤ L ≤ R ≤ 109). They are the lower and upper borders of the number of stripes on the flag.

Print a single number — the number of different flags that would satisfy the condition of the problem and would have from L to R stripes, modulo 1000000007.

## Input

The only line contains two integers L and R (1 ≤ L ≤ R ≤ 109). They are the lower and upper borders of the number of stripes on the flag.

## Output

Print a single number — the number of different flags that would satisfy the condition of the problem and would have from L to R stripes, modulo 1000000007.

## Samples

```
3 4

```

```
23

```

```
5 6

```

```
64

```

## Note

In the first test the following flags exist (they are listed in the lexicographical order, the letters B, R, W, Y stand for Black, Red, White and Yellow correspondingly):

3 stripes: BWB, BYB, BYR, RWR, RYR, WBW, WBY, WRW, WRY, YBY, YRY (overall 11 flags).

4 stripes: BWBW, BWBY, BYBW, BYBY, BYRW, BYRY, RWRW, RWRY, RYBW, RYBY, RYRW, RYRY (12 flags).

That's why the answer to test 1 is equal to 11 + 12 = 23.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-93D |
| Contest | 93 |
| Index | D |
| Rating | 2500 |
| Points | 2000.0 |
| Codeforces 标签 | `dp`、`math`、`matrices` |
| 镜像标签 | `dp`、`math`、`matrices`、`*2500` |
| Codeforces 通过次数 | 435 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/93/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/93/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P93D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

