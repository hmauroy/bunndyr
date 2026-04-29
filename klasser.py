"""Klasser for animasjon av et bunndyr som spiser plankton."""

import tkinter as tk
import time
from random import choice, randrange, randint

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
    def __init__(self, bredde, høyde, fps=30, plankton_bredde=20,generasjons_tid=1):
        self.bredde = bredde
        self.høyde = høyde
        self.window = tk.Tk()
        self.window.lift()
        self.window.focus_force()
        self.canvas =tk.Canvas(self.window, width=bredde, height=høyde, background="black")
        self.canvas.pack()
        self.bunndyr = Bunndyr(self.canvas,self.bredde,self.høyde)
        self.plankton = []
        self.fps = fps
        self.generasjons_tid = generasjons_tid
        self.plankton_bredde = plankton_bredde
        
    def lag_plankton(self,w):
        """Lager en tilfeldig posisjon for hvert plankton der det ikke overlapper med andre plankton."""
        print(w,self.bredde)
        x = randrange(w//2,self.bredde - w//2)  # Bruker heltallsdivisjon pga. randrange krever int for begge parametre.
        y = randrange(-10*w,w//2)
        plankton_1 = Plankton(x, y, w, self.canvas)
        # Sjekker overlapp mot alle andre plankton med en låsende while loop. Lager nytt objekt hvis overlapp.
        overlapp = True
        while overlapp:
            for p in self.plankton:
                if self.kollisjon(p,plankton_1):
                    # Lager nytt objekt og sjekker igjen for overlapp.
                    plankton_1 = Plankton(x, y, w, self.canvas)
            # Hvis for-loop ikke fant noen overlapp.
            overlapp = False
        self.plankton.append(plankton_1)

    def loop(self):
        forrige_tid = time.time()
        plankton_tid = time.time()
        isRunning = True
        isSimulating = True
        fps = self.fps
        intervall = 1 / fps
        self.bunndyr.tegn()
        self.window.update()
        # Lager n antall plankton fra starten
        n = randint(5,15)
        for i in range(n):
            self.lag_plankton(self.plankton_bredde)
        print(self.plankton)
        while isRunning:
            while isSimulating:
                # For hvert 3. sekund lages det tre nye plankton
                if time.time()-plankton_tid >= self.generasjons_tid:
                    for i in range(3):
                        self.lag_plankton(self.plankton_bredde)
                        plankton_tid = time.time()
                if time.time()-forrige_tid >= intervall:
                    forrige_tid = time.time()
                    # Sletter alt i canvas før vi gjør forflytninger etc.
                    self.canvas.delete("bunndyr")
                    self.canvas.delete("plankton")
                    # Flytter en plankton av gangen.
                    for p in self.plankton:
                        p.flytt()
                        # Sjekker om plankton har kommet nedenfor vinduet.
                        if p.y > self.høyde - 10:
                            self.plankton.remove(p)
                        # Kollisjon
                        if self.kollisjon(self.bunndyr,p):
                            if p.giftig:
                                self.bunndyr.w -= 50
                            else:
                                self.bunndyr.w += 50
                            if self.bunndyr.w >= self.bredde or self.bunndyr.w <= p.w:
                                isSimulating = False
                            self.plankton.remove(p)
                            self.bunndyr.tegn()
                            
                        
                    

                    # Tegner opp på nytt
                    self.bunndyr.tegn()
                    # Tegner alle plankton
                    for p in self.plankton:
                        p.tegn()
                self.window.update()
            self.window.update()

    def kollisjon(self,rect1,rect2):
        return not (
            rect1.x + rect1.w/2  <= rect2.x - rect2.w/2 or   # rect1 is left of rect2
            rect2.x + rect2.w/2  <= rect1.x - rect1.w/2 or   # rect2 is left of rect1
            rect1.y + rect1.h/2 <= rect2.y - rect2.h/2 or   # rect1 is above rect2
            rect2.y + rect2.h/2 <= rect1.y - rect1.h/2      # rect2 is above rect1
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
    posisjon dannes automatisk i forhold til vinduets størrelse.
    Opprettes ovenfor vinduet.
    tegnemetode som sjekker giftig for riktig farge. canvas må ligge som parameter.
    """
    def __init__(self,x, y, w, canvas):
        self.canvas = canvas
        self.w = w
        self.h = self.w
        self.x = x
        self.y = y
        self.giftig = choice([True,False])
        self.dy = randint(5,10)

    def flytt(self):
        self.y += self.dy

    def tegn(self):
        """Bør være arv her!"""
        farge = "chartreuse"
        label = "G"
        if self.giftig:
            farge = "red"
            label = "R"
        self.canvas.create_rectangle(self.x-self.w/2,self.y-self.h/2, self.x+self.w/2,self.y+self.h/2,outline="",fill=farge,tags="plankton")
        self.canvas.create_text(self.x,self.y,text=label,font=("Arial", 14), fill="black", tags="label_text")


def main():
    sim = Simulering(600,600,30,20,1)
    sim.loop()
    # Avslutter koden med destroy når bruker lukker vinduet.
    sim.window.destroy()

if __name__ == "__main__":
    main()