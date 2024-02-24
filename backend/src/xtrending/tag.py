import sqlite3
import json
import re
import random
# Your categories dictionary and categorize_description function go here

categories = {
    'Science and technology': ['technology', 'science', 'engineering', 'innovation', 'research', 'softwareengineer', 'software', 'developer', 'code', 'coding', 'sde', 'SDE', 'github', 'Github', 'open source', 'Open Source', 'OpenSource', 'fellow', 'MLH', 'mlh'],
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

print(categories.keys())

# def categorize_description(description):
#     description = description.lower()
#     matched_categories = {}

#     for category, keywords in categories.items():
#         for keyword in keywords:
#             if re.search(r'\b' + re.escape(keyword) + r'\b', description):
#                 if category in matched_categories:
#                     matched_categories[category] += 1
#                 else:
#                     matched_categories[category] = 1

#     # Filter categories to include those with matches
#     # You can adjust the logic here if you want to set a threshold for matches
#     matched_categories = {category: count for category,
#                           count in matched_categories.items() if count > 0}

#     if not matched_categories:
#         # or return an empty list if you prefer []
#         return [random.choice(list(categories.keys())), random.choice(list(categories.keys()))]

#     # If you want to return categories sorted by match count
#     sorted_categories = sorted(
#         matched_categories.items(), key=lambda x: x[1], reverse=True)
#     category = [category for category, count in sorted_categories]
#     category.append(random.choice(list(categories.keys())))
#     return category


# # Connect to your SQLite database
# conn = sqlite3.connect('social_media_data.db')
# cursor = conn.cursor()

# # Select all rows from your table
# cursor.execute("SELECT entryId, description FROM users")
# rows = cursor.fetchall()

# # Iterate over each row
# for row in rows:
#     id, description = row
#     # Use your function to get the categories for the description
#     categoriesss = categorize_description(description)

#     # Convert the list of categories to a JSON string for storage
#     categories_str = json.dumps(categoriesss)

#     # Update the row with the new tags
#     cursor.execute(
#         "UPDATE users SET tags = ? WHERE entryId = ?", (categories_str, id))

# # Commit the changes and close the connection
# conn.commit()
# conn.close()
