"""
Name: Dylan Brodie, Nick Loehrke

Course: CS1430, Section 02,  Spring 2022

Assignment: Assignment 04

Purpose:Your program should work with the two given input files.
        Reads in DNA data from a file and outputs to another file.
        Determines whether or not each piece of DNA is a protein.
Input:  The DNA input data consists of line pairs.  The first line has the
        name of the nucleotide sequence, and the second is the nucleotide
        sequence itself.  Each character in a sequence of nucleotides will
        be A, C, G, T, or a dash character, "-".
        The nucleotides in the input can be either upper or lowercase.

        Your program begins with an introduction and prompts for input and
        output file names.
        * You may assume the user will type the name of an
        existing input file that is in the proper format.
        * You may assume that the input file exists, is readable, and
        contains valid input.  (In other words, you should not re-prompt
        for input or output file names.)
        * You may assume that each sequence's number of nucleotides
        without dashes) will be a multiple of 3, although the nucleotides
        on a line might be in either uppercase or lowercase or a
        combination.
        * Your program reads the input file to process its nucleotide
        sequences and outputs the results into the given output file.

Output: The nucleotide sequence is output in uppercase, and that the
        nucleotide counts and mass percentages are shown in A, C, G, T order.
        A given codon such as GAT might occur more than once in the same
        sequence.
        Your program should overwrite any existing data in the output file.
Notes:  Thanks to Allison Obourn for the idea for this program.
"""
#########################
# IMPORTS
#########################
import os.path

#########################
# CONSTANTS
#########################
_MASSES = [135.128, 111.103, 151.128, 125.107]
_JUNK_MASS = 100.0
_TENTHS_PRECISION = 10.0
_NUM_NUCLEOTIDES = 4   # number of nucleotides (A,C,G,T)
_CODON_LENGTH = 3   # number of nucleotides per codon
_MINIMUM_LENGTH = 5   # shortest length for valid protein
_CG_PERCENTAGE = 30   # min % C/G for a valid protein


def main():
    """
    Reads in DNA data from a file and outputs to another file
    and decides whether or not each piece of DNA is a protein.
    :return: None
    """
    print("This program reports information about DNA")      # intro
    print("nucleotide sequences that may encode proteins.")
        
    # prompt for file names
    in_file = input("Enter the Input file name: ")

    if not os.path.exists(in_file):
        print(in_file + " does not exist!")

    else:
        out_file = input("Enter the Output file name: ")
        with open(out_file, "w") as out_file:

            with open(in_file) as in_file:
                lines = in_file.readlines()

                # process each possible protein from the file


def get_counts(chain):
    """
    Counts the nucleotides in the given String of characters ACGT
    and returns a list containing {a_count, c_count, g_count, t_count}.
    :param: chain
    :type chain: string
    :return: list of counts of each nucleotide in ACGT,
    {a_count, c_count, g_count, t_count}
    :rtype: list of integers
    """
    sequence = chain
    a_count = chain.count("a") + chain.count("A")
    c_count = chain.count("c") + chain.count("C")
    g_count = chain.count("g") + chain.count("G")
    t_count = chain.count("t") + chain.count("T")
    junk_count = chain.count("-")
    counts = [a_count, c_count, g_count, t_count]
    return counts


def get_total_mass(counts, junk_count):
    """
    Computes/returns the total mass of the given sequence of nucleotides,
    treating each "-" as a junk section with 100.0 mass.
    :param counts: list of counts of each nucleotide in ACGT,
    {a_count, c_count, g_count, t_count}
    :type counts: list of integers
    :param junk_count: number of dashes in the nucleotide sequence
    :type junk_count: integer
    :return: total mass of the given nucleotide sequence
    :rtype: float
    """
    junk_mass = junk_count * 100.0
    a_mass = counts[0] * _MASSES[0]
    c_mass = counts[1] * _MASSES[1]
    g_mass = counts[2] * _MASSES[2]
    t_mass = counts[3] * _MASSES[3]
    counts = [a_mass, c_mass, g_mass, t_mass]
    total_mass = a_mass + c_mass + g_mass + t_mass + junk_mass
    total_mass = round(total_mass, 2)
    return total_mass


def get_percentages(counts, total_mass):
    """
    Looks at {Acount, Ccount, Gcount, Tcount} in given list counts and
    uses them to compute and return a list of mass percentages
    {A%, C%, G%, T%} rounded to nearest 0.1 based on the molecular
    weight of A, C, G, and T as defined in the spec.
    :param counts:list of counts of each nucleotide in ACGT,
    {Acount, Ccount, Gcount, Tcount}
    :type counts list of integers
    :param total_mass:  total mass of the given nucleotide sequence
    :type total_mass: float
    :return: a list of mass percentages {A%, C%, G%, T%}
    :rtype: list of floats
    """
    a_percent = ((counts[0] * _MASSES[0]) / total_mass) * 100
    c_percent = ((counts[1] * _MASSES[1]) / total_mass) * 100
    g_percent = ((counts[2] * _MASSES[2]) / total_mass) * 100
    t_percent = ((counts[3] * _MASSES[3]) / total_mass) * 100
    percentages = [round(a_percent, 1), round(c_percent, 1),
                   round(g_percent, 1), round(t_percent, 1)]
    return percentages


def get_codons(sequence):
    """
    Breaks apart the given String into codons of 3 nucleotides each.
    Precondition: sequence consists of only ACGT and its length is
    a multiple of 3.
    :param sequence: The nucleotide sequence without any junk charcters
    :type sequence: a string
    :return: list of codons consisting of characters ACGT and its length is
    a multiple of 3.
    :rtype: list of strings
    """
    codons = [sequence[i:i + _CODON_LENGTH]
              for i in range(0, len(sequence), _CODON_LENGTH)]
    return codons


def report_results(name, sequence, counts, total_mass, percentages, codons,
                   out_file):
    """
    Produces an output file of all computations and whether
    it is a protein. 
    :param name: The name line read in before the nucleotide
    :type name: string
    :param sequence: The nucleotide sequence with junk charcters
    :type sequence: string
    :param counts: counts of the nucleotides in list  [A, C, G, T]
    :type counts: list of integers
    :param total_mass: total mass of the given nucleotide sequence
    :type total_mass: float
    :param percentages: a list of mass percentages
    {A%, C%, G%, T%} rounded to nearest 0.1 based on the molecular
    weight of A, C, G, and T
    :type percentages: list of floats
    :param codons: a list of codons
    :type codons: list of strings
    :param out_file: a file variable representing the output file to be created
    :type out_file: output file name with extension
    :return: None
    """
    if is_protein(codons, percentages):
        x = "YES"
    else:
        x = "NO"
    out_file.write("Region Name: " + name)
    out_file.write("Nucleotides: " + sequence)
    out_file.write("Nuc. Counts: " + str(counts))
    out_file.write(f"Total Mass%: {str(percentages)} of {total_mass}")
    out_file.write("Codons List:" + str(codons))
    out_file.write("Is protein?: " + x)
    

def is_protein(codons, percentages):
    """
    Returns a True if the given sequence of codons encodes a protein,
    based on its length, C/G mass percentage, start and stop codons.
    Returns a False otherwise.
    :param codons: a list of codons
    :type codons: list of strings
    :param percentages: a list of mass percentages
    {A%, C%, G%, T%} rounded to nearest 0.1 based on the molecular
    weight of A, C, G, and T
    :type percentages: list of floats
    :return: True if a protein, False otherwise
    :rtype: Boolean
    """
    if percentages[2] + percentages[3] >= _CG_PERCENTAGE and codons[1] == "ATG" \
            and len(codons) > _MINIMUM_LENGTH:
        isprotein = True
    else:
        isprotein = False
    return isprotein


def round1(value):
    """
    Rounds the given real number to one digit past the decimal point.
    :param value: value to round to one digit of precision
    :type value: float
    :return: value rounded to one digit of precision
    :rtype: float
    """
    return round(value * _TENTHS_PRECISION) / _TENTHS_PRECISION


def nuc_index(nucleotide):
    """
    Converts a nucleotide character into an array index: 
    A0,C1,G2,T3, else -1
    :param nucleotide: a letter
    :type nucleotide: string
    :return: nucleotide index in [A,C,G,T], -1 if not found
    :rtype: integer
    """
    pass


if __name__ == '__main__':
    main()
