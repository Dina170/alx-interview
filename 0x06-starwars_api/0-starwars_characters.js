#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, res, body) => {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, (_err, _res, _body) => {
      if (_err) throw _err;
      console.log(JSON.parse(_body).name);
    });
  });
});
