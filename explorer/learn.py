with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)
    new_data = data.replace(";","l")
with open("practice.txt","w") as f:
    f.write(new_data)
print ("File overwritten successfully.")