# CF-48A Rock-paper-scissors

## 题面快照

## Description

Uncle Fyodor, Matroskin the Cat and Sharic the Dog live their simple but happy lives in Prostokvashino. Sometimes they receive parcels from Uncle Fyodor’s parents and sometimes from anonymous benefactors, in which case it is hard to determine to which one of them the package has been sent. A photographic rifle is obviously for Sharic who loves hunting and fish is for Matroskin, but for whom was a new video game console meant? Every one of the three friends claimed that the present is for him and nearly quarreled. Uncle Fyodor had an idea how to solve the problem justly: they should suppose that the console was sent to all three of them and play it in turns. Everybody got relieved but then yet another burning problem popped up — who will play first? This time Matroskin came up with a brilliant solution, suggesting the most fair way to find it out: play rock-paper-scissors together. The rules of the game are very simple. On the count of three every player shows a combination with his hand (or paw). The combination corresponds to one of three things: a rock, scissors or paper. Some of the gestures win over some other ones according to well-known rules: the rock breaks the scissors, the scissors cut the paper, and the paper gets wrapped over the stone. Usually there are two players. Yet there are three friends, that’s why they decided to choose the winner like that: If someone shows the gesture that wins over the other two players, then that player wins. Otherwise, another game round is required. Write a program that will determine the winner by the gestures they have shown.

## Input

Input

The first input line contains the name of the gesture that Uncle Fyodor showed, the second line shows which gesture Matroskin showed and the third line shows Sharic’s gesture.

## Output

Output

Print "F" (without quotes) if Uncle Fyodor wins. Print "M" if Matroskin wins and "S" if Sharic wins. If it is impossible to find the winner, print "?".

## Samples

### Sample 1

Input
```
rock
rock
rock
```

Output
```
?
```

### Sample 2

Input
```
paper
rock
rock
```

Output
```
F
```

### Sample 3

Input
```
scissors
rock
rock
```

Output
```
?
```

### Sample 4

Input
```
scissors
paper
rock
```

Output
```
?
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-48A |
| Contest | 48 |
| Index | A |
| Rating | 900 |
| Points | - |
| Codeforces 标签 | `implementation`、`schedules` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 7226 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 2 seconds |
| 内存限制 | 256 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/48/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/48/problem/A)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/48/A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

