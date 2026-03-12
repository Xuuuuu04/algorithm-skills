# CF-2A Winner

## 题面快照

## Description

在 Berland 流行着纸牌游戏 `Berlogging`，这个游戏的赢家是根据以下规则确定的：

1. 在每一轮中，玩家获得或失去一定数量的分数，在游戏过程中，分数被记录在 `名称和得分` 行中，其中名字是玩家的名字，得分是在这一轮中获得的分数。得分是负值意味着玩家失去了相应的分数。
2. 如果在比赛结束时只有一名玩家分数最多，他就是获胜者。
3. 如果两名或两名以上的玩家在比赛结束时都有最大的分数 $m$ ，那么其中首先获得至少 $m$ 分的玩家胜利。开始时，每个玩家都是 $0$ 分。


保证在比赛结束时至少有一个玩家的分数为正。

## Input

第一行包含整数 $n(1\leqslant n\leqslant 1000)$，表示是游戏进行的的回合数。

第 $2 \sim n + 1$ 行，按照时间顺序输入 `名称和得分` 行的信息，其中名称是长度不大于 $32$ 的小写字母组成的字符串，分数的绝对值不大于 $1000$。

## Output

输出获胜者的名称。

## Samples

### Sample 1

Input
```
3
mike 3
andrew 5
mike 2
```

Output
```
andrew
```

### Sample 2

Input
```
3
andrew 3
andrew 2
mike 5
```

Output
```
andrew
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-2A |
| Contest | 2 |
| Index | A |
| Rating | 1500 |
| Points | - |
| Codeforces 标签 | `hashing`、`implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 30624 |
| 镜像尝试 / 通过 | 15258 / 3551 |
| 时限 | 1000 ms |
| 内存限制 | 64000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/2/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/2/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF2A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

