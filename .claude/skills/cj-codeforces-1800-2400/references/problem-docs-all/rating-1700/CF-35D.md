# CF-35D Animals

## 题面快照

## Description

Once upon a time DravDe, an outstanding person famous for his professional achievements (as you must remember, he works in a warehouse storing Ogudar-Olok, a magical but non-alcoholic drink) came home after a hard day. That day he had to drink 9875 boxes of the drink and, having come home, he went to bed at once.

DravDe dreamt about managing a successful farm. He dreamt that every day one animal came to him and asked him to let it settle there. However, DravDe, being unimaginably kind, could send the animal away and it went, rejected. There were exactly n days in DravDe’s dream and the animal that came on the i-th day, ate exactly ci tons of food daily starting from day i. But if one day the animal could not get the food it needed, it got really sad. At the very beginning of the dream there were exactly X tons of food on the farm.

DravDe woke up terrified...

When he retold the dream to you, he couldn’t remember how many animals were on the farm by the end of the n-th day any more, but he did remember that nobody got sad (as it was a happy farm) and that there was the maximum possible amount of the animals. That’s the number he wants you to find out.

It should be noticed that the animals arrived in the morning and DravDe only started to feed them in the afternoon, so that if an animal willing to join them is rejected, it can’t eat any farm food. But if the animal does join the farm, it eats daily from that day to the n-th.

The first input line contains integers n and X (1 ≤ n ≤ 100, 1 ≤ X ≤ 104) — amount of days in DravDe’s dream and the total amount of food (in tons) that was there initially. The second line contains integers ci (1 ≤ ci ≤ 300). Numbers in the second line are divided by a space.

Output the only number — the maximum possible amount of animals on the farm by the end of the n-th day given that the food was enough for everybody.

## Input

The first input line contains integers n and X (1 ≤ n ≤ 100, 1 ≤ X ≤ 104) — amount of days in DravDe’s dream and the total amount of food (in tons) that was there initially. The second line contains integers ci (1 ≤ ci ≤ 300). Numbers in the second line are divided by a space.

## Output

Output the only number — the maximum possible amount of animals on the farm by the end of the n-th day given that the food was enough for everybody.

## Samples

```
3 4
1 1 1

```

```
2

```

```
3 6
1 1 1

```

```
3

```

## Note

Note to the first example: DravDe leaves the second and the third animal on the farm. The second animal will eat one ton of food on the second day and one ton on the third day. The third animal will eat one ton of food on the third day.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-35D |
| Contest | 35 |
| Index | D |
| Rating | 1700 |
| Points | 2000.0 |
| Codeforces 标签 | `dp`、`greedy` |
| 镜像标签 | `dp`、`greedy`、`*1700` |
| Codeforces 通过次数 | 3814 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/35/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/35/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P35D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

