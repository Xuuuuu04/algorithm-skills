# CF-78A Haiku

## 题面快照

## Description

俳句是一种日本的传统诗歌体裁。

一首俳句由 17 个音节组成，分为三句，分别包含 5、7 和 5 个音节（第一句正好 5 个音节，第二句正好 7 个音节，第三句正好 5 个音节）。一首杰出的俳句应在这三句话中描绘一个瞬间。因为诗很短，所以每个词都很重要，这也使得俳句充满象征意义。每个单词都具有特殊的含义与作用。俳句的主要原则是在寥寥数语中表达丰富的意境。

为了简化问题，在本题中我们认为一句话中的音节数等于其中元音字母的数量。只有以下字母被视为元音字母："a"、"e"、"i"、"o" 和 "u"。

现在给出某首诗的三句话，请判断它是不是一首俳句。

## Input

输入数据为三行，每行长度在 $1$ 到 $100$ 之间（包括 $1$ 和 $100$）。第 $i$ 行包含该首诗的第 $i$ 句。每句由一个或多个单词组成，单词之间以一个或多个空格分隔。一个单词是由非空的连续小写拉丁字母组成。短句的开头与结尾允许有空格。每句话都至少包含一个非空格字符。参见样例了解详细格式。

## Output

如果这首诗是俳句，输出 "YES"（不包含引号）；否则输出 "NO"（也不包含引号）。

## Samples

### Sample 1

Input
```
on  codeforces 
beta round is running
   a rustling of keys
```

Output
```
YES
```

### Sample 2

Input
```
how many gallons
of edo s rain did you drink
                                cuckoo
```

Output
```
NO
```

## Note

由 ChatGPT 5 翻译

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-78A |
| Contest | 78 |
| Index | A |
| Rating | 800 |
| Points | 500.0 |
| Codeforces 标签 | `implementation`、`strings` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 15276 |
| 镜像尝试 / 通过 | 1209 / 729 |
| 时限 | 2000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/78/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/78/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF78A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

