

fetch("http://swapi.dev/api/films").then(res => res.json()).then(data => data.results.forEach(element => {
    console.log(element.title)
    document.write(`<h1>${element.title}</h1>`)
}))
