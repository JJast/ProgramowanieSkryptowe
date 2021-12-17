var x = window.prompt("Tekst1",x);
        document.write(typeof(x))
        
function mySubmit(e) {
    const tekst = document.getElementsByName("pole_tekstowe")[0].value;
    const liczba = document.getElementsByName("pole_liczbowe")[0].value;
    document.write(`Tekst: ${tekst} <br>Liczba: ${liczba}`)
}