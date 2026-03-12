# CF-23C Oranges and Apples

## 题面快照

## Description

已知有 $2N-1$ 个箱子，每个箱子里有一些苹果和橘子。你的任务是从中选择 $N$ 个箱子使得这 $N$ 个箱子中的苹果数目不小于所有箱子里苹果总数的一半，这 $N$ 个箱子中的橘子数目也不小于所有箱子里橘子总数的一半。

## Input

多测。

对于每一组数据，先输入一个整数 $N$，含义见题面。

接下来的 $2N-1$ 行，每行两个正整数 $a_i,o_i$ 表示苹果和橘子在这个箱子里面的个数。

## Output

第一行输出一个字符串，如果可以选出 $n$ 个箱子，则输出 `YES`，否则输出 `NO`。

如果可以选出 $n$ 个箱子，则在第二行从小到大输出你所选的 $n$ 个箱子的编号（箱子编号从 $1$ 开始），否则直接进入下一组的数据的输出。

## Samples

### Sample 1

Input
```
2
2
10 15
5 7
20 18
1
0 0
```

Output
```
YES
1 3
YES
1
```

## Note

$1 \leq \sum n \leq 10^5$，$0 \leq a_i,o_i \leq 10^9$。

Translated by 稀神探女

Developed by luogu_gza

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-23C |
| Contest | 23 |
| Index | C |
| Rating | 2500 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`sortings` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 1678 |
| 镜像尝试 / 通过 | 999 / 294 |
| 时限 | 1500 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/23/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/23/problem/C)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF23C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

