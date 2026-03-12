# CF-55D Beautiful numbers

## 题面快照

## Description

Volodya 是个古怪的男孩，他的审美也很独特。他认为，一个正整数是“美丽的”，当且仅当它能被其所有非零数字整除。我们不想与他争辩，只需统计给定区间内美丽数的个数。

## Input

第一行包含一个整数 $t$（$1 \leq t \leq 10$），表示测试用例的数量。接下来的 $t$ 行，每行包含两个正整数 $l_{i}$ 与 $r_{i}$（$1 \leq l_{i} \leq r_{i} \leq 9 \cdot 10^{18}$）。

请不要在 C++ 中使用 `%lld` 读写 64 位整数。建议使用 `cin`（也可以用 `%I64d`）。

## Output

输出应包含 $t$ 个数字，每行为一个答案，表示对应区间（从 $l_{i}$ 到 $r_{i}$，包括端点）内美丽数的数量。

## Samples

### Sample 1

Input
```
1
1 9
```

Output
```
9
```

### Sample 2

Input
```
1
12 15
```

Output
```
2
```

## Note

由 ChatGPT 5 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-55D |
| Contest | 55 |
| Index | D |
| Rating | 2500 |
| Points | 2000.0 |
| Codeforces 标签 | `dp`、`number theory` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 4574 |
| 镜像尝试 / 通过 | 8159 / 2263 |
| 时限 | 4000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/55/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/55/problem/D)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF55D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

