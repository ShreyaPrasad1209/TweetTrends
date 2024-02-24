from pydantic import BaseModel
from fastapi import FastAPI, Query
from .utils import is_valid_twitter_username
from databases import Database
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Update this path to your SQLite database file
DATABASE_URL = "sqlite:///./social_media_data.db"
database = Database(DATABASE_URL)


class UserProfile(BaseModel):
    name: str
    screen_name: str
    profile_image_url_https: str


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/verify_user/{username}")
def verify_user(username: str):
    validity: str = is_valid_twitter_username(username=username)
    return {"is_valid": validity}


@app.get("/search/", response_model=List[UserProfile])
async def search(tags: Optional[List[str]] = Query(None)):
    if not tags:
        return []

    # Constructing the WHERE clause to search for any of the tags within the JSON array
    where_clause = " OR ".join([f"tags LIKE '%\"{tag}\"%'" for tag in tags])

    query = f"""
    SELECT name, screen_name, profile_image_url_https
    FROM users
    WHERE {where_clause}
    ORDER BY RANDOM()
    LIMIT 10
    """

    rows = await database.fetch_all(query=query)

    return [UserProfile(name=row["name"], screen_name=row["screen_name"], profile_image_url_https=row["profile_image_url_https"]) for row in rows]
