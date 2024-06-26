import sqlite3
import json
import re
import random


categories = {
    'Science and technology': ['AI', 'artificial intelligence', 'machine learning', 'data science', 'robotics', 'quantum computing', 'biotechnology', 'nanotechnology', 'cybersecurity', 'blockchain', 'cloud computing', 'IoT', 'internet of things', 'virtual reality', 'VR', 'augmented reality', 'AR', 'computer science', 'informatics', 'big data', 'analytics', 'hardware', 'software development', 'programming languages', 'Python', 'Java', 'JavaScript', 'Ruby', 'PHP', 'C++', 'R', 'SQL', 'NoSQL', 'DevOps', 'Linux', 'Windows', 'macOS', 'open-source contributions', 'tech conferences', 'STEM', 'hackathon', 'startups', 'tech startups', 'Silicon Valley', 'patent', 'innovation lab'],
    'Memes': ['dank', 'meme culture', 'viral', 'trending memes', 'meme page', 'shitpost', 'sarcasm', 'parody', 'spoof', 'internet humor', 'pop culture memes', 'meme account', 'meme lord', 'gif', 'video memes', 'meme compilation', 'meme templates', 'rage comics', 'pepe', 'doge', 'wojak', 'nft memes'],
    'Finance': ['financial markets', 'banking', 'savings', 'loans', 'mortgages', 'credit', 'debit', 'budgeting', 'personal finance', 'wealth management', 'financial planning', 'insurance', 'tax', 'accounting', 'auditing', 'fintech', 'blockchain finance', 'NFT', 'Ethereum', 'Bitcoin', 'Litecoin', 'Ripple', 'stock market', 'NASDAQ', 'Dow Jones', 'S&P 500', 'trading', 'forex', 'commodities', 'gold', 'silver', 'oil', 'bonds', 'ETFs', 'mutual funds', 'hedge funds', 'venture capital', 'private equity', 'IPO', 'economics', 'macroeconomics', 'microeconomics', 'inflation', 'deflation', 'recession', 'financial crisis', 'central bank', 'Federal Reserve', 'European Central Bank', 'IMF', 'World Bank'],
    'Beauty': ['makeover', 'beauty tips', 'beauty influencer', 'makeup tutorial', 'haircare', 'nail art', 'esthetician', 'beauty products', 'luxury beauty', 'beauty vlog', 'fashion trends', 'personal style', 'wardrobe', 'outfit', 'modeling', 'fashion design', 'textile design', 'fashion week', 'beauty salon', 'spa', 'grooming', 'perfume', 'fragrance', 'beauty subscription box', 'eco-friendly beauty', 'vegan beauty', 'cruelty-free', 'dermatology', 'cosmetic surgery', 'plastic surgery', 'body care', 'tattoo', 'piercing'],
    'Politics': ['political science', 'campaign', 'voting', 'political party', 'liberal', 'conservative', 'left-wing', 'right-wing', 'centrist', 'independent', 'activism', 'lobbying', 'diplomacy', 'international relations', 'geopolitics', 'political philosophy', 'governance', 'civil service', 'public administration', 'non-profit', 'NGO', 'United Nations', 'NATO', 'EU', 'Brexit', 'legislation', 'congress', 'parliament', 'senate', 'judiciary', 'supreme court', 'constitution', 'civil rights', 'human rights', 'election campaign', 'political debate', 'political analysis', 'political commentary', 'political blogger', 'political journalist'],
    'Comedy': ['stand-up comedy', 'comedian', 'satire', 'sketch comedy', 'improv', 'parody', 'spoof', 'sitcom', 'comedy film', 'comedy series', 'comedy club', 'comedy festival', 'humorous', 'wit', 'punchline', 'comedy podcast', 'comedy writing', 'comedy show', 'comic strip', 'cartoon', 'animation', 'funny videos', 'viral humor', 'social media comedy', 'comedy actor', 'comedy writer', 'comedy director', 'laugh track', 'slapstick', 'dark humor', 'dry humor', 'observational comedy'],
    'Health': ['public health', 'healthcare', 'medicine', 'surgery', 'pharmacy', 'nursing', 'clinical research', 'health policy', 'mental health', 'psychology', 'psychotherapy', 'counseling', 'well-being', 'self-care', 'nutrition', 'dietitian', 'weight loss', 'bodybuilding', 'exercise', 'yoga', 'pilates', 'meditation', 'alternative medicine', 'holistic health', 'naturopathy', 'acupuncture', 'physical therapy', 'rehabilitation', 'occupational therapy', 'vaccination', 'epidemiology', 'disease prevention', 'health education', 'fitness coaching', 'personal trainer', 'health tech', 'wearable tech', 'health apps', 'telemedicine', 'e-health'],
    'Sports': ['competitive sports', 'team sports', 'individual sports', 'Olympic sports', 'Paralympic sports', 'world cup', 'championship', 'league', 'tournament', 'athletics', 'track and field', 'gymnastics', 'swimming', 'cycling', 'boxing', 'martial arts', 'wrestling', 'basketball', 'football', 'soccer', 'baseball', 'tennis', 'golf', 'rugby', 'cricket', 'hockey', 'ice hockey', 'skiing', 'snowboarding', 'skateboarding', 'surfing', 'eSports', 'sports training', 'coaching', 'sports medicine', 'sports nutrition', 'sports psychology', 'sports gear', 'sports apparel', 'sports fan', 'sports media', 'sports journalism', 'sports betting', 'fantasy sports'],
    'Music': ['music production', 'music theory', 'composition', 'songwriting', 'music performance', 'live music', 'concert', 'tour', 'music festival', 'musician', 'composer', 'singer-songwriter', 'instrumentalist', 'band member', 'orchestra', 'choir', 'DJ', 'electronic music', 'pop music', 'rock music', 'jazz music', 'classical music', 'hip hop music', 'rap music', 'country music', 'folk music', 'blues music', 'R&B', 'soul music', 'reggae', 'world music', 'indie music', 'alternative music', 'music video', 'music streaming', 'record label', 'music industry', 'music technology',],
    'Writes': ['write', 'book', 'author', 'novel', 'poetry', 'essay', 'literature', 'fiction',
               'non-fiction', 'publishing', 'editor', 'journalism', 'articles', 'blogs', 'writing tips',
               'creative writing', 'biography', 'memoir', 'short story', 'screenwriting', 'playwriting',
               'copywriting', 'critique', 'editorial', 'freelance writing']
}


# Your categories dictionary and categorize_description function go here

# categories = {
#     'Science and technology': ['technology', 'science', 'engineering', 'innovation', 'research', 'softwareengineer', 'software', 'developer', 'code', 'coding', 'sde', 'SDE', 'github', 'Github', 'open source', 'Open Source', 'OpenSource', 'fellow', 'MLH', 'mlh'],
#     'Memes': ['meme', 'funny', 'lol', 'haha', 'joke'],
#     'Finance': ['finance', 'money', 'economy', 'stock', 'investment', 'crypto'],
#     'Beauty': ['beauty', 'makeup', 'cosmetic', 'skincare', 'fashion', 'design'],
#     'Politics': ['politics', 'government', 'policy', 'election', 'democracy'],
#     'Comedy': ['comedy', 'funny', 'joke', 'humor', 'laugh'],
#     'Health': ['health', 'medical', 'wellness', 'fitness', 'diet'],
#     'Sports': ['sports', 'game', 'team', 'athlete', 'olympics'],
#     'Music': ['music', 'song', 'band', 'singer', 'album', 'vocals', 'Vocalist'],
#     'Writes': ['write', 'book', 'author', 'novel', 'poetry', 'essay']
# }

# print(categories.keys())


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
        # return [random.choice(list(categories.keys())), random.choice(list(categories.keys()))]
        return []

    # If you want to return categories sorted by match count
    sorted_categories = sorted(
        matched_categories.items(), key=lambda x: x[1], reverse=True)
    category = [category for category, count in sorted_categories]
    # category.append(random.choice(list(categories.keys())))
    return category


# Connect to your SQLite database
conn = sqlite3.connect('social_media_data.db')
cursor = conn.cursor()

# Select all rows from your table
cursor.execute("SELECT entryId, description FROM users")
rows = cursor.fetchall()

# Iterate over each row
for row in rows:
    id, description = row
    # Use your function to get the categories for the description
    categoriesss = categorize_description(description)

    # Convert the list of categories to a JSON string for storage
    categories_str = json.dumps(categoriesss)

    # Update the row with the new tags
    cursor.execute(
        "UPDATE users SET tags = ? WHERE entryId = ?", (categories_str, id))

# Commit the changes and close the connection
conn.commit()
conn.close()
