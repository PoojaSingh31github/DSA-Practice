function find_path(mat, i, j, path, res) {
    if (i == n - 1 && j == n - 1) {
        res.push(path);
        return
    }

    mat[i][j] = 0
    // down
    if (i + 1 < n && mat[i + 1][j] == 1) {
        find_path(mat, i + 1, j, path + "D", res)
    }
    // left
    if (j - 1 >= 0 && mat[i][j - 1] == 1) {
        find_path(mat, i, j - 1, path + "L", res)
    }
    // right
    if (j + 1 < n && mat[i][j + 1] == 1) {
        find_path(mat, i, j + 1, path + "R", res)
    }
    // up
    if (i - 1 >= 0 && mat[i - 1][j] == 1) {
        find_path(mat, i - 1, j, path + "U", res)
    }
    mat[i][j] = 1


}
function combination(mat, n) {
    const res = []
    // if (mat[0][0] == 0 || mat[n - 1][n - 1] == 0) {
    //     return []
    // }
    // if (mat[0][1] == 0 && mat[1][0] == 0) {
    //     return []
    // }
    // if (mat[n - 1][n - 2] == 0 && mat[n - 2][n - 1] == 0) {
    //     return []
    // }
    find_path(mat, 0, 0, "", res)
    return res
}
n = 4
mat = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

ans=combination(mat, n)
console.log(ans)