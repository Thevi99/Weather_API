# Weather_API

This project is a weather forecasting system that uses webhooks for sending notifications. The system integrates with a weather API to retrieve real-time weather data and delivers updates via Discord notifications.

## Features
- Real-time weather data retrieval using a weather API
- Automatic weather alerts sent to a Discord channel via webhooks
- Customizable notification settings

## Technologies Used
- Python
- Webhook integration
- Weather API (e.g., OpenWeatherMap, Weatherstack)

## Usage
1. Clone the repository
2. Install the required dependencies
3. Configure the webhook URL and API key in the settings
4. Run the script to start receiving weather notifications

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Weather_API.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Weather_API
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure your webhook URL and weather API key in the `config.py` file.
5. Run the script:
    ```bash
    python weather_notifier.py
    ```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request.
