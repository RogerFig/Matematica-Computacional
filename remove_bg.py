from PIL import Image
import os

def convertImage(fileName):
	img = Image.open(f"./aula7/figs/old/{fileName}")


	img = img.convert("RGBA")

	datas = img.getdata()

	newData = []

	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2] == 255:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

	img.putdata(newData)
	img.save(f"./aula7/figs/{fileName}.png", "PNG")
	print("Successful")

for f in os.listdir("./aula7/figs/old/"):
		if f.endswith(".png"):
			convertImage(f)


