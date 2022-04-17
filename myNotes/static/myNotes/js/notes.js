

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



//main code for display here is inside this .. 
setInterval(() => {
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
    }else if(st == 5)
    {
        kindOfElement = 'li'
    }   
    else
    {
        kindOfElement = 'section'
    }
    
    
    
    let Tobe = document.getElementsByClassName(`d${e.classList[1]}`)[0]
    
    Tobe.innerHTML = `<${kindOfElement} class='d${e.classList[1]}t1' > ${e.value}  </${kindOfElement}>`
     
    
    //now style through js style
    //all the style codeing can be done from here if any..
    let mkStyle = document.getElementsByClassName(`d${e.classList[1]}t1`)[0]
 

    let bold = document.getElementsByClassName('mbold')[0].checked
    let italic = document.getElementsByClassName('mitalic')[0].checked
    let underline = document.getElementsByClassName('munderline')[0].checked
    
    


    //color change
    mkStyle.style.color = ct;
    mkStyle.style.fontFamily = tt;
    //making bold
    if(bold)
    {
        mkStyle.style.fontWeight = '600'

    }

    if(italic)
    {
        mkStyle.style.fontStyle = 'italic'
    }

    if(underline)
    {
       mkStyle.style.textDecoration =  'underline'

    }
    
    
    })
    })
    
}, 1000);
//now clicking on the add button.. 


let addBtn =  document.getElementsByClassName('addbtn')[0];
let insideInsert = document.getElementsByClassName('aldtatoinsert')[0];
var count =2;
addBtn.addEventListener('click',(event)=>{

    AddElements(count++);
})


//key event ctrl + enter 
let  keysPressed = {};

document.addEventListener('keydown', (event) => {
    keysPressed[event.key] = true;
 
    if (keysPressed['Control'] && event.key == 'Enter') {
        AddElements(count++);
    }
 });
 
 document.addEventListener('keyup', (event) => {
    delete keysPressed[event.key];
 });


//this function simply will add innerHtml
function AddElements(count){{

    let newDIV = document.createElement('div');

    newDIV.setAttribute('class','input-group container mt-3')
    newDIV.innerHTML += `
    
    <div class="input-group mt-3">

    <div class="container insertdata db${count}">
  
    </div>


    <div class="container insertdata dbi${count}">
  
    </div>


    <textarea name=""   class="form-control b${count} txtbx" placeholder="Hello World !"></textarea>
      <span class="input-group-text "  id="basic-addon2"><input type="file" name="" id="" class="form-control bi1 i${count}" placeholder="Add image"></span>
    </div>
    
    
    `
    insideInsert.appendChild(newDIV);

}}




//for the image upload function


    
let image_upload = document.getElementsByClassName('bi1');


 
   

setInterval(() => {
    Array.from(image_upload).forEach(function(event,index){

        event.addEventListener('change',(e)=>{
    
            var imageSRC = URL.createObjectURL(e.target.files[0]);


            
       
      
          let insidethisAppend = document.getElementsByClassName(`db${event.classList[2]}`)[0]

         

          insidethisAppend.innerHTML = `<img class ='img-fluid pdfimgs' src='${imageSRC}' width='340px' height='230px'> `
            
    
        })
    

    
    })
    
}, 1000);






//selection particular

document.body.onselectstart = (e)=>{
    let selection = document.getSelection();


   
    location.href = '#popup1'
}