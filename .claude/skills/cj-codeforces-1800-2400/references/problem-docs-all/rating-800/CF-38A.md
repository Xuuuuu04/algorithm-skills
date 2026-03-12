# CF-38A Army

## 题面快照

## Description

在北爱尔兰军队的行政系统中有 $n$ 个军衔，其中 $1$ 最低，$n$ 最高。

你需要 $d_i$ 年来从 $i$ 级升到 $i+1$ 级。在你升到 $i$ 级时必须已经到达前面所有等级。

Vasya 刚刚达到 $a$ 级，但他想达到 $b$ 级。请问他至少还要再参军多少年。

## Input

第一行：$n$（$2 \leq n \leq 100$）；

第二行：$d_1$，$d_2$，$d_3……d_{n-1}$（$1 \leq d_i \leq 100$）；

第三行：$a,b$（$1$ $\leq$ $a$ $<$ $b$ $\leq$ $n$）。

## Output

仅一行：从 $a$ 级升到 $b$ 级所需的年数。

## Samples

### Sample 1

Input
```
3
5 6
1 2
```

Output
```
5
```

### Sample 2

Input
```
3
5 6
1 3
```

Output
```
11
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-38A |
| Contest | 38 |
| Index | A |
| Rating | 800 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 25357 |
| 镜像尝试 / 通过 | 2028 / 1123 |
| 时限 | 2000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/38/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/38/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF38A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

