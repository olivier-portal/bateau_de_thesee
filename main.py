class Part:
    def __init__(self):
        self.name = "Mât"
        self.material = "Bois"
        
    def change_material (self, material):
        self.material = material
        
    def __str__ (self):
        return f"Le {self.name} est fabriqué en {self.material}"
        

class Ship():
    def __init__(self, parts, material):
        self.material = material
        self.__parts = {}
        
        if isinstance(parts, str):
            parts = [part]
            
        for part in parts :
            self.__parts[part] = material
        
    def display_state(self):
        for part, material in self.__parts.items():
            print(f"{part}: {material}")
        
    def replace_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name] = new_material
        else:
            print(f"Erreur : {part_name} n'existe pas dans le bateau.")
        return self.__parts
    
bateau = Ship(["proue", "mât"], "bois")
bateau.display_state()

bateau.replace_part("proue", "bois débène")
bateau.display_state()