# CF-63A Sinking Ship

## 题面快照

## Description

The ship crashed into a reef and is sinking. Now the entire crew must be evacuated. All n crew members have already lined up in a row (for convenience let's label them all from left to right with positive integers from 1 to n) and await further instructions. However, one should evacuate the crew properly, in a strict order. Specifically:

The first crew members to leave the ship are rats. Then women and children (both groups have the same priority) leave the ship. After that all men are evacuated from the ship. The captain leaves the sinking ship last.

If we cannot determine exactly who should leave the ship first for any two members of the crew by the rules from the previous paragraph, then the one who stands to the left in the line leaves the ship first (or in other words, the one whose number in the line is less).

For each crew member we know his status as a crew member, and also his name. All crew members have different names. Determine the order in which to evacuate the crew.

The first line contains an integer n, which is the number of people in the crew (1 ≤ n ≤ 100). Then follow n lines. The i-th of those lines contains two words — the name of the crew member who is i-th in line, and his status on the ship. The words are separated by exactly one space. There are no other spaces in the line. The names consist of Latin letters, the first letter is uppercase, the rest are lowercase. The length of any name is from 1 to 10 characters. The status can have the following values: rat for a rat, woman for a woman, child for a child, man for a man, captain for the captain. The crew contains exactly one captain.

Print n lines. The i-th of them should contain the name of the crew member who must be the i-th one to leave the ship.

## Input

The first line contains an integer n, which is the number of people in the crew (1 ≤ n ≤ 100). Then follow n lines. The i-th of those lines contains two words — the name of the crew member who is i-th in line, and his status on the ship. The words are separated by exactly one space. There are no other spaces in the line. The names consist of Latin letters, the first letter is uppercase, the rest are lowercase. The length of any name is from 1 to 10 characters. The status can have the following values: rat for a rat, woman for a woman, child for a child, man for a man, captain for the captain. The crew contains exactly one captain.

## Output

Print n lines. The i-th of them should contain the name of the crew member who must be the i-th one to leave the ship.

## Samples

```
6
Jack captain
Alice woman
Charlie man
Teddy rat
Bob child
Julia woman

```

```
Teddy
Alice
Bob
Julia
Charlie
Jack

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-63A |
| Contest | 63 |
| Index | A |
| Rating | 900 |
| Points | 500.0 |
| Codeforces 标签 | `implementation`、`sortings`、`strings` |
| 镜像标签 | `implementation`、`sortings`、`strings`、`*900` |
| Codeforces 通过次数 | 13257 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/63/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/63/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P63A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

