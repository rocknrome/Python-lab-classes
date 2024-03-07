// Defining a class
class House {

    // defining an argument to the constructor function with a default value
    constructor(model = "a"){
        //"this" represent the object currently being constructed
        this.squareFeet = 1000
        this.bathrooms = 2
        if (model === "b"){
            this.bedrooms = 2
        } else {
            this.bedrooms = 3
        }
    }

/*// Create an inspect method for House objects
  inspect(){
    console.log(this)
  }*/

}


// Instantiate an instance of the class
const house = new House("a")
const house2 = new House("b")
/*
house.inspect()
house2.inspect()
*/
console.log(house)
console.log(house2)

/*
// Defining a class
class House {
  // defining an argument to the constructor function with a default value
  constructor(model = "a") {
    //"this" represent the object currently being constructed
    this.squareFeet = 1000;
    this.bathrooms = 2;
    if (model === "b") {
      this.bedrooms = 2;
    } else {
      this.bedrooms = 3;
    }
  }

  // Create an inspect method for House objects
  inspect(){
    console.log(this)
  }
}

class Duplex extends House {

    constructor(model = "a"){
        super(model) // calling the parent constructor
        this.units = 2
    }

}

// Instantiate an instance of the class
const house = new House("a");
const house2 = new House("b");

house.inspect()
house2.inspect()

const duplex = new Duplex("b")
duplex.inspect()*/


/*
// Defining a class
class House {

   // create a static property, to track the number of houses
   static numberOfHouses = 0

  // defining an argument to the constructor function with a default value
  constructor(model = "a") {
    House.addHouse() // increment the count each time a house is created
    //"this" represent the object currently being constructed
    this.squareFeet = 1000;
    this.bathrooms = 2;
    if (model === "b") {
      this.bedrooms = 2;
    } else {
      this.bedrooms = 3;
    }
  }

  // Create an inspect method for House objects
  inspect(){
    console.log(this)
  }

  static addHouse(){
    House.numberOfHouses += 1
  }
}

class Duplex extends House {

    constructor(model = "a"){
        super(model) // calling the parent constructor
        this.units = 2
    }

}

// Instantiate an instance of the class
const house = new House("a");
const house2 = new House("b");

house.inspect()
house2.inspect()

const duplex = new Duplex("b")
duplex.inspect()

console.log(House.numberOfHouses)
*/
