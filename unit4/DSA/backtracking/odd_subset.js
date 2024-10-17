function odd_subset(n, arr, k, i, res) {
    const resSum = res.reduce((acc, c) => acc + c, 0)
    if (res.length == k && resSum % 2 != 0) {
        return true
    }
    if (i >= n || res.length > k) {
        return false
    }
    res.push(arr[i])

    if (odd_subset(n, arr, k, i + 1, res)) {
        return true
    }
    res.pop()
    if (odd_subset(n, arr, k, i + 1, res)) {
        return true
    }
    return false

}

n = 3
arr = [1, 2, 3]
k = 2
res = []
ans = odd_subset(n, arr, k, 0, res)
console.log(ans)