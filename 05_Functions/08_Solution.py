def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Shaktiman",power="Lazer")
print_kwargs(name="Shaktiman")
print_kwargs(power="Lazer")

