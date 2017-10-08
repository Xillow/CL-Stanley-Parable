import bomb
import freedom
ON = "on"
OFF = "off"

def power():
    mindSwitch = "none"
    
    while mindSwitch != "on" and mindSwitch != "off":
        print("And as the cold reality of his past began to sink in, Stanley decided that this machinery would never again exert its terrible power over another human life. For he would dismantle the controls once and for all.")
        mindSwitch = input("ON/OFF ")
        
        if mindSwitch == ON:
            bomb.bomb()
        elif mindSwitch == OFF:
            freedom.freedom()
