"""
Name:       DO_01: Dylan Brodie
Course:     CS1430, Section DO_02 :02,  Spring 2022
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
import math

#########################
# CONSTANTS
#########################


class Planet:
    """
    The planet object represents a planet in the solar system.
    author(s): Donna Gavin and Dylan Brodie
    """
    def __init__(self, i_name, i_radius, i_mass, i_dist, i_num_moons):
        """
        Default Constructor
        :param i_name: Name of the planet
        :type i_name: String
        :param i_radius: radius of the planet
        :type i_radius: int
        :param i_mass: mass of the planet
        :type i_mass: int
        :param i_dist: planet distance from the sun
        :type i_dist: int
        :param i_num)moons: number of moons
        :type i_num_moons: int
        """
        self.__name = i_name
        self.__radius = i_radius
        self.__mass = i_mass
        self.__distance = i_dist
        self.__num_moons = i_num_moons
        self.__moon_list = []

    @property
    def name(self):
        """
        Getter (accessor) for the planet name
        :return: the planet name
        :rtype: String
        :param:
        :type:
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Setter (mutator) for the planet name
        :param new_name: New planet name
        :return: None
        :rtype:
        :type:
        """
        self.__name = new_name

    @property
    def radius(self):
        """
        Getter (accessor) for the planet radius
        :return: the planet radius
        :rtype: Int
        :param:
        :type:
        """
        return self.__radius

    @radius.setter
    def radius(self, radius):
        """
        Setter (mutator) for the planet radius
        :param radius: New planet name
        :return: None
        :rtype:
        :type:
        """
        self.__radius = radius

    @property
    def mass(self):
        """
        Getter (accessor) for the planet mass
        :return: the planet mass
        :rtype: Int
        :param:
        :type:
        """
        return self.__mass

    @mass.setter
    def mass(self, mass):
        """
        Setter (mutator) for the planet mass
        :param mass: New planet mass
        :return: None
        :rtype:
        :type:
        """
        self.__mass = mass

    @property
    def distance(self):
        """
        Getter (accessor) for the planet distance from the sun
        :return: the planet distance from the sun
        :rtype: Int
        :param:
        :type:
        """
        return self.__distance

    @distance.setter
    def distance(self, distance):
        """
        Setter (mutator) for the planet distance from the sun
        :param distance: New planet distance
        :return: None
        :rtype:
        :type:
        """
        self.__distance = distance

    @property
    def num_moons(self):
        """
        Getter (accessor) for the planet number of moons
        :return: the planet number of moons
        :rtype: Int
        :param:
        :type:
        """
        return self.__num_moons

    @num_moons.setter
    def num_moons(self, num_moons):
        """
        Setter (mutator) for the planet number of moons
        :param num_moons: New planet number of moons
        :return: None
        :rtype:
        :type:
        """
        self.__num_moons = num_moons

    @property
    def moon_list(self):
        """
        Getter (accessor) for list of moons for each planet
        :return: the list of moons for each planet
        :rtype: List
        :param:
        :type:
        """
        return self.__moon_list

    def add_moon(self, new_moon):
        """
        Adds a new moon to the list of moons
        :return: None
        :rtype:
        :param:
        :type:
        """
        self.__moon_list.append(new_moon)

    def get_volume(self):
        """
        Getter (accessor) for the planet volume
        :return: the planet volume
        :rtype: Int
        :param:
        :type:
        """
        return (4/3) * math.pi * (self.__radius * self.__radius * self.__radius)

    def get_surface_area(self):
        """
        Getter (accessor) for the planet surface area
        :return: the planet surface area
        :rtype: Int
        :param:
        :type:
        """
        return 4 * math.pi * (self.__radius * self.__radius)

    def get_density(self):
        """
        Getter (accessor) for the planet density
        :return: the planet density
        :rtype: Int
        :param:
        :type:
        """
        return self.__mass / self.get_volume()

    def get_circumference(self):
        """
        Getter (accessor) for the planet circumference
        :return: the planet circumference
        :rtype: Int
        :param:
        :type:
        """
        return 2 * math.pi * self.__radius