const { checkAndShow } = require("./skrypt");

function requestListener(request, response) {
    console.log("--------------------------------------");
    console.log("The relative URL of the current request: " + request.url + "\n");
  
    var url = new URL(request.url, `http://${request.headers.host}`);
  
    if (url.pathname == '/submit') {
      /* ************************************************** */
      response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
      /* ************************************************** */
      if (request.method == 'GET') {
        checkAndShow(response, url.searchParams.get('fpath'));
      }
      else {
        response.write(`This application does not support the ${request.method} method`);
        response.end();
      }
    }
    else {
      response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      /* ************************************************** */
      response.write(`<form method="GET" action="/submit">
                    <label for="fpath">Input path to check</label>
                    <input name="fpath">
                    <br>
                    <input type="submit">
                    <input type="reset">
                  </form>`);
      /* ************************************************** */
      response.end();
    }
  }
  
  /* ************************************************** */
  /* Main block
  /* ************************************************** */

  var http =require('http')
  var server = http.createServer(requestListener); // The 'requestListener' function is defined above
  
  server.listen(8080);
  console.log("The server was started on port 8080");
  console.log("To stop the server, press 'CTRL + C'");