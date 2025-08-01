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

function recusion(navTree, res=[]){
    
    res.push(navTree.label)
    if(navTree.children){
       for (let item of navTree.children){
           console.log(item,"items")
           recusion(item, res)
       } 
    }
    return res
    
    
    
}
console.log(recusion(navTree))


const recur=(tree, res=[])=>{
    if (tree.label){
        res.push(tree.label)
    } 
    if (tree.children){
        for (let key of tree.children){
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


let res = items.reduce((acc,{name, category},index)=>{
    (acc[category] ||= []).push(name)
  return acc
},{})

console.log(res)







