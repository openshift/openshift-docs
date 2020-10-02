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

// sets the current version in the drop down and sets up suggest an edit options
function selectVersion(currentVersion) {

  // currentVersion = "3.11"; // for testing

  // set the version selector to what the current version is
  var el = document.getElementById("version-selector");
  if(el) {
    el.value = currentVersion;
  }

  // the rest creates an suggest an edit element for h1 and h2 elements

  // only enabled at the moment on the 3.11 docs
  if(currentVersion != "3.11") return;

  var is3 = (currentVersion.charAt(0) == 3);
  var is4 = (currentVersion.charAt(0) == 4);

  // in version 4 and version 3 books are put together differently. In 3,
  // the WYSIWYG (mostly) and there are not many includes. In 4, everything
  // (mostly) is an include and the wrapper is just an assembly.

  // in version 3, there are generally no modules, and the page you are on, is
  // the page you will edit, so the logic is a bit different.

  // there is always just one h1 whether you are on version 4 or 3.
  // In 4, this is the main assembly, in 3, this is the file to edit.
  // in version 4 it assumes that the h2 section's id is correctly named as per the file that it resides in. This is the convention.

  // we start with adding suggest an edit to the main assembly/file
  var h1s = document.getElementsByTagName('h1');
  var h1 = h1s[0]; // there is only one ever

  // main file to edit is the file path after the version to the html at
  // the end.
  // Example: https://docs.openshift.com/container-platform/4.4/updating/updating-cluster-between-minor.html
  // file path is updating/updating-cluster-between-minor.adoc

  mainFileToEdit =
    window.location.pathname.substring(
      window.location.pathname.lastIndexOf(currentVersion) +
      currentVersion.length, window.location.pathname.length - 4);

  // rest api is put together automatically, so ignore
  if(mainFileToEdit.includes("rest_api")) return;

  var fn = mainFileToEdit + "adoc"; // add adoc to file name

  var message = "message=[Suggested Edit] for " + fn + "' target='_new' id='" + fn + "' style='font-size: x-small; display: inline; visibility: hidden'>Suggest an edit</a>";

  // in 4, edit the file in master, so it can cped to the right places. In 3,
  // edit in the branch
  h1.innerHTML += "&nbsp;<a href='https://github.com/openshift/openshift-docs/edit/" + (is4? "master" : ("enterprise-" + currentVersion)) + "/" + fn + "?" + message;

  // add mouseover and out to the h1 tag to show or hide the link
  // unlike the links added to h2, here it is at [0], the only 'a' tag
  // added
  h1.addEventListener("mouseover", function() {
   this.getElementsByTagName('a')[0].style.visibility = "visible";
  });

  h1.addEventListener("mouseout", function() {
   this.getElementsByTagName('a')[0].style.visibility = "hidden";
  });

  if(is4) { // in version 4 also allow to edit subsections which are modules

    // all h2 elements map to modules
    var h2s = document.getElementsByTagName('h2');

    var i;
    for (i = 0; i < h2s.length; i++) {

      var h2 = h2s[i];
      var splitFile = h2.id.split("_", 1)[0]; // file ids are of the format: filename_context
      if(splitFile === h2.id) { continue; } // nothing was found, don't create an edit file link

      // this overwrites the global fn for h1 from earlier
      var fn = splitFile + ".adoc"; // add adoc to file name

      // we are going to allow the PR to open against the master branch
      h2.innerHTML += "&nbsp;<a href='https://github.com/openshift/openshift-docs/edit/master/modules/" + fn + "?" + "message=[Suggested Edit] for " + fn + "' target='_new' id='" + fn + "' style='font-size: x-small; display: inline; visibility: hidden'>Suggest an edit</a>";

      // add mouseover and out to the h2 tag to show or hide the link
      // in 4, the h2 also has an 'a' tag already, so the tag we are looking for
      // here is the second one ([1] and not [0])
      h2.addEventListener("mouseover", function() {
        this.getElementsByTagName('a')[1].style.visibility = "visible";
      });

      h2.addEventListener("mouseout", function() {
        this.getElementsByTagName('a')[1].style.visibility = "hidden";
      });
    }
  }
}
