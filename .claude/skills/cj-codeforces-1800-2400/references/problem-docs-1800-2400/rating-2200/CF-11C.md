# CF-11C How Many Squares?

## 题面快照

## Description

You are given a 0-1 rectangular matrix. What is the number of squares in it? A square is a solid square frame (border) with linewidth equal to 1. A square should be at least 2 × 2. We are only interested in two types of squares:

-  squares with each side parallel to a side of the matrix;

-  squares with each side parallel to a diagonal of the matrix.

```

For example the following matrix contains only one square of the first type:
0000000
0111100
0100100
0100100
0111100

```

```

The following matrix contains only one square of the second type:
0000000
0010000
0101000
0010000
0000000

```

Regardless of type, a square must contain at least one 1 and can't touch (by side or corner) any foreign 1. Of course, the lengths of the sides of each square should be equal.

How many squares are in the given matrix?

The first line contains integer t (1 ≤ t ≤ 10000), where t is the number of test cases in the input. Then test cases follow. Each case starts with a line containing integers n and m (2 ≤ n, m ≤ 250), where n is the number of rows and m is the number of columns. The following n lines contain m characters each (0 or 1).

The total number of characters in all test cases doesn't exceed 106 for any input file.

You should output exactly t lines, with the answer to the i-th test case on the i-th line.

## Input

The first line contains integer t (1 ≤ t ≤ 10000), where t is the number of test cases in the input. Then test cases follow. Each case starts with a line containing integers n and m (2 ≤ n, m ≤ 250), where n is the number of rows and m is the number of columns. The following n lines contain m characters each (0 or 1).

The total number of characters in all test cases doesn't exceed 106 for any input file.

## Output

You should output exactly t lines, with the answer to the i-th test case on the i-th line.

## Samples

```
2
8 8
00010001
00101000
01000100
10000010
01000100
00101000
11010011
11000011
10 10
1111111000
1000001000
1011001000
1011001010
1000001101
1001001010
1010101000
1001001000
1000001000
1111111000

```

```
1
2

```

```
1
12 11
11111111111
10000000001
10111111101
10100000101
10101100101
10101100101
10100000101
10100000101
10111111101
10000000001
11111111111
00000000000

```

```
3

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

- Worker 2, 20ms

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

window.UiContextNew = '{"problemId":"codeforces-P11C","problemNumId":25120,"codeLang":"cc.cc17o2","pdoc":{"_id":"60d17047f44e0344a27bacd9","content":"## Description\\n\\n<div><p>You are given a 0-1 rectangular matrix. What is the number of squares in it? A square is a solid square frame (border) with linewidth equal to 1. A square should be at least <span class=\\"tex-span\\">2\u2009\xD7\u20092</span>. We are only interested in two types of squares: </p><ol> <li> squares with each side parallel to a side of the matrix; </li><li> squares with each side parallel to a diagonal of the matrix. </li></ol><pre class=\\"verbatim\\"><br>For example the following matrix contains only one square of the first type: <br>0000000 <br>0111100 <br>0100100 <br>0100100 <br>0111100<br></pre><pre class=\\"verbatim\\"><br>The following matrix contains only one square of the second type:<br>0000000<br>0010000<br>0101000<br>0010000<br>0000000<br></pre><p>Regardless of type, a square must contain at least one <span class=\\"tex-font-style-tt\\">1</span> and can\'t touch (by side or corner) any foreign <span class=\\"tex-font-style-tt\\">1</span>. Of course, the lengths of the sides of each square should be equal.</p><p>How many squares are in the given matrix?</p></div><div class=\\"input-specification\\"><p>The first line contains integer <span class=\\"tex-span\\"><i>t</i></span> (<span class=\\"tex-span\\">1\u2009\u2264\u2009<i>t</i>\u2009\u2264\u200910000</span>), where <span class=\\"tex-span\\"><i>t</i></span> is the number of test cases in the input. Then test cases follow. Each case starts with a line containing integers <span class=\\"tex-span\\"><i>n</i></span> and <span class=\\"tex-span\\"><i>m</i></span> (<span class=\\"tex-span\\">2\u2009\u2264\u2009<i>n</i>,\u2009<i>m</i>\u2009\u2264\u2009250</span>), where <span class=\\"tex-span\\"><i>n</i></span> is the number of rows and <span class=\\"tex-span\\"><i>m</i></span> is the number of columns. The following <span class=\\"tex-span\\"><i>n</i></span> lines contain <span class=\\"tex-span\\"><i>m</i></span> characters each (<span class=\\"tex-font-style-tt\\">0</span> or <span class=\\"tex-font-style-tt\\">1</span>).</p><p>The total number of characters in all test cases doesn\'t exceed <span class=\\"tex-span\\">10<sup class=\\"upper-index\\">6</sup></span> for any input file.</p></div><div class=\\"output-specification\\"><p>You should output exactly <span class=\\"tex-span\\"><i>t</i></span> lines, with the answer to the <span class=\\"tex-span\\"><i>i</i></span>-th test case on the <span class=\\"tex-span\\"><i>i</i></span>-th line.</p></div>\\n\\n\\n## Input\\n\\n<p>The first line contains integer <span class=\\"tex-span\\"><i>t</i></span> (<span class=\\"tex-span\\">1\u2009\u2264\u2009<i>t</i>\u2009\u2264\u200910000</span>), where <span class=\\"tex-span\\"><i>t</i></span> is the number of test cases in the input. Then test cases follow. Each case starts with a line containing integers <span class=\\"tex-span\\"><i>n</i></span> and <span class=\\"tex-span\\"><i>m</i></span> (<span class=\\"tex-span\\">2\u2009\u2264\u2009<i>n</i>,\u2009<i>m</i>\u2009\u2264\u2009250</span>), where <span class=\\"tex-span\\"><i>n</i></span> is the number of rows and <span class=\\"tex-span\\"><i>m</i></span> is the number of columns. The following <span class=\\"tex-span\\"><i>n</i></span> lines contain <span class=\\"tex-span\\"><i>m</i></span> characters each (<span class=\\"tex-font-style-tt\\">0</span> or <span class=\\"tex-font-style-tt\\">1</span>).</p><p>The total number of characters in all test cases doesn\'t exceed <span class=\\"tex-span\\">10<sup class=\\"upper-index\\">6</sup></span> for any input file.</p>\\n\\n\\n## Output\\n\\n<p>You should output exactly <span class=\\"tex-span\\"><i>t</i></span> lines, with the answer to the <span class=\\"tex-span\\"><i>i</i></span>-th test case on the <span class=\\"tex-span\\"><i>i</i></span>-th line.</p>\\n\\n\\n## Samples\\n\\n```input1\\n2\\n8 8\\n00010001\\n00101000\\n01000100\\n10000010\\n01000100\\n00101000\\n11010011\\n11000011\\n10 10\\n1111111000\\n1000001000\\n1011001000\\n1011001010\\n1000001101\\n1001001010\\n1010101000\\n1001001000\\n1000001000\\n1111111000\\n\\n```\\n\\n```output1\\n1\\n2\\n\\n```\\n\\n\\n\\n\\n\\n\\n```input2\\n1\\n12 11\\n11111111111\\n10000000001\\n10111111101\\n10100000101\\n10101100101\\n10101100101\\n10100000101\\n10100000101\\n10111111101\\n10000000001\\n11111111111\\n00000000000\\n\\n```\\n\\n```output2\\n3\\n\\n```\\n\\n\\n\\n","owner":1,"domainId":"system","docType":10,"docId":25120,"title":"How Many Squares?","tag":["implementation","*2200"],"hidden":false,"nSubmit":0,"nAccept":0,"pid":"codeforces-P11C","data":[{"_id":"config.yaml","name":"config.yaml","size":72,"lastModified":"2021-06-22T05:08:23.732Z","etag":"828c09004388585739ed090625998920"}],"config":{"count":0,"memoryMin":64,"memoryMax":64,"timeMin":2000,"timeMax":2000,"type":"remote_judge","subType":"codeforces","target":"P11C","langs":["codeforces.43","codeforces.52","codeforces.50","codeforces.80","codeforces.54","codeforces.73","codeforces.89","codeforces.59","codeforces.61","codeforces.65","codeforces.79","codeforces.9","codeforces.28","codeforces.32","codeforces.12","codeforces.60","codeforces.87","codeforces.36","codeforces.83","codeforces.88","codeforces.48","codeforces.19","codeforces.3","codeforces.4","codeforces.51","codeforces.13","codeforces.6","codeforces.7","codeforces.31","codeforces.40","codeforces.41","codeforces.70","codeforces.67","codeforces.75","codeforces.49","codeforces.20","codeforces.34","codeforces.55","codeforces"]},"difficulty":8},"canViewRecord":true,"postSubmitUrl":"/p/25120/submit","getSubmissionsUrl":"/record?fullStatus=true&pid=25120","getRecordDetailUrl":"/record/%7Brid%7D","pretestConnUrl":"record-conn?pretest=1&uidOrName=0&pid=25120&domainId=system"}'; window.UserContextNew = '{}';

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-11C |
| Contest | 11 |
| Index | C |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*2200` |
| Codeforces 通过次数 | 679 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/11/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/11/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P11C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

