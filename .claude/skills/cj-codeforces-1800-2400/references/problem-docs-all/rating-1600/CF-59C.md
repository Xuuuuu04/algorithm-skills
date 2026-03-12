# CF-59C Title

## 题面快照

## Description

Vasya has recently finished writing a book. Now he faces the problem of giving it the title. Vasya wants the title to be vague and mysterious for his book to be noticeable among others. That's why the title should be represented by a single word containing at least once each of the first k Latin letters and not containing any other ones. Also, the title should be a palindrome, that is it should be read similarly from the left to the right and from the right to the left.

Vasya has already composed the approximate variant of the title. You are given the title template s consisting of lowercase Latin letters and question marks. Your task is to replace all the question marks by lowercase Latin letters so that the resulting word satisfies the requirements, described above. Each question mark should be replaced by exactly one letter, it is not allowed to delete characters or add new ones to the template. If there are several suitable titles, choose the first in the alphabetical order, for Vasya's book to appear as early as possible in all the catalogues.

The first line contains an integer k (1 ≤ k ≤ 26) which is the number of allowed alphabet letters. The second line contains s which is the given template. In s only the first k lowercase letters of Latin alphabet and question marks can be present, the length of s is from 1 to 100 characters inclusively.

If there is no solution, print IMPOSSIBLE. Otherwise, a single line should contain the required title, satisfying the given template. The title should be a palindrome and it can only contain the first k letters of the Latin alphabet. At that, each of those k letters must be present at least once. If there are several suitable titles, print the lexicographically minimal one.

The lexicographical comparison is performed by the standard < operator in modern programming languages. The line a is lexicographically smaller than the line b, if exists such an i (1 ≤ i ≤ |s|), that ai < bi, and for any j (1 ≤ j < i) aj = bj. |s| stands for the length of the given template.

## Input

The first line contains an integer k (1 ≤ k ≤ 26) which is the number of allowed alphabet letters. The second line contains s which is the given template. In s only the first k lowercase letters of Latin alphabet and question marks can be present, the length of s is from 1 to 100 characters inclusively.

## Output

If there is no solution, print IMPOSSIBLE. Otherwise, a single line should contain the required title, satisfying the given template. The title should be a palindrome and it can only contain the first k letters of the Latin alphabet. At that, each of those k letters must be present at least once. If there are several suitable titles, print the lexicographically minimal one.

The lexicographical comparison is performed by the standard < operator in modern programming languages. The line a is lexicographically smaller than the line b, if exists such an i (1 ≤ i ≤ |s|), that ai < bi, and for any j (1 ≤ j < i) aj = bj. |s| stands for the length of the given template.

## Samples

```
3
a?c

```

```
IMPOSSIBLE

```

```
2
a??a

```

```
abba

```

```
2
?b?a

```

```
abba

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-59C |
| Contest | 59 |
| Index | C |
| Rating | 1600 |
| Points | 1500.0 |
| Codeforces 标签 | `expression parsing` |
| 镜像标签 | `expression parsing`、`*1600` |
| Codeforces 通过次数 | 2429 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/59/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/59/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P59C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

