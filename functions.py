import json


def load_posts():
    with open("posts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def search_post(s):
    result = []
    for post in load_posts():
        if s.lower() in post["content"].lower():
            result.append(post)
    return result


def add_posts(post):
    posts = load_posts()
    posts.append(post)
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file)
    return post
