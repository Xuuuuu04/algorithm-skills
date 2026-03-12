# CF-81D Polycarp's Picture Gallery

## 题面快照

## Description

Polycarp loves not only to take pictures, but also to show his photos to friends. On his personal website he has recently installed a widget that can display n photos with the scroll option. At each moment of time the widget displays exactly one photograph with the option showing the previous/next one. From the first photo, you can switch to the second one or to the n-th one, from the second photo you can switch to the third one or to the first one, etc. Thus, navigation is performed in a cycle.

Polycarp's collection consists of m photo albums, the i-th album contains ai photos. Polycarp wants to choose n photos and put them on a new widget. To make watching the photos interesting to the visitors, he is going to post pictures so that no two photos from one album were neighboring (each photo will have exactly two neighbors, the first photo's neighbors are the second and the n-th one).

Help Polycarp compile a photo gallery. Select n photos from his collection and put them in such order that no two photos from one album went one after the other.

The first line contains two integers n and m (3 ≤ n ≤ 1000, 1 ≤ m ≤ 40), where n is the number of photos on the widget, and m is the number of albums. The second line contains m integers a1, a2, ..., am (1 ≤ ai ≤ 1000), where ai is the number of photos in the i-th album.

Print the single number -1 if there is no solution. Otherwise, print n numbers t1, t2, ..., tn, where ti represents the number of the album of the i-th picture in the widget. The albums are numbered from 1 in the order of their appearance in the input. If there are several solutions, print any of them.

## Input

The first line contains two integers n and m (3 ≤ n ≤ 1000, 1 ≤ m ≤ 40), where n is the number of photos on the widget, and m is the number of albums. The second line contains m integers a1, a2, ..., am (1 ≤ ai ≤ 1000), where ai is the number of photos in the i-th album.

## Output

Print the single number -1 if there is no solution. Otherwise, print n numbers t1, t2, ..., tn, where ti represents the number of the album of the i-th picture in the widget. The albums are numbered from 1 in the order of their appearance in the input. If there are several solutions, print any of them.

## Samples

```
4 3
1 3 5

```

```
3 1 3 2

```

```
10 2
5 5

```

```
2 1 2 1 2 1 2 1 2 1

```

```
10 3
1 10 3

```

```
-1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-81D |
| Contest | 81 |
| Index | D |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`greedy` |
| 镜像标签 | `constructive algorithms`、`greedy`、`*2100` |
| Codeforces 通过次数 | 790 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/81/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/81/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P81D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

