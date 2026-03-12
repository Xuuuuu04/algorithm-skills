# CF-73B Need For Brake

## 题面快照

## Description

Vasya plays the Need For Brake. He plays because he was presented with a new computer wheel for birthday! Now he is sure that he will win the first place in the championship in his favourite racing computer game!

n racers take part in the championship, which consists of a number of races. After each race racers are arranged from place first to n-th (no two racers share the same place) and first m places are awarded. Racer gains bi points for i-th awarded place, which are added to total points, obtained by him for previous races. It is known that current summary score of racer i is ai points. In the final standings of championship all the racers will be sorted in descending order of points. Racers with an equal amount of points are sorted by increasing of the name in lexicographical order.

Unfortunately, the championship has come to an end, and there is only one race left. Vasya decided to find out what the highest and lowest place he can take up as a result of the championship.

The first line contains number n (1 ≤ n ≤ 105) — number of racers. Each of the next n lines contains si and ai — nick of the racer (nonempty string, which consist of no more than 20 lowercase Latin letters) and the racer's points (0 ≤ ai ≤ 106). Racers are given in the arbitrary order.

The next line contains the number m (0 ≤ m ≤ n). Then m nonnegative integer numbers bi follow. i-th number is equal to amount of points for the i-th awarded place (0 ≤ bi ≤ 106).

The last line contains Vasya's racer nick.

Output two numbers — the highest and the lowest place Vasya can take up as a result of the championship.

## Input

The first line contains number n (1 ≤ n ≤ 105) — number of racers. Each of the next n lines contains si and ai — nick of the racer (nonempty string, which consist of no more than 20 lowercase Latin letters) and the racer's points (0 ≤ ai ≤ 106). Racers are given in the arbitrary order.

The next line contains the number m (0 ≤ m ≤ n). Then m nonnegative integer numbers bi follow. i-th number is equal to amount of points for the i-th awarded place (0 ≤ bi ≤ 106).

The last line contains Vasya's racer nick.

## Output

Output two numbers — the highest and the lowest place Vasya can take up as a result of the championship.

## Samples

```
3
teama 10
teamb 20
teamc 40
2
10 20
teama

```

```
2 3

```

```
2
teama 10
teamb 10
2
10 10
teamb

```

```
2 2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-73B |
| Contest | 73 |
| Index | B |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `binary search`、`greedy`、`sortings` |
| 镜像标签 | `binary search`、`greedy`、`sortings`、`*2000` |
| Codeforces 通过次数 | 540 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 4000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/73/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/73/problem/B)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P73B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

