import pdf2image as pi
import pymsgbox as msg
path = msg.prompt("Enter the the pdf file path.\nEnter 'NO' to exit.","Info Request","NO")
if path == "NO":
    exit()
print("hi")
images = pi.convert_from_path(path,fmt="png",grayscale=True,poppler_path="C:\Users\ernsp\Documents\Python\poppler-0.68.0\bin")

