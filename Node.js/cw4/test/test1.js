const { expect } = require('chai');
const module2 = require('../module');

describe('The sum() method', () => {
  it('Returns 4 for 2+2', () => {
    const op = new module2.Operation(2, 2);
    expect(op.sum()).to.equal(4);
  });
  it('Returns 0 for -2+2', () => {
    const op = new module2.Operation(-2, 2);
    expect(op.sum()).to.equal(0);
  });
});
