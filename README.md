# 🎯 Hangman Game

A modern, full-stack implementation of the classic Hangman word-guessing game built with Django REST Framework and Vue.js.

📸 Screenshots

<div align="center">
  <img src="https://user-images.githubusercontent.com/placeholder/hangman-demo.png" alt="Hangman Game Demo" width="600"/>
  <p><em>Interactive Hangman game with modern UI - guess the word before the drawing is complete!</em></p>
</div>
<!-- Replace the placeholder above with your actual screenshot -->
<!-- Alternative: Use a generic hangman illustration -->
<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Hangman_game.jpg/300px-Hangman_game.jpg" alt="Hangman Game Concept" width="300"/>
  <p><em>Classic Hangman game concept - built with modern web technologies</em></p>
</div>

## 🚀 Features

- **Interactive Gameplay**: Classic hangman mechanics with visual feedback
- **Word Selection**: Dynamic word selection system
- **Session Management**: Persistent game sessions across browser refreshes
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Real-time Updates**: Instant feedback on guesses and game state
- **RESTful API**: Clean separation between backend and frontend

## 🛠️ Tech Stack

### Backend
- **Django**: Web framework for Python
- **Django REST Framework (DRF)**: API development
- **Python**: Backend logic and game mechanics

### Frontend
- **Vue.js**: Progressive JavaScript framework
- **HTML/CSS**: User interface styling
- **JavaScript**: Frontend interactivity

## 🎮 How to Play

1. **Start a New Game**: The system will select a random word
2. **Make Guesses**: Click on letters or use your keyboard to guess
3. **Track Progress**: Watch the hangman drawing and remaining guesses
4. **Win or Lose**: Complete the word before the drawing is finished!

## 🔌 API Endpoints

The Django backend provides the following REST API endpoints:

- `GET /api/game/` - Get current game state
- `POST /api/game/start/` - Start a new game
- `POST /api/game/guess/` - Make a letter guess
- `GET /api/game/status/` - Check game status

## 🌟 Key Features Implemented

### Backend (Django + DRF)
- Game logic and word management
- Session-based game state persistence
- RESTful API design
- Input validation and error handling

### Frontend (Vue.js)
- Interactive user interface
- Real-time game state updates
- Responsive design
- Keyboard and mouse input support

## 📝 License
This project is open source/

## 👨‍💻 Author
**Lahiru Madhawa** - https://github.com/lahiruomadhawa

## 🙏 Acknowledgments
- Thanks to the Django and Vue.js communities for excellent documentation
- Classic Hangman game for the inspiration
- Anyone who contributes to this project

⭐ If you found this project helpful, please give it a star!
