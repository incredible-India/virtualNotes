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



//for changing the color of notes


try {
    
    let bgBody = document.getElementsByClassName('chColor');//body of card  
 

    let colors = ['bg-info','bg-dark','bg-danger','bg-success','bg-primary','bg-light']

    Array.from(bgBody).forEach((e,i)=>{
    
        e.classList.add(colors[i]);
    })



} catch (error) {
    console.log(error);
}


