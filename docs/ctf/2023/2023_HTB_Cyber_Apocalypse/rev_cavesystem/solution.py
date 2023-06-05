import subprocess

characters = [i for i in range(32,127)]

s = "{}"
v5 = "{}"
v6 = "{}"
v7 = "{}"
v8 = "{}"
v9 = "{}"
v10 = "{}"
v11 = "{}"
v12 = "{}"
v13 = "{}"
v14 = "{}"
v15 = "{}"
v16 = "{}"
v17 = "{}"
v18 = "{}"
v19 = "{}"

c_list = [s,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19]
e_list = []

for c1 in characters:
    for c2 in characters:
        if c1 * c2 == 20:
            
