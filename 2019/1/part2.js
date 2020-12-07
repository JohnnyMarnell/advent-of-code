const masses = require('fs')
    .readFileSync('input')
    .toString()
    .split(/\r?\n/)

// at the very least, can memoize the fuel values
// i'm also wondering if we can use log() base 3 math, and subtract 2 * log()...
let sum = 0
masses
    .forEach(mass => {
        let fuel = parseInt(mass)
        while (fuel > 0) {
            console.log(fuel)
            fuel = Math.max(0, Math.floor(fuel / 3) - 2)
            sum += fuel
        }
    })

