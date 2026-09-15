// Normal function 
function greet(name){
    return "Hello " + name;
}

console.log(greet("Usman"));

//Function Expression
{
    const greet = function(name){
        return "Hello " + name;
    }
    console.log(greet)
}

// Arrow Function
{
    const greet = (name) => {
        return "Hello " + name;
    };
}
// Arrow function Example
{
    const square = (num) =>{
        return num * num;
    }
    console.log(square(4));
}

// Arrow function Example 2
{
    const add = (num,num2) => {
        return num + num2;
    }
    console.log(add(10,30));
}

// Arrow Example 3

{
    const deliveryCharges = (km) => {
    return km * 20;
}
    console.log(deliveryCharges(10));

}

// Defualt parameter 

{
    const greet = (name ="Unknown") => {
        return "Hello " + name;
    }
    console.log(greet("Usman"));
    console.log(greet());
}

// Other Example of default parameter

{
    function order(item, quantity=1){
    console.log(item + " x " + quantity);
}
order("Burger",10);
order("pizza");
}

// Rest Parameters

{
    const shownumbers = (...numbers) => {
        console.log("Number :", numbers)
    }
    shownumbers(1,2,3,4,5,6,7);
}

// Rest paramter example 

{
    function totalMarks(...marks){
    let total = 0;
    for(let mark of marks){
        total += mark;
    }
    return total;
}
console.log(totalMarks(90,10,20));
}
