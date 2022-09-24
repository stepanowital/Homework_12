def save_picture(picture):
	filename = picture.filename
	path = f"C:/Homework_12/uploads/images/{filename}"
	picture.save(path)
	return path
