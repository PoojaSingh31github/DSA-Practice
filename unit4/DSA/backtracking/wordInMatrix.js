function exist(board, word) {
    const n = board.length;
    const m = board[0].length;
    const directions = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ];
    function dfs(x, y, idx) {
        if (idx === word.length) {
            return true;
        }
        if (x < 0 || x >= n || y < 0 || y >= m || board[x][y] !== word[idx]) {
            return false;
        }
        const temp = board[x][y];
        board[x][y] = '#';
        for (let [dx, dy] of directions) {
            if (dfs(x + dx, y + dy, idx + 1)) {
                return true;
            }
        }
        board[x][y] = temp;
        return false;
    }
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (dfs(i, j, 0)) {
                return true;
            }}}
    return false;
}
let n = 3, m = 4;
let board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'N', 'E', 'E']
];
let word = "SEEN";
console.log(exist(board, word)); // Output: true
