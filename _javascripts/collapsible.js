const collapsibleButtonHTML = "<div id='collapsibleButtonDiv'><button type='button' name='button-collapse-expand-all' id='button-collapse-expand-all' aria-labelledby='label-collapse-expand-all' class='fa fa-angle-double-up button-collapse-expand' onclick='collapseExpandAll()'></button><span role='tooltip' id='label-collapse-expand-all' class='span-collapse-expand-all' onclick='collapseExpandAll()'>Collapse all</span></div>";

const collapsibleDetails = document.getElementsByTagName("details");

for (var i=0; i < collapsibleDetails.length; i++) {
  collapsibleDetails[i].insertAdjacentHTML('beforebegin', collapsibleButtonHTML);
}

function collapseExpandAll() {
  const collapseExpandButtons = document.getElementsByClassName("button-collapse-expand");
  const collapsibleTooltip = document.getElementsByClassName("span-collapse-expand-all");

  if (collapsibleTooltip[0].innerHTML == "Collapse all") {
    for (var i=0; i < collapsibleDetails.length; i++) {
        collapsibleDetails[i].removeAttribute("open");
    }
    for (var j=0; j < collapsibleTooltip.length; j++) {
      collapsibleTooltip[j].innerHTML = "Expand all";
    }
    for (var k=0; k < collapseExpandButtons.length; k++) {
      collapseExpandButtons[k].classList.remove("fa-angle-double-up");
      collapseExpandButtons[k].classList.add("fa-angle-double-down");
    }
  } else {
    for (var i=0; i < collapsibleDetails.length; i++) {
        collapsibleDetails[i].setAttribute("open", "");
    }
    for (var j=0; j < collapsibleTooltip.length; j++) {
        collapsibleTooltip[j].innerHTML = "Collapse all";
    }
    for (var k=0; k < collapseExpandButtons.length; k++) {
      collapseExpandButtons[k].classList.remove("fa-angle-double-down");
      collapseExpandButtons[k].classList.add("fa-angle-double-up");
    }
  }
}
