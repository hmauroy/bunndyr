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
        isSimulating = True
        fps = 30
        intervall = 1 / fps
        self.bunndyr.tegn()
        self.window.update()
        self.plankton.append(Plankton(self.canvas,self.bredde,self.høyde))
        while isRunning:
            while isSimulating:
                if time.time()-forrige_tid >= intervall:
                    forrige_tid = time.time()
                    # Sletter alt i canvas før vi gjør forflytninger etc.
                    self.canvas.delete("bunndyr")
                    self.canvas.delete("plankton")
                    # Flytter ting
                    for p in self.plankton:
                        p.flytt()
                        # Kollisjon
                        if self.kollisjon(self.bunndyr,p):
                            if p.giftig:
                                self.bunndyr.w -= 10
                            else:
                                self.bunndyr.w += 10
                            if self.bunndyr.w >= self.bredde or self.bunndyr.w <= p.w:
                                isSimulating = False
                            self.plankton.remove(p)
                        
                    

                    # Tegner opp på nytt
                    self.bunndyr.tegn()
                    # Tegner alle plankton
                    for p in self.plankton:
                        p.tegn()
                    
                self.window.update()

    def kollisjon(self,rect1,rect2):
        return not (
            rect1.x + rect1.w  <= rect2.x or   # rect1 is left of rect2
            rect2.x + rect2.w  <= rect1.x or   # rect2 is left of rect1
            rect1.y + rect1.h <= rect2.y or   # rect1 is above rect2
            rect2.y + rect2.h <= rect1.y      # rect2 is above rect1
        )
        

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
        self.h = self.w
        self.x = vindubredde/2
        self.y = self.w/2
        self.giftig = choice([True,False])
        self.dy = 10

    def flytt(self):
        self.y += self.dy

    def tegn(self):
        """Bør være arv her!"""
        farge = "green"
        if self.giftig:
            farge = "red"
        self.canvas.create_rectangle(self.x-self.w/2,self.y-self.h/2, self.x+self.w/2,self.y+self.h/2,outline="",fill=farge,tags="plankton")


def main():
    sim = Simulering(600,600)
    sim.loop()

if __name__ == "__main__":
    main()