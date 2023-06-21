filename = input("please enter the filename:")

parts = filename.split(".")

if len(parts)>1:
    extension = parts[-1]
    print ("The extension of the file is:", extension)
else:
    print("there is no extension")