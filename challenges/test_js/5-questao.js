const laugh = function(number) {
    message = "";
    while (number > 0) {
        message += "ha";
        number--;
    }
    return message += "!";
}

console.log(laugh(1))
console.log(laugh(2))
console.log(laugh(3))
