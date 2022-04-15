

//first for the title of the notes  section

let title =  document.createElement('h3')
let hr = document.createElement('hr')
title.classList.add('titleofthenotes') 
title.setAttribute('title','Title of your notes');


let toBeinAppend = document.getElementsByClassName('maketitle')[0];// we have to appnend the title

let titleNoteTextBox = document.getElementsByClassName('titleNotestxtBox')[0]; //input of the text box

toBeinAppend.appendChild(title)
toBeinAppend.appendChild(hr)

//keypress event 

titleNoteTextBox.addEventListener('keyup', function(e) {

     title.textContent = titleNoteTextBox.value
     

})






//title of the notes done here if any change u have to made write the code in above section..


// now for the notes 
//some global variable need to use 
var sizeOftext = document.getElementsByClassName('textsize')[0]; //size of text
var typeOftext = document.getElementsByClassName('texttype')[0];//type Of text
var colorOftext = document.getElementsByClassName('textcolor')[0];//color Of text

var st,tt,ct; //sizetext typetext colortext

st = sizeOftext.value; 
tt = typeOftext.value;
ct = colorOftext.value;
// if user changes the values of those
sizeOftext.onchange = (e)=>{


    st = sizeOftext.value


}

typeOftext.onchange = (e)=>{

    tt = typeOftext.value
   
}

colorOftext.onchange = (e)=>{

    ct = colorOftext.value
   
}

/////////////








let textBoxes = document.getElementsByClassName('b1');
Array.from(textBoxes).forEach((e,i)=>{

    
    e.addEventListener('keyup', function(e){


    var kindOfElement  ;

 if (st == 1)
 {
     kindOfElement = 'h2'
 }
 else if (st == 2)
 {
     kindOfElement = 'h4'
 }else if(st == 3)
{
    kindOfElement = 'h6'
}
else if(st == 4)
{
    kindOfElement = 'p'
}else
{
    kindOfElement = 'section'
}

console.log(kindOfElement);
var createdElement = document.createElement(kindOfElement);

   document.getElementsByClassName('b1d1')[0].appendChild(createdElement);
        
     
        createdElement.textContent = e.target.value;


    })


})