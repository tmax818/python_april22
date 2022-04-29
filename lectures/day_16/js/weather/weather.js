const key = '61107cb5aeddc3fe473d540e1768ff09'
const lat = "34.3863074"
const lon = "-118.5441854"

// const data = fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}`)
//     .then(response => response.json() )
//     .then(coderData => console.log(coderData) )
//     .catch(err => console.log(err) )
    
    

const data2 = fetch("https://flask-ajax-322.herokuapp.com")
    .then(response => console.log(response) )
    .then(coderData => console.log(coderData) )
    .catch(err => console.log(err) )
    
    
    
