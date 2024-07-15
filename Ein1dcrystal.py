import numpy as np
import matplotlib.pyplot as plt

def compute_electric_field(A, B, n, k, x):
    """
    Compute the electric field E_j(x) for given parameters.
    
    Parameters:
    A (float): Amplitude A
    B (float): Amplitude B
    n (float): Refractive index
    k (float): Wave number
    x (numpy array): Array of x values
    
    Returns:
    numpy array: Electric field E_j(x)
    """
    E_j = A * np.exp(1j * n * k * x) + B * np.exp(-1j * n * k * x)
    return E_j

def plot_electric_fields(A0, B0, n_values, k, x):
    """
    Plot the electric fields E_j(x) for different refractive indices and their sum.
    
    Parameters:
    A0 (float): Initial amplitude A0
    B0 (float): Initial amplitude B0
    n_values (list of floats): List of refractive indices
    k (float): Wave number
    x (numpy array): Array of x values
    """
    plt.figure(figsize=(10, 6))

    A = A0
    B = B0
    total_field = np.zeros_like(x, dtype=complex)

    for j, n in enumerate(n_values):
        E_j = compute_electric_field(A, B, n, k, x)
        total_field += E_j
        plt.plot(x, E_j.real, label=f'E_{j} (Real part, n={n})')
        
        # Update A and B for the next iteration
        if j < len(n_values) - 1:  # Only update if there are more indices to process
            next_A = A - B
            next_B = 0
            A, B = next_A, next_B

    plt.plot(x, total_field.real, label='Total Field (Real part)', linewidth=2, color='black')

    plt.title('Electric Field E_j(x) and Total Field for Different Refractive Indices')
    plt.xlabel('x')
    plt.ylabel('E_j(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Define parameters
x = np.linspace(-0.5, 0.5, 1000)  # x values from -0.5 to 0.5
k = 2 * np.pi / 0.5  # Wave number (example value)
A0 = 1  # Initial amplitude A0
B0 = 0  # Initial amplitude B0
n_values = [1, 3.5,  1.0]  # Refractive indices (example values)

# Plot the electric fields and their sum
plot_electric_fields(A0, B0, n_values, k, x)
