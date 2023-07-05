# Inputs will be the title,lenght,moral_lessons and age_groups
# Outputs will be the storybook name,the storyteller and the transator
# Process is i'll create a class AncestralStories and sub classes that will determine the name of
# the storyteller,the name of the story and the translator.I'll use a conditional statement to 
# determine if the story has been translated or not.

# Story class
class AncestralStories:
    def __init__(self, title, length, moral_lessons, age_groups):
        self.title = title
        self.length = length
        self.moral_lessons = moral_lessons
        self.age_groups = age_groups

class StoryTeller:
    def __init__(self, name, stories=[]):
        self.name = name
        self.stories = stories
       

    def add_story(self, story):
        self.stories.append(story)

    def tell_story(self, story):
        print(f"The storyTeller {self.name} told the children a story : {story.title}")


class Translator:
    def __init__(self, stories, languages):
        self.stories = stories
        self.languages = languages

    def translate(self, story, language):
        if story in self.stories and language in self.languages:
            print(f"It Translated the story '{story.title}' into {language}")
            
        else:
            print(f"Translation has not occured for story '{story.title}' or language '{language}'")

# Instances
Book1 =  AncestralStories("The crocodile", 15, "Trust", "Children")
Book2 =  AncestralStories("Family", 10, "Family love", "Children")

storyteller = StoryTeller("Lekishon Sheila")
storyteller.add_story(Book1)
storyteller.add_story(Book2)
storyteller.tell_story(Book1)

translator = Translator([Book1, Book2], ["British", "Maasai"])
translator.translate(Book2, "Kiswahili")


# Question2

class Recipe:
    def __init__(self, name, country, ingredients, preparation_time, cooking_methods, nutritional_info):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_methods = cooking_methods
        self.nutritional_info = nutritional_info
    def timeForPreparation(self):
        if self.preparationtime>=3:
            return f"this coloured Rice takes a long time to prepare"
        else:
            return f"This coloured Rice  can be prepared within a reasonable amount of time"
    def __str__(self):
        return f"Name: {self.name}\ncountry: {self.country}\ningredients: {', '.join(self.ingredients)}\npreparation_time: {self.prep_time} minutes\ncooking_method: {self.cooking_method}\nnutrition_info: {self.nutrition_info}"

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
moroccan_recipe = MoroccanRecipe(
    "Coloured Rice",
    ["rice", "onion", "olive oil", "spices"],
    45,
    "Boiled ",
    "Nice for vitamins",
    "Medium"
)
print(moroccan_recipe)



ethiopian_recipe = EthiopianRecipe(
    "Boiled eggs",
    ["eggs","water"],
    20,
    "protein",
    "no spicies",
    True
)
print(ethiopian_recipe)

nigerian_recipe = NigerianRecipe(
    "Jollof Rice",
    ["rice", "tomatoes", "onion", "pepper", "spices"],
    45,
    "Popular party dish",
   'is_spicy',
    True
)
print(nigerian_recipe)





    