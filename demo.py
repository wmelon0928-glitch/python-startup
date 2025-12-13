

def parse_numbers(s): return list(map(float, s.split(',')))
#    return list(map(float, (tok.strip() for tok in s.split(',') if tok.strip())))

txt = input("Enter your input:")


print(f"You entered: [{txt}], type={type(txt)}")
txt = txt.strip()
print(f"trip txt=[{txt}], type={type(txt)}")

txt = txt + 0 #TypeError: can only concatenate str (not "int") to str
# txt = int(txt) + 0
# txt = int(txt) + 0.0

print(f"int txt=[{txt}], type={type(txt)}")

txt = float(txt) + 0 
# txt = float(txt) +0.0
print(f"float txt=[{txt}], type={type(txt)}")

txt = int(txt)
print(f"int txt=[{txt}], type={type(txt)}")

