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

