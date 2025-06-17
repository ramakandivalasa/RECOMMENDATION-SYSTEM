# RECOMMENDATION-SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: RAMA KANDIVALASA 

*INTERN ID*: CT04DN904

*DOMAIN*: MACHINE LEARNING 

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

## 📌 Project Title: BUILD A RECOMMENDATION SYSTEM USING COLLABORATIVE FILTERING OR MATRIX FACTORIZATION TECHNIQUES

## 📁 Dataset Details

This prototype uses **sample data** for demonstration purposes. The dataset includes user IDs, anime titles, ratings (from 1 to 5), and genres.

### 📊 Sample Dataset Format:

| user | item            | rating | genre           |
|------|------------------|--------|------------------|
| 1    | Attack on Titan | 5      | Action          |
| 1    | Re:Zero         | 4      | Isekai          |
| 2    | One Piece       | 4      | Adventure       |
| 2    | Bleach          | 3      | Action          |
| 3    | Death Note      | 5      | Psychological   |
| 3    | Naruto          | 4      | Action          |
| 4    | Demon Slayer    | 5      | Fantasy         |
| 4    | Jujutsu Kaisen  | 4      | Supernatural    |

---

## ⚙️ Technologies Used

- **Python 3**
- **Flask** for web app development
- **Pandas** for data handling
- **scikit-surprise** for collaborative filtering
- **HTML & Jinja2** for rendering templates

---

## 📂 Project Structure

├── app.py # Flask backend
├── templates/
│ └── index.html # Web page template
├── static/
│ └── style.css # (Optional) Styling
├── README.md # Project documentation
├── requirements.txt # Python dependencies

yaml
Copy
Edit

---

## 💡 How It Works

1. The system uses collaborative filtering via the SVD algorithm.
2. User inputs a **user ID** and selects a **genre**.
3. Based on previously seen anime and ratings, the model predicts ratings for unseen items in the selected genre.
4. Top 5 anime with the highest predicted ratings are recommended.

---

## 🚀 Getting Started

### 🔧 Installation

Make sure Python is installed, then install the required libraries:


pip install flask pandas scikit-surprise
Or, if you have a requirements.txt:


pip install -r requirements.txt
## ▶️ Running the App

python app.py
Visit http://127.0.0.1:5000 in your browser.

🖥️ UI Preview
Input:
User ID: 2

Genre: Action

## Output:

Top Recommendations:
1. Naruto - Predicted Rating: 4.63
2. Attack on Titan - Predicted Rating: 4.22
## 📌 Features
Predicts top anime recommendations based on user ID and selected genre.

Uses collaborative filtering (SVD) to estimate ratings for unseen anime.

Genre-based filtering simulates personalized recommendations.

✅ Future Improvements
Replace sample data with a real-world dataset (e.g., MyAnimeList or Kaggle)

Add content-based filtering

Allow dynamic user registration and rating input

Improve UI using Tailwind or Bootstrap

## 📣 Acknowledgements
This project was built as part of a machine learning task to demonstrate collaborative filtering and Flask-based web app deployment.

## 🧾 Sample Code Snippet
Here’s a quick view of the core recommendation logic:

def recommend(user_id, genre):
    algo = train_model()
    seen_items = df[df['user'] == int(user_id)]['item'].tolist()
    unseen_items = [anime for anime in get_trending_anime_by_genre(genre) if anime not in seen_items]
    predictions = [(anime, algo.predict(int(user_id), anime).est) for anime in unseen_items]
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:5]
## 🧪 Requirements.txt (Optional)

flask
pandas
scikit-surprise
