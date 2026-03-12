# CF-19B Checkout Assistant

## 题面快照

## Description

Bob 来到一家现购自运商店，将 $n$ 件商品放入了他的手推车，然后到收银台付款。每件商品由它的价格 $c_i$ 和收银员扫描它的时间 $t_i$ 秒定义。

当收银员正在扫描某件商品时，Bob 可以从他的手推车中偷走某些其它商品。Bob 需要恰好 $1$ 秒来偷走一件商品。Bob 需要付给收银员的最少钱数是多少？请记住，收银员扫描商品的顺序由 Bob 决定。

## Input

输入第一行包含数 $n$（$1 \le n \le 2000$）。接下来 $n$ 行每行每件商品由一对数 $t_i$，$c_i$（$0 \le t_i \le 2000$，$1 \le c_i \le 10^9$）描述。如果 $t_i$ 是 $0$，那么当收银员扫描商品 $i$ 时，Bob 不能偷任何东西。

## Output

输出一个数字—— Bob 需要支付的最小金额是多少。

## Samples

### Sample 1

Input
```
4
2 10
0 20
1 5
1 3
```

Output
```
8
```

### Sample 2

Input
```
3
0 1
0 10
0 100
```

Output
```
111
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-19B |
| Contest | 19 |
| Index | B |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `dp` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 5681 |
| 镜像尝试 / 通过 | 5445 / 1709 |
| 时限 | 1000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/19/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/19/problem/B)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF19B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

