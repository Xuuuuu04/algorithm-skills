# CF-50D Bombing

## 题面快照

## Description

The commanding officers decided to drop a nuclear bomb on the enemy's forces. You are ordered to determine the power of the warhead that needs to be used.

The enemy has N strategically important objects. Their positions are known due to the intelligence service. The aim of the strike is to deactivate at least K important objects of the enemy. The bombing impact point is already determined and has coordinates of [X0; Y0].

The nuclear warhead is marked by the estimated impact radius R ≥ 0. All the buildings that are located closer than R to the bombing epicentre will be destroyed. All the buildings that are located further than R from the epicentre, can also be deactivated with some degree of probability. Let's assume that D is the distance between a building and the epicentre. This building's deactivation probability P(D, R) is calculated according to the following formula:
We should regard  as ea, where e ≈ 2.7182818284590452353602874713527
If the estimated impact radius of the warhead is equal to zero, then all the buildings located in the impact point will be completely demolished and all the rest of important objects will not be damaged.

The commanding officers want the probability of failing the task to be no more than ε. Nuclear warheads are too expensive a luxury, that's why you have to minimise the estimated impact radius of the warhead.

The first line contains an integer N which represents the number of the enemy's objects (1 ≤ N ≤ 100). The second line contains two integers: K is the required number of deactivated objects, and ε is the maximally permitted probability of not completing the task, given in per mils (1 ≤ K ≤ N, 1 ≤ ε ≤ 999). The third line contains X0 and Y0 which are the coordinates of the strike impact point. The next N lines contain two numbers Xi and Yi each which are the coordinates of every strategically important object. All the coordinates are integer, their absolute values do not exceed 1000.

Let us remind you that there are a thousand per mils in unity (number one).

There can be several objects in one point.

Print the sought estimated impact radius of the warhead. The absolute or relative measure of the inaccuracy of your answer should not exceed 10 - 6.

## Input

The first line contains an integer N which represents the number of the enemy's objects (1 ≤ N ≤ 100). The second line contains two integers: K is the required number of deactivated objects, and ε is the maximally permitted probability of not completing the task, given in per mils (1 ≤ K ≤ N, 1 ≤ ε ≤ 999). The third line contains X0 and Y0 which are the coordinates of the strike impact point. The next N lines contain two numbers Xi and Yi each which are the coordinates of every strategically important object. All the coordinates are integer, their absolute values do not exceed 1000.

Let us remind you that there are a thousand per mils in unity (number one).

There can be several objects in one point.

## Output

Print the sought estimated impact radius of the warhead. The absolute or relative measure of the inaccuracy of your answer should not exceed 10 - 6.

## Samples

```
1
1 500
5 5
1 2

```

```
3.84257761518762740

```

```
5
3 100
0 0
3 4
60 70
100 100
10 10
5 12

```

```
13.45126176453737600

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-50D |
| Contest | 50 |
| Index | D |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `binary search`、`dp`、`probabilities` |
| 镜像标签 | `binary search`、`dp`、`probabilities`、`*2100` |
| Codeforces 通过次数 | 702 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/50/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/50/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P50D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

