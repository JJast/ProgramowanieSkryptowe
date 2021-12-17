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

function doPointlessComputationsWithBlocking() {
    const t0 = performance.now();

    var primes = calculatePrimes(iterations, multiplier);
    pointlessComputationsButton.disabled = false;

    const t1 = performance.now();
    addChartPoint(t0, t1);

    console.log(primes);
}