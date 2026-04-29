"""Klasser for animasjon av et bunndyr som spiser plankton."""

import tkinter as tk
import time

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
        self.høyde = høyde
        self.window = tk.Tk()
        self.window.lift()
        self.window.focus_force()
        self.canvas =tk.Canvas(self.window, width=bredde, height=høyde, background="black")
        self.canvas.pack()
        self.bunndyr = Bunndyr(self.canvas,self.bredde,self.høyde)
        self.bunndyr.tegn()
        self.window.mainloop()
        
        

class Bunndyr:
    """
    Bunndyr tegnes opp av seg selv, canvas må ligge som en parameter.
    Metode for å tegne seg selv.
    """
    def __init__(self,canvas,vindubredde, vinduhøyde):
        self.canvas = canvas
        self.x = vindubredde/2
        self.h = 30
        self.y = vinduhøyde - self.h/2
        self.w = vindubredde/2
    
    def tegn(self):
        self.canvas.create_rectangle(self.x-self.w/2,self.y-self.h/2, self.x+self.w/2,self.y+self.h/2,fill="grey",tags="bunndyr")

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

def main():
    sim = Simulering(600,600)

if __name__ == "__main__":
    main()