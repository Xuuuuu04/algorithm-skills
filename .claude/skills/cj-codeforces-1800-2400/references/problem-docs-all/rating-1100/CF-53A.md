# CF-53A Autocomplete

## 题面快照

## Description

Autocomplete is a program function that enables inputting the text (in editors, command line shells, browsers etc.) completing the text by its inputted part. Vasya is busy working on a new browser called 'BERowser'. He happens to be working on the autocomplete function in the address line at this very moment. A list consisting of n last visited by the user pages and the inputted part s are known. Your task is to complete s to make it an address of one of the pages from the list. You have to find the lexicographically smallest address having a prefix s.

The first line contains the s line which is the inputted part. The second line contains an integer n (1 ≤ n ≤ 100) which is the number of visited pages. Then follow n lines which are the visited pages, one on each line. All the lines have lengths of from 1 to 100 symbols inclusively and consist of lowercase Latin letters only.

If s is not the beginning of any of n addresses of the visited pages, print s. Otherwise, print the lexicographically minimal address of one of the visited pages starting from s.

The lexicographical order is the order of words in a dictionary. The lexicographical comparison of lines is realized by the '<' operator in the modern programming languages.

## Input

The first line contains the s line which is the inputted part. The second line contains an integer n (1 ≤ n ≤ 100) which is the number of visited pages. Then follow n lines which are the visited pages, one on each line. All the lines have lengths of from 1 to 100 symbols inclusively and consist of lowercase Latin letters only.

## Output

If s is not the beginning of any of n addresses of the visited pages, print s. Otherwise, print the lexicographically minimal address of one of the visited pages starting from s.

The lexicographical order is the order of words in a dictionary. The lexicographical comparison of lines is realized by the '<' operator in the modern programming languages.

## Samples

```
next
2
nextpermutation
nextelement

```

```
nextelement

```

```
find
4
find
findfirstof
findit
fand

```

```
find

```

```
find
4
fondfind
fondfirstof
fondit
fand

```

```
find

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-53A |
| Contest | 53 |
| Index | A |
| Rating | 1100 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1100` |
| Codeforces 通过次数 | 5743 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/53/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/53/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P53A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

