with open("task5.txt","w") as file:
    file.write("Hello! My name is Boya Rajesh.\n"
               "I'm passionate about learning new technologies and exploring new things.\n"
               "I enjoy traveling, cooking, reading, and listening to music.\n"
               "I'm currently building my skills in Python,Web Developement.\n"
               "I believe in consistent learning and staying curious.")
with open("task5.txt","a") as file:
    file.write("\n\nThis is appended line")
with open("task5.txt","r") as file:
    content=file.read()
print("The content in the file is : ")
print(content)