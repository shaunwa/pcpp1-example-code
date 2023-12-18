// 1 1 2 3 5 8 13 21 34 ...

const fibonacci = n => {
    if (n <= 2) {
        return 1;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(1));
console.log(fibonacci(2));
console.log(fibonacci(5));
console.log(fibonacci(10));