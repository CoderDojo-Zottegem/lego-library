from functies import *
from missie_blauw import missie_blauw_start
from missie_groenA import missie_groenA_start
from missie_groenB import missie_groenB_start
from missie_geel import missie_geel_start

##########################################################################
##  NIKS AAN HET HOOFDPROGRAMMA VERANDEREN ZONDER OVERLEG MET IEDEREEN  ##
##########################################################################

laatste_kleur = Color.MAGENTA

while True:
    color =sensor.color()
    if color == laatste_kleur or color == Color.NONE:
        continue
    laatste_kleur = color    
    if color == Color.GREEN: 
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "B")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_groenA_start())
             hub.light.off()
             hub.display.off()
        if selected == "B":
            hub.light.on(color)
            run_task(missie_groenB_start())
            hub.light.off()
            hub.display.off()
              
        
    if color == Color.BLUE:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "F")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_blauw_start())
             hub.light.off()
             hub.display.off()

    if color == Color.YELLOW:
        hub.light.blink(color,[500,500])
        selected = hub_menu("A", "F")  
        if selected == "A":
             hub.light.on(color)
             run_task(missie_geel_start())
             hub.light.off()
             hub.display.off()
