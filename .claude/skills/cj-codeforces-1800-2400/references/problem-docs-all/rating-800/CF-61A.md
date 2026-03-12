# CF-61A Ultra-Fast Mathematician

## 题面快照

## Description

Shapur 是一位极其天赋异禀的学生。他在组合数学、代数、数论、几何、微积分等方面都非常出色。他不仅聪明，而且速度极快！他能在一秒内把 $10^{18}$ 个数字求和。

公元 230 年的一天，Shapur 想知道是否有人能比他算得更快。于是他办了一场极棒的比赛，邀请所有人来参加。

在比赛中，他给选手许多不同的数字对。每个数字只由 $0$ 或 $1$ 构成。选手需要针对每一组数字对写出一个新数字。规则很简单：如果两位数字在第 $i$ 位不同，则结果的第 $i$ 位为 $1$；如果相同，则结果第 $i$ 位为 $0$。

Shapur 制作了许多数字，并首先测试了自己的速度。他发现自己能一瞬间处理任意长度的数字对！他总是能给出正确答案，因此也期望选手给出正确答案。他很友好，不会为任何人出难题，并且每个人拿到的两个数字的位数都相同。

你现在要参加 Shapur 的比赛。看看你是否更快、更准确。

## Input

输入共两行。每行包含一个数字，保证是仅由 $0$ 和 $1$ 构成的字符串，并且两行的数字长度相同。数字可能以 $0$ 开头。每个数字的长度不超过 $100$。

## Output

输出一行，表示对应的结果。请不要省略前导 $0$。

## Samples

### Sample 1

Input
```
1010100
0100101
```

Output
```
1110001
```

### Sample 2

Input
```
000
111
```

Output
```
111
```

### Sample 3

Input
```
1110
1010
```

Output
```
0100
```

### Sample 4

Input
```
01110
01100
```

Output
```
00010
```

## Note

由 ChatGPT 5 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-61A |
| Contest | 61 |
| Index | A |
| Rating | 800 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 133932 |
| 镜像尝试 / 通过 | 2320 / 1328 |
| 时限 | 2000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/61/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/61/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF61A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

