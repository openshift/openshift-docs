// This file runs the Clipboard.js functionality
document.querySelectorAll('div.listingblock, div.literalblock').forEach((codeblock, index) => {
  codeblock.getElementsByTagName('pre')[0].insertAdjacentHTML("beforebegin", "<p class='clipboard-button-container'><span class='clipboard-button fa fa-clipboard'></span></p>");
  document.getElementsByTagName('pre')[index].setAttribute('id',`clipboard-${index}`);
});

document.querySelectorAll('span.clipboard-button').forEach((copybutton, index) => {
  copybutton.setAttribute('data-clipboard-target',`#clipboard-${index}`);
});

var clipboard = new ClipboardJS('.clipboard-button', {
    text: function(target) {
      const targetId = target.getAttribute('data-clipboard-target').substr(1);
      let clipboardText;
      clipboardText = document.getElementById(targetId).innerText.replace(/\$[ ]/g, "");

      if (clipboardText.slice(0,2) === "# ") {
        clipboardText = clipboardText.substr(2);
      }

      if (clipboardText.slice(0,5) === "sh-4.") {
        clipboardText = clipboardText.substr(8);
      }

      if (clipboardText.split(/\r\n|\n|\r/)[0].endsWith("\\ ") | clipboardText.split(/\r\n|\n|\r/)[0].endsWith("\\")) {
        clipboardText = clipboardText.replace(/(\\[ ]\r\n|\\[ ]\n|\\[ ]\r|\\\r\n|\\\n|\\\r)/g,"").replace(/(\s+|\t)/g," ");
      }

      return clipboardText;
    }
});

clipboard.on("success", function (e) {
  const triggerId = e.trigger.getAttribute("data-clipboard-target").substr(1);
  const triggerNode = document.getElementById(triggerId);

  const selection = window.getSelection();
  selection.removeAllRanges();

  const range = document.createRange();
  range.selectNodeContents(triggerNode);
  selection.addRange(range);

  e.trigger.classList.toggle("fa-clipboard");
  e.trigger.classList.toggle("fa-check");

  setTimeout(function () {
    e.clearSelection();
    e.trigger.classList.toggle("fa-clipboard");
    e.trigger.classList.toggle("fa-check");
  }, 2000);
});
