class AncestralStories:
    def __init__(self, length, moralLessons, ageGroup, title, language):
        self.length = length
        self.moralLessons = moralLessons
        self.ageGroup = ageGroup
        self.title = title
        self.language = language
    def __str__(self):
       return f"{self.title} is a {self.length} story that teaches {self.moralLessons} to {self.ageGroup} and is written in {self.language} language."
    def translateStory(self, newLanguage):
        if self.language != newLanguage:
            self.language = newLanguage
            return self.language
        else:
            return self.language
    def addStoryToDatabase(self):
        database = []
        if self.title not in database:
            database.append(self.title)
            print(database)
        else:
            print("This story already exists in storage")
class StoryTeller(AncestralStories):
    def __init__(self, length, moralLessons, ageGroup, title, language, name):
        super().__init__(length, moralLessons, ageGroup, title, language)
        self.name = name
    def tellStory(self):
        print(f"This is a story called {self.title}. It teaches {self.ageGroup} about {self.moralLessons}.")
 # instances
story1 = AncestralStories("long", "courage", "children", "The Lion King", "English")
story2 = AncestralStories("short", "hardwork", "teenagers", "Vuna Ulichopanda", "Kiswahili")
print(story1)
print(story1.translateStory("Kiswahili"))
story1.addStoryToDatabase()




# question2
class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_methods, nutritional_info):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_methods = cooking_methods
        self.nutritional_info = nutritional_info
    def timeForPreparation(self):
        if self.preparation_time >= 3:
            return "This coloured Rice takes a long time to prepare"
        else:
            return "This coloured Rice can be prepared within a reasonable amount of time"
    def __str__(self):
        return f"Name: {self.name}\ncountry: {self.country}\ningredients: {', '.join(self.ingredients)}\npreparation_time: {self.preparation_time} minutes\ncooking_method: {self.cooking_methods}\nnutrition_info: {self.nutritional_info}"
class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, spice_level):
        super().__init__(name, "Morocco", ingredients, preparation_time, cooking_method, nutritional_info)
        self.spice_level = spice_level
class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, injera_included):
        super().__init__(name, "Ethiopia", ingredients, preparation_time, cooking_method, nutritional_info)
        self.injera_included = injera_included
class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, is_spicy):
        super().__init__(name, "Nigeria", ingredients, preparation_time, cooking_method, nutritional_info)
        self.is_spicy = is_spicy
# Instances
moroccan_recipe = MoroccanRecipe("Coloured Rice",["rice", "onion", "olive oil", "spices"],45,"Boiled ","Nice for vitamins","Medium")
print(moroccan_recipe)
ethiopian_recipe = EthiopianRecipe("Boiled eggs",["eggs","water"],20,"protein","no spices",True)
print(ethiopian_recipe)
nigerian_recipe = NigerianRecipe("Jollof Rice",["rice", "tomatoes", "onion", "pepper", "spices"],45,"Popular party dish",'is_spicy',True)
print(nigerian_recipe)

 

# question3
class Species:
    def __init__(self, diet, typical_lifespan, migration_patterns):
        self.diet = diet
        self.typical_lifespan = typical_lifespan
        self.migration_patterns = migration_patterns
    
    def type_of_animal(self):
        if self.diet == "herbivorous":
            print("This animal is not a danger to other animals")
        elif self.diet == "omnivorous":
            print("This animal feeds on plants but also feeds on some animals")
        else:
            print("This animal is very dangerous to other animals and does not eat plants")


class Predator(Species):
    def __init__(self, diet, typical_lifespan, migration_patterns, type_of_teeth, claws, venom, name):
        super().__init__(diet, typical_lifespan, migration_patterns)
        self.type_of_teeth = type_of_teeth
        self.claws = claws
        self.venom = venom
        self.name = name

    def fast_killers(self):
        if self.venom:
            print(f"The bite of a {self.name} kills within hours")
        else:
            print(f"The bite of a {self.name} is not deadly")

    def method_of_killing(self):
        if "carnassial teeth" in self.type_of_teeth:
            print(f"A {self.name} kills by slicing up their prey")
        else:
            print("This predator cannot shear their prey's meat after attacks")


class Prey(Species):
    def __init__(self, diet, typical_lifespan, migration_patterns, defense_mechanisms, name):
        super().__init__(diet, typical_lifespan, migration_patterns)
        self.defense_mechanisms = defense_mechanisms
        self.name = name
  
# instances
lion = Predator("carnivorous", 12, "non-migratory", ["carnassial teeth"], True, False, "Lion")
gazelle = Prey("herbivorous", 10, "seasonal migration", ["speed", "herd behavior"], "Gazelle")
lion.type_of_animal() 
lion.fast_killers()   
lion.method_of_killing() 
gazelle.type_of_animal() 
print(gazelle.defense_mechanisms)  




# question4

# class Artist:
#     def __init__(self, artistsName, country, musicStyle, instruments):
#         self.artistsName = artistsName
#         self.country = country
#         self.musicStyle = musicStyle
#         self.instruments = instruments

#     def addArtists(self, artistDatabase):
#         if self.artistsName not in artistDatabase:
#             artistDatabase.append(self.artistsName)

#     def removeArtists(self, artistDatabase):
#         return artistDatabase.pop(0)


# class Performance(Artist):
#     def __init__(self, artistsName, country, musicStyle, instruments, startTime, stopTime):
#         super().__init__(artistsName, country, musicStyle, instruments)
#         self.startTime = startTime
#         self.stopTime = stopTime

#     def duration(self):
#         timeTaken = self.stopTime - self.startTime
#         return f"The duration for the performance was {timeTaken}"

#     def schedule(self, eventSchedule):
#         eventSchedule[self.artistsName] = self.startTime
#         return eventSchedule


# class Stage(Artist):
#     def __init__(self, artistsName, country, musicStyle, instruments, supportingArtists):
#         super().__init__(artistsName, country, musicStyle, instruments)
#         self.supportingArtists = supportingArtists

#     def spaceOccupied(self):
#         if "drums" in self.instruments and self.supportingArtists:
#             return f"{self.artistsName} will occupy only 50% of the stage"
#         if "drums" in self.instruments:
#             return f"{self.artistsName} will occupy only 70% of the stage"
#         if self.supportingArtists:
#             return f"{self.artistsName} will occupy only 80% of the stage"

# # Create instances of Artist class
# artist1 = Artist("John", "USA", "Rock", ["Guitar", "Vocals"])
# artist2 = Artist("Maria", "Spain", "Pop", ["Piano", "Vocals"])
# artist1.addArtists()
# # Create instances of Performance class
# performance1 = Performance("John", "USA", "Rock", ["Guitar", "Vocals"], 10, 11)
# performance2 = Performance("Maria", "Spain", "Pop", ["Piano", "Vocals"], 14, 15)

# # Create instances of Stage class
# stage1 = Stage("John", "USA", "Rock", ["Guitar", "Vocals"], True)
# stage2 = Stage("Maria", "Spain", "Pop", ["Piano", "Vocals"], False)




# question4
class Artist:
    def __init__(self, artistsName, country, musicStyle, instruments):
        self.artistsName = artistsName
        self.country = country
        self.musicStyle = musicStyle
        self.instruments = instruments

    def addArtists(self):
        if self.artistsName not in artistDatabase:
            artistDatabase.append(self.artistsName)

    def removeArtists(self):
        return artistDatabase.pop(0)


class Performance(Artist):
    def __init__(self, artistsName, country, musicStyle, instruments, startTime, stopTime):
        super().__init__(artistsName, country, musicStyle, instruments)
        self.startTime = startTime
        self.stopTime = stopTime

    def duration(self):
        timeTaken = self.stopTime - self.startTime
        return f"The duration for the performance was {timeTaken}"

    def schedule(self):
        eventSchedule = {}
        eventSchedule[self.artistsName] = self.startTime
        return eventSchedule


class Stage(Artist):
    def __init__(self, artistsName, country, musicStyle, instruments, supportingArtists):
        super().__init__(artistsName, country, musicStyle, instruments)
        self.supportingArtists = supportingArtists

    def spaceOccupied(self):
        if "drums" in self.instruments and self.supportingArtists:
            return f"{self.artistsName} will occupy only 50% of the stage"
        if "drums" in self.instruments:
            return f"{self.artistsName} will occupy only 70% of the stage"
        if self.supportingArtists:
            return f"{self.artistsName} will occupy only 80% of the stage"


artistDatabase = []

# instances
artist1 = Artist("Justine", "USA", "Intentions", ["guitar", "vocals"])
artist1.addArtists()

performance1 = Performance("Drake", "USA", "Rock", ["guitar", "vocals"], 10, 20)
duration = performance1.duration()
schedule = performance1.schedule()

stage1 = Stage("Jay", "USA", "Rock", ["guitar", "vocals"], True)
spaceOccupied = stage1.spaceOccupied()
print(artistDatabase)
print(duration)
print(schedule)
print(spaceOccupied)


# question5
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_value(self):
        return self.price * self.quantity
# Creating multiple objects of Product class
productA = Product('Laptop', 15000, 2)
productB = Product('Phones', 10000, 2)
productC = Product('Television', 18000, 2)
# Calculating total value of all products
total_value = productA.calculate_total_value() + productB.calculate_total_value() + productC.calculate_total_value()
print(f'The total value of all products is {total_value}.')




# question6

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def averageGrade(self):
        total = sum(self.grades)
        average = total / len(self.grades)
        return average
    
    def displayInfo(self):
        average = self.averageGrade()
        print(f"This student's name is {self.name} and they are {self.age} years old and they have an average grade of {average}")
    
    def passMark(self):
        average = self.averageGrade()
        if average >= 60:
            print("The student has passed")
        else:
            print("The student has failed")

John = Student("John", 23, [80, 85, 74, 90])
John.averageGrade()
John.displayInfo()
John.passMark()




