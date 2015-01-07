from PIL import Image
import glob
import config
import os

images = glob.glob(config.image_src+"*")

for imagepath in images:
  if imagepath.find(config.image_prefix) == -1 or config.image_prefix=="":
    if os.path.isdir(imagepath)==False:
      image = Image.open(imagepath)
      print(imagepath, image.format, "%dx%d" % image.size, image.mode)
      optimagename = imagepath.replace(config.image_src,config.image_dest+config.image_prefix)
      print(optimagename)
      image.save(optimagename,quality=config.quality,optimize=True)
    else:
      print(imagepath+" is dir")

print("\n==============================================\n")

print(images)