"""Klasser for animasjon av et bunndyr som spiser plankton."""

import tkinter as tk
import time
from random import choice

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
        self.plankton = []
        
    
    def loop(self):
        forrige_tid = time.time()
        start_tid = time.time()
        isRunning = True
        isSimulating = False
        fps = 10
        intervall = 1 / fps
        self.bunndyr.tegn()
        self.window.update()
        self.plankton.append(Plankton(self.canvas,self.bredde,self.høyde))
        while isRunning:
            if time.time()-forrige_tid >= intervall:
                forrige_tid = time.time()
                # Sletter alt i canvas før vi gjør forflytninger etc.
                self.canvas.delete("bunndyr")
                # Flytter ting

                # Kollisjon

                # Tegner opp på nytt
                self.bunndyr.tegn()
                # Tegner alle plankton
                for p in self.plankton:
                    print(p.x,p.y)
                    p.tegn()
                
                self.window.update()
            """
            self.bunndyr.tegn()
            self.window.update()
            """

        
        

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
        self.canvas.create_rectangle(self.x-self.w/2,self.y-self.h/2, self.x+self.w/2,self.y+self.h/2,outline="",fill="grey",tags="bunndyr")

class Plankton:
    """
    Plankton er to ulike typer: rød=giftig, grønn=mat
    attributt
    giftig = True -> Rød farge
    ikke giftig -> Grønn farge
    tegnemetode som sjekker giftig for riktig farge. canvas må ligge som parameter.
    """
    def __init__(self,canvas,vindubredde, vinduhøyde):
        self.canvas = canvas
        self.w = 20
        self.x = vindubredde/2
        self.y = self.w/2
        self.giftig = choice([True,False])

    def tegn(self):
        """Bør være arv her!"""
        farge = "green"
        if self.giftig:
            farge = "red"
        self.canvas.create_rectangle(self.x-self.w/2,self.y-self.w/2, self.x+self.w/2,self.y+self.w/2,outline="",fill=farge,tags="plankton")


def main():
    sim = Simulering(600,600)
    sim.loop()

if __name__ == "__main__":
    main()