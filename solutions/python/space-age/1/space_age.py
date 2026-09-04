class SpaceAge:
    EARTH_YEAR = 365.25*24*60*60
    ORBITAL_PERIOD = {"mercury": 0.2408467, "venus": 0.61519726, "earth": 1.0, "mars": 1.8808158, "jupiter": 11.862615, "saturn": 29.447498, "uranus": 84.016846, "neptune": 164.79132}
 
    def __init__(self, seconds):
        self.seconds = seconds

    def earth_age(self):
        return self.seconds / self.EARTH_YEAR
    
    def on_earth(self):
        return round(self.earth_age(), 2)

    def on_mercury(self):
        return round(self.earth_age() / self.ORBITAL_PERIOD['mercury'],2)

    def on_venus(self):
        return round(self.earth_age() / self.ORBITAL_PERIOD['venus'],2)

    def on_mars(self):
        return round(self.earth_age() / self.ORBITAL_PERIOD['mars'],2)

    def on_jupiter(self):
        return round(self.earth_age() / self.ORBITAL_PERIOD['jupiter'],2)

    def on_saturn(self):
        return round(self.earth_age() / self.ORBITAL_PERIOD['saturn'],2)

    def on_uranus(self):
        return round(self.earth_age() / self.ORBITAL_PERIOD['uranus'],2)

    def on_neptune(self):
        return round(self.earth_age() / self.ORBITAL_PERIOD['neptune'],2)
        
