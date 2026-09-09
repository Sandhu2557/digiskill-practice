// Conditionals
// What are operators?

// 1) Arithmetic Operators (+, -, *, /)
// 2) Increment & decrement operators (++, --)
// 3) Assignment Operators (=, +=)
// 4) comparison operators (==, ===, !=, <, >)
// 5) Logical operators (&&, ||, !)
// 6) Ternary Operator 

// 1) Arithmetic Operators (+, -, *, /)
{
let a = 1, b = 2;
console.log(a+b)
}
   // 2) Increment & decrement operators (++, --) 
{
    let a = 1;
    a++;
    ++a;
    console.log(a)
    --a;
    a--;
    console.log(a)
}

// 3) Assignment Operators (=, +=)
{
    a = 10;
    a += 90;
    console.log(a)
}

// 4) comparison operators (==, ===, !=, <, >)

{
    let name = "Usman";
    let surname = "Asghar";
    console.log(name != surname)

    let age = "25"; //string
    let height = 25; // Number
    // only == this only check value of the variable
    console.log(age == height)
    // But on the other hand === this also check the datatype of the variable
    console.log(age === height)

    let a = 4;
    let b = 15;
    console.log( a < b)
}

// 5) Logical operators (&&, ||, !)

{
    let age = 20;
    let hasCNIC = false;
    // AND operator check both conditions 
    console.log(age >= 18 && hasCNIC);
    // OR operator only check one condition 
    console.log(age >= 18 || hasCNIC);
    
}

// conditionals statments
{
    if(true && false){
        console.log("Yes ture");
    }
    else if(false){
        console.log("Hello World");
    }
    else{
        console.log("not you")
    }

    let age = 15;
    if(age >= 18){
        console.log("Adult");
    }
    else if(age < 18){
        console.log(age)
    }
    else{
        console.log("Not Adult");
    }
}

// 6) Ternary Operator 

{
    let age = 14;
    let result = age >= 18 ? "Adult" : "Minor";
    console.log(result)
}