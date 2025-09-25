from flask import Flask, render_template, request
import pandas as pd
import os
app = Flask(__name__)

# Sample user-anime ratings
sample_data = [
    {'user': 1, 'item': 'Attack on Titan', 'rating': 5, 'genre': 'Action'},
    {'user': 1, 'item': 'Re:Zero', 'rating': 4, 'genre': 'Isekai'},
    {'user': 2, 'item': 'One Piece', 'rating': 4, 'genre': 'Adventure'},
    {'user': 2, 'item': 'Bleach', 'rating': 3, 'genre': 'Action'},
    {'user': 3, 'item': 'Death Note', 'rating': 5, 'genre': 'Psychological'},
    {'user': 3, 'item': 'Naruto', 'rating': 4, 'genre': 'Action'},
    {'user': 4, 'item': 'Demon Slayer', 'rating': 5, 'genre': 'Fantasy'},
    {'user': 4, 'item': 'Jujutsu Kaisen', 'rating': 4, 'genre': 'Supernatural'}
]

df = pd.DataFrame(sample_data)

# def train_model():
#     reader = Reader(rating_scale=(1, 5))
#     data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)
#     trainset = data.build_full_trainset()
#     algo = SVD()
#     algo.fit(trainset)
#     return algo

def get_trending_anime_by_genre(genre):
    fallback = {
        "Action": ["Attack on Titan", "Naruto", "Bleach"],
        "Isekai": ["Re:Zero", "No Game No Life"],
        "Fantasy": ["Demon Slayer", "Made in Abyss"],
        "Psychological": ["Death Note", "Paranoia Agent"],
        "Supernatural": ["Jujutsu Kaisen", "Mob Psycho 100"],
        "Adventure": ["One Piece", "Hunter x Hunter"]
    }
    return fallback.get(genre, [])

def recommend(user_id, genre):
    # algo = train_model()
    user_id = int(user_id)
    seen_items = df[df['user'] == user_id]['item'].tolist()
    # unseen_items = [anime for anime in get_trending_anime_by_genre(genre) if anime not in seen_items]
    # predictions = [(anime, algo.predict(user_id, anime).est) for anime in unseen_items]
    # predictions.sort(key=lambda x: x[1], reverse=True)
    # Candidate anime (from fallback list for chosen genre)
    candidates = [anime for anime in get_trending_anime_by_genre(genre) if anime not in seen_items]

    # If we had ratings in df, take avg rating for that anime
    avg_ratings = df.groupby("item")["rating"].mean().to_dict()

    # Predict scores: use avg rating if available, else 3.0 baseline
    predictions = [(anime, avg_ratings.get(anime, 3.0)) for anime in candidates]

    # Sort high → low
    predictions.sort(key=lambda x: x[1], reverse=True)
    return predictions[:5]

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    genres = ["Action", "Isekai", "Fantasy", "Psychological", "Supernatural", "Adventure"]
    if request.method == "POST":
        user_id = request.form['user_id']
        genre = request.form['genre']
        if user_id.isdigit():
            recommendations = recommend(user_id, genre)
    return render_template("index.html", recommendations=recommendations, genres=genres)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT if available
    app.run(host="0.0.0.0", port=port, debug=False)


