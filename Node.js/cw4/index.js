// import Operation from './module.mjs';
const module2 = require('./module');

const o = new module2.Operation(parseInt(process.argv[2], 10), parseInt(process.argv[3], 10));

console.log(o.sum());
