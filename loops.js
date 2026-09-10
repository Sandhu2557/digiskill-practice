// Topics: Loops & Iteration

// for loop
// While, Do while 
// Syntax :
// for(initialization; condition; increment){}
{
    for(let i=1; i <= 5; i++){
    console.log(i);
}
}

{
    let array = ["Usman", "Ali", "Umer"];
    for(let val of array){
        console.log(val);
    }
}

{
    // object iterate in loop
let obj = {name : "usman", age:90, gender:"home"};

for(let key in obj){
    console.log(key, obj[key]);
}
}

// continue keyword and break keyword
for(let i=1; i<=5; i++){
    if(i == 3) continue;
    if(i == 4) break;
    console.log(i);
}

