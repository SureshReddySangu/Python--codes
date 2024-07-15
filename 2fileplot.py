import matplotlib.pyplot as plt

# Function to read data from a file
# Function to read data from a file
def read_data(file_path, start_col=2):
    x_data = []
    y_data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split(',')
                try:
                    # Extract the relevant columns, start_col for x and start_col + 1 for y
                    x_data.append(float(parts[start_col].strip()))
                    y_data.append(float(parts[start_col + 1].strip()))
                except (ValueError, IndexError):
                    continue  # Skip lines that do not contain valid float numbers
    except Exception as e:
        print(f"An error occurred while reading the file {file_path}: {e}")
    return x_data, y_data


# Read data from the files
fre_x, fre_y = read_data('/home/sureshreddy/Meeeep/Spyder-Codes/Band gapss/fim.dat')
fim_x, fim_y = read_data('/home/sureshreddy/Meeeep/Spyder-Codes/Band gapss/fre.dat')

# Plot the data
plt.figure(figsize=(10, 6))

plt.plot(fre_x, fre_y, label='Frequency Data (fre.dat)', color='blue', linewidth=1)
plt.plot(fim_x, fim_y, label='Imaginary Data (fim.dat)', color='red', linewidth=1)

plt.title('Frequency and Imaginary Data Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.grid(True)

#plt.savefig('/mnt/data/combined_plot.png', dpi=300)  # Save the plot with high resolution
plt.show()
