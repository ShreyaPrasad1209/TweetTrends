from twitter.account import Account
from twitter.scraper import Scraper
email, username, password = "blossomlabs.io@gmail.com", "@BlossomL67796", "Python1991!"
print(email, username, password)
scraper = Scraper(username=username, password=password)
following = scraper.following(
    [1132563136186183680, 1126068392308297729, 402064691, 18839785, 159822053, 14343311])
print(following)
# # with open("data/userdata.json", "wb") as f:
# #     f.write(following)

# scraper = Scraper(username, password)

# user_id = "shreyacasmalert"
# cursor = '1|200'  # example cursor
# limit = 100  # arbitrary limit for demonstration
# follower_subset, last_cursor = scraper.followers(
#     [user_id], limit=limit)

# # use last_cursor to resume pagination
