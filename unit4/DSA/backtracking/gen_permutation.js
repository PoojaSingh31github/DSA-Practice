function gen_per(n, arr, start, res) {

    if (start == n) {
        res.push([...arr]);
        return;
    }
    let i = start;
    while (i < n) {
        [arr[i], arr[start]] = [arr[start], arr[i]];
        gen_per(n, arr, start + 1, res);
        [arr[i], arr[start]] = [arr[start], arr[i]];
        i++
    }

}

let n = 3
let arr = [1, 2, 3]
let res = []
gen_per(n, arr, 0, res)
console.log(res)
// function gen_per(n, arr, start, res) {
//     if (start == n) {
//         res.push([...arr]);
//         return;
//     }
    
//     let i = start; // Declare 'i' with 'let'
//     while (i < n) {
//         [arr[i], arr[start]] = [arr[start], arr[i]];  // Swap elements
//         gen_per(n, arr, start + 1, res);              // Recursive call
//         [arr[i], arr[start]] = [arr[start], arr[i]];  // Swap back
//         i++;
//     }
// }

// let n = 3;
// let arr = [1, 2, 3];
// let res = [];
// gen_per(n, arr, 0, res);
// console.log(res);
