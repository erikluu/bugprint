from bugprint import bp, bp_setup

bp_setup(verbose=True)

def add(x, y):
    print(f"Adding {x} + {y} = {x + y}")
    bp()

def subtract(x, y):
    print(f"Subtracting {x} - {y} = {x - y}")
    bp()

# Call bp() at specific lines in your code
bp()
add(1, 2)
bp()
subtract(5, 4)
bp()
