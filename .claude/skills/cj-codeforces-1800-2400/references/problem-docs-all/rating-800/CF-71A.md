# CF-71A Way Too Long Words

## 题面快照

## Description

有时候，像“localization”或“internationalization”这样的词汇如此之长，以至于在一篇文章中多次写下这些词语令人厌烦。

让我们考虑一个词太长，如果它的长度严格超过 10个字符。太长的单词应该用一个特殊的缩写代替。

这个缩写是这样写的：我们写下一个单词的第一个和最后一个字母，并在它们之间写出第一个和最后一个字母之间的字母数。该数字是十进制系统，不包含任何前导零。

因此，“localization”将拼写为“l10n”，而“internationalization”将拼写为”i18n”。

建议您使用缩写来自动更改单词的过程。因为所有太长的单词应该用缩写代替，不太长的单词不应该经历任何改变。

## Input

第一行包含一个整数 n（ 1 <= N <= 100 1 < = n < = 1 0 0）。以下各项 n 行包含一个词。所有的单词由小写拉丁字母组成， 并且拥有从1到100个字符的长度。 _ _

## Output

输出n行。第i行应包含来自输入数据的第 i个字替换的结果。

## Samples

### Sample 1

Input
```
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
```

Output
```
word
l10n
i18n
p43s
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Luogu 镜像 |
| 编号 | CF-71A |
| Contest | 71 |
| Index | A |
| Rating | 800 |
| Points | 500.0 |
| Codeforces 标签 | `strings` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 492130 |
| 镜像尝试 / 通过 | 3486 / 1806 |
| 时限 | 1000 ms |
| 内存限制 | 256000 KB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/71/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/71/problem/A)
- Luogu 镜像：[mirror](https://www.luogu.com.cn/problem/CF71A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

