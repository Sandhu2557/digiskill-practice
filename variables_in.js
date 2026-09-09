//variables and scope
// Types of variables (var, let, const)

// let was introduced in ECMAS (ECMASScript 2015), which was released in 2015.

//Avoid var (variable re-declaration, block scope, hoisting confusion, accidental)

// var name="Usman";
// name = "ali";
// // console.log(name);

// use let keyword for variables
let name1 = "usman";
name1 = "asghar";
console.log(name1)

//const for assign permanent value to variable

const cnic = 34601;
console.log(cnic);
// cnic=90234; --> error can not change constant value

//Globel variable 
let name="usman";

function greet(){
    var surname="Asghar"
    console.log(name)
    console.log(surname)
}

greet();

if(true){
    var age=25
    console.log(age)
}
console.log(age)

// Hoisting

console.log(a);
var a = 5;

// Javascript will run this code like this form
var a;
console.log(a)
a = 5;

// on the other hand if we use let keyword this same code give us error
console.log(a);
var a = 5;