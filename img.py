import google.generativeai as genai
from PIL import Image  # PIL - Python Img Lib.'''
img = Image.open(r"C:\Users\HP\Downloads\puppy.jpg")  #r - raw data or else it read as the string 
genai.configure(api_key="AIzaSyAaVHIyDw6wsvPqWBfrxnLiN-HqDbDyAcE")
model=genai.GenerativeModel("gemini-2.5-flash")
prompt=input("enter the question")
response = model.generate_content([prompt,img])  # (prompt+a) or ([prompt,a])'''
print(response.text)