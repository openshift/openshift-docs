// the new final link to load
newLink = "";
newVersion = "";
currentVersion = "";

// the fileRequested
fileRequested = "";

function versionSelector(list) {

  // the version we want
  newVersion = list[list.selectedIndex].value;

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
  // window.location = newLink;
  // testing async validations
  $.ajax({
    type: 'HEAD',
    url: newLink,
    success: function() {
      window.location = newLink;
    },
    error: function(jqXHR, exception) {
      if(jqXHR.status == 404) {
        list.value = currentVersion;
        if(confirm("This page doesn't exist in version " + newVersion + ". Click OK to search the " + newVersion + " docs OR Cancel to stay on this page.")) {
          window.location = "https://google.com/search?q=site:https://docs.openshift.com/container-platform/" + newVersion + " " + document.title;
        } else {
          // do nothing, user doesn't want to search
        }
      } else {
        window.location = newLink; // assumption here is that we can follow through with a redirect
      }
    }
  });

}

// checks what language was selected and then sends the user to the portal for their localized version
function selectLang(langList) {

  var lang = langList[langList.selectedIndex].value;
  var winPath = window.location.pathname;

  console.log("Lang: " + lang);
  console.log("Win Path: " + winPath);

  var currentVersion = document.getElementById("version-selector").value;
  console.log("CurrentVersion: " + currentVersion);

  // path for the file to reference on portal (the last bit removes .html)
  var path = winPath.substring(winPath.lastIndexOf(currentVersion) +   (currentVersion.length + 1), winPath.length - 5);

  var parts = path.split("/");

  console.log(parts);

  // map things to html-single. While plain HTML is preferred, it is harder to map and get all anchors right. html-single ensures there is no 404 and the user at least lands on the right book
  console.log(parts[parts.length-1]);

  var anchorid = parts[parts.length-1];
  var book = parts[0];

  // add changed book names here
  if(book == "updating") book = "updating_clusters";
  if(book == "virt") book = "openshift_virtualization";
  if(book == "post_installation_configuration") book = "post-installation_configuration";

  // var section = parts[1].replace(/\_/g, "-"); // replace underscore with dash
  // var section = subGroup.toLowerCase().replace(" ", "-");
  // console.log(section);
  // var subsection = parts[2].replace(/\_/g, "-");
  // console.log(subsection);

  // path = book + "/" + section + "#" + subsection;
  path = book + "#" + anchorid;

  console.log("Path: " + path);

  var portalBaseURL = "https://access.redhat.com/documentation";
  var finalURL = portalBaseURL + "/" + lang + "/openshift_container_platform/" + currentVersion + "/html-single/" + path;

  console.log("Final URL: " + finalURL);
  window.location.href = finalURL;

}

// sets the current version in the drop down and sets up suggest an edit options
function selectVersion(currentVersion) {

  // currentVersion = "3.11"; // for testing

  // set the version selector to what the current version is
  var el = document.getElementById("version-selector");
  if(el) {
    el.value = currentVersion;
  }

  // check the docs referrer to add warning box based on whether we are coming from rosa docs or elsewhere
  addReferrer();

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
  // Example: https://docs.openshift.com/container-platform/4.4/updating/updating-cluster-within-minor.html
  // file path is updating/updating-cluster-within-minor.adoc

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

function addReferrer() {

  // grab target element reference

  // we want to add a notice to the top of the OCP docs page if the reader is coming from ROSA docs

  // check the referrer
  // alert(document.referrer);

  // var ref = "http://127.0.0.1/addreferrer";
  // var ref = "http://127.0.0.1/addreferrer/authentication/understanding-authentication.html";

  var ref = "https://docs.openshift.com/rosa";

  if(document.referrer && document.referrer.startsWith(ref) && !document.location.href.startsWith(ref)) {

    // get the first section/header
    var elements = document.getElementsByClassName('sect1');
    var requiredElement = elements[0];

    // the warning text
    var text = '<div class="admonitionblock important"><table><tbody><tr><td class="icon"><i class="fa icon-important" title="Important"></i></td><td class="content"><div class="paragraph"><p>This is the <b>OpenShift Container Platform</b> documentation. There may be some sections that don\'t apply to ROSA docs.</p><p>Click <a href="' + document.referrer + '">here</a> to go back to the page you came from or browse the full <a href="https://docs.openshift.com/rosa/welcome/index.html">ROSA documentation</a>.</p></div></td></tr></tbody></table></div>';

    // insert the element before target element
    requiredElement.insertAdjacentHTML("beforebegin", text);
  }


}
