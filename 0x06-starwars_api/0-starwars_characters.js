#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, async function (err, res, body) {
  if (err) return console.error(err);

  const characters = JSON.parse(body).characters;

  for (const char of characters) {
    await new Promise(function (resolve, reject) {
      request(char, function (err, res, body) {
        if (err) return console.error(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
