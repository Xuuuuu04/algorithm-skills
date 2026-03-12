# CF-44C Holidays

## 题面快照

## Description

School holidays come in Berland. The holidays are going to continue for n days. The students of school №N are having the time of their lives and the IT teacher Marina Sergeyevna, who has spent all the summer busy checking the BSE (Berland State Examination) results, has finally taken a vacation break! Some people are in charge of the daily watering of flowers in shifts according to the schedule. However when Marina Sergeyevna was making the schedule, she was so tired from work and so lost in dreams of the oncoming vacation that she perhaps made several mistakes. In fact, it is possible that according to the schedule, on some days during the holidays the flowers will not be watered or will be watered multiple times. Help Marina Sergeyevna to find a mistake.

The first input line contains two numbers n and m (1 ≤ n, m ≤ 100) — the number of days in Berland holidays and the number of people in charge of the watering respectively. The next m lines contain the description of the duty schedule. Each line contains two integers ai and bi (1 ≤ ai ≤ bi ≤ n), meaning that the i-th person in charge should water the flowers from the ai-th to the bi-th day inclusively, once a day. The duty shifts are described sequentially, i.e. bi ≤ ai + 1 for all i from 1 to n - 1 inclusively.

Print "OK" (without quotes), if the schedule does not contain mistakes. Otherwise you have to find the minimal number of a day when the flowers will not be watered or will be watered multiple times, and output two integers — the day number and the number of times the flowers will be watered that day.

## Input

The first input line contains two numbers n and m (1 ≤ n, m ≤ 100) — the number of days in Berland holidays and the number of people in charge of the watering respectively. The next m lines contain the description of the duty schedule. Each line contains two integers ai and bi (1 ≤ ai ≤ bi ≤ n), meaning that the i-th person in charge should water the flowers from the ai-th to the bi-th day inclusively, once a day. The duty shifts are described sequentially, i.e. bi ≤ ai + 1 for all i from 1 to n - 1 inclusively.

## Output

Print "OK" (without quotes), if the schedule does not contain mistakes. Otherwise you have to find the minimal number of a day when the flowers will not be watered or will be watered multiple times, and output two integers — the day number and the number of times the flowers will be watered that day.

## Samples

```
10 5
1 2
3 3
4 6
7 7
8 10

```

```
OK

```

```
10 5
1 2
2 3
4 5
7 8
9 10

```

```
2 2

```

```
10 5
1 2
3 3
5 7
7 7
7 10

```

```
4 0

```

## Note

Keep in mind that in the second sample the mistake occurs not only on the second day, but also on the sixth day, when nobody waters the flowers. However, you have to print the second day, i.e. the day with the minimal number.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-44C |
| Contest | 44 |
| Index | C |
| Rating | 1300 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1300` |
| Codeforces 通过次数 | 4016 |
| 镜像尝试 / 通过 | 4 / 2 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/44/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/44/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P44C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

