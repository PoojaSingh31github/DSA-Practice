let i, j;
console.log("first star pattern");
for (i = 1; i <= 5; i++) {
    let row = "";
    for (j = 1; j <= 5; j++) {
        row += "* ";
    }
    console.log(row);
}

console.log("second star pattern");
for (i = 1; i <= 5; i++) {
    let row = "";
    for (j = 1; j <= i; j++) {
        row += "* ";
    }
    console.log(row);
}

console.log("third star pattern");
for (i = 1; i <= 5; i++) {
    let row = "";
    for (j = 5; j >= i; j--) {
        row += "* ";
    }
    console.log(row);
}
// finding prime no 
let num = 10;
console.log("prime no. from 1 to 10");
let isprime = true;
for (let i = 2; i <= num - 1; i++) {
    if (num % i === 0) {
        isprime = false;
        break;
    }
}
if(isprime){
    console.log(`${num} is prime no.`);
}else{
    console.log(`${num} is not prime no.`);
}

// map
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log("map method")
const maparr = arr.map((x) => {
    // binary value getting from decimal
    return x.toString(2);
})
console.log(maparr);

// filter method 
console.log('filter method');

const output = arr.filter((x) => x.toString(2));
console.log(output);

// reduce method 
const output2 = arr.reduce((acc, curr) => {
    acc = acc + curr;
    return acc;
}, 0);  // 0 is initial value
console.log(output2);

// sum of array
let sum = 0;
for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
}
console.log(sum);
// maximum of array
let max = 0;
for (let i = 0; i < arr.length; i++) {
    if (arr[i] > max) { max = arr[i] }
}
console.log(max);

// minimum of array
const array = [-1, -2, -3, 1, 2, 3, 4, 6,]
let min = 0;
for (let i = 0; i < array.length; i++) {
    if (array[i] < min) { min = array[i] }
}
console.log(min);
// reduce metohod to find minimum of array
console.log("minimum of array by reduce function ")
const reduceArray = array.reduce((acc, curr) => {
    if (curr < acc) {
        acc = curr;
    }
    return acc;
}, 0)
console.log(reduceArray);

//  objects with map reduce and filter method 
const users = [
    { name: 'Suraj', age: 29 },
    { name: 'Shikha', age: 22 },
    { name: 'pooja', age: 22 },
    { name: 'anjali', age: 27 },
    { name: 'meena', age: 22 }
];
console.log("map over objects and filter over all objests");
const filtervalue = users.filter((user) => {
    return `my name is ${user.name} and my age is ${user.age}`
})
const mappedvalue = users.map((user) => {
    return `my name is ${user.name} and my age is ${user.age}`
})
const reducevalue = users.reduce((acc, curr) => {
    if (acc[curr.age]) {
        acc[curr.age] = ++acc[curr.age];
    } else {
        acc[curr.age] = 1
    }
    return acc;
}, {})
console.log(filtervalue);
console.log(mappedvalue);
console.log(reducevalue);













