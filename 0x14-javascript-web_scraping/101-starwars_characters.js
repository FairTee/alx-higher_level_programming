#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;
  const characters = [];

  let completedRequests = 0;

  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      characters.push(character.name);
      completedRequests++;

      if (completedRequests === charactersUrls.length) {
        characters.forEach(character => {
          console.log(character);
        });
      }
    });
  });
});
