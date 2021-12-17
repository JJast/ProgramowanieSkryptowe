const iterations = 100;
const multiplier = 1000000000;

var worker = new Worker("js/calculate.js");

var chartData = [];
var chartIndex = 0;

/**
 * Doing the pointless computations.
 */
var pointlessComputationsButton = document.getElementById("pointless-computations");
pointlessComputationsButton.disabled = false;
pointlessComputationsButton.addEventListener("click", doPointlessComputations, false);

function doPointlessComputations() {
    pointlessComputationsButton.disabled = true;
    var useWorkerButton = document.getElementById("use-worker");
    var useBlockingJsButton = document.getElementById("use-blocking-js");
    var useRequestAnimationFrame = document.getElementById("use-request-animation-frame");
    var useSetTimeout = document.getElementById("use-set-timeout");
    var useSetInterval = document.getElementById("use-set-interval");

    if (useRequestAnimationFrame.checked) {
        doPointlessComputationsWithRequestAnimationFrame();
    }
    if (useSetTimeout.checked) {
        doPointlessComputationsWithSetTimeout();
    }
    if (useSetInterval.checked) {
        doPointlessComputationsWithSetInterval();
    }
    if (useWorkerButton.checked) {
        doPointlessComputationsInWorker();
    }
    if (useBlockingJsButton.checked) {
        doPointlessComputationsWithBlocking();
    }
}

/**
 * Start/stop animation
 */
var started = false;
var startStopButton = document.getElementById("start-stop");

startStopButton.addEventListener("click", startStop, false);

function startStop() {
    started = !started;
    if (started) {
        container.classList.add("started");
        startStopButton.value = "Stop animations";
    }
    else {
        container.classList.remove("started");
        startStopButton.value = "Start animations";
    }
}

function addChartPoint(t0, t1) {
    chart.data[0].addTo("dataPoints", {x:chartIndex, y:t1-t0});
    chartIndex++;
}