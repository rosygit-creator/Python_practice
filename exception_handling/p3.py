

try:
    with open ("f1.txt", 'r') as f:
        line=f.read()
except FileNotFoundError:
    print("File not found") 
   
