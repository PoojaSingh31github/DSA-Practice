
const arr = [1, 2, 3,4, 0,4, 4,0,  7,0,0, 9];
let j =arr.length-1
for (let i=arr.length-1; i>=0;i--){
    if (arr[i] !== 0){
        [arr[i], arr[j]] = [arr[j], arr[i]]
        j-=1
    }
}
console.log(arr)

let j =0
for (let i in arr){
    if (arr[i] !== 0){
        [arr[i], arr[j]]=[arr[j], arr[i]]
        j+=1
    }
}
console.log(arr)

// const arr = [24,25,36,52,92,49]

// first highest second highest and third highest 





first = 0
second = 0
third = 0 

for (let i of arr){
    if (i > first){
        third = second
        second = first 
        first = i
    }else if (i < first && second < i ){
        third = second
        second = i 
    }else if (i < second && third < i){
        third = i
    }
    
}
console.log(third , first , second)


// subset
arr = [1,2,3,4]

let res = [[]]
for (let i in arr){
    let newsubset = []
    for (let subset of res){
        newsubset.push([...subset, i])
    }
    res = [...res, ...newsubset]
    
}
// console.log(res)


function twoSum(arr, target) {
  const obj = {};
  for (let i = 0; i < arr.length; i++) {
    let comp = target - arr[i];
    if (obj.hasOwnProperty(comp)) {
      return [obj[comp], i];
    }
    obj[arr[i]] = i;
  }
}
console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]

console.log("listen".split("").sort().join("") === "silent".split("").sort().join("")); // true

function rotate(nums, k) {
  k = k % nums.length;
  let part1 = nums.slice(0, nums.length - k);
  let part2 = nums.slice(-k);
  return [...part2, ...part1];
}
console.log(rotate([1, 2, 3, 4, 5, 6, 7], 3)); // [5,6,7,1,2,3,4]

function len(s) {
  let charSet = new Set();
  let maxlen = 0;
  let right = 0, left = 0;
  while (right < s.length) {
    if (charSet.has(s[right])) {
      charSet.delete(s[left]);
      left++;
    } else {
      charSet.add(s[right]);
      right++;
      maxlen = Math.max(maxlen, charSet.size);
    }
  }
  return maxlen;
}
console.log(len("abcabcbb")); // 3

function isValid(s) {
  const st = [];
  const map = { "(": ")", "{": "}", "[": "]" };
  for (let i of s) {
    if (map[i]) {
      st.push(i);
    } else {
      const last = st.pop();
      if (map[last] !== i) return false;
    }
  }
  return st.length === 0;
}
console.log(isValid("()[]{}")); // true


function flatten(arr, res = []) {
  for (let i of arr) {
    if (Array.isArray(i)) {
      flatten(i, res);
    } else {
      res.push(i);
    }
  }
  return res;
}
console.log(flatten([1, [2, [3, [4]]]])); // [1,2,3,4]


function debounce(func, delay) {
  let timer;
  return function() {
    clearTimeout(timer);
    timer = setTimeout(() => func(), delay);
  };
}

function throttle(func, delay) {
  let timer;
  return function() {
    if (!timer) {
      func();
      timer = true;
      setTimeout(() => (timer = false), delay);
    }
  };
}

 function firstUniqueChar(str){
    const obj={};
    for (let i of str){
      obj[i] = obj[i] +1 || 1
    }

    for (let i in obj){
      if (obj[i] ===1){
        return i
      }
    }

  }

  console.log(firstUniqueChar("aaddbcdd"))

  function moveZero(arr) {
    let j = 0
    for (let i in arr) {
      if (arr[i] !== 0) {
        [arr[i], arr[j]] = [arr[j], arr[i]]
        j++
      }
    }
    return arr
  }

  console.log(moveZero([0, 1, 0, 3, 12]))

  function removeinplaceduplicate(arr) {
    arr.sort()
    let j =0
    for (let i in arr){
      if (arr[i] !==arr[j]){
        arr[++j] = arr[i]
      }

    }
    return arr.slice(0,j+1)
    
  }

  console.log(removeinplaceduplicate([1,1,2,2,3,2,3]))

  function kadane(arr){
    let sum = -Infinity
    let currsum =0
    for (let i of arr){
      currsum +=i
      if (currsum > sum){
        sum = currsum
      }
      if (currsum< 0){
        currsum = 0
      }
    }
    return sum
  }

  console.log(kadane([-2,1,-3,4,-1,2,1,-5,4]))


// wriote an function whcih will try to call same function again and gaain tiull 4-5 time after some delay 
function sum(a,b){
    return a+b 
}
for (let i=0; i<4;i++){
    const tryy = setTimeout(()=>{
        console.log(sum(2,4))
    }, i*1000)
}






