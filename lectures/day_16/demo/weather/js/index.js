

const key = '61107cb5aeddc3fe473d540e1768ff09'
const lat = "34.3863074"
const lon = "-118.5441854"

const data = fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}`).then(res => res.json()).then(data => console.log(data))