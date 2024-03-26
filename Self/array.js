// sum and its average 
const a = [1,2,3,4,5,]
let sum = 0 
for (let i = 0; i < a.length; i++) {
    sum += a[i] 
}
console.log(sum / a.length)

// duplicate numbers 
const array = [1, 2, 2, 3, 4, 6,5, 5, 6,7]
let p = [...new Set(array)];
// let p = array.filter((each, index)=>{
//     return array.indexOf(each) !== index
// })
console.log('duplicte array start')
console.log(p)
console.log('duplicte array end')


// sreaching and sorting 
let sortedarray = array.sort()
console.log(sortedarray)

// reverse string 
let str = "shivam"
for (let i = str.length-1;i>=0; i--){
    console.log(str[i]);
}
 let reversestring = str.split("").reverse().join("");
 console.log(reversestring);

 let string = "my name is shivam rathore"
 let newstring = string.split(" ").reverse().join(" ");
 console.log(newstring) 

 let s = 'my name is shivam rathore'
 let reverse = s.split(" ").reverse().join(" ").split("").reverse().join("");
 console.log(reverse)

 