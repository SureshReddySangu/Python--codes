import matplotlib.pyplot as plt

# Initialize empty lists to hold x and y values
x = []
y = []

# Function to check if a string can be converted to a float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Open the file and read its contents
try:
    with open(r'/home/sureshreddy/Meeeep/Spyder-Codes/Band gapss/flux', 'r') as f:
        for row in f:
            # Split the row into columns
            columns = row.split(',')
            # Check for at least 3 columns
            if len(columns) >= 3:
                try:
                    # Convert to float only if valid
                    x.append(float(columns[1]))
                    y.append(float(columns[2]))
                except ValueError:
                    # Handle invalid data (optional: print a warning)
                    pass
except FileNotFoundError:
    print("Error: File not found!")
# Plot the data
plt.figure(dpi=100)
plt.plot(x, y, marker='o', linewidth=0.5)
plt.title("Flux vs f")
plt.xlabel('val')
plt.ylabel('va')
plt.grid(True)
plt.show()