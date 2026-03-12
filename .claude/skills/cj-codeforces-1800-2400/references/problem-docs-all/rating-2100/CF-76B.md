# CF-76B Mice

## 题面快照

## Description

Modern researches has shown that a flock of hungry mice searching for a piece of cheese acts as follows: if there are several pieces of cheese then each mouse chooses the closest one. After that all mice start moving towards the chosen piece of cheese. When a mouse or several mice achieve the destination point and there is still a piece of cheese in it, they eat it and become well-fed. Each mice that reaches this point after that remains hungry. Moving speeds of all mice are equal.

If there are several ways to choose closest pieces then mice will choose it in a way that would minimize the number of hungry mice. To check this theory scientists decided to conduct an experiment. They located N mice and M pieces of cheese on a cartesian plane where all mice are located on the line y = Y0 and all pieces of cheese — on another line y = Y1. To check the results of the experiment the scientists need a program which simulates the behavior of a flock of hungry mice.

Write a program that computes the minimal number of mice which will remain hungry, i.e. without cheese.

The first line of the input contains four integer numbers N (1 ≤ N ≤ 105), M (0 ≤ M ≤ 105), Y0 (0 ≤ Y0 ≤ 107), Y1 (0 ≤ Y1 ≤ 107, Y0 ≠ Y1). The second line contains a strictly increasing sequence of N numbers — x coordinates of mice. Third line contains a strictly increasing sequence of M numbers — x coordinates of cheese. All coordinates are integers and do not exceed 107 by absolute value.

The only line of output should contain one number — the minimal number of mice which will remain without cheese.

## Input

The first line of the input contains four integer numbers N (1 ≤ N ≤ 105), M (0 ≤ M ≤ 105), Y0 (0 ≤ Y0 ≤ 107), Y1 (0 ≤ Y1 ≤ 107, Y0 ≠ Y1). The second line contains a strictly increasing sequence of N numbers — x coordinates of mice. Third line contains a strictly increasing sequence of M numbers — x coordinates of cheese. All coordinates are integers and do not exceed 107 by absolute value.

## Output

The only line of output should contain one number — the minimal number of mice which will remain without cheese.

## Samples

```
3 2 0 2
0 1 3
2 5

```

```
1

```

## Note

All the three mice will choose the first piece of cheese. Second and third mice will eat this piece. The first one will remain hungry, because it was running towards the same piece, but it was late. The second piece of cheese will remain uneaten.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-76B |
| Contest | 76 |
| Index | B |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `greedy`、`two pointers` |
| 镜像标签 | `greedy`、`two pointers`、`*2100` |
| Codeforces 通过次数 | 797 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/76/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/76/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P76B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

