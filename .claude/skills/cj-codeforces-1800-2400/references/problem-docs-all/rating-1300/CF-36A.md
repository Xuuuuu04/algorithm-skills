# CF-36A Extra-terrestrial Intelligence

## 题面快照

## Description

Recently Vasya got interested in finding extra-terrestrial intelligence. He made a simple extra-terrestrial signals’ receiver and was keeping a record of the signals for n days in a row. Each of those n days Vasya wrote a 1 in his notebook if he had received a signal that day and a 0 if he hadn’t. Vasya thinks that he has found extra-terrestrial intelligence if there is a system in the way the signals has been received, i.e. if all the intervals between successive signals are equal. Otherwise, Vasya thinks that the signals were sent by some stupid aliens no one cares about. Help Vasya to deduce from the information given by the receiver if he has found extra-terrestrial intelligence or not.

The first line contains integer n (3 ≤ n ≤ 100) — amount of days during which Vasya checked if there were any signals. The second line contains n characters 1 or 0 — the record Vasya kept each of those n days. It’s guaranteed that the given record sequence contains at least three 1s.

If Vasya has found extra-terrestrial intelligence, output YES, otherwise output NO.

## Input

The first line contains integer n (3 ≤ n ≤ 100) — amount of days during which Vasya checked if there were any signals. The second line contains n characters 1 or 0 — the record Vasya kept each of those n days. It’s guaranteed that the given record sequence contains at least three 1s.

## Output

If Vasya has found extra-terrestrial intelligence, output YES, otherwise output NO.

## Samples

```
8
00111000

```

```
YES

```

```
7
1001011

```

```
NO

```

```
7
1010100

```

```
YES

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-36A |
| Contest | 36 |
| Index | A |
| Rating | 1300 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1300` |
| Codeforces 通过次数 | 3472 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/36/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/36/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P36A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

