final_data = []

file_name = r"/home/ahmed/Bureau/archive/log2.txt"
#file2 = r"/home/ahmed/Bureau/archive/log2.txt"

with open(file_name, "r") as f:
    data = f.read().rstrip()
    data = data.replace('\r', '\n')
    data = data.split('\n')
    for line in data :
        if len(line) > 3 :
            final_data.append(line)

    
    
        
with open(file_name, "w") as f:
    f.write("\n".join(final_data))


