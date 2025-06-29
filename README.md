#  CinemaBuddy – Movie Outcome Predictor
**Powered by Flask & Machine Learning**

CinemaBuddy is a Flask-based web application that predicts a movie’s **rating**, **box office gross**, and whether it will be a **Hit** or **Flop** using machine learning models trained on historical movie data.

---

##  Project Overview

**Objective**: Let users predict a movie’s expected performance — its **rating**, **box office gross**, and whether it will be a **Hit or Flop** — based on features like director, actors, genre, runtime, and censor rating.

The app uses:
- Flask for the web backend
- HTML/CSS for templated frontend
- Machine Learning (Linear Regression) for predictions
- Flask sessions for user login/signup/logout

---

##  Features

-  **User Authentication** (Signup, Login, Logout)
-  **Prediction Form** for entering movie details
-  **Results Page** showing predictions
-  **Light/Dark Theme Toggle**
-  **ML Integration** using Scikit-learn Linear Regression

---

##  Tech Stack

| Component       | Technology                   |
|------------------|-------------------------------|
| Frontend         | HTML, CSS (Flask Templates)   |
| Backend          | Flask (Python)                |
| ML Model         | Scikit-learn (Linear Regression) |
| Data Handling    | pandas                        |
| User Auth        | Flask sessions                |

---

##  Machine Learning Details

- **Dataset**: `moviesList.csv`
- **Features**:
  - Director
  - Actors
  - Genre
  - Censor Rating
  - Runtime
- **Targets**:
  - `Rating` (float)
  - `Total_Gross` (float)
- **Models**:
  - `model_rating`: Predicts movie rating
  - `model_gross`: Predicts box office revenue
- **Prediction Logic**:
  - If predicted `Total_Gross ≥ 500M`, label as `Hit`, else `Flop`
- **Preprocessing**:
  - Label encoding for categorical features
  - Runtime cleaning and conversion

---

##  Website Routes

| Route           | Description                          |
|------------------|--------------------------------------|
| `/signup`        | New user registration                |
| `/login`         | Existing user login                  |
| `/logout`        | Logout and clear session             |
| `/predict`       | Movie input form for predictions     |
| `/result`        | Displays predicted rating and gross  |
| `/toggle_theme`  | Switch between light/dark modes      |

---

##  Running Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/amitanetne/CinemaBuddy.git
   cd CinemaBuddy



   Team

- Kanishk  
- Aditya  
- Rachit  
- Renuka  
- Anshika  
- Amita (Team Lead)

---

##  Contact

For questions, feedback, or collaboration:

Amita (Team Lead) – [amitanetne929@gmail.com](mailto:amitanetne929@gmail.com)

