from json import JSONDecodeError
import logging
from flask import Blueprint, render_template, request
from loader.utils import save_picture
from functions import add_posts

load_blueprint = Blueprint("load_blueprint", __name__)


@load_blueprint.route("/add_post")
def add_post_page():
	return render_template("post_form.html")


@load_blueprint.route("/add_post", methods=["POST"])
def uploaded_post_page():
	# Получаем объект картинки из формы
	picture = request.files.get("picture")

	# Получаем текст поста из формы
	content = request.form.get("content")

	if not content:
		content = "В качестве подписи ничего не придумано"

	if not picture:
		logging.info("Отсутствует фотография, повторите попытку")
		return "Отсутствует фотография, повторите попытку"

	if picture.filename.split(".")[-1] not in ["jpg", "png", "jpeg"]:
		logging.info("Неверный файл (фото)")
		return "Неверный файл (фото)"

	try:
		picture_path = save_picture(picture)
	except FileNotFoundError:
		logging.error("Файл картинки не найден")
		return "Файл картинки не найден"
	except JSONDecodeError:
		logging.error("Файл испорчен")
		return "Файл испорчен"
	path_for_page = picture_path[14:]
	post = add_posts({"pic": path_for_page, "content": content})

	return render_template("post_uploaded.html", post=post)
