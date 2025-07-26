from PIL import Image 
import os
print(os.path.abspath("teto.jpg"))
# /home/nasor/Downloads/thunderbird.tmp/teto.jpg
myiamge = Image.open("/home/nasor/Downloads/thunderbird.tmp/one/nano.webp")
myiamge.show()
mybox=(30,19,50,50)
a= myiamge.crop(mybox)
a.show()
a=myiamge.convert("L")
a.show()