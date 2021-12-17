const iterations = 50;
const multiplier = 1000000000;

function calculatePrimes(iterations, multiplier) {
  var primes = [];
  for (var i = 0; i < iterations; i++) {
    var candidate = i * (multiplier * Math.random());
    var isPrime = true;
    for (var c = 2; c <= Math.sqrt(candidate); ++c) {
      if (candidate % c === 0) {
          // not prime
          isPrime = false;
          break;
       }
    }
    if (isPrime) {
      primes.push(candidate);
    }
  }
  return primes;
}

var SetIntervalTime = []
var SetTimeoutTime = []

var N = 10000;

var setIntId;
var setTimId;

document.getElementById('start').onclick = function () {
    var M = parseInt(document.getElementById('delay').value);
    var useSetTimeout = document.getElementById("use-set-timeout");
    var useSetInterval = document.getElementById("use-set-interval");
    
    if (useSetTimeout.checked) {
        setIntId = setInterval(doTimeConsumingCalculationsWithSetInterval, M);
    }
    if (useSetInterval.checked) {
        setTimId = setTimeout(doTimeConsumingCalculationsWithSetTimeout, M);
    }
    requestAnimationFrame(drawChart);
}

document.getElementById('stop').onclick = function () {
    console.log('stop');
    clearInterval(setIntId);
    clearTimeout(setTimId);
}

function doTimeConsumingCalculationsWithSetInterval() {
    SetIntervalTime.push(performance.now());
    if (SetIntervalTime.length > N) {
        SetIntervalTime.shift();
    }
    calculatePrimes(1000, 100000000);
}

function doTimeConsumingCalculationsWithSetTimeout() {
    SetTimeoutTime.push(performance.now());
    if (SetTimeoutTime.length > N) {
        SetTimeoutTime.shift();
    }
    calculatePrimes(1000, 100000000);
    var M = parseInt(document.getElementById('delay').value);
    setTimId = setTimeout(doTimeConsumingCalculationsWithSetTimeout, M);
}

function drawChart(){
    var tmpInt = [];
    var tmpTim = [];
    for (var i = 1 ; i < SetIntervalTime.length; i++) {
        tmpInt.push({x: i, y: SetIntervalTime[i] - SetIntervalTime[i - 1]});
    }
    for (var i = 1 ; i < SetTimeoutTime.length; i++) {
        tmpTim.push({x: i, y: SetTimeoutTime[i] - SetTimeoutTime[i - 1]});
    }
    var chart = new CanvasJS.Chart("chartContainer", {
        title:{
            text: "Pointless computations chart"
        },
        axisX:{
            title: "pointlessAnimation button count",
        },
        axisY:{
            title: "Computation Time [ms]",
        },
        data: [
        {
            type: "line",
            dataPoints: tmpInt
        },
        {
            type: "line",
            dataPoints: tmpTim
        }
    ]
    });
    chart.render();
    requestAnimationFrame(drawChart);
}