# Week 2 Assignment 2


TASK: Here you will write a final variation of the script we worked on in class that converts energy in eV to wavelength in nm. Instead of finding red photons, modify your code so that it determines if the photon wavelength is within the *visible* spectrum. (What is this range?) The code also needs to print out a message for the photon energy that is close to 520nm within a range of plus or minus 10nm. Another requirement: you will need to do sweep of photon energies between 1.0 and 3.0 eV using the linspace() function in the numpy module instead of the arange() function. Check google or consult the official numpy documentation for hints about how to use the linspace() function.

Webpage for linspace() in NumPy documentation: 
https://numpy.org/doc/stable/reference/generated/numpy.linspace.html



EXPECTED OUTCOME: 

A photon with energy 1.0 eV has a wavelength of 1243.1 nm

A photon with energy 1.2 eV has a wavelength of 1035.9 nm

A photon with energy 1.4 eV has a wavelength of 887.9 nm

A photon with energy 1.6 eV has a wavelength of 777.0 nm

A photon with energy 1.8 eV has a wavelength of 690.6 nm

   this is visible
   
A photon with energy 2.0 eV has a wavelength of 621.6 nm

   this is visible
   
A photon with energy 2.2 eV has a wavelength of 565.1 nm

   this is visible
   
A photon with energy 2.4 eV has a wavelength of 518.0 nm

   this is visible
   
   ---- this is closest to 520 nm ----

A photon with energy 2.6 eV has a wavelength of 478.1 nm

   this is visible
   
A photon with energy 2.8 eV has a wavelength of 444.0 nm

   this is visible
   
A photon with energy 3.0 eV has a wavelength of 414.4 nm

   this is visible
