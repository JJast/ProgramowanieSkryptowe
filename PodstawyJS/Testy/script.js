var expect = chai.expect;

function sum(x,y) {
    return x+y;
}

describe('The sum() function', function() {
    it('Returns 4 for 2+2', function() {
        expect(sum(2,2)).to.equal(4);
    });
    it('Returns 0 for -2+2', function() {
        expect(sum(-2,2)).to.equal(0);
    });
});


describe('The cyfry() function', function() {
    it('Same cyfry', function() {
        expect(cyfry("123")).to.equal(6);
    });
    it('Same litery', function() {
        expect(cyfry("abcdefghijk")).to.equal(0);
    });
    it('Litery, a po nich cyfry', function() {
        expect(cyfry("abc123")).to.equal(6);
    });
    it('Cyfry, a po nich litery', function() {
        expect(cyfry("123abc")).to.equal(6);
    });
    it('Pusty napis', function() {
        expect(cyfry("")).to.equal(0);
    });
});

describe('The litery() function', function() {
    it('Same cyfry', function() {
        expect(litery("123")).to.equal(0);
    });
    it('Same litery', function() {
        expect(litery("abcdefghijk")).to.equal(11);
    });
    it('Litery, a po nich cyfry', function() {
        expect(litery("abc123")).to.equal(3);
    });
    it('Cyfry, a po nich litery', function() {
        expect(litery("123abc")).to.equal(3);
    });
    it('Pusty napis', function() {
        expect(litery("")).to.equal(0);
    });
});

describe('The suma() function', function() {
    globalnaSuma = 0;
    it('Same cyfry', function() {
        expect(suma("123")).to.equal(123);
    });
    it('Same litery', function() {
        expect(suma("abcdefghijk")).to.equal(123);
    });
    it('Litery, a po nich cyfry', function() {
        expect(suma("abc123")).to.equal(123);
    });
    it('Cyfry, a po nich litery', function() {
        expect(suma("123abc")).to.equal(246);
    });
    it('Pusty napis', function() {
        expect(suma("")).to.equal(246);
    });
});