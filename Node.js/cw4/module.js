/**
 * Operation class.
 * @constructor
 */
class Operation {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  /** This is a description of the get x. */
  get getX() {
    return this.x;
  }

  /** This is a description of the sum method. */
  sum() {
    return this.x + this.y;
  }
}

module.exports.Operation = Operation;
