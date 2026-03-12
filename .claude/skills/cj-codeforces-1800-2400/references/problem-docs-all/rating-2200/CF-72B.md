# CF-72B INI-file

## 题面快照

## Description

The INI file format is a de facto standard for configuration files. INI files are simple text files with a basic structure. They are commonly associated with Microsoft Windows, but are also used on other platforms.

Each line in INI-file stands for key-value mapping or defines new section. A key-value line has a format "key=value",where key — is the name of some property, and value — it's value. It is possible that it will be spaces from the both sides of key and/or value, the spaces should be ignored.

A section line has a format "[section]". It means that all key-value lines after it define properties of the specified section. Of cause, the following section line changes the current section. A section line may have spaces around any of brackets.

Also you should ignore comment lines — the first non-space character of comment line is ";".

You task is to write the program which will format given INI-file in a special way:

-  first, print key-value lines which do not belong to any section;

-  print all the sections in the lexicographical (alphabetical) order of their names;

-  inside each of two previous items, order key-value lines lexicographically by "key";

-  if there are more than one key-value lines with the same key inside a single section (or outside any sections), leave only one line (which appears later in the input data);

-  remove all redundant spaces and lines.

The first line contains single integer n (1 ≤ n ≤ 510) — the number of lines in given INI-file.

The rest of the input contains a valid INI-file in n lines. Values of section, key and value contain only Latin letters, digits, "." and/or "-".

Each line has length not exceeding 255 characters and not less than 1 character. The total length of all the lines does’t exceed 10000.

Print formatted INI-file.

## Input

The first line contains single integer n (1 ≤ n ≤ 510) — the number of lines in given INI-file.

The rest of the input contains a valid INI-file in n lines. Values of section, key and value contain only Latin letters, digits, "." and/or "-".

Each line has length not exceeding 255 characters and not less than 1 character. The total length of all the lines does’t exceed 10000.

## Output

Print formatted INI-file.

## Samples

```
11
a= 1
b=a
a = 2
; comment
[z]
1=2
[y]
2=3
[z]
2=1
[w]

```

```
a=2
b=a
[w]
[y]
2=3
[z]
1=2
2=1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-72B |
| Contest | 72 |
| Index | B |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `*special`、`implementation` |
| 镜像标签 | `*special problem`、`implementation`、`*2200` |
| Codeforces 通过次数 | 117 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/72/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/72/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P72B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

