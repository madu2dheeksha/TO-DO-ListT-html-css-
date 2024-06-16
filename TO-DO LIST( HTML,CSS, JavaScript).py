


# TO-DO LIST--------> HTML CODE
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dheeksha's To-Do List </title>
    <link rel="stylesheet" href="stylee.css">
</head>
<body>
    <div class="container">
        <div class="todo-app">
            <h2>dheeksha's To-Do List <img src="images.png"></h2>

            <div class="row">
                <input type="text" name="" id="input-box" placeholder="Add your Text">
                <button onclick="add task"()">ADD TASK</button>
            </div>

            <ul id="list-container">
                <!-- <li class="checked">Task 1</li>
                <li>Task 2</li>
                <li>Task 3</li> -->
            </ul>
        </div>
    </div>
    <script src="TODOLIST.JS"></script>
</body>
</html>

##CONTINUATION --------------------------> CSS
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}


.container {
    width: 100%;
    min-height: 100vh;
    /* background: linear-gradient(to top, #cfd9df 0%, #e2ebf0 100%); */
    padding: 10px;
}


.todo-app{
    width: 100%;
    max-width: 540px;
    background: #fff;
    margin:150px auto 20px;
    padding: 40px 30px 70px;
    border-radius: 50px;
    /* box-shadow: 0px 0px 50px #afafaf; */
    box-shadow: 0px 0px 30px #afafaf;

    /* box-shadow: 0 0 5px 30px #d6d6d6; */
}

h2{
    color:#002765;
    display: flex;
    align-items: center;
    margin-bottom: 50px;
    font-size: 30px;
    position: relative;
}

.todo-app h2 img{
    position: absolute;
    right: 0;
    width: 40px;
    margin-left: 20px;
}

.row{
    display: flex;
    align-items: center;
    justify-content: space-between;
    /* background: #edeef0; */
    background: #fff;
    border: none;
    outline: 3px groove #000;
    outline-offset: 5px;
    border-radius: 30px;
    padding-left: 20px;
    margin-bottom: 25px;
    box-shadow: 0px 0px 10px #5d5d5d;
}

.row input{
    flex: 1; /*text full availabe width*/
    border:none ;
    outline: none;
    padding: 10px;
    background: transparent;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 1px;
}
.row input::placeholder{
    color: #1e008d;
}

.row button{
    border: none;
    outline: none;
    padding: 16px 30px;
    /* background:linear-gradient(45deg,#161823,#16386a) ; */
    background:coral;
    color: #fff;
    font-size: 18px;
    font-weight: 600;
    cursor: pointer;
    border-radius: 30px;
    margin: 1px;
}

ul li{
    list-style: none;
    font-size: 18px;
    font-weight: 500;
    letter-spacing: 1px;
    padding: 12px 8px 12px 50px;
    user-select: none;
    cursor: pointer;
    position: relative;
    margin-block: 10px;
}

ul li::before{
    content: '';
    position: absolute;
    height: 30px;
    width: 30px;
    border-radius: 50%;
    background: url(images/unchecked.png);
    background-size: cover;
    background-position: center;
    top:12px;
    left: 8px;
}

ul li.checked{
    background:darkorange;
    color: #fff;
    border-radius: 50px;
}

ul li.checked::before{
    background: url(images/checked.png);
    background-size: cover;
}

ul li span{
    position: absolute;
    top: 10px;
    margin-right: 5px;
    width: 30px;
    height: 30px;
    font-size: 22px;
    color: #000;
    line-height: 30px;
    text-align: center;
    border-radius: 50%;
}

ul li.checked span{
    color: #ffffff;
}

ul li.checked span:hover{
    background: #fff;
    color: #000;
}

ul li span:hover{
    background: #000;
    color: #fff;
}

    #JAVASCRIPT (TO-DO LIST)
let listContainer = document.getElementById('list-container')
let head = document.querySelector('head')
let inputBox = document.getElementById('input-box')


function addTask(){
    if(inputBox.value == ''){
        alert('Please Enter the Text')
    }
    else{
        const task = document.createElement('li')
        task.textContent = inputBox.value;
        listContainer.appendChild(task)
        // inputBox.value = ''
        let span = document.createElement('span')
        span.textContent = "\u00d7"
        task.appendChild(span)
        span.style.right = '0px';
    }
    inputBox.value = '';
    saveData()
}

listContainer.addEventListener('click', (e)=>{
    if(e.target.tagName === 'LI'){
        e.target.classList.toggle("checked")
        saveData()
    }
    else if(e.target.tagName === 'SPAN'){
        e.target.parentElement.remove()
        saveData()
    }
})

function saveData(){
    localStorage.setItem("data",listContainer.innerHTML)
}

function showTask(){
    listContainer.innerHTML = localStorage.getItem("data");
}

showTask()
