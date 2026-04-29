"""Klasser for animasjon av et bunndyr som spiser plankton."""

class Simulering:
    """
    Oppretter Bunndyr og Plankton
    Kjører simuleringsloop med tidsdifferanse.
    Sjekker kollisjon ved å se på posisjonene til bunndyr og plankton
    Tegning gjøres med objektenes tegnemetode.
    TODO
    1) Tegne bunndyr
    2) Tegne plankton
    3) Animere plankton
    4) Sjekke kollisjon
    5) Hva skjer ved kollisjon.
    6) Lage flere plankton
    """
    def __init__(self, bredde, høyde):
        self.bredde = bredde

class Bunndyr:
    """
    Bunndyr tegnes opp av seg selv, canvas må ligge som en parameter.
    """
    def __init__(self,canvas):
        self.canvas = canvas

class Plankton:
    """
    Plankton er to ulike typer: rød=giftig, grønn=mat
    attributt
    giftig = True -> Rød farge
    ikke giftig -> Grønn farge
    tegnemetode som sjekker giftig for riktig farge. canvas må ligge som parameter.
    """
    def __init__(self,canvas):
        self.canvas = canvas
