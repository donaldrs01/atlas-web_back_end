export function taskFirst() {
    // const ensures that it's a constant value that doesn't change
    const task = 'I prefer const when I can.';
    return task;
}

export function getLast() {
    return ' is okay';
}

export function taskNext() {
    // because the value of 'combination' is changed, we use 'let' keyword
    let combination = 'But sometimes let';
    combination += getLast();

    return combination;
}