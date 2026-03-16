Dist=12

if Dist<3:
    Transport="Walk"

elif Dist<15:
    Transport="Bike"

else:
    Transport="Car"

print(Transport)