# CF-19C Deletion of Repeats

## 题面快照

## Description

有一天，Bob 看到了一个字符串。该字符串包含了许多不同的字母，但这些字母都用数字来表示，并且每种字母在字符串中最多出现 10 次。Bob 不喜欢这个字符串，因为里面有“重复段”：长度为 $x$ 的重复段是指一个长度为 $2x$ 的子串，其前一半和后一半字符一一对应完全相同。Bob 决定删掉所有的重复段。他的操作方式如下：只要仍有重复段存在，Bob 就选择最短的重复段；如果有多个最短的，他选择最左边的一个，然后删除这个重复段的左半部分及其左边的所有内容。

给定 Bob 看到的字符串，请你找出在按照上述规则删除所有重复段后，字符串会变成什么样子。

## Input

第一行包含一个整数 $n$（$1 \leq n \leq 10^5$），表示字符串的长度。  
第二行包含 $n$ 个用空格分隔的整数，每个整数在 $0$ 到 $10^9$ 之间，表示字符串中的字母。保证每种字母在字符串中最多出现 10 次。

## Output

第一行输出经过删除操作后剩余字符串的长度。  
第二行输出剩余字符串中的所有字母（数字），用空格隔开。

## Samples

### Sample 1

Input
```
6
1 2 3 1 2 3
```

Output
```
3
1 2 3
```

### Sample 2

Input
```
7
4 5 6 5 6 7 7
```

Output
```
1
7
```

## Note

由 ChatGPT 5 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-19C |
| Contest | 19 |
| Index | C |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `greedy`、`hashing`、`string suffix structures` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 1302 |
| 镜像尝试 / 通过 | 484 / 176 |
| 时限 | 2000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/19/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/19/problem/C)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF19C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

