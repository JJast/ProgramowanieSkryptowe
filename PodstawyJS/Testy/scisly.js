"use strict";

var globalnaSuma = 0;

function cyfry(napis) {
    let sum = 0;
    for (let i = 0; i < napis.length; i++) {
        let c = napis.charAt(i);
        if(c >= '0' && c <= '9') {
            sum += parseInt(c, 10);
        }
    }
    return sum;
}

function litery(napis) {
    let sum = 0;
    for (let i = 0; i < napis.length; i++) {
        let c = napis.charAt(i);
        if((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            sum++;
        }
    }
    return sum;
}

function suma(napis) {
    var matches = napis.match(/(^\d+)/);
    if(matches) {
        globalnaSuma += parseInt(matches[0], 10);
    }
    return globalnaSuma;
}

async function runPrompting() {
    while(true) {
        await new Promise(r => setTimeout(r, 100));
        let userInput = window.prompt("Wprowadz dane");
        if(typeof userInput != "string") {
            break;
        }
        let sumaCyfr = cyfry(userInput);
        let sumaLiczb = litery(userInput);
        let sumaWszystkich = suma(userInput);

        var para = document.createElement("pre");
        var textNode = document.createTextNode(`${userInput}\n\t${sumaCyfr}\t${sumaLiczb}\t${sumaWszystkich}`);
        para.appendChild(textNode);
        document.body.appendChild(para);
    }
}


