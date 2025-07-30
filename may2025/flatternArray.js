let arr = [1,2,[3,4],5,[6,7,[8,9,[10,11]]]];

function flatternArr(arr){
    res=[]
    for (let item of arr){
        if (Array.isArray(item)){
            res = (res.concat(flatternArr(item)))
        }
        else{
            res.push(item)
        }
    }
    return res
}

console.log(flatternArr(arr))

function stackFalter(arr){
    res=[]
    stack =[...arr]
    while (stack.length>0){
        let item = stack.pop()
        if (Array.isArray(item)){
            stack.push(...item)
        }else{
        res.unshift(item)
        }
    }
    return res    
}
console.log(stackFalter(arr))


const array =[45, 44, 32, 10, 23, 12];

let max = 0
let max2 =0

const a = array.forEach((ele, idex)=>{
    if(ele > max){
        max2 = max
        max = ele
    }else if(ele < max && ele > max2){
        max2 = ele
    }
})

// const b = array.forEach((ele,idnex)=>{
//     if(ele < max && ele > max2){
//         max2 = ele
//     }
// })
console.log(max, max2)

const array =    [45, 44, 32, 10,];
        //     i  0 1 2 3 4 5 6 7
        //  count 0 1 2 2 3 4 4 5

// let count = 0
// for(let i=0; i<array.length; i++){
//     if (array[i]!==0){
//         [[array[i], array[count]]=[array[count], array[i]]]
//         count ++
//     }
// }
// console.log(array)


const words = ["Hello", "I", "am", "learning", "JavaScript"];

const ans = words.reduce((acc,curr)=>{
    acc+=curr+" "
    return acc
}, "")

console.log(ans)

const arr = ["apple", "banana", "grapes", "kiwi", "pineapple","pineapple","pineapple","pineapple","pineapple", "cat"];
let count = 0;
arr.map(ele=>{
    if (ele.split("").length > 5 ){
        count +=1
        
    } 
    
})

console.log(count)
