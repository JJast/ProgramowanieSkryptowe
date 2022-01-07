//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8080");

// UNIT test begin
describe('GET /submit?fpath=testfile.txt', function () {
  it('respond with contents of testfile.txt', function (done) {
    server
      .get('/submit?fpath=testfile.txt')
      .expect('Content-Type', /text\/plain/)
      .expect(200, "testfile.txt is a file. Content:sss", done);
  });
});