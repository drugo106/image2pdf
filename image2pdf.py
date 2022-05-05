from PIL import Image
import sys

#image1 = Image.open(sys.argv[1])
#im1 = image1.convert('RGB')
#name = sys.argv[1].split('.')[0] + ".pdf" if len(sys.argv) <= 2 else sys.argv[2]
#im1.save(name)

imglist = sys.argv[1:len(sys.argv)-1]
name = sys.argv[-1] if ".pdf" in sys.argv[-1] else sys.argv[-1] + ".pdf"
img = Image.open(sys.argv[1])
print(imglist)
img.save(name,save_all=True,append_images=list(map(lambda x: Image.open(x), imglist[1:])))
