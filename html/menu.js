function Nav() {
  const sideBarWidth = document.getElementById("mySidebar").style.width;

  if (!sideBarWidth || sideBarWidth == "0px"){
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.querySelector("body").style.background = "rgba(0, 0, 0, 0.2)";
    document.querySelector(".container").style = "filter: blur(5px)";
    document.querySelector(".container").style = "-webkit-filter: blur(5px)";
  }
  else if (sideBarWidth !== "0px"){
    document.getElementById("mySidebar").style.width = "0px";
    document.getElementById("main").style.marginLeft = "0px";
    document.querySelector("body").style.background = "none";
    document.querySelector(".container").style = "filter: blur(0px)";
    document.querySelector(".container").style = "-webkit-filter: none";
  }
}