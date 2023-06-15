// Inputs will be the lenght,moralLessons and the age group in the main class
// Process- I will have a main class that carries the inputs of lenght,moral lessons and agegroups which
// then i will have other two classes of a storyteller and that of a translator and in the
// in each class will have different input but will inherit other attributes from the main class
// The storyteller will have attributes of name and story and will have methods and that of a translator will have 
// stories and languages and a method.Use a conditional statement to see if the story is transalted
// or not.
// Output- The name of the storyteller,the name of the story,the moral lesson and theage group it lies.

class AncestralStories {
    constructor(title, length, moralLessons, ageGroups) {
      this.title = title;
      this.length = length;
      this.moralLessons = moralLessons;
      this.ageGroups = ageGroups;
    }
  }
  
 
  class StoryTeller {
    constructor(name, stories) {
      this.name = name;
      this.stories = stories;
    }
  
    addStory(story) {
      this.stories.push(story);
    }
  
    tellStory(story) {
      console.log(`The StoryTeller ${this.name} told them the story: ${story.title}`);
    }
  }
  
  
  class Translator {
    constructor(stories, languages) {
      this.stories = stories;
      this.languages = languages;
    }
  
    translate(story, language) {
      if (this.stories.includes(story) && this.languages.includes(language)) {
        console.log(`Translating a story '${story.title}' into this ${language}`);
      
      } else {
        console.log(`Translation for either story '${story.title}' or language '${language}' is not available`);
      }
    }
  }
  
  const story1 = new AncestralStories("The hare and the elephant", 20, "Being nice to others", "Children");
  const story2 = new AncestralStories("The lion and the zebra", 10, "Love", "Children");
  
  const storyteller = new StoryTeller("Lekishon Sheila", [story1, story2]);
  storyteller.tellStory(story1);
  
  const translator = new Translator([story1, story2], ["French", "Spanish"]);
  translator.translate(story2, "French");
  


//   Question2

class Recipe {
    constructor(name, country, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
      this.name = name;
      this.country = country;
      this.ingredients = ingredients;
      this.preparationTime = preparationTime;
      this.cookingMethod = cookingMethod;
      this.nutritionalInfo = nutritionalInfo;
    }
  }
  
  class MoroccanRecipe extends Recipe {
    constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo, spiceLevel) {
      super(name, "Morocco", ingredients, preparationTime, cookingMethod, nutritionalInfo);
      this.spiceLevel = spiceLevel;
    }
  
    setSpiceLevel(level) {
      this.spiceLevel = level;
    }
  }

  class EthiopianRecipe extends Recipe {
    constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo, injeraIncluded) {
      super(name, "Ethiopia", ingredients, preparationTime, cookingMethod, nutritionalInfo);
      this.injeraIncluded = injeraIncluded;
    }
  
    includeInjera() {
      this.injeraIncluded = true;
    }
  }
  
  class NigerianRecipe extends Recipe {
    constructor(name, ingredients, preparationTime, cookingMethod, nutritionalInfo, isSpicy) {
      super(name, "Nigeria", ingredients, preparationTime, cookingMethod, nutritionalInfo);
      this.isSpicy = isSpicy;
    }

    setSpicy(isSpicy) {
      this.isSpicy = isSpicy;
    }
  }

  const moroccanRecipe = new MoroccanRecipe(
    "Chicken",
    ["chicken", "onion", "garlic", "olive oil", "spices"],
    55,
    "Stew",
    "High in protein",
    "Medium"
  );
  moroccanRecipe.setSpiceLevel("High");
  
  const ethiopianRecipe = new EthiopianRecipe(
    "chicken",
    ["chicken", "berbere spice", "onion", "garlic", "ginger"],
    60,
    "stew",
    "flavors",
    true
  );
  ethiopianRecipe.includeInjera();
  
  const nigerianRecipe = new NigerianRecipe(
    "Jollof Rice",
    ["rice", "tomatoes", "onion", "pepper", "spices"],
    45,
    "Popular party dish",
    true
  );
  nigerianRecipe.setSpicy(true);

console.log(nigerianRecipe);
console.log(ethiopianRecipe);
console.log(moroccanRecipe);
  