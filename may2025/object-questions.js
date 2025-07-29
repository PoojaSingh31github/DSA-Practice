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

const a = ["a", "b", "c"];
// need this output  => { a:05, b:15, c:25 }
let count = 1;
const reduce = a.reduce((acc, ele, ind)=>{
    acc[ele]=(5*count).toString().padStart(2,"0")
    count+=2
    return acc;
},{})

console.log(reduce)
