f_name=input("Enter the first name")
l_name=input("Enter the Last name")
def convert(f_name,l_name):
    f_name=f_name.lower()
    l_name=l_name.lower()
    full_name=f_name.capitalize()+" "+l_name.capitalize()
    return full_name
out=convert(f_name,l_name)
print(out)