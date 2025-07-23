let latitude;
let longitude;

// Get user location to change background according to the weather
function findLocation() {
    return new Promise((resolve, reject) => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                latitude = position.coords.latitude;
                longitude = position.coords.longitude;
                resolve({latitude, longitude});
            })

        }
        else {
            reject(new Error('Geolocation is not supported'));
        }
    })

}

async function getApi() {
    try {
        // Receive api key through flask routes
        const data = await fetch('/weather-api')
        const api = await data.json();
        weatherLocation(api)
    }
    catch(error) {
        console.error(error);
    }
}

async function weatherLocation(api) {
    try {
        const position = await (findLocation())
        const url = `https://api.weatherapi.com/v1/current.json?key=${api}&q=${position.latitude},${position.longitude}`;
        const response = await fetch(url)
        const weather = await response.json();
        const day = weather.current.is_day
        const icon = weather.current.condition
        changeWeatherIcon(icon)
        background(icon.code, day)

    }
    catch(error) {
        console.log(error);
    }
}
function changeWeatherIcon(weather) {
    const icon = document.getElementById('weatherIcon');
    icon.innerHTML = `<image src = ${weather.icon} alt = ${weather.text} title= ${weather.text}></image>`
}

function background(code, day = 1) {
    const current_weather = codes[code];
    const screen = document.getElementById('navigationBar')
    if (`${current_weather}`=='Clear' && day == 0) {
        screen.style.backgroundImage = 'url(static/images/weather/Night.jpg)';
    }
    else {
        screen.style.backgroundImage = `url(static/images/weather/${current_weather}.jpg)`;
    }
}

codes =  {
    "1000": "Clear",
    "1003": "Cloudy",
    "1006": "Cloudy",
    "1009": "Cloudy",
    "1030": "Fog",
    "1063": "Rain",
    "1066": "Snow",
    "1069": "Snow",
    "1072": "Rain",
    "1087": "Thunder",
    "1114": "Snow",
    "1117": "Snow",
    "1135": "Fog",
    "1147": "Fog",
    "1150": "Rain",
    "1153": "Rain",
    "1168": "Rain",
    "1171": "Rain",
    "1180": "Rain",
    "1183": "Rain",
    "1186": "Rain",
    "1189": "Rain",
    "1192": "Rain",
    "1195": "Rain",
    "1198": "Rain",
    "1201": "Rain",
    "1204": "Snow",
    "1207": "Snow",
    "1210": "Snow",
    "1213": "Snow",
    "1216": "Snow",
    "1219": "Snow",
    "1222": "Snow",
    "1225": "Snow",
    "1237": "Snow",
    "1240": "Rain",
    "1243": "Rain",
    "1246": "Rain",
    "1249": "Snow",
    "1252": "Snow",
    "1255": "Snow",
    "1258": "Snow",
    "1261": "Snow",
    "1264": "Snow",
    "1273": "Thunder",
    "1276": "Thunder",
    "1279": "Thunder",
    "1282": "Thunder"
}




getApi()
