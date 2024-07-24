import numpy as np
import matplotlib.pyplot as plt

# Wavelength range (micrometers)
wavelength = np.linspace(0.1, 2.0, 200)  # 0.1 to 2.0 µm, 200 points

# Layer properties
layerWidth = np.array([0.15, 0.25, 0.15, 0.25, 0.15, 0.25, 0.15, 0.25, 0.15])  # Thicknesses in µm
layerRI = np.array([3.5, 1, 3.5, 1, 3.5, 1, 3.5, 1, 3.5])  # Refractive indices

# Number of wavelengths
num_wavelengths = len(wavelength)

# Initialize array to store solutions
reflectance_spectrum = np.zeros(num_wavelengths)

# Loop over each wavelength
for wl_idx in range(num_wavelengths):
    # Compute wave number
    k0 = 2 * np.pi / wavelength[wl_idx]

    # Initialize coefficient matrix and free term vector
    num_layers = len(layerWidth)
    coefMatrix = np.zeros((2 * num_layers + 2, 2 * num_layers + 2), dtype=np.complex128)
    freeTermVector = np.zeros(2 * num_layers + 2, dtype=np.complex128)

    # Initial coefficients (A0 = 1)
    coefMatrix[0, 0:3] = [1, -1, -1]
    coefMatrix[1, 0:3] = [-1j * k0, -1j * k0 * layerRI[0], 1j * k0 * layerRI[0]]

    # Current interface position
    xCurrent = layerWidth[0]

    # Loop over interfaces
    for boundary_idx in range(num_layers - 1):
        # Boundary conditions at the interface
        coefMatrix[2 * (boundary_idx + 1), 2 * boundary_idx:2 * boundary_idx + 4] = [
            np.exp(1j * k0 * layerRI[boundary_idx] * xCurrent),
            np.exp(-1j * k0 * layerRI[boundary_idx] * xCurrent),
            -np.exp(1j * k0 * layerRI[boundary_idx + 1] * xCurrent),
            -np.exp(-1j * k0 * layerRI[boundary_idx + 1] * xCurrent)
        ]

        # Derivative boundary conditions
        coefMatrix[2 * (boundary_idx + 1) + 1, 2 * boundary_idx:2 * boundary_idx + 4] = [
            1j * k0 * layerRI[boundary_idx] * np.exp(1j * k0 * layerRI[boundary_idx] * xCurrent),
            -1j * k0 * layerRI[boundary_idx] * np.exp(-1j * k0 * layerRI[boundary_idx] * xCurrent),
            -1j * k0 * layerRI[boundary_idx + 1] * np.exp(1j * k0 * layerRI[boundary_idx + 1] * xCurrent),
            1j * k0 * layerRI[boundary_idx + 1] * np.exp(-1j * k0 * layerRI[boundary_idx + 1] * xCurrent)
        ]

        # Update current interface position
        xCurrent += layerWidth[boundary_idx + 1]

    # Last boundary conditions manually set (BN+1 = 0)
    coefMatrix[2 * num_layers, 2 * (num_layers - 1):2 * (num_layers - 1) + 3] = [
        np.exp(1j * k0 * layerRI[-1] * xCurrent),
        np.exp(-1j * k0 * layerRI[-1] * xCurrent),
        -np.exp(1j * k0 * xCurrent)
    ]
    coefMatrix[2 * num_layers + 1, 2 * (num_layers - 1):2 * (num_layers - 1) + 3] = [
        1j * k0 * layerRI[-1] * np.exp(1j * k0 * layerRI[-1] * xCurrent),
        -1j * k0 * layerRI[-1] * np.exp(-1j * k0 * layerRI[-1] * xCurrent),
        -1j * k0 * np.exp(1j * k0 * xCurrent)
    ]

    # Set free terms (A0 = 1)
    freeTermVector[0] = -1
    freeTermVector[1] = -1j * k0

    # Solve the linear system
    try:
        sol = np.linalg.solve(coefMatrix, freeTermVector)
        r = sol[-2] / sol[-1]  # Reflectance (r = B0 / A0)
        reflectance_spectrum[wl_idx] = np.abs(r)**2  # Store reflectance spectrum
    except np.linalg.LinAlgError as e:
        print(f"Error: {e}")

# Plotting the reflectance spectrum
plt.figure()
plt.plot(wavelength, reflectance_spectrum, linewidth=2)
plt.xlabel(r'Wavelength ($\mu$m)', fontsize=16)
plt.ylabel('Reflectance', fontsize=16)
plt.title('Reflectance Spectrum of 1D Photonic Crystal')
plt.grid(True)
plt.show()
