# CF-4C Registration System

## 题面快照

## Description

A new e-mail service "Berlandesk" is going to be opened in Berland in the near future. The site administration wants to launch their project as soon as possible, that's why they ask you to help. You're suggested to implement the prototype of site registration system. The system should work on the following principle.

Each time a new user wants to register, he sends to the system a request with his name. If such a name does not exist in the system database, it is inserted into the database, and the user gets the response OK, confirming the successful registration. If the name already exists in the system database, the system makes up a new user name, sends it to the user as a prompt and also inserts the prompt into the database. The new name is formed by the following rule. Numbers, starting with 1, are appended one after another to name (name1, name2, ...), among these numbers the least i is found so that namei does not yet exist in the database.

## Input

Input

The first line contains number n (1 ≤ n ≤ 105). The following n lines contain the requests to the system. Each request is a non-empty line, and consists of not more than 32 characters, which are all lowercase Latin letters.

## Output

Output

Print n lines, which are system responses to the requests: OK in case of successful registration, or a prompt with a new name, if the requested name is already taken.

## Samples

### Sample 1

Input
```
4
abacaba
acaba
abacaba
acab
```

Output
```
OK
OK
abacaba1
OK
```

### Sample 2

Input
```
6
first
first
second
second
third
third
```

Output
```
OK
first1
OK
second1
OK
third1
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-4C |
| Contest | 4 |
| Index | C |
| Rating | 1300 |
| Points | - |
| Codeforces 标签 | `data structures`、`hashing`、`implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 104911 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 5 seconds |
| 内存限制 | 64 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/4/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/4/problem/C)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/4/C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

