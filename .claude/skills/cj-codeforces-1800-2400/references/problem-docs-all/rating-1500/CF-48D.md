# CF-48D Permutations

## 题面快照

## Description

A permutation is a sequence of integers from 1 to n of length n containing each number exactly once. For example, (1), (4, 3, 5, 1, 2), (3, 2, 1) are permutations, and (1, 1), (4, 3, 1), (2, 3, 4) are not.

There are many tasks on permutations. Today you are going to solve one of them. Let’s imagine that somebody took several permutations (perhaps, with a different number of elements), wrote them down consecutively as one array and then shuffled the resulting array. The task is to restore the initial permutations if it is possible.

The first line contains an integer n (1 ≤ n ≤ 105). The next line contains the mixed array of n integers, divided with a single space. The numbers in the array are from 1 to 105.

If this array can be split into several permutations so that every element of the array belongs to exactly one permutation, print in the first line the number of permutations. The second line should contain n numbers, corresponding to the elements of the given array. If the i-th element belongs to the first permutation, the i-th number should be 1, if it belongs to the second one, then its number should be 2 and so on. The order of the permutations’ numbering is free.

If several solutions are possible, print any one of them. If there’s no solution, print in the first line  - 1.

## Input

The first line contains an integer n (1 ≤ n ≤ 105). The next line contains the mixed array of n integers, divided with a single space. The numbers in the array are from 1 to 105.

## Output

If this array can be split into several permutations so that every element of the array belongs to exactly one permutation, print in the first line the number of permutations. The second line should contain n numbers, corresponding to the elements of the given array. If the i-th element belongs to the first permutation, the i-th number should be 1, if it belongs to the second one, then its number should be 2 and so on. The order of the permutations’ numbering is free.

If several solutions are possible, print any one of them. If there’s no solution, print in the first line  - 1.

## Samples

```
9
1 2 3 1 2 1 4 2 5

```

```
3
3 1 2 1 2 2 2 3 2

```

```
4
4 3 2 1

```

```
1
1 1 1 1

```

```
4
1 2 2 3

```

```
-1

```

## Note

In the first sample test the array is split into three permutations: (2, 1), (3, 2, 1, 4, 5), (1, 2). The first permutation is formed by the second and the fourth elements of the array, the second one — by the third, the fifth, the sixth, the seventh and the ninth elements, the third one — by the first and the eigth elements. Clearly, there are other splitting variants possible.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-48D |
| Contest | 48 |
| Index | D |
| Rating | 1500 |
| Points | - |
| Codeforces 标签 | `greedy` |
| 镜像标签 | `greedy`、`*1500` |
| Codeforces 通过次数 | 2967 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/48/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/48/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P48D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

