var worker = new Worker("js/calculate.js");

function doPointlessComputationsInWorker() {
    const t0 = performance.now();

    function handleWorkerCompletion(message) {
        if (message.data.command == "done") {
            const t1 = performance.now();
            addChartPoint(t0, t1);

            pointlessComputationsButton.disabled = false;
            console.log(message.data.primes);
            worker.removeEventListener("message", handleWorkerCompletion);
        }
    }

    worker.addEventListener("message", handleWorkerCompletion, false);

    worker.postMessage({
        "multiplier": multiplier,
        "iterations": iterations
    });
}