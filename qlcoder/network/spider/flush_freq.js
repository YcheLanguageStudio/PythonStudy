const request = require('request');
const arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
var url = 'http://www.qlcoder.com/train/spider3/';
var i = 0;
var txt = [];

function getContent(url) {
  var promise = new Promise(function(resolve, resject) {
    request(url, function(err, res, body) {
      txt[url] = body;
      resolve(url);
    })
  })
  return promise;
}

function check(url) {
  setTimeout(function() {
    //console.log(url)
    request(url, (err, res, body) => {
      if (txt[url] == body) {
        check(url);
      } else {
        console.log(url);
      }
    })
  }, 3000)
}

for (; i < arr.length; i++) {
  getContent(url + arr[i]).then(function(url) {
    check(url);
  })
}
