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
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////
