function versionSelector(list) {

  // the version we want
  newVersion = list[list.selectedIndex].value;

  // the new final link to load
  newLink = "";

  // spilt the current path
  var pathArray = window.location.pathname.split( '/' );

  // so we can get the current version
  currentVersion = pathArray[2];

  // the file path is just the version number + the end of the path
  var fileRequested =
    window.location.pathname.substring(
      window.location.pathname.lastIndexOf(currentVersion) +
      currentVersion.length);

  // alert(fileRequested);

  // in 3.3 and above, we changed to container-platform
  if(newVersion == 3.10 || newVersion >= 3.3) {
    newLink = "https://docs.openshift.com/container-platform/" +
      newVersion +
      fileRequested;
  } else {
    newLink = "https://docs.openshift.com/enterprise/" +
      newVersion +
      fileRequested;
  }

  // without doing async loads, there is no way to know if the path actually
  // exists - so we will just have to load
  window.location = newLink;

}

function selectVersion(currentVersion) {
  document.getElementById("version-selector").value = currentVersion;
  // alert(currentVersion);
}
