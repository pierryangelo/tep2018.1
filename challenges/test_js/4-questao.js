const fizzBuzz = function(number) {
    if ((number % 15) === 0) {
        return "JuliaJames";
    }

    if ((number % 5) === 0) {
        return "James";
    }

    if ((number % 3) === 0) {
        return "Julia";
    }

    return String(number);
}

for (let i = 1; i <= 20; i++) {
    console.log(fizzBuzz(i))
}
