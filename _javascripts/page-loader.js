function versionSelector(list) {

  // the version we want
  newVersion = list[list.selectedIndex].value;

  //decimal places in version
  decimalPlaces = list.toString().split(".")[1].length

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
  //count decimal places to diffrentiate between 3.10 and 3.1
  if( (newVersion == 3.10 && decimalPlaces == 2)|| newVersion >= 3.3) {
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

  //decimal places in version
  decimalPlaces = currentVersion.toString().split(".")[1].length

  //hrefLink to load
  hrefLink = "";

  if( (currentVersion == 3.10 && decimalPlaces == 2)|| currentVersion >= 3.3) {
    hrefLink = "https://docs.openshift.com/container-platform/" +
    currentVersion + "/welcome/index.html";
  } else {
    hrefLink = "https://docs.openshift.com/enterprise/" +
    currentVersion + "/welcome/index.html";
  }

  // update the welcome page URL
  document.getElementById("welcome-page-link").href = hrefLink;
}
