speackButton =  document.getElementById('speack')


    var speech = true;
window.SpeechRecognition = window.SpeechRecognition
                || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = true;


recognition.addEventListener('result', e => {
    const transcript = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('')

    document.getElementById("notes").innerHTML = transcript;
  
});
  
if (speech == true) {
    recognition.start();
    recognition.addEventListener('end', recognition.start);
}







