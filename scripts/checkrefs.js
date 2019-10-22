#!/usr/bin/env node

"use strict";

//to read the file line by line
var readl = require("readl-async");

//to read files referenced by external references
var fs = require("fs");

//to convert ../ and / and ./ to absolute paths
var path = require("path");

//to check whether an URL is reachable
var linkCheck = require("link-check");

//Difference function to compare internal references stored in arrays
function difference(a1, a2) {
  var result = [];
  for (let i = 0; i < a1.length; i++) {
    if (a2.indexOf(a1[i]) === -1) {
      result.push(a1[i]);
    }
  }
  return result;
}

//To check for only unique values
function uniq(a) {
  var prims = {
      boolean: {},
      number: {},
      string: {}
    },
    objs = [];
  return a.filter(function(item) {
    var type = typeof item;
    if (type in prims) {
      return prims[type].hasOwnProperty(item)
        ? false
        : (prims[type][item] = true);
    } else {
      return objs.indexOf(item) >= 0 ? false : objs.push(item);
    }
  });
}

(async () => {
  try {
    if (process.argv[2] != undefined) {
      const stat = await fs.lstatSync(process.argv[2]);
      if (stat.isFile()) {
        checkReferencesFromFile(process.argv[2]);
      } else if (stat.isDirectory()) {
        checkReferencesFromFolder(process.argv[2]);
      }
    } else console.log("Please provide a file or folder path to check!");
  } catch (err) {
    console.log("\x1b[31m%s\x1b[0m", err);
  }
})();

var httpStatusCodes = "200,201";
var cfgHttpStatusCodes = httpStatusCodes.split(",");
for (let a in cfgHttpStatusCodes) {
  // convert to array of integer
  cfgHttpStatusCodes[a] = parseInt(cfgHttpStatusCodes[a], 10); // Explicitly include base
}

// check the specified file selected
function checkReferencesFromFile(filename) {
  checkReferences(filename, path.resolve(filename));
}

// check recursively for the specified folder
function checkReferencesFromFolder(folderPath) {
  //walk recursively through the folder and returns file list
  function walk(dir) {
    var results = [];
    var list = fs.readdirSync(dir);
    list.forEach(file => {
      file = dir + "/" + file;
      var stat = fs.statSync(file);
      if (stat && stat.isDirectory()) {
        /* Recurse into a subdirectory */
        results = results.concat(walk(file));
      } else {
        /* Is a file */
        var fileType = file.split(".").pop();
        if (fileType === "adoc") {
          results.push(file);
        }
      }
    });
    return results;
  }
  var fileList = walk(folderPath);
  var numberFiles = fileList.length;
  var fileListShort = "";
  fileList.forEach(file => {
    fileListShort += path.relative(folderPath, file) + ", ";
  });
  console.log("Checking: `" + fileListShort + "`");
  for (let i = 0; i < numberFiles; i++) {
    checkReferences(fileList[i], folderPath);
  }
}

// check the references contained in the file
// basePath is a shorter version of the filePath that will be used in log messages
function checkReferences(filePath, basePath) {
  // string identifying the current file in any log message
  // if a basePath is given, the file will be identified
  // relatively to this basePath
  var logMsgFilePath;
  if (basePath !== undefined) {
    logMsgFilePath = path.relative(path.parse(basePath).dir, filePath);
  } else {
    logMsgFilePath = path.parse(filePath).base;
  }

  //get directory of current file
  var folderPath = path.parse(filePath).dir;

  //to ignore everything if it is commented out
  var insideCommentBlock = false;

  //to hold anchors
  var anchorArray = [];

  //to hold internal references
  var internalRefs = [];

  //to hold references to external files
  var externalRefs = [];

  //to hold references to URLs
  var externalURLs = [];

  // add an anchor to the anchor array
  // raise an error if the anchor was already defined
  function registerAnchor(newAnchor) {
    if (anchorArray.includes(newAnchor)) {
      console.log(
        "\x1b[31m%s\x1b[0m",
        "- [ ] *" +
          logMsgFilePath +
          "*: Found duplicate anchors for `" +
          newAnchor +
          "`."
      );
    } else {
      anchorArray.push(newAnchor);
    }
  }

  //lets read file contents line by line
  var reader = new readl(filePath, {
    encoding: "utf8",
    emptyLines: "true"
  });

  //Emit this function when one line is read:
  reader.on("line", function(line, index, start, end) {
    //detect start and end of code blocks
    if (line.startsWith("////")) {
      insideCommentBlock = !insideCommentBlock;
    }

    //ignore everything inside comment blocks
    if (insideCommentBlock) {
      return;
    }

    //ignore single line comments
    if (line.startsWith("//")) {
      return;
    }

    //find if line contains an anchor with format [[anchor]] or [[anchor, description]]
    if (line.match(/\[\[[^\]]+\]\]/g)) {
      let extractLink = line.match(/\[\[[^\]]+\]\]/g);
      //console.log('LINE: '+ line);
      //console.log('EXTRACT LINK: '+ extractLink);
      for (let i = 0; i < extractLink.length; i++) {
        let newAnchor = extractLink[i];
        newAnchor = newAnchor.replace("[[", "");
        newAnchor = newAnchor.replace("]]", "");
        newAnchor = newAnchor.replace(/,.*/g, ""); // take into account ','

        registerAnchor(newAnchor);

        //console.log('NEW ANCHOR with [[...]]: ' + newAnchor);
      }
    }

    //find if line contains an anchor with format [[[anchor]]] or [[[anchor, something]]]
    //this type of format of used for bibliography
    if (line.match(/^[\s]*[\*\-][\s]+\[\[\[[^\]]+\]\]\]/g)) {
      let extractLink = line.match(/\[\[\[[^\]]+\]\]\]/g);
      //console.log('LINE: '+ line);
      //console.log('EXTRACT LINK: '+ extractLink);
      for (let i = 0; i < extractLink.length; i++) {
        let newAnchor = extractLink[i];
        newAnchor = newAnchor.replace("[[[", "");
        newAnchor = newAnchor.replace("]]]", "");
        newAnchor = newAnchor.replace(/,.*/g, ""); // take into account ','

        registerAnchor(newAnchor);

        //console.log('NEW ANCHOR with [[[...]]]: ' + newAnchor);
      }
    }

    //find if line contains anchor with format [#anchorname] (Inline anchors)
    if (line.match(/\[#[^\]]+\]/g)) {
      let extractLink = line.match(/\[#[^\]]+\]/g);
      for (let i = 0; i < extractLink.length; i++) {
        let newAnchor = extractLink[i];
        newAnchor = newAnchor.replace("[#", "");
        newAnchor = newAnchor.replace("]", "");

        registerAnchor(newAnchor);
      }
    }

    //find if line contains anchor with format anchor:anchorname[some text]
    if (line.match(/(anchor:)[^\[]+\[[^\]]*\]/g)) {
      let extractLink = line.match(/:[^\[]+\[/g);
      for (let i = 0; i < extractLink.length; i++) {
        let newAnchor = extractLink[i];
        newAnchor = newAnchor.replace(":", "");
        newAnchor = newAnchor.replace("[", "");

        registerAnchor(newAnchor);
      }
    }

    //find internal and external references
    //with format <<anchorname>> or <<anchorname, some text>>
    //or with format <<file.adoc, some text>> or <<file#anchorname, some text>>
    if (line.match(/<<[^\>]+>>/g)) {
      //console.log('LINE-----',line)
      let extractLink = line.match(/<<[^\>]+>>/g); //there may be more than one matching items
      for (let i = 0; i < extractLink.length; i++) {
        let newReference = extractLink[i];
        newReference = newReference.replace("<<", "");
        newReference = newReference.replace(">>", "");
        newReference = newReference.replace(/,.*/g, ""); // take into account <<anchor, some text>>

        //distinguish internal and external references
        if (newReference.match(/(\.adoc)|(#)/g)) {
          //add ".adoc" if it is missing
          newReference = newReference.replace(/(\.adoc)?#/, ".adoc#");

          externalRefs.push(path.resolve(folderPath, newReference));
        } else {
          internalRefs.push(newReference);
        }
      }
    }

    //find internal and external references with format xref:link[text]
    if (line.match(/xref:[^\[]+\[[^\]]*\]/g)) {
      //console.log('LINE: ' + line);
      let extractLink = line.match(/xref:[^\[]+\[/g);
      //console.log('extractLink: ' + extractLink)
      for (let i = 0; i < extractLink.length; i++) {
        let newReference = extractLink[i];
        newReference = newReference.replace("xref:", "");
        newReference = newReference.replace("[", "");

        //distinguish internal and external references
        if (newReference.match(/(\.adoc)|(#)/g)) {
          //add ".adoc" if it is missing
          newReference = newReference.replace(/(\.adoc)?#/, ".adoc#");

          externalRefs.push(path.resolve(folderPath, newReference));
        } else {
          internalRefs.push(newReference);
        }
      }
    }

    //find external references that use the link:URI[some description] syntax
    if (line.match(/link:[^\[]+\[[^\]]*\]/g)) {
      //console.log('LINE-----',line)
      let extractLink = line.match(/link:[^\[]+\[/g); //there may be more than one matching items
      for (let i = 0; i < extractLink.length; i++) {
        let newReference = extractLink[i];
        newReference = newReference.replace("link:", "");
        newReference = newReference.replace("[", "");

        //distinguish local files from URLs
        if (newReference.match(/^(http|https):\/\//g)) {
          if (
            !newReference.match(
              /(example\.(?:com|org|test)|http:\/\/localhost|https:\/\/localhost|my\.proxy|http(?:s|):\/\/\$|http(?:s|):\/\/\%|location_of_rpm_server|\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|someaccount\.|\*\.|mycorp|mydev|youruser|yourrepo|starter-us-east-1|api\.openshift\.com|index\.docker\.io)/
            )
          )
            externalURLs.push(newReference);
        } else if (newReference.match(/^(ftp|irc|mailto):\/\//g)) {
          // we currently don't handle these
        } else {
          //assuming it is a local file
          //in case of html, drop the part after #, we won't check it
          newReference = newReference.replace(/(\.html?5?)#.*/, "$1");
          externalRefs.push(path.resolve(folderPath, newReference));
        }
      }
    }

    //find URLs that don't use the "link:" macro (e.g. "http://www.google.com")
    //this regex is derived from: https://github.com/asciidoctor/atom-language-asciidoc/blob/master/grammars/repositories/inlines/link-macro-grammar.cson
    if (
      line.match(
        /(?:^|<|[\s>\(\)\[\];])((https?|file|ftp|irc):\/\/[^\s\[\]<]*[^\s.,\[\]<\)])/g
      )
    ) {
      //console.log('LINE-----',line)
      let extractLink = line.match(
        /((https?|file|ftp|irc):\/\/[^\s\[\]<]*[^\s.,\[\]<\)])/g
      ); //there may be more than one matching items
      for (let i = 0; i < extractLink.length; i++) {
        let newReference = extractLink[i];
        //console.log('URL without link: macro: ', newReference);
        if (
          !newReference.match(
            /(example\.(?:com|org|test)|http:\/\/localhost|https:\/\/localhost|my\.proxy|http(?:s|):\/\/\$|http(?:s|):\/\/\%|location_of_rpm_server|\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|someaccount\.|\*\.|mycorp|mydev|youruser|yourrepo|starter-us-east-1|api\.openshift\.com|index\.docker\.io)/
          )
        )
          externalURLs.push(newReference);
        //console.log("PUSHED: " + newReference)
      }
    }
  });

  //Emit this function when the file is fully read
  reader.on("end", () => {
    //console.log(externalURLs)
    // returns a promise that resolves to true if the
    // external reference exists, and to false otherwise
    function checkExternalRef(item) {
      var itemOk = true;

      //console.log('ITEM: ', item);
      return new Promise((resolve, reject) => {
        process.nextTick(() => {
          var currentLink = item.split("#");
          var targetFilePath = currentLink[0];
          var targetAnchor = currentLink[1];

          // if there is NO ref to an anchor, just check file exists
          if (!targetAnchor || targetAnchor.length === 0) {
            //console.log(item);
            if (!fs.existsSync(targetFilePath)) {
              itemOk = false;
              var errorLine =
                "- [ ] *" +
                logMsgFilePath +
                "*: Cannot find referenced file: `" +
                targetFilePath +
                "`";
              console.log("\x1b[31m%s\x1b[0m", errorLine);
            }
          } else {
            // try to find the anchor in the target file
            try {
              var data = fs.readFileSync(targetFilePath, "utf8");
              if (data.indexOf("[[" + targetAnchor + "]]") >= 0) {
                //all good
                //do nothing
                //console.log('LINK FINE: ' + targetAnchor);
              } else {
                // console.log(
                //   '----------------------ERROR-----------------------'
                // );
                // console.log(
                //   'Cannot find anchor!' +
                //     targetAnchor +
                //     ' in file ' +
                //     item
                // );
                itemOk = false;
                console.log(
                  "\x1b[31m%s\x1b[0m",
                  "- [ ] *" +
                    logMsgFilePath +
                    "* : Cannot find anchor: `" +
                    targetAnchor +
                    "` in `" +
                    targetFilePath +
                    "`"
                );
              }
            } catch (err) {
              //console.log('ERROR READING FILE', err);
              itemOk = false;
              console.log(
                "\x1b[31m%s\x1b[0m",
                "- [ ] *" +
                  logMsgFilePath +
                  "*: Cannot find referenced file: `" +
                  targetFilePath +
                  "`"
              );
            }
          }

          resolve(itemOk);
        });
      });
    }

    // returns a promise that resolves to true if the
    // URL exists, and to false otherwise
    function checkExternalURL(item) {
      //console.log('ITEM: ', item);
      return new Promise((resolve, reject) => {
        process.nextTick(() => {
          let opts = {
            aliveStatusCodes: cfgHttpStatusCodes
          };

          linkCheck(item, opts, function(err, result) {
            if (result.status === "alive") {
              resolve(true);
            } else {
              console.log(
                "\x1b[31m%s\x1b[0m",
                "- [ ] *" +
                  logMsgFilePath +
                  "*: Cannot reach URL (status code `" +
                  result.statusCode +
                  "`): `" +
                  item +
                  "`"
              );
              resolve(false);
            }
          });
        });
      });
    }

    //check all internal references
    var notFoundInternal = difference(internalRefs, anchorArray);
    if (internalRefs[0] == null) {
      //console.log("`" + logMsgFilePath + "`: No internal reference found.");
    } else if (notFoundInternal[0] == null) {
      /* console.log(
        "`" + logMsgFilePath + "`: All internal references are `OK`."
      ); */
    } else {
      notFoundInternal.forEach(function(it) {
        //console.log('Cannot find the anchor: ' + it + ' in current file.');
        console.log(
          "\x1b[31m%s\x1b[0m",
          "- [ ] *" + logMsgFilePath + "*: Cannot find anchor: `" + it + "`."
        );
      });
    }

    //check al external references
    if (externalRefs[0] == null) {
      //console.log("`" + logMsgFilePath + "`: No external reference found.");
    } else {
      //get uniques so that we only check them once
      externalRefs = uniq(externalRefs);
      Promise.all(externalRefs.map(checkExternalRef)).then(returnCodes => {
        /* if (!returnCodes.includes(false)) {
          console.log(
            "`" + logMsgFilePath + "`: All external references are `OK`."
          );
        } */
      });
    }

    //check if all URLs are reachable
    //if (cfgCheckURL) {
    if (externalURLs[0] == null) {
      //console.log("`" + logMsgFilePath + "`: No URLs found.");
    } else {
      //get uniques so that we only check them once
      externalURLs = uniq(externalURLs);
      Promise.all(externalURLs.map(checkExternalURL)).then(returnCodes => {
        if (!returnCodes.includes(false)) {
          //console.log("`" + logMsgFilePath + "`: All URLs are reachable.");
        }
      });
    }
    //}
  });

  //Emit this function when an error occurs
  reader.on("error", function(error) {
    //Do some stuff with the error
    // ....
  });

  //Start reading the file
  reader.read();
}
