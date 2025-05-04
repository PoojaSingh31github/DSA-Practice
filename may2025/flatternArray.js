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











