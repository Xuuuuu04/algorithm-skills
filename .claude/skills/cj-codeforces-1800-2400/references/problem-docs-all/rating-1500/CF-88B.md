# CF-88B Keyboard

## 题面快照

## Description

Vasya learns to type. He has an unusual keyboard at his disposal: it is rectangular and it has n rows of keys containing m keys in each row. Besides, the keys are of two types. Some of the keys have lowercase Latin letters on them and some of the keys work like the "Shift" key on standard keyboards, that is, they make lowercase letters uppercase.

Vasya can press one or two keys with one hand. However, he can only press two keys if the Euclidean distance between the centers of the keys does not exceed x. The keys are considered as squares with a side equal to 1. There are no empty spaces between neighbouring keys.

Vasya is a very lazy boy, that's why he tries to type with one hand as he eats chips with his other one. However, it is possible that some symbol can't be typed with one hand only, because the distance between it and the closest "Shift" key is strictly larger than x. In this case he will have to use his other hand. Having typed the symbol, Vasya returns other hand back to the chips.

You are given Vasya's keyboard and the text. Count the minimum number of times Vasya will have to use the other hand.

The first line contains three integers n, m, x (1 ≤ n, m ≤ 30, 1 ≤ x ≤ 50).

Next n lines contain descriptions of all the keyboard keys. Each line contains the descriptions of exactly m keys, without spaces. The letter keys are marked with the corresponding lowercase letters. The "Shift" keys are marked with the "S" symbol.

Then follow the length of the text q(1 ≤ q ≤ 5·105). The last line contains the text T, which consists of q symbols, which are uppercase and lowercase Latin letters.

If Vasya can type the text, then print the minimum number of times he will have to use his other hand. Otherwise, print "-1" (without the quotes).

## Input

The first line contains three integers n, m, x (1 ≤ n, m ≤ 30, 1 ≤ x ≤ 50).

Next n lines contain descriptions of all the keyboard keys. Each line contains the descriptions of exactly m keys, without spaces. The letter keys are marked with the corresponding lowercase letters. The "Shift" keys are marked with the "S" symbol.

Then follow the length of the text q(1 ≤ q ≤ 5·105). The last line contains the text T, which consists of q symbols, which are uppercase and lowercase Latin letters.

## Output

If Vasya can type the text, then print the minimum number of times he will have to use his other hand. Otherwise, print "-1" (without the quotes).

## Samples

```
2 2 1
ab
cd
1
A

```

```
-1

```

```
2 2 1
ab
cd
1
e

```

```
-1

```

```
2 2 1
ab
cS
5
abcBA

```

```
1

```

```
3 9 4
qwertyuio
asdfghjkl
SzxcvbnmS
35
TheQuIcKbRoWnFOXjummsovertHeLazYDOG

```

```
2

```

## Note

In the first sample the symbol "A" is impossible to print as there's no "Shift" key on the keyboard.

In the second sample the symbol "e" is impossible to print as there's no such key on the keyboard.

In the fourth sample the symbols "T", "G" are impossible to print with one hand. The other letters that are on the keyboard can be printed. Those symbols come up in the text twice, thus, the answer is 2.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-88B |
| Contest | 88 |
| Index | B |
| Rating | 1500 |
| Points | 1000.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1500` |
| Codeforces 通过次数 | 5226 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/88/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/88/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P88B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

