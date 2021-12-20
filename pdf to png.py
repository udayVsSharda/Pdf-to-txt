import pdf2image as pi
import pymsgbox as msg
path = msg.prompt("Enter the the pdf file path.\nEnter 'NO' to exit.","Info Request","NO")
if path == "NO":
    exit()
print("hi")
images = pi.conver_from_path(path,fmt="png",grayscale=True)

