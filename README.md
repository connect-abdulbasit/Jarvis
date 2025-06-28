# JARVIS - Voice Assistant

A Python-based voice assistant inspired by Iron Man's JARVIS, capable of performing various tasks through voice commands.

## Features

- **Voice Recognition**: Listen and respond to voice commands
- **Text-to-Speech**: Speak responses back to the user
- **Web Navigation**: Open websites like YouTube, Facebook, Google, LinkedIn, GitHub, Netflix
- **Weather Information**: Get current weather for any city
- **Time and Date**: Tell current time and date
- **Web Search**: Search Google for any query
- **Wikipedia Lookup**: Get information about people, places, or things
- **Music Playback**: Play specific songs (e.g., "Millionaire")
- **Wake Word**: Activate with "Jarvis"
- **Sleep Mode**: Put assistant to sleep and wake up later

## Commands

### Basic Commands
- **"Jarvis"** - Wake up the assistant
- **"Sleep"** - Put assistant to sleep
- **"Shutdown/Exit/Quit"** - Close the application

### Website Commands
- **"Open YouTube"** - Opens YouTube
- **"Open Facebook"** - Opens Facebook
- **"Open Google"** - Opens Google
- **"Open LinkedIn"** - Opens LinkedIn
- **"Open GitHub"** - Opens GitHub
- **"Open Netflix"** - Opens Netflix

### Information Commands
- **"What time is it?"** - Tells current time
- **"What's the date?"** - Tells current date
- **"Weather in [city]"** - Gets weather for specified city
- **"Search [query]"** - Searches Google for the query
- **"Who is [person]?"** - Gets Wikipedia information about a person
- **"What is [thing]?"** - Gets Wikipedia information about a thing

### Entertainment Commands
- **"Play millionaire"** - Plays "Millionaire" song on YouTube

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Jarvis
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root and add your OpenWeather API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

4. **Get OpenWeather API Key**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Get your free API key
   - Add it to the `.env` file

## Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Wake up JARVIS**
   - Say "Jarvis" to activate the assistant
   - The assistant will respond with "Jarvis Activated"

3. **Give commands**
   - Speak your commands clearly
   - Wait for JARVIS to respond
   - Say "Sleep" to put JARVIS to sleep
   - Say "Shutdown" to exit the application

## Requirements

- Python 3.7+
- Microphone access
- Internet connection
- OpenWeather API key (for weather functionality)

## Dependencies

- `speech_recognition` - For voice recognition
- `pyttsx3` - For text-to-speech
- `requests` - For API calls
- `wikipedia` - For information lookup
- `python-dotenv` - For environment variable management

## Troubleshooting

### Microphone Issues
- Ensure your microphone is properly connected and working
- Check microphone permissions in your system settings
- Try running the application with administrator privileges

### Speech Recognition Issues
- Speak clearly and in a quiet environment
- Ensure you have a stable internet connection
- Check if your microphone is set as the default input device

### Weather API Issues
- Verify your OpenWeather API key is correct
- Check if you've exceeded the free API limit
- Ensure the city name is spelled correctly

## Contributing

Feel free to contribute to this project by:
- Adding new voice commands
- Improving speech recognition accuracy
- Adding new features
- Fixing bugs
- Improving documentation

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Inspired by Iron Man's JARVIS
- Uses Google Speech Recognition API
- Weather data provided by OpenWeatherMap
- Information lookup powered by Wikipedia
