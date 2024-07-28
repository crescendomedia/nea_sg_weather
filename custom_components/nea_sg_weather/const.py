"""New config variable"""
from homeassistant.components.weather import (
    ATTR_CONDITION_CLEAR_NIGHT,
    ATTR_CONDITION_CLOUDY,
    ATTR_CONDITION_FOG,
    ATTR_CONDITION_LIGHTNING,
    ATTR_CONDITION_LIGHTNING_RAINY,
    ATTR_CONDITION_PARTLYCLOUDY,
    ATTR_CONDITION_POURING,
    ATTR_CONDITION_RAINY,
    ATTR_CONDITION_SNOWY,
    ATTR_CONDITION_SNOWY_RAINY,
    ATTR_CONDITION_SUNNY,
    ATTR_CONDITION_WINDY,
    ATTR_CONDITION_WINDY_VARIANT,
)

CONF_AREAS = "areas"
CONF_RAIN = "rain"
CONF_SENSOR = "sensor"
CONF_WEATHER = "weather"

DOMAIN = "nea_sg_weather"
ATTRIBUTION = "Weather data from Singapore's NEA"
DEFAULT_NAME = "Singapore Weather"
DEFAULT_SCAN_INTERVAL = 15
DEFAULT_TIMEOUT = 10
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "referer": "https://www.nea.gov.sg",
}
RAIN_MAP_HEADERS = {
    "authority": "www.weather.gov.sg",
    "referer": "https://www.nea.gov.sg/weather/rain-areas",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
}
RAIN_MAP_URL_PREFIX = "https://www.weather.gov.sg/files/rainarea/50km/v2/dpsri_70km_"
RAIN_MAP_URL_SUFFIX = "0000dBR.dpsri.png"
RAIN_MAP_GIF_URL = "https://www.weather.gov.sg/weather-rain-area-50km/"

FORECAST_ICON_BASE_URL = "https://www.nea.gov.sg/assets/images/icons/weather-bg/"

MAP_CONDITION = {
    "Mist": ATTR_CONDITION_FOG,
    "Cloudy": ATTR_CONDITION_CLOUDY,
    "Drizzle": ATTR_CONDITION_RAINY,
    "Fair": ATTR_CONDITION_SUNNY,
    "Fair (Day)": ATTR_CONDITION_SUNNY,
    "Fog": ATTR_CONDITION_FOG,
    "Fair (Night)": ATTR_CONDITION_CLEAR_NIGHT,
    "Fair & Warm": ATTR_CONDITION_SUNNY,
    "Heavy Thundery Showers with Gusty Winds": ATTR_CONDITION_LIGHTNING,
    "Heavy Rain": ATTR_CONDITION_POURING,
    "Heavy Showers": ATTR_CONDITION_POURING,
    "Heavy Thundery Showers": ATTR_CONDITION_LIGHTNING,
    "Hazy": ATTR_CONDITION_FOG,
    "Slightly Hazy": ATTR_CONDITION_FOG,
    "Light Rain": ATTR_CONDITION_RAINY,
    "Light Showers": ATTR_CONDITION_RAINY,
    "Overcast": ATTR_CONDITION_CLOUDY,
    "Partly Cloudy": ATTR_CONDITION_PARTLYCLOUDY,
    "Partly Cloudy (Day)": ATTR_CONDITION_PARTLYCLOUDY,
    "Partly Cloudy (Night)": ATTR_CONDITION_PARTLYCLOUDY,
    "Passing Showers": ATTR_CONDITION_RAINY,
    "Moderate Rain": ATTR_CONDITION_RAINY,
    "Showers": ATTR_CONDITION_RAINY,
    "Strong Winds, Showers": ATTR_CONDITION_POURING,
    "Snow": ATTR_CONDITION_SNOWY,
    "Strong Winds, Rain": ATTR_CONDITION_RAINY,
    "Snow Showers": ATTR_CONDITION_SNOWY_RAINY,
    "Sunny": ATTR_CONDITION_SUNNY,
    "Strong Winds": ATTR_CONDITION_WINDY,
    "Thundery Showers": ATTR_CONDITION_LIGHTNING_RAINY,
    "Windy, Cloudy": ATTR_CONDITION_WINDY_VARIANT,
    "Windy": ATTR_CONDITION_WINDY,
    "Windy, Fair": ATTR_CONDITION_WINDY,
    "Windy, Rain": ATTR_CONDITION_RAINY,
    "Windy, Showers": ATTR_CONDITION_RAINY,
}

FORECAST_ICON_MAP_CONDITION = {
    "Mist": "BR",
    "Cloudy": "CL",
    "Drizzle": "DR",
    "Fair": "FA",
    "Fair (Day)": "FA",
    "Fog": "FG",
    "Fair (Night)": "FN",
    "Fair & Warm": "FW",
    "Heavy Thundery Showers with Gusty Winds": "HG",
    "Heavy Rain": "HR",
    "Heavy Showers": "HS",
    "Heavy Thundery Showers": "HT",
    "Hazy": "HZ",
    "Slightly Hazy": "LH",
    "Light Rain": "LR",
    "Light Showers": "LS",
    "Overcast": "OC",
    "Partly Cloudy": "PC",
    "Partly Cloudy (Day)": "PC",
    "Partly Cloudy (Night)": "PN",
    "Passing Showers": "PS",
    "Moderate Rain": "RA",
    "Showers": "SH",
    "Strong Winds, Showers": "SK",
    "Snow": "SN",
    "Strong Winds, Rain": "SR",
    "Snow Showers": "SS",
    "Sunny": "SU",
    "Strong Winds": "SW",
    "Thundery Showers": "TL",
    "Windy, Cloudy": "WC",
    "Windy": "WD",
    "Windy, Fair": "WF",
    "Windy, Rain": "WR",
    "Windy, Showers": "WS",
}

FORECAST_MAP_CONDITION = {
    "thundery showers": ATTR_CONDITION_LIGHTNING_RAINY,
    "partly cloudy": ATTR_CONDITION_PARTLYCLOUDY,
    "rain": ATTR_CONDITION_RAINY,
    "showers": ATTR_CONDITION_RAINY,
    "fair": ATTR_CONDITION_SUNNY,
    "hazy": ATTR_CONDITION_FOG,
    "cloudy": ATTR_CONDITION_CLOUDY,
    "overcast": ATTR_CONDITION_CLOUDY,
    "windy": ATTR_CONDITION_WINDY,
}

AREAS = [
    "Ang Mo Kio",
    "Bedok",
    "Bishan",
    "Boon Lay",
    "Bukit Batok",
    "Bukit Merah",
    "Bukit Panjang",
    "Bukit Timah",
    "Central Water Catchment",
    "Changi",
    "Choa Chu Kang",
    "Clementi",
    "City",
    "Geylang",
    "Hougang",
    "Jalan Bahar",
    "Jurong East",
    "Jurong Island",
    "Jurong West",
    "Kallang",
    "Lim Chu Kang",
    "Mandai",
    "Marine Parade",
    "Novena",
    "Pasir Ris",
    "Paya Lebar",
    "Pioneer",
    "Pulau Tekong",
    "Pulau Ubin",
    "Punggol",
    "Queenstown",
    "Seletar",
    "Sembawang",
    "Sengkang",
    "Sentosa",
    "Serangoon",
    "Southern Islands",
    "Sungei Kadut",
    "Tampines",
    "Tanglin",
    "Tengah",
    "Toa Payoh",
    "Tuas",
    "Western Islands",
    "Western Water Catchment",
    "Woodlands",
    "Yishun",
]

RAIN_SENSOR_LIST = [
    {
        "id": "S77",
        "device_id": "S77",
        "name": "Alexandra Road",
        "location": {"latitude": 1.2937, "longitude": 103.8125},
    },
    {
        "id": "S109",
        "device_id": "S109",
        "name": "Ang Mo Kio Avenue 5",
        "location": {"latitude": 1.3764, "longitude": 103.8492},
    },
    {
        "id": "S90",
        "device_id": "S90",
        "name": "Bukit Timah Road",
        "location": {"latitude": 1.3191, "longitude": 103.8191},
    },
    {
        "id": "S114",
        "device_id": "S114",
        "name": "Choa Chu Kang Avenue 4",
        "location": {"latitude": 1.38, "longitude": 103.73},
    },
    {
        "id": "S50",
        "device_id": "S50",
        "name": "Clementi Road",
        "location": {"latitude": 1.3337, "longitude": 103.7768},
    },
    {
        "id": "S107",
        "device_id": "S107",
        "name": "East Coast Parkway",
        "location": {"latitude": 1.3135, "longitude": 103.9625},
    },
    {
        "id": "S215",
        "device_id": "S215",
        "name": "GEYLANG EAST CENTRAL",
        "location": {"latitude": 1.32785, "longitude": 103.88899},
    },
    {
        "id": "S118",
        "device_id": "S118",
        "name": "Handy Road",
        "location": {"latitude": 1.2994, "longitude": 103.8461},
    },
    {
        "id": "S120",
        "device_id": "S120",
        "name": "Holland Road",
        "location": {"latitude": 1.30874, "longitude": 103.818},
    },
    {
        "id": "S33",
        "device_id": "S33",
        "name": "Jurong Pier Road",
        "location": {"latitude": 1.3081, "longitude": 103.71},
    },
    {
        "id": "S71",
        "device_id": "S71",
        "name": "Kent Ridge Road",
        "location": {"latitude": 1.2923, "longitude": 103.7815},
    },
    {
        "id": "S43",
        "device_id": "S43",
        "name": "Kim Chuan Road",
        "location": {"latitude": 1.3399, "longitude": 103.8878},
    },
    {
        "id": "S66",
        "device_id": "S66",
        "name": "Kranji Way",
        "location": {"latitude": 1.4387, "longitude": 103.7363},
    },
    {
        "id": "S112",
        "device_id": "S112",
        "name": "Lim Chu Kang Road",
        "location": {"latitude": 1.43854, "longitude": 103.70131},
    },
    {
        "id": "S40",
        "device_id": "S40",
        "name": "Mandai Lake Road",
        "location": {"latitude": 1.4044, "longitude": 103.78962},
    },
    {
        "id": "S108",
        "device_id": "S108",
        "name": "Marina Gardens Drive",
        "location": {"latitude": 1.2799, "longitude": 103.8703},
    },
    {
        "id": "S113",
        "device_id": "S113",
        "name": "Marine Parade Road",
        "location": {"latitude": 1.30648, "longitude": 103.9104},
    },
    {
        "id": "S44",
        "device_id": "S44",
        "name": "Nanyang Avenue",
        "location": {"latitude": 1.34583, "longitude": 103.68166},
    },
    {
        "id": "S119",
        "device_id": "S119",
        "name": "Nicoll Highway",
        "location": {"latitude": 1.30105, "longitude": 103.8666},
    },
    {
        "id": "S121",
        "device_id": "S121",
        "name": "Old Choa Chu Kang Road",
        "location": {"latitude": 1.37288, "longitude": 103.72244},
    },
    {
        "id": "S35",
        "device_id": "S35",
        "name": "Old Toh Tuck Road",
        "location": {"latitude": 1.3329, "longitude": 103.7556},
    },
    {
        "id": "S94",
        "device_id": "S94",
        "name": "Pasir Ris Street 51",
        "location": {"latitude": 1.3662, "longitude": 103.9528},
    },
    {
        "id": "S78",
        "device_id": "S78",
        "name": "Poole Road",
        "location": {"latitude": 1.30703, "longitude": 103.89067},
    },
    {
        "id": "S106",
        "device_id": "S106",
        "name": "Pulau Ubin",
        "location": {"latitude": 1.4168, "longitude": 103.9673},
    },
    {
        "id": "S81",
        "device_id": "S81",
        "name": "Punggol Central",
        "location": {"latitude": 1.4029, "longitude": 103.9092},
    },
    {
        "id": "S201",
        "device_id": "S201",
        "name": "S201",
        "location": {"latitude": 1.32311, "longitude": 103.76714},
    },
    {
        "id": "S202",
        "device_id": "S202",
        "name": "S202",
        "location": {"latitude": 1.30968, "longitude": 103.7578},
    },
    {
        "id": "S203",
        "device_id": "S203",
        "name": "S203",
        "location": {"latitude": 1.29164, "longitude": 103.7702},
    },
    {
        "id": "S204",
        "device_id": "S204",
        "name": "S204",
        "location": {"latitude": 1.40081, "longitude": 103.88217},
    },
    {
        "id": "S205",
        "device_id": "S205",
        "name": "S205",
        "location": {"latitude": 1.38829, "longitude": 103.9116},
    },
    {
        "id": "S207",
        "device_id": "S207",
        "name": "S207",
        "location": {"latitude": 1.32485, "longitude": 103.95836},
    },
    {
        "id": "S208",
        "device_id": "S208",
        "name": "S208",
        "location": {"latitude": 1.3136, "longitude": 104.00317},
    },
    {
        "id": "S209",
        "device_id": "S209",
        "name": "S209",
        "location": {"latitude": 1.42111, "longitude": 103.84472},
    },
    {
        "id": "S210",
        "device_id": "S210",
        "name": "S210",
        "location": {"latitude": 1.44003, "longitude": 103.76904},
    },
    {
        "id": "S211",
        "device_id": "S211",
        "name": "S211",
        "location": {"latitude": 1.42918, "longitude": 103.75711},
    },
    {
        "id": "S212",
        "device_id": "S212",
        "name": "S212",
        "location": {"latitude": 1.31835, "longitude": 103.93574},
    },
    {
        "id": "S213",
        "device_id": "S213",
        "name": "S213",
        "location": {"latitude": 1.32427, "longitude": 103.8097},
    },
    {
        "id": "S214",
        "device_id": "S214",
        "name": "S214",
        "location": {"latitude": 1.29911, "longitude": 103.88289},
    },
    {
        "id": "S216",
        "device_id": "S216",
        "name": "S216",
        "location": {"latitude": 1.36019, "longitude": 103.85335},
    },
    {
        "id": "S217",
        "device_id": "S217",
        "name": "S217",
        "location": {"latitude": 1.35041, "longitude": 103.85526},
    },
    {
        "id": "S218",
        "device_id": "S218",
        "name": "S218",
        "location": {"latitude": 1.36491, "longitude": 103.75065},
    },
    {
        "id": "S219",
        "device_id": "S219",
        "name": "S219",
        "location": {"latitude": 1.37999, "longitude": 103.87643},
    },
    {
        "id": "S220",
        "device_id": "S220",
        "name": "S220",
        "location": {"latitude": 1.38666, "longitude": 103.89797},
    },
    {
        "id": "S221",
        "device_id": "S221",
        "name": "S221",
        "location": {"latitude": 1.35691, "longitude": 103.89088},
    },
    {
        "id": "S222",
        "device_id": "S222",
        "name": "S222",
        "location": {"latitude": 1.28987, "longitude": 103.82364},
    },
    {
        "id": "S223",
        "device_id": "S223",
        "name": "S223",
        "location": {"latitude": 1.29984, "longitude": 103.80264},
    },
    {
        "id": "S224",
        "device_id": "S224",
        "name": "S224",
        "location": {"latitude": 1.34392, "longitude": 103.98409},
    },
    {
        "id": "S226",
        "device_id": "S226",
        "name": "S226",
        "location": {"latitude": 1.27472, "longitude": 103.80389},
    },
    {
        "id": "S227",
        "device_id": "S227",
        "name": "S227",
        "location": {"latitude": 1.43944, "longitude": 103.80389},
    },
    {
        "id": "S228",
        "device_id": "S228",
        "name": "S228",
        "location": {"latitude": 1.34703, "longitude": 103.70073},
    },
    {
        "id": "S229",
        "device_id": "S229",
        "name": "S229",
        "location": {"latitude": 1.35167, "longitude": 103.72195},
    },
    {
        "id": "S230",
        "device_id": "S230",
        "name": "S230",
        "location": {"latitude": 1.30167, "longitude": 103.76444},
    },
    {
        "id": "S111",
        "device_id": "S111",
        "name": "Scotts Road",
        "location": {"latitude": 1.31055, "longitude": 103.8365},
    },
    {
        "id": "S900",
        "device_id": "S900",
        "name": "Seletar Aerospace View",
        "location": {"latitude": 1.41284, "longitude": 103.86922},
    },
    {
        "id": "S84",
        "device_id": "S84",
        "name": "Simei Avenue",
        "location": {"latitude": 1.3437, "longitude": 103.9444},
    },
    {
        "id": "S79",
        "device_id": "S79",
        "name": "Somerset Road",
        "location": {"latitude": 1.3004, "longitude": 103.8372},
    },
    {
        "id": "S88",
        "device_id": "S88",
        "name": "Toa Payoh North",
        "location": {"latitude": 1.3427, "longitude": 103.8482},
    },
    {
        "id": "S123",
        "device_id": "S123",
        "name": "Towner Road",
        "location": {"latitude": 1.3214, "longitude": 103.8577},
    },
    {
        "id": "S89",
        "device_id": "S89",
        "name": "Tuas Road",
        "location": {"latitude": 1.31985, "longitude": 103.66162},
    },
    {
        "id": "S115",
        "device_id": "S115",
        "name": "Tuas South Avenue 3",
        "location": {"latitude": 1.29377, "longitude": 103.61843},
    },
    {
        "id": "S82",
        "device_id": "S82",
        "name": "Tuas West Road",
        "location": {"latitude": 1.3247, "longitude": 103.6351},
    },
    {
        "id": "S24",
        "device_id": "S24",
        "name": "Upper Changi Road North",
        "location": {"latitude": 1.3678, "longitude": 103.9826},
    },
    {
        "id": "S69",
        "device_id": "S69",
        "name": "Upper Peirce Reservoir Park",
        "location": {"latitude": 1.37, "longitude": 103.805},
    },
    {
        "id": "S36",
        "device_id": "S36",
        "name": "Upper Serangoon Road",
        "location": {"latitude": 1.3382, "longitude": 103.8657},
    },
    {
        "id": "S08",
        "device_id": "S08",
        "name": "Upper Thomson Road",
        "location": {"latitude": 1.3701, "longitude": 103.8271},
    },
    {
        "id": "S116",
        "device_id": "S116",
        "name": "West Coast Highway",
        "location": {"latitude": 1.281, "longitude": 103.754},
    },
    {
        "id": "S104",
        "device_id": "S104",
        "name": "Woodlands Avenue 9",
        "location": {"latitude": 1.44387, "longitude": 103.78538},
    },
    {
        "id": "S100",
        "device_id": "S100",
        "name": "Woodlands Road",
        "location": {"latitude": 1.4172, "longitude": 103.74855},
    },
]

REGIONS = ["West", "East", "Central", "South", "North"]

PRIMARY_ENDPOINTS = {
    "forecast2hr": "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast",
    "forecast24hr": "https://api.data.gov.sg/v1/environment/24-hour-weather-forecast",
    "temperature": "https://api.data.gov.sg/v1/environment/air-temperature",
    "humidity": "https://api.data.gov.sg/v1/environment/relative-humidity",
    "wind-direction": "https://api.data.gov.sg/v1/environment/wind-direction",
    "wind-speed": "https://api.data.gov.sg/v1/environment/wind-speed",
    "forecast4day": "https://api.data.gov.sg/v1/environment/4-day-weather-forecast",
    "rainfall": "https://api.data.gov.sg/v1/environment/rainfall",
}

SECONDARY_ENDPOINTS = {
    "forecast2hr": "https://www.nea.gov.sg/api/WeatherForecast/forecast24hrnowcast2hrs/",
    "forecast24hr": "https://www.nea.gov.sg/api/WeatherForecast/forecast24hrnowcast2hrs/",
    "temperature": "",
    "humidity": "",
    "wind-direction": "",
    "wind-speed": "",
    "forecast4day": "https://www.nea.gov.sg/api/Weather4DayOutlook/GetData/",
    "rainfall": "",
}