# CF-44J Triminoes

## 题面快照

## Description

There are many interesting tasks on domino tilings. For example, an interesting fact is known. Let us take a standard chessboard (8 × 8) and cut exactly two squares out of it. It turns out that the resulting board can always be tiled using dominoes 1 × 2, if the two cut out squares are of the same color, otherwise it is impossible.

Petya grew bored with dominoes, that's why he took a chessboard (not necessarily 8 × 8), cut some squares out of it and tries to tile it using triminoes. Triminoes are reactangles 1 × 3 (or 3 × 1, because triminoes can be rotated freely), also the two extreme squares of a trimino are necessarily white and the square in the middle is black. The triminoes are allowed to put on the chessboard so that their squares matched the colors of the uncut squares of the chessboard, and also the colors must match: the black squares must be matched with the black ones only and the white ones — with the white squares. The triminoes must not protrude above the chessboard or overlap each other. All the uncut squares of the board must be covered with triminoes.

Help Petya find out if it is possible to tile his board using triminos in the described way and print one of the variants of tiling.

The first line contains two integers n and m (1 ≤ n, m ≤ 1000) — the board size. Next n lines contain m symbols each and represent the board description. If some position contains ".", then the square in this position has been cut out. Symbol "w" stands for a white square, "b" stands for a black square. It is guaranteed that through adding the cut squares can result in a correct chessboard (i.e. with alternating black and white squares), thought, perhaps, of a non-standard size.

If at least one correct tiling exists, in the first line print "YES" (without quotes), and then — the tiling description. The description must contain n lines, m symbols in each. The cut out squares, as well as in the input data, are marked by ".". To denote triminoes symbols "a", "b", "c", "d" can be used, and all the three squares of each trimino must be denoted by the same symbol. If two triminoes share a side, than they must be denoted by different symbols. Two triminoes not sharing a common side can be denoted by one and the same symbol (c.f. sample).

If there are multiple correct ways of tiling, it is allowed to print any. If it is impossible to tile the board using triminoes or the correct tiling, for which four symbols "a", "b", "c", "d" would be enough, doesn't exist, print "NO" (without quotes) in the first line.

## Input

The first line contains two integers n and m (1 ≤ n, m ≤ 1000) — the board size. Next n lines contain m symbols each and represent the board description. If some position contains ".", then the square in this position has been cut out. Symbol "w" stands for a white square, "b" stands for a black square. It is guaranteed that through adding the cut squares can result in a correct chessboard (i.e. with alternating black and white squares), thought, perhaps, of a non-standard size.

## Output

If at least one correct tiling exists, in the first line print "YES" (without quotes), and then — the tiling description. The description must contain n lines, m symbols in each. The cut out squares, as well as in the input data, are marked by ".". To denote triminoes symbols "a", "b", "c", "d" can be used, and all the three squares of each trimino must be denoted by the same symbol. If two triminoes share a side, than they must be denoted by different symbols. Two triminoes not sharing a common side can be denoted by one and the same symbol (c.f. sample).

If there are multiple correct ways of tiling, it is allowed to print any. If it is impossible to tile the board using triminoes or the correct tiling, for which four symbols "a", "b", "c", "d" would be enough, doesn't exist, print "NO" (without quotes) in the first line.

## Samples

```
6 10
.w.wbw.wbw
wbwbw.w.w.
bw.wbwbwbw
w.wbw.wbwb
...wbw.w.w
..wbw.wbw.

```

```
YES
.a.aaa.ccc
baccc.c.a.
ba.dddcbab
b.aaa.cbab
...bbb.b.b
..ccc.ddd.

```

```
2 2
wb
bw

```

```
NO

```

```
1 3
wbw

```

```
YES
bbb

```

```
1 3
...

```

```
YES
...

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-44J |
| Contest | 44 |
| Index | J |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`greedy` |
| 镜像标签 | `constructive algorithms`、`greedy`、`*2000` |
| Codeforces 通过次数 | 612 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/44/J)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/44/problem/J)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P44J)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

