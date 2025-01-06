# Personal AI Assistant (Jarvis)

Jarvis is an intelligent and interactive AI assistant developed using Python. It integrates natural language processing, voice recognition, and automation features to assist users in everyday tasks. Jarvis provides a futuristic user interface powered by Kivy and performs tasks such as web searches, email management, news updates, and much more.

---

## Features

### Core Functionalities:
1. **Voice Interaction**: Seamless communication through voice commands.
2. **Web Search**: Search queries on Google and Wikipedia.
3. **Email Management**: Send emails directly via voice commands.
4. **IP Address Lookup**: Retrieve the public IP address of the system.
5. **News Updates**: Get the latest news headlines.
6. **Integration with Generative AI**: Responds intelligently using Google's Gemini API.

### User Interface:
- Built with **Kivy** for an interactive and user-friendly experience.
- Dynamic animations using rotating buttons and real-time updates.

### Automation Features:
- Open applications like Notepad, Command Prompt, and Camera through voice commands.
- Web browser control and video playback on YouTube.

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.9 or higher
- Pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd personal-ai-assistant
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file or edit the `jarvis.env` file to include the following:
     ```
     USER=YourName
     BOT=Jarvis
     EMAIL=YourEmail@gmail.com
     PASSWORD=YourEmailPassword
     IP_ADDR_API_URL=https://api64.ipify.org?format=json
     NEWS_FETCH_API_URL=https://newsapi.org/v2/
     NEWS_FETCH_API_KEY=YourNewsAPIKey
     SMTP_URL=smtp.gmail.com
     SMTP_PORT=587
     GEMINI_API_KEY=YourGeminiAPIKey
     ```

---

## Project Structure

```
project_root/
│
├── main.py                    # Main entry point with Kivy-based GUI
├── main_without_gui.py        # Alternate entry point without GUI
├── jarvis.py                  # Core AI logic and assistant commands
├── jarvis_button.py           # GUI button and animation functionalities
├── utils.py                   # Utility functions for web searches, email, news, etc.
├── constants.py               # Configuration constants loaded from environment
├── online.py                  # Simplified functions for online queries
├── jarvis.env                 # Environment variables for sensitive configurations
├── requirements.txt           # Python dependencies
├── const.py                   # Additional constants
└── README.md                  # Documentation
```

---

## Usage

1. **Run Jarvis with GUI**:
   ```bash
   python main.py
   ```

2. **Run Jarvis without GUI**:
   ```bash
   python main_without_gui.py
   ```

3. Use voice commands to interact with Jarvis. Example commands:
   - "Open Google"
   - "Search Wikipedia for Artificial Intelligence"
   - "Send an email"

---

## Technologies Used

- **Python Libraries**:
  - `Kivy`: GUI development.
  - `SpeechRecognition`: Voice command processing.
  - `gTTS`: Text-to-speech conversion.
  - `Requests`: API interactions.
  - `pywhatkit`: YouTube playback and web automation.
  - `pydub`: Audio manipulation.
  - `google.generativeai`: Integrating Gemini API for intelligent responses.

- **APIs**:
  - Gemini API
  - News API

---

## Screenshots

1. **Interactive GUI**
   - Dynamic animations and voice command input.
2. **Terminal Mode**
   - Minimalist command-line interaction.

---

## Contributing

Feel free to fork this repository and submit pull requests for feature enhancements or bug fixes.

---

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Contact

For questions or support, reach out to:
- **GitHub**: [GitHub Profile](https://github.com/hhdjwdabsxsx)
