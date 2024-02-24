import json
import os
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data = json.load(f)
# with open("data/raw/14343311/1708798016594631000_Following.json", "r") as f:
#     data2 = json.load(f)
# with open("data/raw/14343311/1708798017835932000_Following.json", "r") as f:
#     data3 = json.load(f)
# with open("data/raw/14343311/1708798018545539000_Following.json", "r") as f:
#     data4 = json.load(f)
# with open("data/raw/14343311/1708798019262354000_Following.json", "r") as f:
#     data5 = json.load(f)
# with open("data/raw/14343311/1708798019947568000_Following.json", "r") as f:
#     data6 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data7 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data8 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data9 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data10 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data11 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data12 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data13 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data14 = json.load(f)
# with open("data/raw/14343311/1708798015331893000_Following.json", "r") as f:
#     data15 = json.load(f)
# Function to extract and print the required information


# def extract_info(data):
#     entries = data.get("data", {}).get("user", {}).get("result", {}).get(
#         "timeline", {}).get("timeline", {}).get("instructions", [])

#     for instruction in entries:
#         if instruction.get("type") == "TimelineAddEntries":
#             for entry in instruction.get("entries", []):
#                 content = entry.get("content", {}).get("itemContent", {}).get(
#                     "user_results", {}).get("result", {}).get("legacy", {})
#                 if content:
#                     print(f"entryId: {entry.get('entryId')}")
#                     print(
#                         f"is_blue_verified: {content.get('is_blue_verified')}")
#                     print(f"description: {content.get('description')}")
#                     urls = content.get("entities", {}).get(
#                         "url", {}).get("urls", [])
#                     print("URLs:")
#                     for url in urls:
#                         print(f"  - {url.get('expanded_url')}")
#                     print(
#                         f"favourite_count: {content.get('favourites_count')}")
#                     print(f"followers_count: {content.get('followers_count')}")
#                     print(f"location: {content.get('location')}")
#                     print(f"name: {content.get('name')}")
#                     print(
#                         f"normal_followers_count: {content.get('normal_followers_count')}")
#                     print(
#                         f"profile_image_url_https: {content.get('profile_image_url_https')}")
#                     print(f"screen_name: {content.get('screen_name')}")
#                     print("------------------------------------------------")


# Call the function with the provided JSON data
# extract_info(data)
# extract_info(data2)
# extract_info(data3)
import sqlite3
import json

# # JSON data as provided in the previous example
# with open("data/raw/1184206092714164224/1708791992850662000_Following.json", "r") as f:
#     data = json.load(f)

# # with open("data/raw/1184206092714164224/1708791994255304000_Following.json", "r") as f:
# #     data2 = json.load(f)


# Connect to SQLite database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('social_media_data.db')
cursor = conn.cursor()

# Create table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     entryId TEXT PRIMARY KEY,
#     rest_id TEXT,
#     description TEXT,
#     urls TEXT,
#     favourite_count INTEGER,
#     followers_count INTEGER,
#     location TEXT,
#     name TEXT,
#     normal_followers_count INTEGER,
#     profile_image_url_https TEXT,
#     screen_name TEXT
# )
# ''')

# Function to insert data into the database


def insert_data(entry):
    cursor.execute('SELECT entryId FROM users WHERE entryId = ?', (entry[0],))
    data = cursor.fetchone()
    if data is None:
        cursor.execute('''
        INSERT INTO users (entryId, description, urls, favourite_count, followers_count, location, name, normal_followers_count, profile_image_url_https, screen_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', entry)
        conn.commit()
    else:
        # If entryId exists, skip this entry
        print(
            f"Entry with entryId {entry[0]} already exists. Skipping insertion.")

# Function to extract information and prepare it for insertion


def extract_and_insert_info(data):
    entries = data.get("data", {}).get("user", {}).get("result", {}).get(
        "timeline", {}).get("timeline", {}).get("instructions", [])

    for instruction in entries:
        if instruction.get("type") == "TimelineAddEntries":
            for entry in instruction.get("entries", []):
                content = entry.get("content", {}).get("itemContent", {}).get(
                    "user_results", {}).get("result", {}).get("legacy", {})
                if content:
                    urls = ', '.join([url.get('expanded_url') for url in content.get(
                        "entities", {}).get("url", {}).get("urls", [])])
                    entry_data = (
                        entry.get('entryId'),
                        content.get('description'),
                        urls,
                        content.get('favourites_count'),
                        content.get('followers_count'),
                        content.get('location'),
                        content.get('name'),
                        content.get('normal_followers_count'),
                        content.get('profile_image_url_https'),
                        content.get('screen_name')
                    )
                    insert_data(entry_data)


def read_and_insert_data():
    folder_path = "data/raw/159822053"
    files = os.listdir(folder_path)
    for file_name in files:
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)

        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Open and read the file
            with open(file_path, "r") as f:
                data = json.load(f)
            extract_and_insert_info(data)
            print(file_path)


read_and_insert_data()

# Extract and insert data
# extract_and_insert_info(data)
# extract_and_insert_info(data2)
# extract_and_insert_info(data3)
# extract_and_insert_info(data4)
# extract_and_insert_info(data5)
# extract_and_insert_info(data6)
# Close the connection
conn.close()
