# CF-12A Super Agent

## 题面快照

## Description

在 Potatoland 有一个非常秘密的基地，那里按照特殊的配方制作土豆泥。邻国 Porridgia 决定窃取这个配方并将其卖给 Pilauland。为此任务，他们多年来一直在培养特工 Pearlo。最终，Pearlo 学会了所有间谍的秘密，潜入了 Potatoland 的领土，并到达了秘密基地。

现在他正站在入口处，但要进入基地，他需要通过一个组合锁。一分钟前，一名工人在终端上输入了密码并打开了门。该终端是一个 $3 \times 3$ 的数字键盘，数字从 $1$ 到 $9$。

Pearlo 知道密码由不同的数字组成，并且很可能关于终端的中心按钮对称。他有一个热感应器，可以检测到工人按下了哪些数字。现在他想检查工人输入的密码是否关于终端的中心按钮对称。如果是这样，这将帮助 Pearlo 减少可能的密码组合数量。

## Input

输入包含一个 $3$ 行 $3$ 列的矩阵，每个位置是一个符号。符号「X」表示对应的按钮被按下，「.」表示没有被按下。矩阵中可能没有「X」，也可能没有「.」。

## Output

如果密码关于终端的中心按钮对称，输出 YES，否则输出 NO。

## Samples

### Sample 1

Input
```
XX.
...
.XX
```

Output
```
YES
```

### Sample 2

Input
```
X.X
X..
...
```

Output
```
NO
```

## Note

如果你不熟悉「中心对称」这个术语，可以参考 http://en.wikipedia.org/wiki/Central\_symmetry。

由 ChatGPT 4.1 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-12A |
| Contest | 12 |
| Index | A |
| Rating | 800 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 15233 |
| 镜像尝试 / 通过 | 5869 / 3038 |
| 时限 | 2000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/12/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/12/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF12A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

