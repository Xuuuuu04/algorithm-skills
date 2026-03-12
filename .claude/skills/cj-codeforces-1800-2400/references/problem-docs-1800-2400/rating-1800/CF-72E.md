# CF-72E Ali goes shopping

## 题面快照

## Description

Ali Koochooloo is going to buy new clothes since we're reaching Noruz, the ancient Persian festival and the beginning of new Persian year.

When Ali entered a shop, he saw that the shopkeeper was a programmer and since there is no money in programming he had changed his career. The shopkeeper told Ali that he can buy anything for free if he could answer a simple question in 10 seconds. But to see the question Ali has to pay 3 tomans.

Ali agreed instantly and the shopkeeper handed him a piece of paper containing the task. The task was indeed very simple. It said:

Let string A be ababababababab. Which non-empty substring of A is repeated the most times in it?

Ali answered fast. He said the answer is a. But the shopkeeper said that Ali is wrong and asked him to read the rest of statement:

If several substrings have the maximal repeat time, then the substring with maximal length would be the answer, in case of a tie the alphabetically latest substring will be chosen.

So the answer is ab.

Now Ali wants us to solve this problem for different strings. We don't have a great advantage over Ali, we just have a computer and a weird language.

The single line consisting of a string A. It is non-empty, made of lower-case Latin letters and contains at most 30 characters.

The single line contains the answer.

## Input

The single line consisting of a string A. It is non-empty, made of lower-case Latin letters and contains at most 30 characters.

## Output

The single line contains the answer.

## Samples

```
abab

```

```
ab

```

```
abcd

```

```
abcd

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-72E |
| Contest | 72 |
| Index | E |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `*special`、`brute force`、`strings` |
| 镜像标签 | `*special problem`、`brute force`、`strings`、`*1800` |
| Codeforces 通过次数 | 181 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/72/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/72/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P72E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

