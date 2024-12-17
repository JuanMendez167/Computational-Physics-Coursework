# These are comments, it is a good idea to always add some to explain what the code is supposed to be doing
# Code to convert energy (in eV) to wavelength (in nm)

#Defening variable useful for the calculation
6.626e-34 * 3e8 / (1.9 * 1.6e-19) / (1e-9)


h = 6.626e-34
c = 3e8
energy = 1.9
ev2J= 1.6e-19
m2nm = 1e-9
# convert photon energy in ev into wavelength
L= h * c / (energy * ev2J) / m2nm

print("The wavelength of the photon is", L)

print("The wavelength of a phton with energy", energy, "eV is", L, "nm")

#✔
