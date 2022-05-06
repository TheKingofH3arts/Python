"""
Name:       Dylan brodie
Course:     CS1430, Section 02,  Spring 2022
Assignment: Lab 08
Purpose:    This program implements a solar system. It uses the classes
            solarsystem.py, sun.py, planet.py
Input:      A sun, it's planets, and moons
Output:     Information about the planets in the solar system, and a
            table of volume and surface area of a sun with varying radii.
"""
#########################
# IMPORTS
#########################
from student.sun import *
from student.planet import *
from student.solarsystem import *


def print_table():
    """
    Prints a a table of data for a sun with radius that varies from 10 units to
    500 units, in increments of 10 units.
    :return: None
    :rtype:
    :param:
    :type:
    """
    print("Table of volume and surface area of a sun with radius varying from "
          "10 units to 500 units, in increments of 10 units:")
    print()
    print(f"Radius       Volume      Surface Area")
    print(f"=======================================")
    for radius in range(10, 500, 10):
        sun = Sun("Sun", radius, 1000, 5800)
        print(f"{radius:>6d} | {sun.get_volume():>14.2f} | "
              f"{sun.get_surface_area():>11.2f}")


def main():
    """
    This program creates a Sun, with planets Mercury, Earth with moon, Mars with
    two moons, and Jupiter with moons. It prints the total mass of all of the
    planets in the solar system including the sun, but not the moons. It prints
    the name of the farthest planet from the sun, and the closest planet from
    the sun.
    :return:
    :rtype:
    """
    # Create a sun object
    sun = Sun("Sun", 5000, 1000, 5800)

    # Create a solar system object with the Sun as a planet
    ss = SolarSystem(sun)

    # Create an Earth planet with our Moon
    earth = Planet("Earth", 50, 60, 30, 1)
    earth.add_moon("Moon")

    # Add Earth to the Solar System object
    ss.add_planet(earth)

    # Create a Mars planet with moons Phobos and Deimos
    mars = Planet("Mars", 47, 50, 35, 2)
    mars.add_moon("Phobos")
    mars.add_moon("Deimos")

    # Add Mars to the Solar System object
    ss.add_planet(mars)

    # Create a Mercury planet
    mercury = Planet("Mercury", 19, 10, 25, 0)
    ss.add_planet(mercury)

    ss.print_all()

    print("Planets in the solar system: ")
    ss.show_planets()
    print()

    print(f"Total mass of solar system, not including moons: "
          f"{ss.get_total_mass():.2f}")
    print(f"Farthest planet from sun: {ss.get_farthest()}")
    print(f"Nearest planet to sun: {ss.get_nearest()}")
    print()
    print_table()


if __name__ == "__main__":
    main()
