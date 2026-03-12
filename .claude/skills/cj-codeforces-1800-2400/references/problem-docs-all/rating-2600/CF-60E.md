# CF-60E Mushroom Gnomes

## 题面快照

## Description

Once upon a time in the thicket of the mushroom forest lived mushroom gnomes. They were famous among their neighbors for their magic mushrooms. Their magic nature made it possible that between every two neighboring mushrooms every minute grew another mushroom with the weight equal to the sum of weights of two neighboring ones.

The mushroom gnomes loved it when everything was in order, that's why they always planted the mushrooms in one line in the order of their weights' increasing. Well... The gnomes planted the mushrooms and went to eat. After x minutes they returned and saw that new mushrooms had grown up, so that the increasing order had been violated. The gnomes replanted all the mushrooms in the correct order, that is, they sorted the mushrooms in the order of the weights' increasing. And went to eat again (those gnomes were quite big eaters). What total weights modulo p will the mushrooms have in another y minutes?

The first line contains four integers n, x, y, p (1 ≤ n ≤ 106, 0 ≤ x, y ≤ 1018, x + y > 0, 2 ≤ p ≤ 109) which represent the number of mushrooms, the number of minutes after the first replanting, the number of minutes after the second replanting and the module. The next line contains n integers ai which represent the mushrooms' weight in the non-decreasing order (0 ≤ ai ≤ 109).

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d).

The answer should contain a single number which is the total weights of the mushrooms modulo p in the end after x + y minutes.

## Input

The first line contains four integers n, x, y, p (1 ≤ n ≤ 106, 0 ≤ x, y ≤ 1018, x + y > 0, 2 ≤ p ≤ 109) which represent the number of mushrooms, the number of minutes after the first replanting, the number of minutes after the second replanting and the module. The next line contains n integers ai which represent the mushrooms' weight in the non-decreasing order (0 ≤ ai ≤ 109).

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d).

## Output

The answer should contain a single number which is the total weights of the mushrooms modulo p in the end after x + y minutes.

## Samples

```
2 1 0 657276545
1 2

```

```
6

```

```
2 1 1 888450282
1 2

```

```
14

```

```
4 5 0 10000
1 2 3 4

```

```
1825

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-60E |
| Contest | 60 |
| Index | E |
| Rating | 2600 |
| Points | 2500.0 |
| Codeforces 标签 | `math`、`matrices` |
| 镜像标签 | `math`、`matrices`、`*2600` |
| Codeforces 通过次数 | 406 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/60/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/60/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P60E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

