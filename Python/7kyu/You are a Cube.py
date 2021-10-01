"""
In geometry, a cube is a three-dimensional solid object bounded by six square faces, facets or sides, 
with three meeting at each vertex.The cube is the only regular hexahedron and is one of the five Platonic solids. 
It has 12 edges, 6 faces and 8 vertices.The cube is also a square parallelepiped, an equilateral cuboid and a right rhombohedron. 
It is a regular square prism in three orientations, and a trigonal trapezohedron in four orientations.

You are given a task of finding a if the provided value is a perfect cube!
"""



def main():
    print(you_are_a_cube(27),True)
    print(you_are_a_cube(1),True)
    print(you_are_a_cube(2),False)
    print(you_are_a_cube(99),False)
    print(you_are_a_cube(64),True)


def you_are_a_cube(cube):
    return True if int(round(cube ** (1 / 3))) ** 3 == cube else False


if __name__ == "__main__":
    main()
