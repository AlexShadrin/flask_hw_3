from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

from ..user.views import get_user_name

article = Blueprint("article", __name__, url_prefix="/article", static_folder="../static")

ARTICLES = {
    1: {
        "title": "Title 1",
        "text": "text 1",
        "author": 2
    },
    2: {
        "title": "Title 2",
        "text": "text 2",
        "author": 2
    },
    3: {
        "title": "Title 3",
        "text": "text 3",
        "author": 1
    },
    4: {
        "title": "Title 4",
        "text": "text 4",
        "author": 3
    }
}


@article.route("/")
@login_required
def article_list():
    return render_template(
        "articles/list.html",
        articles=ARTICLES
    )


@article.route("/<int:pk>")
@login_required
def get_article(pk: int):
    if pk in ARTICLES:
        article_raw = ARTICLES[pk]
    else:
        raise NotFound("Article id:{}, not found".format(pk))
    title = article_raw["title"]
    text = article_raw["text"]
    author = get_user_name(article_raw["author"])
    return render_template(
        "articles/details.html",
        title=title,
        text=text,
        author=author
    )
