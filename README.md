# Homework 2 for Algorithmic Methods of Data Mining, Fall 2022: *Places of the World*
This repository is for submitting the third homework for the course in the Algorithmic Methods of Data Mining, in the name of Group 36.

![A person using Instagram on their mobile phone](https://images.pexels.com/photos/3569950/pexels-photo-3569950.jpeg?auto=compress&cs=tinysrgb&w=300&h=375&dpr=2)

*Kaputaş Beach, Kaş, Turkey*

Photo by courtesy of Cemal Taskiran @ [Pexels](https://www.pexels.com/@cemal-taskiran-420171/)

## Overview of the Project
This projected attempted to use scrape data from Atlas Obscura, a website that contains a list of the most interesting places in the world. The goal was to use the data to create various search engines that would allow users to search for places based on their query. First, basic scoring methods such as term frequency and inverse document frequency were used to create a search engine. Then, we developed a more advanced search engine with the data avaialble to us. Later we have implemented map visualization of the places. Finally, we have demonstrated our skills in bash scripting and sortin algorithms.


## Summary of the files

1. __`main.ipynb`__: 
	> This notebook contains the all the answers the assignment exercise 7.

2. __`data`__:
   > This folder contains the data was scraped and produced in the project. In particular, you may find `misc/place_urls.txt`, that is the list of URLs of all the places for exercise 1.1. The folder `places` contain all the html files of the places which was asked in part 1.2. Lastly, the folder `parsed_places` contain all the .tsv files which was asked in part 1.3. 

3. __`scripts.py`__:
    > This file contains all the functions that were used in the project. Mainly, functions concerning preprocessing, parsing, and scoring.

4. __`complex_engine.py`__:
   > This file contains the ComplexEngine class which served to implement the advanced search engine for exercise 5

5. __`exer7.ipynb`__: 
    > This notebook contains the all the answers the assignment exercise 7. It is a separate notebook because it is was executed using AWS.

6. __`RankingList.txt`__:
   > This file contains the ranking list of the places for exercise 7.