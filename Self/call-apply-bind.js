// pass by value = primitive datatype  
// pass by refferce = non primitive datatype

// example 
var a=5;
var b = a;
a = 10;
console.log("value of a "+a);
console.log( "value of b "+b);
// it dont change becos it store in stack 

let obj1 = {
    name:"pooja",
    age:22,
    designation: "software developer",
    printDetails:function(){
        console.log( "Name of obj "+this.name);
        console.log( "age of obj "+this.age);
        console.log( "Designation of obj "+this.designation);

    }
}
obj1.printDetails();

let obj2= obj1;
obj1.name = "suraj";
console.log("value of obj1 "+obj1.name);
console.log("value of obj2 "+obj2.name);

let arr1=[1,2,3,4,5]
let arr2=arr1
arr2.push(8)
console.log(arr1)
console.log(arr2)
// it change the refrence as it store in heap



// call = in parentheisis
// apply = in array
// bind  = 
console.log('------------------------')
let printDetails =function(state, country){
    console.log(this.name +" "+state+ " "+ country)
}
let user1 = {
    name:"pooja",
    age:22,
    designation: "software developer",
}
let user2 = {
    name:"suraj",
    age:29,
    designation: "software developer",
}
printDetails.call(user1, "Delhi", "India");
printDetails.apply(user2, ["Delhi", "India"]);
console.log('----------------------------')

// bind
let newfun = printDetails.bind(user1, "Delhi", "India");
newfun();

