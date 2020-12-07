const masses = require('fs')
    .readFileSync('input')
    .toString()
    .split(/\r?\n/)

let sum = masses
    .map(m => Math.floor(parseInt(m) / 3) - 2)
    .reduce((sum, m) => sum + m)

console.log(sum)