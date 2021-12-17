document.addEventListener("DOMContentLoaded", ()=> {
  
  document.body.style.background = "black";
  let btns = []      
  let tiles = []
  let tileContainer;
  let cubeColors = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


  //Creates buttons for this small project
  function createBtns(){
    for (var i = 0; i < 4; i++) {
      var btn = document.createElement("button")
      btn.addEventListener("click", (e)=>{
        //Modify list with value from button clicked and save it to localstorage
        //-1 -> None
        //0  -> Yellow
        //1  -> Blue
        //2  -> Red
        //3  -> Green
        cubeColors.pop()
        switch(e.currentTarget.style.background){
          case "yellow":
            cubeColors.unshift(0);
            break;
          case "blue":
            cubeColors.unshift(1);
            break;
          case "red":
            cubeColors.unshift(2);
            break;
          case "green":
            cubeColors.unshift(3);
            break;
          default:
            cubeColors.unshift(-1);
        }
        console.log("halo?", cubeColors);
        paintTiles();
        localStorage.setItem("cubesColors", cubeColors.join(' '))
      }, false);
      btns.push(btn)
    }

    btns[1].style.bottom = "0";
    btns[2].style.right = "0";
    btns[3].style.right = "0";
    btns[3].style.bottom = "0";

    btns[0].style.background = "yellow";
    btns[1].style.background = "blue";
    btns[2].style.background = "red";
    btns[3].style.background = "green";

    for (let i = 0; i < 4; i++) {
      document.body.appendChild(btns[i]);
    }
  }

  //Iterates through tiles list and updates background accordingly 
  function paintTiles(){
    for (var i = 0; i < tiles.length; i++){
      switch(cubeColors[i]) {
        case 0:
          tiles[i].style.background = "yellow";
          break;
        case 1:
          tiles[i].style.background = "blue";
          break;
        case 2:
          tiles[i].style.background = "red";
          break;
        case 3:
          tiles[i].style.background = "green";
          break;
        default:
          tiles[i].style.background = "grey";
      }
    }
  }

  //Creates tiles for this small project
  function createTiles(){
    tileContainer = document.createElement("div")
    tileContainer.classList.add("tileContainer")
    for (var i = 0; i < 10; i++) {
      var tile = document.createElement("div")
      tile.classList.add("tile");
      tiles.push(tile)
      tileContainer.appendChild(tiles[i]);
    }
    document.body.appendChild(tileContainer);
  }

  //Checks to see it tile colors already exists
  function checkLocalStorage(){
    if (localStorage.getItem("cubesColors") !== null) {
      cubeColors = localStorage.getItem("cubesColors").split(' ').map(Number);
    }
  }

  checkLocalStorage()
  createBtns()
  createTiles()
  paintTiles()
});