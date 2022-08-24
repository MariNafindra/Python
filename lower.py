# To open the first file in read mode
f1 = open("E:\Documents\file.txt", "r")
  
# To open the second file in write mode
f2 = open("E:\Documents\file_2.txt", "w")
  
# For loop to traverse through the file
for line in f1:
  
    # Writing the content of the first
    # file to the second file
      
    # Using upper() function to
    # capitalize the letters
    f2.write(line.lower())  