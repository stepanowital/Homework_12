from json import JSONDecodeError
import logging
from flask import Blueprint, render_template, request


from functions import search_post, load_posts


view_blueprint = Blueprint("view_blueprint", __name__)


@view_blueprint.route("/")
def view_blueprint_page():
	return render_template("index.html")


@view_blueprint.route("/search")
def list_page():
	s = request.args.get("s")
	logging.info("Выполняю поиск")
	try:
		result = search_post(s)
	except FileNotFoundError:
		logging.error("Файл posts.json не найден")
		return "Файл posts.json не найден"
	except JSONDecodeError:
		logging.error("Файл испорчен")
		return "Файл испорчен"
	return render_template("post_list.html", s=s, result=result)
