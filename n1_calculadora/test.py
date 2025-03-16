lines = []

with open("./contenido.py", "r") as f:
    lines = [line.rstrip()+"\n" for line in f.readlines()]
    
with open("./contenido_mejorado.py", "w") as f:
    f.writelines(lines)