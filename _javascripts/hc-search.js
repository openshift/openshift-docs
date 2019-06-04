function hcSearchCategory(label, version) {
// optional version filters search results for a single specific product version
// currently can be used with OCP and Origin only

  var modalSearch = document.getElementById("hc-search-modal");
  var searchBtn = document.getElementById("hc-search-btn");
  var closeModal = document.getElementById("hc-modal-close");
  var searchResults = document.getElementById("hc-search-results");
  var query = document.getElementById("hc-search-input");

  // pressing enter in the input = search btn click
  query.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode == 13) {
        searchBtn.click();
    }
  });

  //prepare iframe (without source)
  var iframe = document.createElement("iframe");
  iframe.frameBorder=0;
  iframe.width="100%";
  iframe.height=0.7*window.innerHeight;
  iframe.id="search-result-iframe";

  // open the modal and finalize the iframe on click
  searchBtn.onclick = function() {
    if (query.value) {
  	modalSearch.style.display = "block";
    // limit search to a signle version, if specified
    var urlFilter = (typeof version === "undefined" || version == "Branch Build") ? "" : (" url:*\\/" + version + "\\/*");
    var iframeSrc = "https://help.openshift.com/customsearch.html?q=" +
                    encodeURIComponent(query.value) +
                    encodeURIComponent(urlFilter) +
                    "&l=" + encodeURIComponent(label);
  	iframe.setAttribute("src", iframeSrc);
          searchResults.appendChild(iframe);
    }
  }

  // hide search modal
  closeModal.onclick = function() {
    modalSearch.style.display = "none";
  }

  window.onclick = function(event) {
    if (event.target == modalSearch) {
      modalSearch.style.display = "none";
    }
  }
}  // hcSearchCategory(label)
