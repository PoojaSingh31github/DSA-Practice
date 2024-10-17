function coin_com(p, k) {
    function backTracking(start, res, sum) {
        if (res.length == k) {
            if (sum == p) {
                result.push([...res]);
            }
            return;
        }
        for (let i = start; i < 10; i++) {
            if (sum + i > p) {
                break
            }
            res.push(i)
            backTracking(i + 1, res, sum + i);
            res.pop()
        }
    }

    let result = []
    backTracking(1, [], 0)
    return result
}

let p = 8
let k = 2
let ans = coin_com(p, k)
console.log(ans)


// function coin_com(p, k) {
//     function backTracking(start, res, sum) {
//         // Base case: if we have exactly K coins
//         if (res.length == k) {
//             // Check if their sum equals P
//             if (sum == p) {
//                 result.push([...res]);  // Push a copy of the current combination
//             }
//             return;  // Stop here; don't add more coins if we already have K coins
//         }

//         // Loop through possible coin values from `start` to 9
//         for (let i = start; i < 10; i++) {
//             if (sum + i > p) {
//                 break;  // Stop if the sum exceeds P
//             }

//             // Add the current coin to the combination and explore further
//             res.push(i);
//             backTracking(i + 1, res, sum + i);  // Recursive call
//             res.pop();  // Backtrack by removing the last added coin
//         }
//     }

//     let result = [];
//     backTracking(1, [], 0);  // Start with coin 1, empty result, and sum 0
//     return result;
// }

// // Example usage
// let p = 8;
// let k = 2;
// let ans = coin_com(p, k);
// console.log(ans);
