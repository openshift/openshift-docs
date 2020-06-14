function versionSelector(list) {

  // the version we want
  newVersion = list[list.selectedIndex].value;

  // the new final link to load
  newLink = "";

  // the fileRequested
  var fileRequested = "";

  // spilt the current path
  var pathArray = window.location.pathname.split( '/' );

  // so we can get the current version
  currentVersion = pathArray[2];

  // if switching major versions, just take the user to the main landing page
  // as files change a lot between major versions.

  if(currentVersion.charAt(0) === newVersion.charAt(0)) {
    // the file path is just the version number + the end of the path
    fileRequested =
      window.location.pathname.substring(
        window.location.pathname.lastIndexOf(currentVersion) +
        currentVersion.length);
  } else {
    fileRequested = "/welcome/index.html";
  }


  // alert(fileRequested);

  // in 3.3 and above, we changed to container-platform
  if(newVersion == '3.0' || newVersion == '3.1' || newVersion == '3.2') {
    newLink = "https://docs.openshift.com/enterprise/" +
      newVersion +
      fileRequested;
  } else {
    newLink = "https://docs.openshift.com/container-platform/" +
      newVersion +
      fileRequested;
  }

  // without doing async loads, there is no way to know if the path actually
  // exists - so we will just have to load
  window.location = newLink;

}

function selectVersion(currentVersion) {
  var el = document.getElementById("version-selector");
  if(el) {
    el.value = currentVersion;
  }

  // alert(currentVersion);

  // in enterprise branch 4, allow users to directly edit the file on GH (users with edit rights on the repo, others open the PR)
  // this assumes that the h2 section's id is correctly named as per the file that it resides in. This is the convention.
  currentVersion = "4"; // for testing

  if(currentVersion.charAt(0) === "4") {

    // all h2 elements map to modules
    var elements = document.getElementsByTagName('h2');
    var i;

    for (i = 0; i < elements.length; i++) {

      var element = elements[i];
      var splitFile = element.id.split("_", 1)[0]; // file ids are of the format: filename_context
      if(splitFile === element.id) { continue; } // nothing was found, don't create an edit file link

      var fn = splitFile + ".adoc"; // add adoc to file name

      element.innerHTML += "&nbsp;<a href='https://github.com/openshift/openshift-docs/edit/master/modules/" + fn + "?message=[Suggested Edit] for " + fn + "' target='_new' id='" + fn + "' style='font-size: x-small; display: inline; visibility: hidden'>Suggest an edit</a>";

      var newElement = document.getElementById(fn); // this is the id of the new edit link

      // console.log(newElement);

      // add mouseover and out to the h2 tag to show or hide the link
      element.addEventListener("mouseover", function() {
        this.getElementsByTagName('a')[1].style.visibility = "visible";
      });

      element.addEventListener("mouseout", function() {
        this.getElementsByTagName('a')[1].style.visibility = "hidden";
      });
    }
 }

//    Object.entries(element).map(( object ) => {
//      object[1].innerHTML += "&nbsp;&nbsp;<font size='-2'><a href=''>Edit this section</a></font>";
//      var fn = this.id.split("_", 1)[0] + ".adoc";
//      alert(fn);
//      object[1].addEventListener("dblclick", function() {
//         // alert(this.id);
//         // alert(this.id.split("_", 1)[0] + ".adoc");
//        var fn = this.id.split("_", 1)[0] + ".adoc";
// //       window.open("https://github.com/openshift/openshift-docs/edit/enterprise-" +
// //         currentVersion + "/modules/" + fn, "_new");
//         window.open("https://github.com/openshift/openshift-docs/edit/master/modules/" + fn, "_new");
//      });
//    });
//  }

}
