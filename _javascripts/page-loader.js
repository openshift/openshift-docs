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

  // in enterprise branch 4, we have modules and this is an attempt to load the
  // modules by double clicking on them.
  if(currentVersion.charAt(0) === "4") {
    var element = document.getElementsByTagName('h2');
    Object.entries(element).map(( object ) => {
      object[1].addEventListener("dblclick", function() {
        // alert(this.id);
        // alert(this.id.split("_", 1)[0] + ".adoc");
        var fn = this.id.split("_", 1)[0] + ".adoc";
        window.open("https://github.com/openshift/openshift-docs/tree/enterprise-" +
          currentVersion + "/modules/" + fn, "_new");
      });
    });
  }

}
