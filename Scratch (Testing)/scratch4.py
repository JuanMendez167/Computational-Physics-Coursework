import matplotlib.pyplot as plt

# Define the coordinates of atoms
atoms = {
    'C1': (0, 0),
    'C2': (1, 0),
    'C3': (2, 0),
    'C4': (3, 0),
    'C5': (4, 0),
    'C6': (5, 0),
    'C7': (0.5, 1),
    'C8': (2.5, 1),
    'S': (3, 2),
    'H1': (-0.5, 0),
    'H2': (5.5, 0),
    'H3': (0.5, 2),
    'H4': (1.5, 2),
    'H5': (4.5, 2),
    'H6': (5.5, 2)
}

# Define bonds
bonds = [
    ('C1', 'C2'), ('C2', 'C3'), ('C3', 'C4'), ('C4', 'C5'), ('C5', 'C6'),
    ('C1', 'C7'), ('C3', 'C8'), ('C4', 'S'),
    ('C1', 'H1'), ('C6', 'H2'),
    ('C1', 'H3'), ('C2', 'H4'), ('C5', 'H5'), ('C6', 'H6')
]

# Draw atoms
for atom, coord in atoms.items():
    plt.scatter(coord[0], coord[1], color='black')
    plt.text(coord[0], coord[1], atom, fontsize=12, ha='center', va='center')

# Draw bonds
for bond in bonds:
    atom1 = atoms[bond[0]]
    atom2 = atoms[bond[1]]
    plt.plot([atom1[0], atom2[0]], [atom1[1], atom2[1]], color='black')

# Set axis limits and remove axis ticks
plt.axis('off')
plt.xlim(-1, 6)
plt.ylim(-1, 3)

# Show plot
plt.show()
