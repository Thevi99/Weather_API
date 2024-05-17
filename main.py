import requests

def get_weather(city, api_key):
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=th'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['current']['condition']['text']
        temperature = data['current']['temp_c']
        humidity = data['current']['humidity']
        wind_speed = data['current']['wind_kph']
        cloud = data['current'].get('cloud', 0) 
        
        print("Weather Data:", data)
        return {
            "description": weather_description,
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed,
            "cloud": cloud
        }
    else:
        return None

def calculate_pop(humidity, cloud, wind_speed):
    # Heuristic to calculate probability of precipitation
    if cloud >= 75:
        pop = 80 + (humidity - 50) / 2  # High cloud coverage with high humidity
    elif cloud >= 50:
        pop = 50 + (humidity - 50) / 2  # Medium cloud coverage with high humidity
    else:
        pop = humidity / 2  # Low cloud coverage, basic PoP based on humidity
    
    # Adjusting with wind speed
    if wind_speed > 20:
        pop += 10  # Increase PoP if wind speed is high
    
    # Ensure PoP is between 0 and 100
    pop = max(0, min(100, pop))
    return round(pop, 2)

def interpret_weather(temperature, humidity, cloud, pop):
    if pop >= 50:
        return f"☔ มีโอกาสฝนตก {pop}% น้องหว่าหวาอย่าลืมพกร่มนะ"
    if temperature > 30:
        if humidity > 70:
            return "🔥 ร้อนและชื้นมาก หว่าหวาอย่าลืมกินน้ำ"
        else:
            return "☀️ ร้อน เปิดแอร์โชว์พุงเลยเด็กอ้วง"
    elif temperature < 20:
        return "❄️ หนูน้อยของเค้าใส่เสื้อกันหนาวด้วยละ อิอิ"
    elif humidity > 80:
        return "☔ ฝนอาจจะตก คุณแฟนต้องระวังนะ"
    else:
        return "🌤️ วันนี้อากาศสดใส ขอให้น้องหว่าหวา Have a nice day"

def send_to_discord(webhook_url, weather_data, city):
    if weather_data:
        pop = calculate_pop(weather_data["humidity"], weather_data["cloud"], weather_data["wind_speed"])
        weather_status = interpret_weather(weather_data["temperature"], weather_data["humidity"], weather_data["cloud"], pop)
        embed = {
            "title": f"🌥️ **Weather in {city}**",
            "color": 9332727,
            "image": {
                "url": "https://media.giphy.com/media/FWtVYDHIxgGgE/giphy.gif"
            },
            "fields": [
                {
                    "name": "📜 __คำอธิบาย__",
                    "value": f"```lua\n{weather_data['description']}\n```",
                    "inline": False
                },
                {
                    "name": "🌡️ __อุณหภูมิ__",
                    "value": f"```lua\n{weather_data['temperature']}°C\n```",
                    "inline": True
                },
                {
                    "name": "💧 __ความชื้น__",
                    "value": f"```lua\n{weather_data['humidity']}%\n```",
                    "inline": True
                },
                {
                    "name": "💨 __ความเร็วลม__",
                    "value": f"```lua\n{weather_data['wind_speed']} km/h\n```",
                    "inline": True
                },
                {
                    "name": "☁️ __ครึ้ม__",
                    "value": f"```lua\n{weather_data['cloud']}%\n```",
                    "inline": True
                },
                {
                    "name": "🌧️ __โอกาสฝนตก__",
                    "value": f"```lua\n{pop}%\n```",
                    "inline": True
                },
                {
                    "name": "🌡️ __สภาพอากาศ__",
                    "value": f"```lua\n{weather_status}\n```",
                    "inline": False
                }
            ]
        }

        data = {
            "embeds": [embed]
        }

        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            print("ส่งข้อความไปยัง Discord สำเร็จ")
        else:
            print("การส่งข้อความไปยัง Discord ล้มเหลว")
    else:
        print("ไม่สามารถดึงข้อมูลสภาพอากาศได้")
        
        
city = "Bangkok"
api_key = "e2030e86945940f18d872703241605"
webhook_url = "https://discord.com/api/webhooks/1240499752173436958/PuCBeJe9Kazakce--S9He_BEuz0c_qmedJTDhjdnKFui3GxZM4icIq7Xb3ah1KyaOE4U"

weather_info = get_weather(city, api_key)
send_to_discord(webhook_url, weather_info, city)
