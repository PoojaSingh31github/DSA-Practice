const arr = [1, 5, 2, 3, 7];
let k =3
let ws = 1
const ans =[];
for (let i=0; i<k; i++){
    ws*=arr[i]
}
// ans.push(ws/4)
console.log(ws)
let maxx =ws;
for (let i =k ; i<arr.length; i++){
    ws = ws* arr[i] / arr[i-k];
    ans.push(ws/4)
    if (maxx < ws){
        maxx = ws
    }
}
console.log(maxx, ans)

// longest subarray with sum ≤ K
// const arr = [1,2,3,4,5,6];
sum = 16;
i=0
j=0
ws =0
maxx = 0

while (i<arr.length){
    ws+=arr[i]
    
    while (ws> sum){
        ws-=arr[j]
        j+=1
    }
    i+=1
    maxx = Math.max(maxx, i-j)
}
console.log(maxx)


input= [12, -1, -7, 8, -15, 30, 16, 28], k = 3
// Output: [-1, -1, -7, -15, -15, 0]

const anss =[];
for (let i=0; i<=input.length-k; i++){
let found = false
    for (let j=i; j<i+k; j++){
    if (input[j] < 0){
        anss.push(input[j])
        found=true
        break
    }
    }
    if(!found){
        anss.push(0)
    }
}
console.log(anss)






















