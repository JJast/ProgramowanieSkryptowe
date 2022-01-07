const { expect } = require('chai');
const module2 = require('../skrypt');


describe('checkAndShow()', () => {
    it('Test directory', () => {
        let op = module2.checkAndShow(".");
        expect(op).to.equal(". is a directory");
    });
    it('Test file', () => {
        let op = module2.checkAndShow("testfile.txt");
        expect(op).to.equal("testfile.txt is a file. Content:sss");
    });
});