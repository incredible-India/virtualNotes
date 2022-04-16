

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








let textBoxes = document.getElementsByClassName('txtbx');


Array.from(textBoxes).forEach((e,i)=>{

    
    e.addEventListener('keyup', function(event){
//isme hum ctrl aur enter ka func likh sakte hai

    var kindOfElement  ;

 if (st == 1)
 {
     kindOfElement = 'h1'
 }
 else if (st == 2)
 {
     kindOfElement = 'h3'
 }else if(st == 3)
{
    kindOfElement = 'h4'
}
else if(st == 4)
{
    kindOfElement = 'p'
}else
{
    kindOfElement = 'section'
}



let Tobe = document.getElementsByClassName(`d${e.classList[1]}`)[0]

Tobe.innerHTML = `<${kindOfElement} class='d${e.classList[1]}t1' > ${e.value}  </${kindOfElement}>`
 

//now style through js style
//all the style codeing can be done from here if any..
let mkStyle = document.getElementsByClassName(`d${e.classList[1]}t1`)[0]
//type bold italic or normal
if (tt == 3)
{

        mkStyle.style.fontWeight = '600';

}else if (tt == 2)
{

    mkStyle.style.fontStyle = 'italic';

}else
{
    mkStyle.style.fontWeight = '200';

}


//color change
mkStyle.style.color = ct;



})
})



//now clicking on the add button.. 


let addBtn =  document.getElementsByClassName('addbtn')[0];
let insideInsert = document.getElementsByClassName('aldtatoinsert')[0];
var count =2;
addBtn.addEventListener('click',(event)=>{

  
    AddElements(count++);
})

function AddElements(count){{

    let newDIV = document.createElement('div');

    newDIV.setAttribute('class','input-group container mt-3')
    newDIV.innerHTML += `
    
    <div class="input-group mt-3">

    <div class="container insertdata db${count}">
  
    </div>

    <textarea name=""   class="form-control b${count} txtbx" placeholder="Hello World !"></textarea>
      <span class="input-group-text bi1" id="basic-addon2"><input type="file" name="" id="" class="form-control" placeholder="Add image"></span>
    </div>
    
    
    `
    insideInsert.appendChild(newDIV);

}}


Array.from(document.getElementsByClassName('txtbx')).forEach(e=>{

    e.addEventListener('click',()=>{

        console.log('isko chhua ',e.className);

    })
   })