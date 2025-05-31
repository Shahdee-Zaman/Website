let latitude;
let longitude;
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

async function weatherLocation(api) {
    try {
        const position = await (findLocation())
        const url = `https://api.weatherapi.com/v1/current.json?key=${api}&q=${position.latitude},${position.longitude}`;
        fetch(url)
            .then(response => response.json())
            .then(value => {console.log(value)});
        console.log(position);
        return position
    }
    catch(error) {
        console.log(error);
    }
}
