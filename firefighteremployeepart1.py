class Firefighter:
    count = 0
    
    def __init__(self, navn, etternavn, ansettelsesnummer, alder, ):
        self.navn = navn
        self.etternavn = etternavn
        self.ansettelsenummer = ansettelsesnummer
        self.alder = alder
        Firefighter.count += 1
    
    def display(self):
        print(f"{self.navn}, {self.etternavn}, {self.ansettelsenummer}, {self.alder}")





