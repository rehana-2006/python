# A file manager needs to classify files based on their extension.
# .csv  → print output as "This is an Excel File"
# .jpg  → print output as "This is a JPEG File"
# .doc  → print output as "This is a Word File"
# .pdf → print output as "This is a PDF File"
# .py → print output as "This is a Python File"
# .Any other input, print output as "Unknown File Type"
# Print the result based on the input
# Sample Input:
# .csv
# Sample Output:
# This is an Excel file
# Sample input:
# .py
# Sample Output:
# This is a Python File

f=input("Enter the file extension:")
match f:
    case ".csv":
        print("This is an Excel file")
    case ".jpg":
        print("This is a JPEG file")
    case ".doc":
        print("This is a word file")
    case ".pdf":
        print("This is a PDF file")
    case ".py":
        print("This is a python file")
    case _:
        print("Unknown File Type")