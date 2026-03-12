# CF-49A Sleuth

## 题面快照

## Description

Vasya plays the sleuth with his friends. The rules of the game are as follows: those who play for the first time, that is Vasya is the sleuth, he should investigate a "crime" and find out what is happening. He can ask any questions whatsoever that can be answered with "Yes" or "No". All the rest agree beforehand to answer the questions like that: if the question’s last letter is a vowel, they answer "Yes" and if the last letter is a consonant, they answer "No". Of course, the sleuth knows nothing about it and his task is to understand that.

Unfortunately, Vasya is not very smart. After 5 hours of endless stupid questions everybody except Vasya got bored. That’s why Vasya’s friends ask you to write a program that would give answers instead of them.

The English alphabet vowels are: A, E, I, O, U, Y

The English alphabet consonants are: B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z

The single line contains a question represented by a non-empty line consisting of large and small Latin letters, spaces and a question mark. The line length does not exceed 100. It is guaranteed that the question mark occurs exactly once in the line — as the last symbol and that the line contains at least one letter.

Print answer for the question in a single line: YES if the answer is "Yes", NO if the answer is "No".

Remember that in the reply to the question the last letter, not the last character counts. I. e. the spaces and the question mark do not count as letters.

## Input

The single line contains a question represented by a non-empty line consisting of large and small Latin letters, spaces and a question mark. The line length does not exceed 100. It is guaranteed that the question mark occurs exactly once in the line — as the last symbol and that the line contains at least one letter.

## Output

Print answer for the question in a single line: YES if the answer is "Yes", NO if the answer is "No".

Remember that in the reply to the question the last letter, not the last character counts. I. e. the spaces and the question mark do not count as letters.

## Samples

```
Is it a melon?

```

```
NO

```

```
Is it an apple?

```

```
YES

```

```
Is     it a banana ?

```

```
YES

```

```
Is   it an apple  and a  banana   simultaneouSLY?

```

```
YES

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-49A |
| Contest | 49 |
| Index | A |
| Rating | 800 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*800` |
| Codeforces 通过次数 | 15106 |
| 镜像尝试 / 通过 | 2 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/49/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/49/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P49A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

