# CF-57E Chess

## 题面快照

## Description

兔子 Brian 十分喜欢国际象棋。不久前，他与兔子 Stewie 争论骑士比国王更优秀。为了证明自己的观点，他试图展示骑士的速度非常快，但 Stewie 并不接受没有证据的说法。于是他为 Brian 构建了一个无限大的棋盘，并删去了一些格子，使游戏更加有趣。现在 Brian 只需要计算一下，一只站在坐标为 $ (0,0) $ 的骑士，最多经过 $ k $ 步能够到达多少个不同的棋盘格子。显然，不能跳到被删掉的格子上。

Brian 并不喜欢精确科学，也不懂编程，所以他几乎无法赶在 Stewie 之前完成这个题目。请你帮助 Brian，比 Stewie 更快解决这个问题。

## Input

第一行包含两个整数 $ k $ 和 $ n $（$ 0 \leq k \leq 10^{18},\ 0 \leq n \leq 440 $），分别表示骑士可以行动的最大步数，以及被删去的格子数。接下来 $ n $ 行，每一行给出一个被删去格子的坐标 $ (x_i,y_i) $（$ |x_i| \leq 10,\ |y_i| \leq 10 $）。所有数字均为整数，被删去的格子不会重复，并保证格子 $(0,0)$ 没有被删去。

## Output

输出一个整数，表示答案。由于可能非常大，输出其对 $ 1000000007 $ 取模的结果。

## Samples

### Sample 1

Input
```
1 0
```

Output
```
9
```

### Sample 2

Input
```
2 7
-1 2
1 2
2 1
2 -1
1 -2
-1 -2
-2 -1
```

Output
```
9
```

## Note

由 ChatGPT 5 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-57E |
| Contest | 57 |
| Index | E |
| Rating | 3000 |
| Points | 2500.0 |
| Codeforces 标签 | `math`、`shortest paths` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 283 |
| 镜像尝试 / 通过 | 434 / 107 |
| 时限 | 2000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/57/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/57/problem/E)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF57E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

