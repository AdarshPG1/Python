password="12345565"

if len(password)<6:
    valid="weak"

elif len(password)<10:
    valid="Medium"

else:
    valid="Strong"

print("Password is :",valid)
    
