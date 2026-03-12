# CF-97A Domino

## 题面快照

## Description

Little Gennady was presented with a set of domino for his birthday. The set consists of 28 different dominoes of size 2 × 1. Both halves of each domino contain one digit from 0 to 6.

```
0-0 0-1 0-2 0-3 0-4 0-5 0-6
1-1 1-2 1-3 1-4 1-5 1-6
2-2 2-3 2-4 2-5 2-6
3-3 3-4 3-5 3-6
4-4 4-5 4-6
5-5 5-6
6-6

```

The figure that consists of 28 dominoes is called magic, if it can be fully covered with 14 non-intersecting squares of size 2 × 2 so that each square contained four equal numbers. Every time Gennady assembles a magic figure, some magic properties of the set appear — he wins the next contest. Gennady noticed that he can't assemble a figure that has already been assembled, otherwise someone else wins the contest.

Gennady chose a checked field of size n × m and put there rectangular chips of sizes 1 × 2 and 2 × 1. Each chip fully occupies exactly two neighboring squares of the field. Those chips do not overlap but they can touch each other. Overall the field has exactly 28 chips, equal to the number of dominoes in the set. Now Gennady wants to replace each chip with a domino so that a magic figure appeared as a result. Different chips should be replaced by different dominoes. Determine in what number of contests Gennady can win over at the given position of the chips. You are also required to find one of the possible ways of replacing chips with dominoes to win the next Codeforces round.

The first line contains two positive integers n and m (1 ≤ n, m ≤ 30). Each of the following n lines contains m characters, which is the position of chips on the field. The dots stand for empty spaces, Latin letters from "a" to "z" and "A", "B" stand for the positions of the chips. There are exactly 28 chips on the field. The squares covered by the same chip are marked by the same letter, different chips are marked by different letters. It is guaranteed that the field's description is correct.

It is also guaranteed that at least one solution exists.

Print on the first line the number of ways to replace chips with dominoes to get a magic figure. That is the total number of contests that can be won using this arrangement of the chips. Next n lines containing m characters each, should contain a field from dots and numbers from 0 to 6 — any of the possible solutions. All dominoes should be different.

## Input

The first line contains two positive integers n and m (1 ≤ n, m ≤ 30). Each of the following n lines contains m characters, which is the position of chips on the field. The dots stand for empty spaces, Latin letters from "a" to "z" and "A", "B" stand for the positions of the chips. There are exactly 28 chips on the field. The squares covered by the same chip are marked by the same letter, different chips are marked by different letters. It is guaranteed that the field's description is correct.

It is also guaranteed that at least one solution exists.

## Output

Print on the first line the number of ways to replace chips with dominoes to get a magic figure. That is the total number of contests that can be won using this arrangement of the chips. Next n lines containing m characters each, should contain a field from dots and numbers from 0 to 6 — any of the possible solutions. All dominoes should be different.

## Samples

```
8 8
.aabbcc.
.defghi.
kdefghij
klmnopqj
.lmnopq.
.rstuvw.
xrstuvwy
xzzAABBy

```

```
10080
.001122.
.001122.
33440055
33440055
.225566.
.225566.
66113344
66113344

```

-  登录后递交

-

-  讨论 (0)

-  题解 (0)

-  文件

-  统计

-

状态
- 评测队列

- 服务状态

开发
- 开源

支持
- 帮助

- 联系我们

关于
- 关于

- 隐私

- 服务条款

- 版权申诉

-  Language
- English

- 한국어

- 简体中文

- 正體中文

- 兼容模式

-  主题
- 亮色

- 暗色

-

- © 2021-2026 Hydro.ac

-

- Worker 2, 32ms

- Hydro v5.0.0-beta.18-f9f3fd7-dirty Professional

还没有账户？
注册一个 HydroOJ 通用账户，您就可以在我们提供的所有在线评测服务上提交代码、参与讨论。
现在注册

关闭
登录
使用您的 HydroOJ 通用账户
用户名

密码

记住我

Login with GitHub

Login with Telegram

Login with Wechat

忘记密码或者用户名？

window.UiContextNew = '{"problemId":"codeforces-P97A","problemNumId":25557,"codeLang":"cc.cc17o2","pdoc":{"_id":"60d16385f44e0344a27bab30","content":"## Description\\n\\n<div><p>Little Gennady was presented with a set of domino for his birthday. The set consists of <span class=\\"tex-span\\">28</span> different dominoes of size <span class=\\"tex-span\\">2\u2009\xD7\u20091</span>. Both halves of each domino contain one digit from <span class=\\"tex-span\\">0</span> to <span class=\\"tex-span\\">6</span>. </p><pre class=\\"verbatim\\">0-0 0-1 0-2 0-3 0-4 0-5 0-6<br>1-1 1-2 1-3 1-4 1-5 1-6<br>2-2 2-3 2-4 2-5 2-6<br>3-3 3-4 3-5 3-6<br>4-4 4-5 4-6<br>5-5 5-6<br>6-6<br></pre><p>The figure that consists of <span class=\\"tex-span\\">28</span> dominoes is called <span class=\\"tex-font-style-underline\\">magic</span>, if it can be fully covered with <span class=\\"tex-span\\">14</span> non-intersecting squares of size <span class=\\"tex-span\\">2\u2009\xD7\u20092</span> so that each square contained four equal numbers. Every time Gennady assembles a magic figure, some magic properties of the set appear \u2014 he wins the next contest. Gennady noticed that he can\'t assemble a figure that has already been assembled, otherwise someone else wins the contest.</p><center> <img class=\\"tex-graphics\\" src=\\"./25557/file/VDVihqQ4.png\\" style=\\"max-width: 100.0%;max-height: 100.0%;\\"> </center><p>Gennady chose a checked field of size <span class=\\"tex-span\\"><i>n</i>\u2009\xD7\u2009<i>m</i></span> and put there rectangular chips of sizes <span class=\\"tex-span\\">1\u2009\xD7\u20092</span> and <span class=\\"tex-span\\">2\u2009\xD7\u20091</span>. Each chip fully occupies exactly two neighboring squares of the field. Those chips do not overlap but they can touch each other. Overall the field has exactly <span class=\\"tex-span\\">28</span> chips, equal to the number of dominoes in the set. Now Gennady wants to replace each chip with a domino so that a magic figure appeared as a result. Different chips should be replaced by different dominoes. Determine in what number of contests Gennady can win over at the given position of the chips. You are also required to find one of the possible ways of replacing chips with dominoes to win the next Codeforces round.</p></div><div class=\\"input-specification\\"><p>The first line contains two positive integers <span class=\\"tex-span\\"><i>n</i></span> and <span class=\\"tex-span\\"><i>m</i></span> (<span class=\\"tex-span\\">1\u2009\u2264\u2009<i>n</i>,\u2009<i>m</i>\u2009\u2264\u200930</span>). Each of the following <span class=\\"tex-span\\"><i>n</i></span> lines contains <span class=\\"tex-span\\"><i>m</i></span> characters, which is the position of chips on the field. The dots stand for empty spaces, Latin letters from \\"a\\" to \\"z\\" and \\"A\\", \\"B\\" stand for the positions of the chips. There are exactly 28 chips on the field. The squares covered by the same chip are marked by the same letter, different chips are marked by different letters. It is guaranteed that the field\'s description is correct.</p><p>It is also guaranteed that at least one solution exists.</p></div><div class=\\"output-specification\\"><p>Print on the first line the number of ways to replace chips with dominoes to get a magic figure. That is the total number of contests that can be won using this arrangement of the chips. Next <span class=\\"tex-span\\"><i>n</i></span> lines containing <span class=\\"tex-span\\"><i>m</i></span> characters each, should contain a field from dots and numbers from <span class=\\"tex-span\\">0</span> to <span class=\\"tex-span\\">6</span> \u2014 any of the possible solutions. All dominoes should be different.</p></div>\\n\\n\\n## Input\\n\\n<p>The first line contains two positive integers <span class=\\"tex-span\\"><i>n</i></span> and <span class=\\"tex-span\\"><i>m</i></span> (<span class=\\"tex-span\\">1\u2009\u2264\u2009<i>n</i>,\u2009<i>m</i>\u2009\u2264\u200930</span>). Each of the following <span class=\\"tex-span\\"><i>n</i></span> lines contains <span class=\\"tex-span\\"><i>m</i></span> characters, which is the position of chips on the field. The dots stand for empty spaces, Latin letters from \\"a\\" to \\"z\\" and \\"A\\", \\"B\\" stand for the positions of the chips. There are exactly 28 chips on the field. The squares covered by the same chip are marked by the same letter, different chips are marked by different letters. It is guaranteed that the field\'s description is correct.</p><p>It is also guaranteed that at least one solution exists.</p>\\n\\n\\n## Output\\n\\n<p>Print on the first line the number of ways to replace chips with dominoes to get a magic figure. That is the total number of contests that can be won using this arrangement of the chips. Next <span class=\\"tex-span\\"><i>n</i></span> lines containing <span class=\\"tex-span\\"><i>m</i></span> characters each, should contain a field from dots and numbers from <span class=\\"tex-span\\">0</span> to <span class=\\"tex-span\\">6</span> \u2014 any of the possible solutions. All dominoes should be different.</p>\\n\\n\\n## Samples\\n\\n```input1\\n8 8\\n.aabbcc.\\n.defghi.\\nkdefghij\\nklmnopqj\\n.lmnopq.\\n.rstuvw.\\nxrstuvwy\\nxzzAABBy\\n\\n```\\n\\n```output1\\n10080\\n.001122.\\n.001122.\\n33440055\\n33440055\\n.225566.\\n.225566.\\n66113344\\n66113344\\n\\n```\\n\\n\\n\\n","owner":1,"domainId":"system","docType":10,"docId":25557,"title":"Domino","tag":["brute force","implementation","*2400"],"hidden":false,"nSubmit":0,"nAccept":0,"pid":"codeforces-P97A","additional_file":[{"_id":"VDVihqQ4.png","name":"VDVihqQ4.png","size":109677,"lastModified":"2021-06-22T04:14:04.660Z","etag":"77a29ba4fbc5392e036c1fcb5976af8a"}],"data":[{"_id":"config.yaml","name":"config.yaml","size":73,"lastModified":"2021-06-22T04:14:04.739Z","etag":"cedac709f283403e8f2bf9938f030bc3"}],"config":{"count":0,"memoryMin":256,"memoryMax":256,"timeMin":1000,"timeMax":1000,"type":"remote_judge","subType":"codeforces","target":"P97A","langs":["codeforces.43","codeforces.52","codeforces.50","codeforces.80","codeforces.54","codeforces.73","codeforces.89","codeforces.59","codeforces.61","codeforces.65","codeforces.79","codeforces.9","codeforces.28","codeforces.32","codeforces.12","codeforces.60","codeforces.87","codeforces.36","codeforces.83","codeforces.88","codeforces.48","codeforces.19","codeforces.3","codeforces.4","codeforces.51","codeforces.13","codeforces.6","codeforces.7","codeforces.31","codeforces.40","codeforces.41","codeforces.70","codeforces.67","codeforces.75","codeforces.49","codeforces.20","codeforces.34","codeforces.55","codeforces"]},"difficulty":9},"canViewRecord":true,"postSubmitUrl":"/p/25557/submit","getSubmissionsUrl":"/record?fullStatus=true&pid=25557","getRecordDetailUrl":"/record/%7Brid%7D","pretestConnUrl":"record-conn?pretest=1&uidOrName=0&pid=25557&domainId=system"}'; window.UserContextNew = '{}';

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-97A |
| Contest | 97 |
| Index | A |
| Rating | 2400 |
| Points | - |
| Codeforces 标签 | `brute force`、`implementation` |
| 镜像标签 | `brute force`、`implementation`、`*2400` |
| Codeforces 通过次数 | 335 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/97/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/97/problem/A)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P97A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

