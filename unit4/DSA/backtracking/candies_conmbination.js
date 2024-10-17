function buy_candies(arr, N, C) {
    function combination(start, C, com, result) {
        if (C == 0) {
            result.push([...com])
            return;
        }

        for (let i = start; i < N; i++) {
            if (arr[i] > C) {
                break;
            }
            com.push(arr[i])
            combination(i, C - arr[i], com, result)
            com.pop()
        }
    }
    result = [];
    combination(0, C, [], result);
    if (result.length > 0) {
        return result;
    } else {
        return -1
    }
}

N = 4
C = 7
arr = [2, 3, 6, 7]
ans = buy_candies(arr, N, C)
if (ans == -1) {
    console.log(-1)
} else {
    for (let i of ans) {
        console.log(i.join(" "))
    }
}

