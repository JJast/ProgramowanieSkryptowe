const fs = require('fs');

function checkAndShow(fileName) {
    let retStr = "";
    const stats = fs.lstatSync(fileName);
    if (stats.isFile()) {
        retStr += fileName + " is a file. Content:";
        const data = fs.readFileSync(fileName, {encoding: 'utf8', flag: 'r'});
        retStr += data;
    } else if (stats.isDirectory()) {
        retStr += fileName + " is a directory";
    }
    return retStr;
}

module.exports.checkAndShow = checkAndShow;
