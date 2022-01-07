const fs = require('fs');

function checkAndShow(res, fileName) {
    let retStr = "";
    const stats = fs.lstatSync(fileName);
    if (stats.isFile()) {
        retStr += fileName + " is a file. Content:";
        const data = fs.readFileSync(fileName, {encoding: 'utf8', flag: 'r'});
        retStr += data;
        res.write(retStr);
        res.end();
    } else if (stats.isDirectory()) {
        retStr += fileName + " is a directory";
        res.write(retStr);
        res.end();
    }
}

module.exports.checkAndShow = checkAndShow;