# CF-2C Commentator problem

## 题面快照

## Description

The Olympic Games in Bercouver are in full swing now. Here everyone has their own objectives: sportsmen compete for medals, and sport commentators compete for more convenient positions to give a running commentary. Today the main sport events take place at three round stadiums, and the commentator's objective is to choose the best point of observation, that is to say the point from where all the three stadiums can be observed. As all the sport competitions are of the same importance, the stadiums should be observed at the same angle. If the number of points meeting the conditions is more than one, the point with the maximum angle of observation is prefered.

Would you, please, help the famous Berland commentator G. Berniev to find the best point of observation. It should be noted, that the stadiums do not hide each other, the commentator can easily see one stadium through the other.

The input data consists of three lines, each of them describes the position of one stadium. The lines have the format x, y, r, where (x, y) are the coordinates of the stadium's center ( - 103 ≤ x, y ≤ 103), and r (1 ≤ r ≤ 103) is its radius. All the numbers in the input data are integer, stadiums do not have common points, and their centers are not on the same line.

Print the coordinates of the required point with five digits after the decimal point. If there is no answer meeting the conditions, the program shouldn't print anything. The output data should be left blank.

## Input

The input data consists of three lines, each of them describes the position of one stadium. The lines have the format x, y, r, where (x, y) are the coordinates of the stadium's center ( - 103 ≤ x, y ≤ 103), and r (1 ≤ r ≤ 103) is its radius. All the numbers in the input data are integer, stadiums do not have common points, and their centers are not on the same line.

## Output

Print the coordinates of the required point with five digits after the decimal point. If there is no answer meeting the conditions, the program shouldn't print anything. The output data should be left blank.

## Samples

```
0 0 10
60 0 10
30 30 10

```

```
30.00000 0.00000

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-2C |
| Contest | 2 |
| Index | C |
| Rating | 2600 |
| Points | - |
| Codeforces 标签 | `geometry` |
| 镜像标签 | `geometry`、`*2600` |
| Codeforces 通过次数 | 1988 |
| 镜像尝试 / 通过 | 2 / 1 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/2/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/2/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P2C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

