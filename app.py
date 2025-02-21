from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

# Load profiles from JSON file
def load_profiles():
    try:
        with open("/home/nixon-wainaina/Documents/dating/profile.json", "r") as file:
            data = json.load(file)
            return data.get("profiles", [])  # Default to empty list if key is missing
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file is missing or invalid

profiles = load_profiles()

# Interest mapping for related interests
interest_mapping = {
    "travelling": ["hiking", "adventure", "exploring"],
    "working out": ["fitness", "yoga", "sports"],
    "watching movies": ["cinema", "documentaries", "series"],
    "reading": ["books", "writing", "poetry"],
    "listening to music": ["singing", "dancing", "concerts"],
    "gaming": ["chess", "board games", "puzzles"],
    "volunteering": ["community service", "charity", "mentoring"]
}

# Matchmaking function
def calculate_compatibility(profile_a, profile_b):
    if profile_a["gender"] == profile_b["gender"]:
        return 0  # Skip same-gender matches

    age_diff = abs(profile_a["age"] - profile_b["age"])
    age_score = max(0, 1 - (age_diff / 10)) * 0.3  # Age weight 30%

    interest_score = 0
    total_interests = len(profile_a["interests"])
    
    if total_interests > 0:  # Avoid division by zero
        for interest in profile_a["interests"]:
            if interest in profile_b["interests"]:
                interest_score += 1
            for related in interest_mapping.get(interest, []):
                if related in profile_b["interests"]:
                    interest_score += 0.5  # Partial match
        interest_score = (interest_score / total_interests) * 0.4  # 40% weight

    location_score = 0.2 if profile_a["location"] == profile_b["location"] else 0
    love_language_score = 0.1 if profile_a["love_language"] == profile_b["love_language"] else 0

    return round(age_score + interest_score + location_score + love_language_score, 2)

# Get best matches for a user
def find_best_matches(user_profile):
    matches = [
        {
            "name": profile["name"],
            "age": profile["age"],
            "gender": profile["gender"],
            "location": profile["location"],
            "love_language": profile["love_language"],
            "hobbies": profile["interests"],
            "score": calculate_compatibility(user_profile, profile)
        }
        for profile in profiles 
        if profile["name"] != user_profile["name"] 
        and profile["gender"] != user_profile["gender"]  # Only show opposite gender
    ]

    return sorted(matches, key=lambda x: x["score"], reverse=True)[:5]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/match.html", methods=["GET", "POST"])
def match():
    if not request.method in ["GET", "POST"]:
        return redirect(url_for("home"))
        
    try:
        if request.method == "POST":
            form_data = request.form
        else:
            form_data = request.args

        user_profile = {
            "name": form_data.get("name"),
            "gender": form_data.get("gender"),
            "age": int(form_data.get("age")),
            "location": form_data.get("location"),
            "love_language": form_data.get("loveLanguage"),
            "interests": form_data.getlist("hobbies")
        }

        matches = find_best_matches(user_profile)
        return render_template("match.html", matches=matches)
    except Exception as e:
        print(f"Error processing match: {e}")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
