const navTree = {
  label: "Home",
  children: [
    {
      label: "Products",
      children: [
        {
          label: "Electronics",
          children: [
            { label: "Mobile" }
          ]
        }
      ]
    }
  ]
};
// console.log(navTree.children[0].children[0].children[0].label)

function recusion(navTree, res = []) {

  res.push(navTree.label)
  if (navTree.children) {
    for (let item of navTree.children) {
      console.log(item, "items")
      recusion(item, res)
    }
  }
  return res



}
console.log(recusion(navTree))

const flat = (node) => [node.label, ...(node.children ? node.children.flatMap(flat) : [])];

console.log(flat(navTree));


const recur = (tree, res = []) => {
  if (tree.label) {
    res.push(tree.label)
  }
  if (tree.children) {
    for (let key of tree.children) {
      recur(key, res)
    }
  }
  return res
}

console.log(recur(navTree))



const items = [
  { name: "Apple", category: "Fruit" },
  { name: "Broccoli", category: "Vegetable" },
  { name: "Banana", category: "Fruit" },
  { name: "Carrot", category: "Vegetable" },
];

// let obj = {};
// for(let {name, category} of items){
//     if(!obj[category]){
//         obj[category] = []
//     }
//   obj[category].push(name)
// }

// console.log(obj)


let res = items.reduce((acc, { name, category }, index) => {
  (acc[category] ||= []).push(name)
  return acc
}, {})

console.log(res)



const items = [
  { name: "Apple", category: "Fruit" },
  { name: "Broccoli", category: "Vegetable" },
  { name: "Banana", category: "Fruit" },
  { name: "Carrot", category: "Vegetable" },
];


// [
//     {Friuts : [apple , banana],
//     vegetable: [broccoli, carrot]
//     }
// ]

const ans = items.reduce((acc, { name, category }) =>
  // acc[category] ? acc[category].push(name) : acc[category] = []
  (acc[category] ||= []).push(name)
  //      {(acc[category] ||= []).push(name)
  //   return acc}
  // {if (!acc[category]) acc[category] = []
  // acc[category].push(name)
  // return acc}
  , {})
const ans = items.reduce((acc, { name, category }) =>
  ((acc[category] ||= []).push(name), acc),
  {}
);

console.log(ans);
// { Fruit: [ 'Apple', 'Banana' ], Vegetable: [ 'Broccoli', 'Carrot' ] }


console.log(ans)


const obj1 = { a: 1, b: { c: 2 } };
const obj2 = { b: { d: 3 }, e: 4 };

function recur(obj1, obj2) {
  const res = { ...obj1 };
  console.log(res, "hhhhhhhhhh")

  for (let i in obj2) {
    if (obj2.hasOwnProperty(i) && typeof obj2[i] === "object") {
      res[i] = recur(res[i], obj2[i]);
    } else {
      res[i] = obj2[i]
      console.log(res[i])
    }
  }
  return res;
}
console.log(recur(obj1, obj2));

// Input: a nested array of integers, e.g., [1, [2, [2, 3], 3], 1]
const input = [1, [2, [2, 3], 3], 1]
// - Output: [1,2,3]
function flat(input, res = []) {
  for (let i of input) {
    if (Array.isArray(i)) {
      flat(i, res)
    } else {
      if (!res.includes(i)) {
        res.push(i)
      }
    }
  }
  return res
}
console.log(flat(input))

const inp = { a: 1, b: { c: 2 } }
// - Output: {1:'a', b:{2:'c'}}

function rever(inp, res = {}) {
  for (let i in inp) {
    if (typeof inp[i] === "object") {
      res[i] = rever(inp[i])
    } else {
      res[inp[i]] = i
    }
  }
  return res
}
console.log(rever(inp))

const object = { a: { b: { c: 1 } }, d: { c: 2 } }
// - Output: ['a.b.c', 'd.c']

function restedobj(obj, key = "", res = []) {
  for (let i in obj) {
    if (typeof obj[i] === "object") {
      restedobj(obj[i], key + i + ".", res)
    } else {
      res.push(key + i)
    }
  }
  return res
}
console.log(restedobj(object))

const obj3 = [{ id: 1, info: { type: 'a' } }, { id: 2, info: { type: 'b' } }]
// - Output: [{id:1,info:{type:'a'}}]



// 20. Sum all numeric values in nested arrays and objects
// - Description: Combine sums from nested arrays and objects.
// - Input: {a:[1,2], b:{c:3,d:[4,5]}}
// - Output: 15

const obj4 = { a: [1, 2], b: { c: 1, d: [4, , 1, 1, 5] } }
function sumNested(obj, sum = { value: 0 }) {
  for (let i in obj) {
    if (typeof obj[i] === "object") {
      sumNested(obj[i], sum)
    } else {
      // if(typeof obj[i] ==="number"){
      console.log(obj[i], "kkkkkkkkkkkkkkkkkkkkkkkkk")
      sum.value += obj[i]
      // }
    }
  }
  return sum.value
}
console.log(sumNested(obj4))


// 21. Flatten nested object to query string
// - Description: Convert nested object to URL query parameters with dot notation.
// - Input: {a:1,b:{c:2}}
// - Output: "a=1&b.c=2"

const obj5 = { a: 1, b: { c: 2 } }
function toQueryString(obj, prefix = '', str = "") {
  for (let i in obj) {
    if (typeof obj[i] === "object") {
      str = toQueryString(obj[i], prefix + i + ".", str)
    } else {
      str += `${ prefix + i }=${ obj[i] }&`
            }
  }
  return str
}
console.log(toQueryString(obj5).slice(0, -1)) // Remove trailing '&'

// 22. Build nested object from flat dot notation keys
// - Description: Convert { 'a.b':1, 'a.c':2 } to {a:{b:1,c:2}}
// - Input: { 'a.b':1, 'a.c':2 }
// - Output: {a:{b:1,c:2}}

const obj6 = { 'a.b': 1, 'a.c': 2 }
function fromDotNotation(obj, key = "", res = {}) {
  for (let i in obj) {
    const keys = i.split(".")
    let curr = res
    for (let j = 0; j < keys.length; j++) {
      if (!curr[keys[j]]) {
        curr[keys[j]] = j === keys.length - 1 ? obj[i] : {}
      }
      curr = curr[keys[j]]
    }
  }
  return res
}
console.log(fromDotNotation(obj6))









