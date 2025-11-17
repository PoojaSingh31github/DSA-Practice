function combine(obj1, obj2) {
  console.log({ ...obj1, ...obj2 });
}

var a = { name: "pooja" };
var b = { lastname: "singh" };

combine.call(null, a, b); 


function combine(obj1, obj2) {
  console.log({ ...obj1, ...obj2 });
}

var a = { name: "pooja" };
var b = { lastname: "singh" };

combine.apply(null, [a, b]);



function combine(obj1, obj2) {
  console.log({ ...obj1, ...obj2 });
}

var a = { name: "pooja" };
var b = { lastname: "singh" };

const newFn = combine.bind(null, a, b);
newFn(); 
