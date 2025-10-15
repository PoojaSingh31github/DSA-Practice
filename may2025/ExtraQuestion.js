
const arr = [1, 2, 3,4, 0,4, 4,0,  7,0,0, 9];
let j =arr.length-1
for (let i=arr.length-1; i>=0;i--){
    if (arr[i] !== 0){
        [arr[i], arr[j]] = [arr[j], arr[i]]
        j-=1
    }
}
console.log(arr)

let j =0
for (let i in arr){
    if (arr[i] !== 0){
        [arr[i], arr[j]]=[arr[j], arr[i]]
        j+=1
    }
}
console.log(arr)

// const arr = [24,25,36,52,92,49]

// first highest second highest and third highest 



first = 0
second = 0
third = 0 

for (let i of arr){
    if (i > first){
        third = second
        second = first 
        first = i
    }else if (i < first && second < i ){
        third = second
        second = i 
    }else if (i < second && third < i){
        third = i
    }
    
}
console.log(third , first , second)








