
let paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
let ban = "hit"

let arr = paragraph.toLowerCase().replace(/[^\w\s]/g,"").split(" ")
let arr2 = ban.split(" ")

arr = arr.filter((ele)=> !arr2.includes(ele) )
console.log(arr)

let dic = {};
arr.forEach((ele) => {
    dic[ele] = (dic[ele] || 0) + 1;
});

let maxx = 0
let ans=""
for (let word in dic){
    if (dic[word] > maxx){
        maxx=dic[word]
        ans = word
    }
    console.log(word, dic[word])
}

console.log(ans)
