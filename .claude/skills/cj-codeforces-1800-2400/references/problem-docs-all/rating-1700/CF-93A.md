# CF-93A Frames

## 题面快照

## Description

Throughout Igor K.'s life he has had many situations worthy of attention. We remember the story with the virus, the story of his mathematical career and of course, his famous programming achievements. However, one does not always adopt new hobbies, one can quit something as well.

This time Igor K. got disappointed in one of his hobbies: editing and voicing videos. Moreover, he got disappointed in it so much, that he decided to destroy his secret archive for good.

Igor K. use Pindows XR operation system which represents files and folders by small icons. At that, m icons can fit in a horizontal row in any window.

Igor K.'s computer contains n folders in the D: disk's root catalog. The folders are numbered from 1 to n in the order from the left to the right and from top to bottom (see the images). At that the folders with secret videos have numbers from a to b inclusive. Igor K. wants to delete them forever, at that making as few frame selections as possible, and then pressing Shift+Delete exactly once. What is the minimum number of times Igor K. will have to select the folder in order to select folders from a to b and only them? Let us note that if some selected folder is selected repeatedly, then it is deselected. Each selection possesses the shape of some rectangle with sides parallel to the screen's borders.

The only line contains four integers n, m, a, b (1 ≤ n, m ≤ 109, 1 ≤ a ≤ b ≤ n). They are the number of folders in Igor K.'s computer, the width of a window and the numbers of the first and the last folders that need to be deleted.

Print a single number: the least possible number of times Igor K. will have to select the folders using frames to select only the folders with numbers from a to b.

## Input

The only line contains four integers n, m, a, b (1 ≤ n, m ≤ 109, 1 ≤ a ≤ b ≤ n). They are the number of folders in Igor K.'s computer, the width of a window and the numbers of the first and the last folders that need to be deleted.

## Output

Print a single number: the least possible number of times Igor K. will have to select the folders using frames to select only the folders with numbers from a to b.

## Samples

```
11 4 3 9

```

```
3

```

```
20 5 2 20

```

```
2

```

## Note

The images below illustrate statement tests.

The first test:

In this test we can select folders 3 and 4 with out first selection, folders 5, 6, 7, 8 with our second selection and folder 9 with our third, last selection.

The second test:

In this test we can first select all folders in the first row (2, 3, 4, 5), then — all other ones.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-93A |
| Contest | 93 |
| Index | A |
| Rating | 1700 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1700` |
| Codeforces 通过次数 | 2054 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/93/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/93/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P93A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

