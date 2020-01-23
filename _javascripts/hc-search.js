function hcSearchCategory(label, version) {
// optional version filters search results for a single specific product version
// currently can be used with OCP and OKD docs only

  // elements used repeatedly:
  var modalSearch = $("#hc-search-modal");
  var searchBtn = $("#hc-search-btn");
  var closeModal = $("#hc-modal-close");
  var query = $("#hc-search-input");

  // pressing enter in the input = search btn click
  query.keyup( function(event) {
    event.preventDefault();
    if (event.keyCode == 13) {
        searchBtn.click();
    }
  });

  // open the modal and fetch the first set of results on click
  searchBtn.click(function() {
    if (query.val()) {
      // remove any results from previous searches
      $("#hc-search-results").empty();
      var searchParams = {
        si: 0,
        q: query.val(),
        label: label,
        urlFilter: (typeof version === "undefined" || version == "Branch Build") ? "" : (" url:*\\/" + version.toLowerCase() + "\\/*")
      };
      modalSearch.show();
      hcsearch(searchParams);
    }
  });

  // hide search modal by 'X' or by clicking outside of the modal
  closeModal.click(function() {
    modalSearch.hide();
  });
  $(window).click(function(event) {
    if ($(event.target).is(modalSearch)) {
      modalSearch.hide();
    }
  });
}  // hcSearchCategory(label, version)

// fetch search results
function hcsearch(searchParams) {
  // elements used repeatedly
  var hcMoreBtn = $("#hc-search-more-btn");
  var hcSearchIndicator = $("#hc-search-progress-indicator");
  var hcSearchResult = $("#hc-search-results");

  // the "searchprovider" is to return a JSON response in the expected format
  var searchprovider = "https://help.openshift.com/search/search_custom.php";
  var searchReq = { "q" : searchParams.q + searchParams.urlFilter,
                    "fields.label" : searchParams.label,
                    "start" : searchParams.si }

  hcMoreBtn.hide();
  hcSearchIndicator.show();
  $.get(searchprovider, searchReq).done(function (hcsearchresults) {
    // GET success
    if (hcsearchresults == "") {
      // success, but no response (response code mismatch)
      $("#hc-search-result").append("<p><strong>An error occured while retrieving search results. Please try again later.</strong></p>");
      hcSearchIndicator.hide();
    }
    if (!$.isEmptyObject(hcsearchresults.response.result)) { 
      // if there are any results
      $(hcsearchresults.response.result).each(function () {
        var row = '<div class="search-result-item"><a href="' + this.url +
          '" target="_blank">' + this.title + '</a>';
        row += '<p class="excerpt">' + this.content_description.replace(/\<br\>/g, ' ') + '</p></div>';
        hcSearchResult.append(row);
      });
      if (hcsearchresults.response.page_number < hcsearchresults.response.page_count) {
        // if there are more results beyond the retrieved ones
        // index of the first item on the next page (first item = 0, first page = 1)
        searchParams.si = hcsearchresults.response.page_number * hcsearchresults.response.page_size;
        // replace any existing click handler with one to fetch the next set of results
        hcMoreBtn.off('click');
        hcMoreBtn.click(function() {
          hcsearch(searchParams);
        });
        hcMoreBtn.show();
      } else {
        // no more results beyond the retrieved ones
        hcSearchResult.append("<p><strong>No more results.</strong></p>");
      }
    } else {
      if (searchParams.si > 0) {
          // no results reurned, but some already displayed
          hcSearchResult.append("<p><strong>No more results.</strong></p>");
      } else {
        // no results on initial search
        hcSearchResult.append("<p><strong>No results found. Try rewording your search.</strong></p>");
      }
    }
    hcSearchIndicator.hide();
  }).fail(function(response) {
    // GET error
    hcSearchResult.append("<p><strong>An error occured while retrieving search results. Please try again later.</strong></p>");
    hcSearchIndicator.hide();
  });
}  // function hcsearch()
