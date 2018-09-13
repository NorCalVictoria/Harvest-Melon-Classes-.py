############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""



    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.rep_code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

       
    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        if pairing not in self.pairings:
            self.pairings.append(pairing) 
 

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.rep_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon_type = MelonType("musk", "1998","green", True , True, "muskmelon")
    muskmelon_type.add_pairing("mint")
    all_melon_types.append(muskmelon_type)

    casaba_type = MelonType("cas",2003,"orange", True, False, "casaba")
    casaba_type.add_pairing("mint")
    casaba_type.add_pairing("strawberries")
    all_melon_types.append(casaba_type)

    crenshaw_type = MelonType("cren", 1996, "green" , True, False, "crenshaw")
    crenshaw_type.add_pairing("proscuitto")
    all_melon_types.append(crenshaw_type)

    yellow_watermelon_type = MelonType("yw", 2003, "yellow" , True, True, "yellow watermelow")
    yellow_watermelon_type.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon_type)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        print(f"{melon_type.name} pairs with" )
        for pairing in melon_type.pairings:
            print (f"- {pairing}")
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_type_dict = {}

    for melon_type in melon_types:
        rep_code = melon_type.rep_code
        melon_type_dict[rep_code] = melon_type

    return melon_type_dict


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



