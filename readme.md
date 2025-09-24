🌍Echo Footprint Tracker

A full-stack Python web application that helps users understand and reduce their carbon footprint.
Users log their daily activities (transport, food, electricity, shopping), and the system calculates emissions, visualizes trends, and provides eco-friendly suggestions.


✨Features

👤 User Authentication – Secure sign up, login, and personalized profile.

📝 Activity Logging – Record daily activities like:

🚗 Transport (car, bus, bike, flight distance)

⚡ Electricity usage (kWh consumed)

🍔 Food habits (veg, non-veg, dairy, etc.)

🛒 Shopping & lifestyle activities

📊 Carbon Footprint Calculator – Automatically computes CO₂ emissions using scientifically backed emission factors.

📈 Interactive Dashboard – Visualize emissions:

Daily, weekly, and monthly trends

Pie charts by category (transport vs food vs energy)

💡 Personalized Eco Tips – Get actionable suggestions to reduce footprint (e.g., switch to public transport, eat more plant-based meals).

🏆 Gamification (Optional) – Earn badges and eco-scores for sustainable choices.

🌐 Community (Stretch Goal) – Share eco-friendly tips, take part in challenges, and compare with others on leaderboards.

📂 Data Storage – All logs securely stored in a database for history tracking.

🚀 Scalable Architecture – Built with Python backend + modern frontend for easy expansion.


## projrct Structure

ECOFOOTPRINTTRACKER/
│── API/
│   └── main.py              # Main API entry point
│
│── FrontEnd/                # Frontend application
│   └── app.py               # streamlit web interface
│
│── src/                     #core application logic
│   ├── db.py                #Database operations
│   └── logic.py             # Business logic and task operations
│
│── .env                     # Environment variables (DB URL, API keys, secrets)
│── readme.md                # Project documentation
│── requirements.txt         # Python dependencies


# Quick Start

### Prerequisites

- python 3.8 or higher
- A Supabase account
- Git (cloning,push)

## 1. Clone or Download the project
# Option 1:Clone with Git
git clone <repository-url>

# Option 2: Download and extract the zip file

### 2.Install Dependencies

# Install all required python packages
pip install -r requirements.txt

### 3. Set Up supabase Database

1.create a supabase Project:

2.Create the Tasks Table:

-Go to the SQL Editor in your supabase dashboard
-Run this SQL command
```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    age INT,
    location VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

3.**Get Your credentials

### 4.Configure Environmental Variables

1.Create a '.env' file in the project root

2.Add your supabase credentials to '.env':
eg:
SUPABSE_URL=your_projrct_url_here
SUPASE_KEY=your_anon_key_here

### 5. Run the Application

 ## Streamlit Frontend
 stramlit run frontend/app.py

 The app will open in your browser at 'http://localhost:8001'

 ## FastAPI Backend

 cd api
 python main.py

 The API will be available at 'http://localhost:8000'

 ## How to use 

 1.Register / Login → Create a new account

 2.Log Activities → Add daily transport, electricity, and food data

 3.Track Emissions → View your daily/weekly/monthly carbon footprint

 4.Get Suggestions → See personalized eco-friendly recommendations

### Technical Details
  
🛠️ Technologies Used
Backend

 Python – Core programming language

 FastAPI / Flask – For building RESTful APIs

 SQLAlchemy – ORM for database interaction

 PostgreSQL / SQLite – Database for storing users, activities, and carbon logs

Frontend

 Flask (Jinja2 templates) or React (optional) – For the user interface

 HTML5, CSS3, JavaScript – Core web technologies for UI design

 Bootstrap / TailwindCSS – For responsive styling

Other Tools

 dotenv – Manage environment variables

 Pydantic – Data validation for API inputs

 pytest / unittest – For testing application logic

 Git & GitHub – Version control and collaboration

Optional Enhancements

 Matplotlib / Plotly / Chart.js – Visualizing carbon footprint trends

 Docker – Containerization for deployment

 Heroku / Render / Vercel – Deployment platforms

## Key componenets
1.'src/db.py':Database operations,handles all crud operations with supabase
2.'src/logic.py':Business logic Task validation and processing

## Trouble Shooting

## Common Issues


## Future Enhancements
🌱 Future Enhancements

📊 Advanced Analytics Dashboard
Add detailed charts and graphs (using Plotly/Chart.js) to visualize weekly/monthly/yearly carbon trends.

🤖 AI-Powered Suggestions
Use machine learning to recommend personalized eco-friendly habits (e.g., diet changes, transport alternatives).

🎯 Gamification
Add challenges, badges, and leaderboards to motivate users to lower their carbon footprint.

🌍 Social Sharing
Allow users to share their achievements or footprint reduction on social media.

📱 Mobile App Support
Build a React Native / Flutter app version for easy tracking on the go.

🔌 IoT Integration
Connect with smart meters or fitness trackers to automatically log energy usage and travel distance.

🌐 Multi-language Support
Add support for multiple languages to make the app accessible globally.

💸 Carbon Offset Marketplace
Integrate a feature where users can purchase carbon offsets (like tree planting or renewable energy credits).

## Support
 in case of any queries contact:
 email:viishweshwar665@gmail.com
 phno:8885123004
 


