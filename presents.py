# Fill a box of presents
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
    
    def __str__(self):
        return f"Present: {self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.content = []
        self.tw =0
    
    def add_present(self, present: Present):
        self.content.append(present.name)
        self.tw = self.tw + present.weight
    
    def total_weight(self):
        tw = self.tw
        return tw



