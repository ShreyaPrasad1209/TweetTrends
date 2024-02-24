import re
import random


def is_valid_twitter_username(username):
    """
    Check if the provided username is a valid Twitter username.

    Args:
    - username (str): The Twitter username to validate.

    Returns:
    - bool: True if valid, False otherwise.
    """
    # Check the length of the username
    if len(username) < 4 or len(username) > 15:
        return False

    # Check for invalid characters
    if not re.match("^[A-Za-z0-9_]+$", username):
        return False

    # Check for restricted words
    if "twitter" in username.lower() or "admin" in username.lower():
        return "False"

    return "True"


# Categories and their associated keywords/patterns
categories = {
    'Science and technology': ['technology', 'science', 'engineering', 'innovation', 'research', 'softwareengineer', 'software', 'developer', 'code', 'coding', 'sde', 'SDE', 'github', 'Github'],
    'Memes': ['meme', 'funny', 'lol', 'haha', 'joke'],
    'Finance': ['finance', 'money', 'economy', 'stock', 'investment', 'crypto'],
    'Beauty': ['beauty', 'makeup', 'cosmetic', 'skincare', 'fashion', 'design'],
    'Politics': ['politics', 'government', 'policy', 'election', 'democracy'],
    'Comedy': ['comedy', 'funny', 'joke', 'humor', 'laugh'],
    'Health': ['health', 'medical', 'wellness', 'fitness', 'diet'],
    'Sports': ['sports', 'game', 'team', 'athlete', 'olympics'],
    'Music': ['music', 'song', 'band', 'singer', 'album', 'vocals', 'Vocalist'],
    'Writes': ['write', 'book', 'author', 'novel', 'poetry', 'essay']
}


def categorize_description(description):
    description = description.lower()
    matched_categories = {}

    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', description):
                if category in matched_categories:
                    matched_categories[category] += 1
                else:
                    matched_categories[category] = 1

    # Filter categories to include those with matches
    # You can adjust the logic here if you want to set a threshold for matches
    matched_categories = {category: count for category,
                          count in matched_categories.items() if count > 0}

    if not matched_categories:
        # or return an empty list if you prefer []
        return [random.choice(list(categories.keys())), random.choice(list(categories.keys()))]

    # If you want to return categories sorted by match count
    sorted_categories = sorted(
        matched_categories.items(), key=lambda x: x[1], reverse=True)
    category = [category for category, count in sorted_categories]
    category.append(random.choice(list(categories.keys())))
    return category
