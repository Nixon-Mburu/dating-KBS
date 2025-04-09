# Solar Opposites - Dating App

A Flask-based dating app that matches users based on interests, location, age, and love languages.

## Features

- User profile creation with preferences
- Smart matching algorithm considering:
  - Age compatibility (30% weight)
  - Shared interests (40% weight)
  - Location matching (20% weight)
  - Love language alignment (10% weight)
- Beautiful, responsive UI
- Real-time match scoring

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- ngrok (for tunneling, optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Nixon-Mburu/dating-KBS.git
cd dating-KBS
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask werkzeug
```

## Running the App

1. Start the Flask server:
```bash
python app.py
```

2. Access the app at: http://localhost:5000

### Using with ngrok (Optional)

1. Install ngrok
2. Start ngrok:
```bash
ngrok http 5000
```

3. Use the provided ngrok URL to access your app

## Project Structure

```
dating/
├── app.py                # Main Flask application with matching logic
├── profile.json         # Database of user profiles
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── templates/
    ├── index.html     # User registration form
    └── match.html     # Match results display
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request to the main repository at https://github.com/Nixon-Mburu/dating-KBS

## License

This project is released under the MIT License.

## Acknowledgments

- Flask web framework
- Love Languages concept by Gary Chapman
- Font Awesome for icons
- Ngrok for tunneling

