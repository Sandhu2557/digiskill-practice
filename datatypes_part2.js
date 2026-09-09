// Object design structure

let user = {name:"usman", age:90, gender:"male"};
console.log(user.name);

// second way to acces value of object
console.log(user["gender"])

// array
let fruits=["apple","banana","orange", 90, 56.90];
console.log(fruits[4]);
// how to check variable type
console.log(typeof(fruits))


// How to change variable type
let age = 20;
console.log(typeof(age));
age = String(age);
console.log(typeof(age));

// Javascript buildin function String() Number() for type conversion