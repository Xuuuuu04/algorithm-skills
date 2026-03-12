package ict

// 区间最大子段和（带区间修改）- 线段树实现
// 完整的懒标记处理：存储"选空"和"选非空"两组信息
import std.convert.*

// 节点信息 - 同时维护"选非空"的信息用于正确处理区间加
class Node {
    var sum: Int64       // 区间和
    var lmax: Int64      // 最大前缀和（允许空）
    var rmax: Int64      // 最大后缀和（允许空）
    var ans: Int64       // 最大子段和（允许空）
    var nlmax: Int64     // 选非空的最大前缀和
    var nrmax: Int64     // 选非空的最大后缀和
    var nans: Int64      // 选非空的最大子段和
    var nlmaxK: Int64    // nlmax 对应的前缀长度
    var nrmaxK: Int64    // nrmax 对应的后缀长度
    var nansK: Int64     // nans 对应的子段长度

    public init(sum: Int64, lmax: Int64, rmax: Int64, ans: Int64,
                nlmax: Int64, nrmax: Int64, nans: Int64,
                nlmaxK: Int64, nrmaxK: Int64, nansK: Int64) {
        this.sum = sum
        this.lmax = lmax
        this.rmax = rmax
        this.ans = ans
        this.nlmax = nlmax
        this.nrmax = nrmax
        this.nans = nans
        this.nlmaxK = nlmaxK
        this.nrmaxK = nrmaxK
        this.nansK = nansK
    }
}

class SegTree {
    var n: Int64
    var tree: Array<Node>
    var lazy: Array<Int64>

    public init(n: Int64, a: Array<Int64>) {
        this.n = n
        this.tree = Array<Node>(4 * n + 4, {_ => 
            Node(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        })
        this.lazy = Array<Int64>(4 * n + 4, {_ => 0})
        build(a, 1, 1, n)
    }

    // 建树
    func build(a: Array<Int64>, node: Int64, l: Int64, r: Int64): Unit {
        if (l == r) {
            let val = a[l - 1]
            let v = max(0, val)
            tree[node] = Node(val, v, v, v, val, val, val, 1, 1, 1)
            return
        }
        let mid = (l + r) / 2
        build(a, node * 2, l, mid)
        build(a, node * 2 + 1, mid + 1, r)
        pushUp(node, l, r)
    }

    // 向上合并
    func pushUp(node: Int64, l: Int64, r: Int64): Unit {
        let left = tree[node * 2]
        let right = tree[node * 2 + 1]
        let mid = (l + r) / 2
        let leftLen = mid - l + 1
        let rightLen = r - mid

        let sum = left.sum + right.sum

        // nlmax = max(left.nlmax, left.sum + right.nlmax)
        var nlmax: Int64 = 0
        var nlmaxK: Int64 = 0
        let leftPlusRightNL = left.sum + right.nlmax
        if (left.nlmax >= leftPlusRightNL) {
            nlmax = left.nlmax
            nlmaxK = left.nlmaxK
        } else {
            nlmax = leftPlusRightNL
            nlmaxK = leftLen + right.nlmaxK
        }
        // lmax = max(0, nlmax)
        let lmax = max(0, nlmax)

        // nrmax = max(right.nrmax, right.sum + left.nrmax)
        var nrmax: Int64 = 0
        var nrmaxK: Int64 = 0
        let rightPlusLeftNR = right.sum + left.nrmax
        if (right.nrmax >= rightPlusLeftNR) {
            nrmax = right.nrmax
            nrmaxK = right.nrmaxK
        } else {
            nrmax = rightPlusLeftNR
            nrmaxK = rightLen + left.nrmaxK
        }
        // rmax = max(0, nrmax)
        let rmax = max(0, nrmax)

        // nans = max(left.nans, right.nans, left.nrmax + right.nlmax)
        var nans: Int64 = 0
        var nansK: Int64 = 0
        let crossN = left.nrmax + right.nlmax
        if (left.nans >= right.nans && left.nans >= crossN) {
            nans = left.nans
            nansK = left.nansK
        } else if (right.nans >= left.nans && right.nans >= crossN) {
            nans = right.nans
            nansK = right.nansK
        } else {
            nans = crossN
            nansK = left.nrmaxK + right.nlmaxK
        }
        // ans = max(0, nans)
        let ans = max(0, nans)

        tree[node] = Node(sum, lmax, rmax, ans, nlmax, nrmax, nans, nlmaxK, nrmaxK, nansK)
    }

    // 对节点应用区间加操作
    func applyNode(node: Int64, len: Int64, val: Int64): Unit {
        let old = tree[node]
        let newSum = old.sum + val * len
        
        // 选非空的信息直接加 val * k
        let newNlmax = old.nlmax + val * old.nlmaxK
        let newNrmax = old.nrmax + val * old.nrmaxK
        let newNans = old.nans + val * old.nansK
        
        // 允许空的 = max(0, 选非空)
        let newLmax = max(0, newNlmax)
        let newRmax = max(0, newNrmax)
        let newAns = max(0, newNans)
        
        tree[node] = Node(newSum, newLmax, newRmax, newAns, 
                          newNlmax, newNrmax, newNans,
                          old.nlmaxK, old.nrmaxK, old.nansK)
        lazy[node] += val
    }

    // 下推懒标记
    func pushDown(node: Int64, l: Int64, r: Int64): Unit {
        if (lazy[node] == 0) { return }
        let mid = (l + r) / 2
        applyNode(node * 2, mid - l + 1, lazy[node])
        applyNode(node * 2 + 1, r - mid, lazy[node])
        lazy[node] = 0
    }

    // 区间修改
    public func rangeAdd(node: Int64, l: Int64, r: Int64, ql: Int64, qr: Int64, val: Int64): Unit {
        if (ql <= l && r <= qr) {
            applyNode(node, r - l + 1, val)
            return
        }
        pushDown(node, l, r)
        let mid = (l + r) / 2
        if (ql <= mid) { rangeAdd(node * 2, l, mid, ql, qr, val) }
        if (qr > mid) { rangeAdd(node * 2 + 1, mid + 1, r, ql, qr, val) }
        pushUp(node, l, r)
    }

    // 区间查询
    public func query(node: Int64, l: Int64, r: Int64, ql: Int64, qr: Int64): ?Node {
        if (ql <= l && r <= qr) {
            return tree[node]
        }
        pushDown(node, l, r)
        let mid = (l + r) / 2
        if (qr <= mid) {
            return query(node * 2, l, mid, ql, qr)
        } else if (ql > mid) {
            return query(node * 2 + 1, mid + 1, r, ql, qr)
        } else {
            let leftOpt = query(node * 2, l, mid, ql, qr)
            let rightOpt = query(node * 2 + 1, mid + 1, r, ql, qr)
            if (leftOpt.isSome() && rightOpt.isSome()) {
                let left = leftOpt.getOrThrow()
                let right = rightOpt.getOrThrow()
                let leftLen = mid - max(l, ql) + 1
                let rightLen = min(r, qr) - mid

                let sum = left.sum + right.sum

                var nlmax: Int64 = 0
                var nlmaxK: Int64 = 0
                let leftPlusRightNL = left.sum + right.nlmax
                if (left.nlmax >= leftPlusRightNL) {
                    nlmax = left.nlmax
                    nlmaxK = left.nlmaxK
                } else {
                    nlmax = leftPlusRightNL
                    nlmaxK = leftLen + right.nlmaxK
                }
                let lmax = max(0, nlmax)

                var nrmax: Int64 = 0
                var nrmaxK: Int64 = 0
                let rightPlusLeftNR = right.sum + left.nrmax
                if (right.nrmax >= rightPlusLeftNR) {
                    nrmax = right.nrmax
                    nrmaxK = right.nrmaxK
                } else {
                    nrmax = rightPlusLeftNR
                    nrmaxK = rightLen + left.nrmaxK
                }
                let rmax = max(0, nrmax)

                var nans: Int64 = 0
                var nansK: Int64 = 0
                let crossN = left.nrmax + right.nlmax
                if (left.nans >= right.nans && left.nans >= crossN) {
                    nans = left.nans
                    nansK = left.nansK
                } else if (right.nans >= left.nans && right.nans >= crossN) {
                    nans = right.nans
                    nansK = right.nansK
                } else {
                    nans = crossN
                    nansK = left.nrmaxK + right.nlmaxK
                }
                let ans = max(0, nans)

                return Some(Node(sum, lmax, rmax, ans, nlmax, nrmax, nans, nlmaxK, nrmaxK, nansK))
            }
        }
        return None
    }
}

func max(a: Int64, b: Int64): Int64 {
    if (a >= b) { a } else { b }
}

func min(a: Int64, b: Int64): Int64 {
    if (a <= b) { a } else { b }
}

main() {
    let firstLine = readln().split(" ")
    let n = Int64.parse(firstLine[0])
    let q = Int64.parse(firstLine[1])
    
    let aParts = readln().split(" ")
    let a = Array<Int64>(n, {i => Int64.parse(aParts[i])})
    
    let seg = SegTree(n, a)
    
    var i: Int64 = 0
    while (i < q) {
        let parts = readln().split(" ")
        let op = Int64.parse(parts[0])
        if (op == 1) {
            let l = Int64.parse(parts[1])
            let r = Int64.parse(parts[2])
            let v = Int64.parse(parts[3])
            seg.rangeAdd(1, 1, n, l, r, v)
        } else {
            let l = Int64.parse(parts[1])
            let r = Int64.parse(parts[2])
            let result = seg.query(1, 1, n, l, r)
            if (result.isSome()) {
                println(result.getOrThrow().ans)
            } else {
                println(0)
            }
        }
        i++
    }
}
