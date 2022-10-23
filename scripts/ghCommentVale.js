#!/usr/bin/env node

'use strict';

const fs = require('fs');

var gitDiff = JSON.parse(fs.readFileSync('difflines.json', 'utf8'));
var valeErrors = JSON.parse(fs.readFileSync('valeerrors.json', 'utf8'));

for (const [key, value] of Object.entries(valeErrors)) {
    for (var i = 0, len = gitDiff.length; i < len; i++){
        //console.log("DIFF: ", gitDiff[i].file)
        if (gitDiff[i].file == "/"+key){
            //console.log("MATCHED: ", gitDiff[i].file);
            //console.log("----BREAK----")
            for (var x = 0, linesLength = gitDiff[i].lines.length; x < linesLength; x++){
                //console.log("LINES: ", gitDiff[i].lines[x])
                for (var n=0, lengthErrors = value.length; n < lengthErrors; n++){
                    var low = parseInt(gitDiff[i].lines[x].start)
                    var high = parseInt(gitDiff[i].lines[x].end)

                    if (parseInt(value[n].Line) >= low && parseInt(value[n].Line) <= high){
                        //console.log("Modified line " + value[n].Line + " is in errors.")
                        console.log("FILE: ", key)
                        console.log("LINE: ", value[n].Line)
                        console.log("ERROR: ", value[n].Check + " " + value[n].Message )
                    }
                }
            }
            break;
        } else {
            //console.log("Running for: ", key)
        }
    }
}