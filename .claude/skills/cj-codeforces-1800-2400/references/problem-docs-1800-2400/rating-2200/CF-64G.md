# CF-64G Path Canonization

## 题面快照

## Description

A path in some Unix-similar file system is given. The path consists of elements separated with characters "/". For example: "/usr/share/mysql/../tomcat6/conf/server.xml". The path starts with the root directory (i.e. starts with the character "/"). Each element means a name of file or directory, or it is one of two special elements: "." или "..". First of them stands for the current directory (for example, path "/./usr/././share" is equal to "/usr/share"). The second element ".." stands for the moving to the parent directory (for example, path "/usr/share/../lib" is equal to "/usr/lib").

You task is to convert the given path to such a path, which doesn't contain special elements "." and/or "..". If it is impossible, print "-1". The only reason for it is an attempt to move to the parent directory from the root.

The only line contains the given path. The path starts with "/" and consists of elements separated with "/". No two "/" follow one after another (consecutively). The only path which can end with "/" is the root directory path equal to "/".

Each element may contain "a"-"z", "0"-"9" and dots. Any element different from specials "." and ".." contains at least one character different from the dots.

The path length is between 1 and 1000 inclusively.

Print the required path or "-1".

## Input

The only line contains the given path. The path starts with "/" and consists of elements separated with "/". No two "/" follow one after another (consecutively). The only path which can end with "/" is the root directory path equal to "/".

Each element may contain "a"-"z", "0"-"9" and dots. Any element different from specials "." and ".." contains at least one character different from the dots.

The path length is between 1 and 1000 inclusively.

## Output

Print the required path or "-1".

## Samples

```
/usr/share/mysql/../tomcat6/conf/server.xml

```

```
/usr/share/tomcat6/conf/server.xml

```

```
/a/./././..

```

```
/

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-64G |
| Contest | 64 |
| Index | G |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `*special` |
| 镜像标签 | `*special problem`、`*2200` |
| Codeforces 通过次数 | 129 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/64/G)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/64/problem/G)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P64G)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

