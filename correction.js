class Recipe{
    constructor(ingredients,cookingmethod,nutritionalinfo){
        this.ingredients=ingredients;
        // this.preparationtime=preparationtime;
        this.cookingmethod=cookingmethod;
        this.nutritionalinfo=nutritionalinfo;
    }
    timeForPreparation(){
        if(this.preparationtime>=3){
            console.log("this cuisine takes a long time to prepare")
        }
        else{
            console.log("This cuisine can be prepared within a reasonable amount of time");
        }
    }
}
 class MoroccanRecipe extends Recipe{
    constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,flavorings){
        super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
        this.flavorings = flavorings;
    }
 }
 class EthiopianRecipe extends Recipe{
    constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,typeOfOilUsed){
        super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
        this.typeOfOilUsed = typeOfOilUsed;
    }
 }
 class NigerianRecipe extends Recipe{
    constructor(ingredients,preparationtime,cookingmethod,nutritionalinfo,chilliesUsed){
        super(ingredients,preparationtime,cookingmethod,nutritionalinfo)
        this.chilliesUsed = chilliesUsed;
 }
}
const recipe1 = new Recipe("Rice beans", "Nigerian", ["Rice", "Tomatoes", "Pepper", "Onions", "Chicken"], "Boiling/Stir-frying", {"Calories": 200, "Fat": 5});
console.log(recipe1)
const moroccan_recipe = new MoroccanRecipe("chapo beans", ["Lentils", "Tomatoes", "Chickpeas", "Coriander", "Lemon"], 30, "Boiling", {"Calories": 250, "Fat": 3})
console.log(moroccan_recipe)
const ethiopian_recipe = new EthiopianRecipe("Injera", ["Flour", "Water", "Salt"], 60, "Fermentation", {"Calories": 150, "Fat": 2})
console.log(ethiopian_recipe)
const nigerian_recipe = new NigerianRecipe("mushroom Soup", ["mushroom", "Meat", "Fish", "Vegetables", "Pepper"], 90, "Boiling", {"Calories": 300, "Fat": 8})
console.log(nigerian_recipe)


// 3. **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to
// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.
class Species{
    constructor(diet,typicalLifespan,migrationPatterns){
        this.diet =diet;
        this.typicalLifespan = typicalLifespan;
        this.migrationPatterns = migrationPatterns;
    }
    typeOfAnimal(){
        if(this.diet === "herbivorous"){
            console.log("This animal is not a danger to other animals");
        }
        else if(this.diet === "omnivorous"){
            console.log("This animal feeds on plants but also feeds on aome animals");
        }
        else{
            console.log("This animal is very dangerous to other animals and does not eat plants");
        }
    }
}
class Predator extends Species{
    constructor(diet,typicalLifespan,migrationPatterns,typeOfTeeth,claws,venom,name){
    super(diet,typicalLifespan,migrationPatterns)
        this.typeOfTeeth = typeOfTeeth;
        this.claws = claws;
        this.venom = venom;
        this.name = name;
    }
    fastKillers(){
        if(this.venom === true){
            console.log(`The bite of a ${this.name} kills within hours`);
        }
        else{
            console.log(`The bite of a ${this.name} is not deadly`);
        }
    methodOfKilling();{
        if(this.typeOfTeeth.includes("carnassial teeth")){
            console.log(`A ${this.name} kills by slicing up their prey`);
        }
        else{
            console.log("This predator cannot shear their prey's meat after attacks");
        }
    }
    }
}
class Prey extends Species{
    constructor(diet,typicalLifespan,migrationPatterns,defenseMechanisms,name){
    super(diet,typicalLifespan,migrationPatterns)
        this.defenseMechanisms = defenseMechanisms;
        this.name = name;
    }
}

// question4
class Artist{
    constructor(artistsName,country,musicStyle,instruments){
        this.artistsName = artistsName;
        this.country = country;
        this.musicStyle = musicStyle;
        this.instruments = instruments
    }
 addArtists(){
    let artistDatabase = []
    if(!artistDatabase.includes(this.artistsName)){
        return artistDatabase.push(this.artistsName)
    }
 }
 removeArtists(){
    return artistDatabase.shift()
 }
}
class Perfomance extends Artist{
    constructor(artistsName,country,musicStyle,instruments,startTime,stopTime){
        super(artistsName,country,musicStyle,instruments)
        this.startTime = startTime;
        this.stopTime = stopTime;
        this.musicStyle = musicStyle;
}
duration(){
    let timeTaken = this.stopTime - this.startTime;
    return `The duration for the perfomance was ${timeTaken}`
}
schedule(){
    const eventSchedule = {}
   return eventSchedule[this.artistsName] = this.startTime;
}
}
class stage extends Artist{
    constructor(artistsName,country,musicStyle,instruments,supportingArtists){
        super(artistsName,country,musicStyle,instruments)
        this.supportingArtists = supportingArtists;
}
spaceOcuppied(){
    if(this.instruments.includes("drums") && this.supportingArtists===True){
        return `${this.artistsName} will occupy only 50% of the stage`
    }
    if(this.instruments.includes("drums")){
        return `${this.artistsName} will occupy only 70% of the stage`
    }
    if(this.supportingArtists===True){
        return `${this.artistsName} will occupy only 80% of the stage`
    }
}
}

// question5
class Product {
    constructor(name, price, quantity) {
      this.name = name;
      this.price = price;
      this.quantity = quantity;
    }
    calculateTotalValue() {
      return this.price * this.quantity;
    }
    getInfo() {
      const totalValue = this.calculateTotalValue();
      return `${this.name} - Total Value: ${totalValue}`;
    }
  }
  let products = [
    new Product('Laptop', 15000, 2),
    new Product('Phones', 10000, 2),
    new Product('Television', 18000, 2)
  ];
  let totalValue = 0;
  for (let i = 0; i < products.length; i++) {
    totalValue += products[i].calculateTotalValue();
  }
  console.log(`The total value of all products is ${totalValue}`);


