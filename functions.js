/* 
 why do we need functions?
 Function declaration: basic syntax
 Function call: "button press" concept
 Parameters : passing data into a function
 Arguments vs parameters
 Return values: result
 console.log vs return
 Function expression
 Declaration vs expression (hoisted)
 common beginner mistakes
*/

function greet(name){ //parameter given to function
    console.log("Say hello",name);
}

{
    greet("usman");//argument the value of the parameter
    greet("Ali");
    greet("Zain");
}

{
    function add(num1,num2){
    return num1 + num2;
}
    console.log(add(2,10));
}

// console vs return

{
    function add(num1,num2){
    console.log(num1 + num2);
}
   add(2,10);
}

// Functional expression

const sayHi = function(){
    console.log("Functional Expression");
};

sayHi();

 