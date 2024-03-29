#!/usr/bin/node

const myArray = process.argv.slice(2);
const request = require('request');

if (Number.isInteger(parseInt(myArray[0]))) {
  request('https://swapi-api.hbtn.io/api/films/' + myArray[0], function (error, response, body) {
    if (error) console.error('error:', error);
    JSON.parse(body).characters.forEach(link => request(link, (error, response, body) => {
      if (error) console.error('error:', error);
      console.log(JSON.parse(body).name);
    }));
  });
}
