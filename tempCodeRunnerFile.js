function totalMarks(...marks){
    let total = 0;
    for(let mark of marks){
        total += mark;
    }
    return total;
}
console.log(totalMarks(90,10,20));