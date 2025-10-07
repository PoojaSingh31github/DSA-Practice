const people = [
  { name: "Alice", age: 20 },
  { name: "Bob", age: 30 },
  { name: "Charlie", age: 20 },
  { name: "David", age: 30 },
  { name: "Eva", age: 25 }
];

// 20:[alice chaler, ], 30: [bob, david] , 25:[eva]

const ans = people.reduce((acc, curr)=>{
    const {name, age}= curr;
    console.log(name, age)
    if (acc[age]){
        acc[age].push(name)
    }else{
    acc[age] = [name]
        
    }
    return acc
},{})
console.log(ans)

//////////////////////////////////////////////////////////////////////////////////////////////////////////

const a = ["a", "b", "c"];
// need this output  => { a:05, b:15, c:25 }
let count = 1;
const reduce = a.reduce((acc, ele, ind)=>{
    acc[ele]=(5*count).toString().padStart(2,"0")
    count+=2
    return acc;
},{})

console.log(reduce)

// second appoch 
const ans = a.reduce((acc, curr, index)=>{
    // console.log(acc, curr, index)
    if (!acc[curr]) acc[curr] = `${index}5`
    return acc
}, {})

console.log(ans)

//////////////////////////////////////////////////////////////////////////////////////////////////////////


const obj = { name: "John", age: 30 } 
// => "name=John&age=30"

let ans =[];
let ans2 =[];

for (let key in obj){
   ans.push(key , "=" , obj[key], "&")
//   console.log(key, "=" ,obj[key] , "&")
}
for (let key in obj){
   ans2.push(`${key}=${obj[key]}`)
}
ans.pop()
console.log(ans.join(""), typeof ans.join(""))
console.log(ans2.join("&"))

//////////////////////////////////////////////////////////////////////////////////////////////////////////

// Iterate through an object and convert all keys to camelCase.
const input = {
  "first_name": "Alice",
  "last-name": "Johnson",
  "user age": 25,
  "is_active": true
};

// {
//   firstName: "Alice",
//   lastName: "Johnson",
//   userAge: 25,
//   isActive: true
// }

const obj ={};
for (let key in input){
    if (key.includes("_")){
        ans = (key.split("_"))
    }else if(key.includes("-")){
        ans= (key.split("-"))
    }else if(key.includes(" ")){
        ans = (key.split(" "))
    }
    let bbbb = ans.map((ele,index)=>{
       return ele= ele.split("")[0].toUpperCase() + ele.slice(1)
    })
    let bbbbb= bbbb.join("")
    obj[bbbbb] = input[key]
    
    // key.split("_")
}
console.log(obj)

//////////////////////////////////////////////////////////////////////////////////////////////////////////
// Write a function that flattens a nested array using loops only.

let arr = [1,2,[3,4],5,[6,7,[8,9,[10,11]]]];
console.log(typeof arr)

function recursion(arr, res=[]){
    if( typeof arr !== "object"  ){
        res.push(arr)
    }else{
        if (Array.isArray(arr)){
            arr.map((ele)=>{
               recursion(ele, res)
            })
        }
    }
    return res
}

console.log(recursion(arr))

//////////////////////////////////////////////////////////////////////////////////////////////////////////
const words = ["apple", "banana", "apple", "orange", "banana", "apple"];
// { apple: 3, banana: 2, orange: 1 }

const ans = words.reduce((acc, key)=>{
    if (acc[key]){
        acc[key] +=1
    }else{
        acc[key] = 1
    }
    return acc
},{})

console.log(ans)
//////////////////////////////////////////////////////////////////////////////////////////////////////////
const arr = [
  ["name", "John"],
  ["age", 30]
]

// { name: "John", age: 30 }

const ans = arr.reduce((acc, curr)=>{
    acc[curr[0]] = curr[1]
    return acc
}, {})

console.log(ans)

//////////////////////////////////////////////////////////////////////////////////////////////////////////
const obj1 = { a: 1, b: { c: 2 } };
const obj2 = { a: 1, b: { c: 2 } };
function checkEqual(obj1, obj2) {
  // If both are not objects, compare directly (base case)
  if (typeof obj1 !== "object" || obj1 === null || typeof obj2 !== "object" || obj2 === null) {
    return obj1 === obj2;
  }

  // If number of keys don't match
  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) return false;

  // Loop through all keys in obj1
  for (let key of keys1) {
    // If key not found in obj2
    if (!(key in obj2)) return false;

    // Recursive check for each key-value pair
    if (!checkEqual(obj1[key], obj2[key])) return false;
  }

  return true;
}
console.log(checkEqual(obj1, obj2))

//////////////////////////////////////////////////////////////////////////////////////////////////////////
// Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)
input= [2,0,2,1,1,0]
// Output: [0,0,1,1,2,2]

let count =input.length-1;
for (let i=input.length-1; i>=0; i--){
    if (input[i] != 1 ){
        [[input[count],input[i]]=[input[i], input[count]]]
        count-=1
    }
} 
count = input.length-1;
for (let i=input.length-1; i>=0; i--){
    if (input[i] != 0 ){
        [[input[count],input[i]]=[input[i], input[count]]]
        count-=1
    }
} 

console.log(input)


//////////////////////////////////////////////////////////////////////////////////////////////////////////
// Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.

// nput Format: N = 6,
array = [9, -3, 3, -1, 6, -5]
let maximum = 0;

for (let i=0; i<array.length; i++){
    let a =0;
    let count =0
    let maxx;
    for (let j =i; j<array.length; j++){
        // console.log(array[j])
        a+=array[j]
        count+=1
        if (a==0){
            maxx = count
        }
        if (maximum < maxx){
            maximum = maxx
        }
    }
    console.log(a, count, maxx, "maxxxxxxxxxxxxxxxxx", maximum)
}
console.log(maximum)

// console.log(-3+ 3+ -1+ 6+-5)


// Result: 5
// Explanation: The following subarrays sum to zero:
// {-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
// Since we require the length of the longest subarray, our answer is 5!

//////////////////////////////////////////////////////////////////////////////////////////////////////////

const obj = { a: { b: { c: 10 } }, d: 20 }

const recursion =(obj, ans="")=>{
    for (let key in obj){
      const neww = ans ? `${ans}.${key}` : key
    if (typeof obj[key] ==="object" && obj[key] !==null ){
        recursion(obj[key], neww)
    }else{
        console.log(neww ,"=", obj[key])
    }
}
return ans
}

console.log(recursion(obj))

//////////////////////////////////////////////////////////////////////////////////////////////////////////
Input = {a:1, b:{c:2,d:{e:3}}}


// - Output: 6
console.log(typeof(Input))

function recur(input, sum={value:0}){
    for (let i in input){
        if (typeof input[i] == "object"){
            recur(input[i], sum)
        }else{
            sum.value+=input[i]
        }
    }
   return sum.value
}

console.log(recur(Input))

//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
