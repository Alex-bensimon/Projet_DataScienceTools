# Determine the differents factors of succes for a movie 

**Description** : We scrap the data from the wellknow website IMDB, whish is the bigest movie database from our banchmark. From IMDB we get : 21 attributes compose by : 
```
    names
    years
    imdb_ratings
    metascores
    votes
    categories
    mv_pages
    genre1
    genre2
    genre3 
    stars1
    stars2
    stars3
    rank
    nb_oscar
    win
    nom
    runtime
    budget
    gross
```
After cleaning those data and place them in a pandas dataframe. We also decided to add one other features, the director from  "Themoviedb" API which is kind of conected to IMDB (same movie id). To finish we analyse the entire data by using machine learning in order to find correlation betweenn attributes. The 2 different machine learning algothme that we use are, Linear Regression and Decision Tree Regressor from SKlearn.

## Authors

* **Alexadre Bensimon** 
* **Jules Enguehard**
* **Victor Henrio** 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

You need to clone the entire project on your device by doing this command :
```
* git clone https://github.com/Alex-bensimon/Projet_DataScienceTools.git
```
And then execute the main file by execute this command :
```
* main()
```
A menu should appear on your consol. You can now follow the instructions to discover all the functionalities implemented.

### Prerequisites

You need to insatll Python version 2 at least to run beautifulsoup4 

We use all those library :

* BeautifulSoup
* Urllib
* Pandas
* Numpy
* Matplotlib.pyplot
* seaborn
* time
* warning
* requests
* sklearn

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Built With

Python 3.7.6


## License

This project is licensed under the MIT License 

## Acknowledgments

* We thank Remi Ferreira for his high quality courses and his impressive green background. 
We also thank him for sharing his knowledge and his passion with us.
