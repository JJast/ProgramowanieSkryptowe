function doPointlessComputationsWithRequestAnimationFrame() {
    const t0 = performance.now();


    function testCandidate(index) {
        // finishing condition
        if (index == iterations) {
            const t1 = performance.now();
            addChartPoint(t0, t1);

            console.log(primes);
            pointlessComputationsButton.disabled = false;
            return;
        }
        // test this number
        var candidate = index * (multiplier * Math.random());
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
        // schedule the next
        var testFunction = testCandidate.bind(this, index + 1);
        window.requestAnimationFrame(testFunction);
    }

    var primes = [];
    var testFunction = testCandidate.bind(this, 0);
    window.requestAnimationFrame(testFunction);
}

function doPointlessComputationsWithSetInterval() {
    const t0 = performance.now();

    function testCandidate(index) {
        // finishing condition
        if (index == iterations) {
            const t1 = performance.now();
            addChartPoint(t0, t1);

            console.log(primes);
            pointlessComputationsButton.disabled = false;
            return;
        }
        // test this number
        var candidate = index * (multiplier * Math.random());
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
        // schedule the next
        var testFunction = testCandidate.bind(this, index + 1);
        window.setInterval(testFunction);
    }

    var primes = [];
    var testFunction = testCandidate.bind(this, 0);
    window.setInterval(testFunction, 100);
}

function doPointlessComputationsWithSetTimeout() {
    const t0 = performance.now();

    function testCandidate(index) {
        // finishing condition
        if (index == iterations) {
            const t1 = performance.now();
            addChartPoint(t0, t1);

            console.log(primes);
            pointlessComputationsButton.disabled = false;
            return;
        }
        // test this number
        var candidate = index * (multiplier * Math.random());
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
        // schedule the next
        var testFunction = testCandidate.bind(this, index + 1);
        var id =  window.setTimeout(testFunction);
        //clearTimeout(id);
    }

    var primes = [];
    var testFunction = testCandidate.bind(this, 0);
    var id = window.setTimeout(testFunction, 100);
    //clearTimeout(id);
}