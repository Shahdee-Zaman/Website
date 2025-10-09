# Website

This is my currently used website hosted at: www.shahdee.dev. Feel free to check it out.

## Background

My previous website was extremely barebones as I had created that one right after learning html and css so I wanted to change it. Everything in this website is built with scalability in mind.

## Features 
- Dynamic Changing background that changes based on User current location and weather.
- Gemini interface that allows recruiters and users to learn more based on the text provided in systeminstructions.txt.
- [Redis based Token limiter](https://github.com/Shahdee-Zaman/Gemini-TPD-Limiter) applied to prevent any unexpected overcharge from Gemini.
- Dockerfile included for quick setup and deployment.

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python(Flask)
- Database: Redis
- Containerization: Docker
- Deployment: AWS EC2

## Installation

### Local
```bash
# Clone the repository
git clone https://github.com/Shahdee-Zaman/Website.git
cd Website

# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

### Docker
```bash
# Build Docker image
docker build -t website .

# Run Docker container
docker run -p 5000:5000 website
# Access the site at http://localhost:5000
```

## Enviroment Key Configuration
- Set GEMINI_API_KEY enviroment variable in your machine with your Gemini API key.
- Set weather_api_key enviroment variable in your machine with your weatherapi.com API key.

### For macOS/Linux
export GEMINI_API_KEY="your_key_here"
export weather_api_key="your_key_here"

### For Windows (PowerShell)
setx GEMINI_API_KEY "your_key_here"
setx weather_api_key "your_key_here"
 

## Future Updates
- Optimize background images for faster initial load.
- Redesign navigation bar for improved aesthetics and usability.



# Art Credits
- Clear: Chandan Chaurasia - https://unsplash.com/photos/areal-photo-of-white-clouds-during-daytime-wCYuhCA4T9k?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash
- Clear(Night): Jackson Hendry - https://unsplash.com/photos/silhouette-of-trees-near-body-of-water-under-sky-with-stars-eodA_8CTOFo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash
- Snow: Brian Jones - https://unsplash.com/photos/snow-covered-forest-s8QSJTJI6qg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash
- Rain: Joy Stamp - https://unsplash.com/photos/glass-with-dew-pGQbWXBC1dA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash
- Thunder: Johannes Plenio - https://unsplash.com/photos/photo-of-island-and-thunder-E-Zuyev2XWo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash
- Fog: Inggrid Koe - https://unsplash.com/photos/gray-forest-with-fog-kbKEuU-YEIw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash
- Cloudy: Daria Nepriakhina 🇺🇦 - https://unsplash.com/photos/white-clouds-over-field-auMjWDfTFhI?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash.

# Author
Created by Shahdee Zaman - [Shahdee.dev](https://www.shahdee.dev)
- 📧**Feedback or Questions?** Send me an email: [Shahdeezaman@gmail.com](mailto:shahdeezaman@gmail.com)
- 🤝**Wish to Connect?** [LinkedIn](https://www.linkedin.com/in/shahdee-zaman-35455a276)

