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

//  two sum

var twoSum = function (nums, target) {
  const obj = {};
    for (let i = 0; i < nums.length; i++) {
      console.log(nums[i], "index value in line 45")
    const newNum = nums[i];
    const compliment = target - newNum;
        if (compliment in obj) {
            console.log(obj, "obj in line 49")
            console.log(compliment, "compliemnt is here line 50");
            return [obj[compliment], i];
        }
        console.log(obj, "obj in line 53");
        console.log(compliment, "compliemnt is here line 54");
    obj[newNum] = i;
  }
  console.log(obj, "obj in line 57");
  return null;
};
const nums = [2, 3, 4, 5, 6, 7]
const target = 6
const result = twoSum(nums, target);
console.log(result); 