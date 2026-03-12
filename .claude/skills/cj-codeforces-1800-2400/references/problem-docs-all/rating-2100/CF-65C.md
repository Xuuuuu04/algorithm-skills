# CF-65C Harry Potter and the Golden Snitch

## 题面快照

## Description

Brothers Fred and George Weasley once got into the sporting goods store and opened a box of Quidditch balls. After long and painful experiments they found out that the Golden Snitch is not enchanted at all. It is simply a programmed device. It always moves along the same trajectory, which is a polyline with vertices at the points (x0, y0, z0), (x1, y1, z1), ..., (xn, yn, zn). At the beginning of the game the snitch is positioned at the point (x0, y0, z0), and then moves along the polyline at the constant speed vs. The twins have not yet found out how the snitch behaves then. Nevertheless, they hope that the retrieved information will help Harry Potter and his team in the upcoming match against Slytherin. Harry Potter learned that at the beginning the game he will be at the point (Px, Py, Pz) and his super fast Nimbus 2011 broom allows him to move at the constant speed vp in any direction or remain idle. vp is not less than the speed of the snitch vs. Harry Potter, of course, wants to catch the snitch as soon as possible. Or, if catching the snitch while it is moving along the polyline is impossible, he wants to hurry the Weasley brothers with their experiments. Harry Potter catches the snitch at the time when they are at the same point. Help Harry.

The first line contains a single integer n (1 ≤ n ≤ 10000). The following n + 1 lines contain the coordinates xi, yi, zi, separated by single spaces. The coordinates of any two consecutive points do not coincide. The next line contains the velocities vp and vs, the last line contains Px, Py, Pz, separated by single spaces. All the numbers in the input are integers, their absolute value does not exceed 104. The speeds are strictly positive. It is guaranteed that vs ≤ vp.

If Harry Potter can catch the snitch while it is moving along the polyline (including the end (xn, yn, zn)), print "YES" in the first line (without the quotes). Print in the second line t, which is the earliest moment of time, when Harry will be able to catch the snitch. On the third line print three numbers X, Y, Z, the coordinates of the point at which this happens. The absolute or relative error in the answer should not exceed 10 - 6. If Harry is not able to catch the snitch during its moving along the described polyline, print "NO".

## Input

The first line contains a single integer n (1 ≤ n ≤ 10000). The following n + 1 lines contain the coordinates xi, yi, zi, separated by single spaces. The coordinates of any two consecutive points do not coincide. The next line contains the velocities vp and vs, the last line contains Px, Py, Pz, separated by single spaces. All the numbers in the input are integers, their absolute value does not exceed 104. The speeds are strictly positive. It is guaranteed that vs ≤ vp.

## Output

If Harry Potter can catch the snitch while it is moving along the polyline (including the end (xn, yn, zn)), print "YES" in the first line (without the quotes). Print in the second line t, which is the earliest moment of time, when Harry will be able to catch the snitch. On the third line print three numbers X, Y, Z, the coordinates of the point at which this happens. The absolute or relative error in the answer should not exceed 10 - 6. If Harry is not able to catch the snitch during its moving along the described polyline, print "NO".

## Samples

```
4
0 0 0
0 10 0
10 10 0
10 0 0
0 0 0
1 1
5 5 25

```

```
YES
25.5000000000
10.0000000000 4.5000000000 0.0000000000

```

```
4
0 0 0
0 10 0
10 10 0
10 0 0
0 0 0
1 1
5 5 50

```

```
NO

```

```
1
1 2 3
4 5 6
20 10
1 2 3

```

```
YES
0.0000000000
1.0000000000 2.0000000000 3.0000000000

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-65C |
| Contest | 65 |
| Index | C |
| Rating | 2100 |
| Points | 1500.0 |
| Codeforces 标签 | `binary search`、`geometry` |
| 镜像标签 | `binary search`、`geometry`、`*2100` |
| Codeforces 通过次数 | 859 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/65/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/65/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P65C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

