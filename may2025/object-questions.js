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

Input= {a:1, b:{c:2, d:{e:3}}}
// - Output: ['a','b','c','d','e']

function recur(obj, res=[]){
    for (let i in obj){
        if (typeof obj[i] =="object"){
            res.push(i)
            recur(obj[i], res)
        }else{
            res.push(i)
        }
    }
    return res
}

console.log(recur(Input))
//////////////////////////////////////////////////////////////////////////////////////////////////////////
 Input =  [1,[2,[3,4],5],6]
// - Output: 21

function recur(arr, sum={value:0}){
    for ( let i of arr){
        if (Array.isArray(i)){
            recur(i, sum)
        }else{
            sum.value+=i
        }
    }
    return sum.value
}
console.log(recur(Input))
//////////////////////////////////////////////////////////////////////////////////////////////////////////
const items = [
    { id: 1, parentId: null, label: "Home" },
    { id: 2, parentId: 1, label: "Products" },
    { id: 3, parentId: 2, label: "Electronics" },
    { id: 4, parentId: 2, label: "Clothes" },
    { id: 5, parentId: 3, label: "Mobile" }
  ];

  function build(items) {
    let map = {}
    let tree = []
    items.forEach((item) => {
      map[item.id] = { ...item, children: [] }
    })
    console.log(map)
    items.forEach((item) => {
      if (item.parentId === null) {
        tree.push(map[item.id])
      } else {
        map[item.parentId].children.push(map[item.id])
      }
    })
    return tree

  }

  console.log(build(items))


  let Input = { a: 1, b: { c: 2 }, d: 3, e: { f: 4, g: 5, h: { i: 6 } } }
  // - Output: [['a',1],['b.c',2]]

  function flat(input, key = "", res = []) {
    for (let j in input) {
      if (typeof input[j] === "object") {
        flat(input[j], key + j + ".", res)
        continue;
      }
      res.push([key + j, input[j]])
      console.log(j, "jjjjjjjjjjjjjjjjjjjjj")
    }
    return res;
  }
  console.log(flat(Input))


  let input = {
    label: 'Home',
     children: [{
      label: 'Products', 
      children: [{
        label:'Electronics', 
          children: [{ label: 'Mobile' }]
      }]
    }]
  };
  // Output: ['Home','Home > Products','Home > Products > Electronics','Home > Products >
  // Electronics > Mobile']

  function letFlat(input, prefix="", res=[]) {
    res.push(prefix + input.label)
    if (input.children && input.children.length > 0) {
      input.children.forEach(child => letFlat(child, prefix + input.label + " > ", res))
    }
    return res;
  }
  console.log(letFlat(input))
///////////////////////////////////////////////////////////////////////////////////////////////////////////

const input = {a:{b:{c:{d:1}}}}
// - Output: 4

function countfunc(input, count={value:1}){
    for (let i in input){
        if (typeof input[i] ==="object"){
            count.value+=1
            countfunc(input[i], count)
        }
    }
    return count.value
}

console.log(countfunc(input))

/////////////////////////////////////////////////////////////////////////////////////////////////////////


// Question 1 :- 

function isAnagram(str1, str2) {
  if (str1.length !== str2.length) return false;

  let count = {};

  for (let ch of str1) {
    count[ch] = (count[ch] || 0) + 1;
  }

  for (let ch of str2) {
    if (!count[ch]) return false;
    count[ch]--;
  }

  return true;
}

console.log(isAnagram("listen", "silent")); // true
console.log(isAnagram("hello", "world"));   // false

// Myself :- 
// Check if two strings are anagrams.
const a = "listen"
const b = "sileunt" 
// → true

obj = {}
obj2= {}

for (let i of a){
   if (obj[i]){
       obj[i]+=1
   }else{
       obj[i] =1
   }
}
for (let i of b){
   if (obj2[i]){
       obj2[i]+=1
   }else{
       obj2[i] =1
   }
}

let flag = true

flag = a.length == b.length

for (let i in obj){
    console.log(obj[i] !== obj2[i])
    if (obj[i] !== obj2[i]){
        flag = false 
    }
    
}

console.log(flag)


// Question 2 :- 

const string = "I love JavaScript so much" 
// → "I evol JavaScript os much

const arr = string.split(" ")

let ans = []
for (let i in arr){
   if (i%2 !== 0){
       let a = []
       a = arr[i].split("").reverse().join("")
       ans.push(a)
   }else{
       ans.push(arr[i])
   }
}
console.log(ans.join(" "))


// Question 3 :- 
let arr = [1,3,4,5,6,9,10];

let first = -Infinity;
let second = -Infinity;

for(let item of arr){
    if(first<item){
        console.log(item, "iiiiiiiiiii")
        second = first;
        first = item;
    }else if(item>second && item<first){
        second = item;
    }
}

console.log(first , second)

// Myself :- 
const input = [21 , 20, 19, 200, 78,100, 65]
// Output: 9
let max = 0
for (let i =0; i<input.length; i++){
    if (max <=input[i]){
        max = input[i]
    }
}

// console.log(max ) = 10 
let second = max

max=0
for (let i =0; i<input.length; i++){
    if (max < input[i] && input[i] < second){
        max = input[i]
    }
}
console.log(max)

// Question 4 :- 
const input = [ 
  { dept: "IT", name: "A" },
  { dept: "HR", name: "B" },
  { dept: "IT", name: "C" }
]
// Output:
// {
//   IT: [{name: "A"}, {name: "C"}],
//   HR: [{name: "B"}]
// }


const ans = input.reduce((acc, {dept, name})=>{
   acc[dept] ? acc[dept].push({"name":name}) : acc[dept] = [{"name": name}]
   return acc
},{})

console.log(ans )


// Question 5 ;-
// Remove falsy values from an array.
const ar = [0, false, '', 'hello', undefined, 5]
// → ['hello', 5]

// falsy = 0 false , "" , undefined

const arr = [0 ,false , "" , undefined]
const ans =[]
for (let i of ar){
    if (arr.includes(i)){
        continue
    }
    ans.push(i)
}
    
console.log(ans)
Second eazy oneliner - 
console.log(ar.filter(Boolean))



// Question 6:-

const ar ={ name: "John", age: 25 } 
// → "name=John&age=25"
s=""
for (let i in ar){
    s+=`${i}=${ar[i]}&`
}

ans = s.split("")
ans.pop()
// console.log(ans)
console.log(ans.join(""))


// Question 7 :-
const input= 5
// Output: 0, 1, 1, 2, 3

function recursion(i,a=0,b=1,res=[]){
    if(res.length == i) return res
    res.push(a)
    console.log(a, b)
    return recursion(i, b, a+b, res)
}
console.log(recursion(input))



//////////////////////////////////////////////////////////////////////////////////////////////////////////
// Curry recursion solution

function func(a){
    if (a!==undefined){
        return function(b){
            if (b==undefined){
                return a
            }
            return func(a+b)
        }
    }
    
    
}
function func(){
    return function func(b){
        return  function func(c){
          return function func(){
                return a+b+c
          }
        }
    }
}

console.log(func(9)(8)(7)())
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
