# CF-56C Corporation Mail

## 题面快照

## Description

The Beroil corporation structure is hierarchical, that is it can be represented as a tree. Let's examine the presentation of this structure as follows:

- employee ::= name. | name:employee1,employee2, ... ,employeek.

- name ::= name of an employee

That is, the description of each employee consists of his name, a colon (:), the descriptions of all his subordinates separated by commas, and, finally, a dot. If an employee has no subordinates, then the colon is not present in his description.

For example, line MIKE:MAX.,ARTEM:MIKE..,DMITRY:DMITRY.,DMITRY... is the correct way of recording the structure of a corporation where the director MIKE has subordinates MAX, ARTEM and DMITRY. ARTEM has a subordinate whose name is MIKE, just as the name of his boss and two subordinates of DMITRY are called DMITRY, just like himself.

In the Beroil corporation every employee can only correspond with his subordinates, at that the subordinates are not necessarily direct. Let's call an uncomfortable situation the situation when a person whose name is s writes a letter to another person whose name is also s. In the example given above are two such pairs: a pair involving MIKE, and two pairs for DMITRY (a pair for each of his subordinates).

Your task is by the given structure of the corporation to find the number of uncomfortable pairs in it.

The first and single line contains the corporation structure which is a string of length from 1 to 1000 characters. It is guaranteed that the description is correct. Every name is a string consisting of capital Latin letters from 1 to 10 symbols in length.

Print a single number — the number of uncomfortable situations in the company.

## Input

The first and single line contains the corporation structure which is a string of length from 1 to 1000 characters. It is guaranteed that the description is correct. Every name is a string consisting of capital Latin letters from 1 to 10 symbols in length.

## Output

Print a single number — the number of uncomfortable situations in the company.

## Samples

```
MIKE:MAX.,ARTEM:MIKE..,DMITRY:DMITRY.,DMITRY...

```

```
3

```

```
A:A..

```

```
1

```

```
A:C:C:C:C.....

```

```
6

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-56C |
| Contest | 56 |
| Index | C |
| Rating | 1700 |
| Points | 1500.0 |
| Codeforces 标签 | `data structures`、`expression parsing`、`implementation` |
| 镜像标签 | `data structures`、`expression parsing`、`implementation`、`*1700` |
| Codeforces 通过次数 | 1294 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/56/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/56/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P56C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

