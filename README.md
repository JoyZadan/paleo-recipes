# **PALEO RECIPES**


Paleo Recipes is a place for visitors to find recipes and delicious meal ideas. Users are able to register a free account, share, manage and dish out *(no pun intended!)* their own paleo recipes for eating healthy.

![amiresponsive mock-ups of Paleo Recipes App](documentation/testing/paleo-recipes.png)

### [Link to the Deployed App](https://paleo-recipes.herokuapp.com/)

![GitHub last commit](https://img.shields.io/github/last-commit/JoyZadan/paleo-recipes?color=blue&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/JoyZadan/paleo-recipes?color=green&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/JoyZadan/paleo-recipes?color=orange&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/JoyZadan/paleo-recipes?color=brown&style=for-the-badge)

# Project Overview

Paleo Recipes is a recipe sharing and management Application built using **Python**, **Flask+SQLAlchemy**, **Flask+PyMongo**, **Bootstrap 5**, **Jinja2** and **JavaScript**. It uses **Cloudinary API** to manage user-uploaded images. This Application is a **hybrid database project** using both **MongoDB** and **PostgreSQL**.

- User Authentication is handled using **relational-backed database** (PostgreSQL using Flask+SQLAlchemy).
- Standard CRUD data manipulation is handled using a **nonrelational-backed database** (MongoDB using Flask+PyMongo).

Paleo Recipes is my third milestone project for **Code Institute's** Level 5 Diploma in Web Application Development (Full Stack Software Development).

It was an easy choice to decide on building this App as I have tried and enjoyed the paleo-eating lifestyle and know that I have enough background information to make the job of building a hybrid database application a little less daunting! Plus paleo dishes almost always look great in photos, though that may mean a few extra trips to the kitchen to raid the fridge!

But what is the Paleo diet? According to the [Mayo Clinic](https://www.mayoclinic.org/healthy-lifestyle/nutrition-and-healthy-eating/in-depth/paleo-diet/art-20111182), *"a paleo diet is a dietary plan based on foods similar to what might have been eaten during the Paleolithic era, which dates from approximately 2.5 million to 10,000 years ago. A paleo diet typically includes lean meats, fish, fruits, vegetables, nuts and seeds — foods that in the past could be obtained by hunting and gathering. A paleo diet limits foods that became common when farming emerged about 10,000 years ago. These foods include dairy products, legumes and grains."*


<details>
<summary>
Table of Contents - Click to Expand
</summary>

- [UX DEVELOPMENT](#ux-development)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs, Issues and Solutions](#bugs-issues-and-solutions)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

</details>

---

# UX Development

## Strategy
### Project Goals
* To develop an App where users can easily find Paleo recipes.
* Gues users will be able to view and find recipes, even without having their own account.
* Registered users will also be able to share and manage their own Paleo recipes.
* Use Mobile First design principle in building a responsive App
* Present the available information in a user friendly way
* Provide users the option to register and create an account.
* Provide registered users (members) access to a full CRUD functionality
* Provide registered users (superadmin) access to a full CRUD functionality
* Provide registered users (members and superadmin) access to a custom user dashboard with read functionality.
* Include defensive programming to enable users to make an informed decision when deleting recipes
* Handle any errors to help the users understand the issue

### User Demographic
* Ages 16 and above for viewing, registering and contributing to recipes
* Visitors who are interested in Paleo diet or who already follow the Paleo lifestyle
* Visitors who are looking for healthier dishes (paleo)
* Registered users who want to an easy to way find Paleo recipes and meal plans
* Registered users who want to share their favourite recipes for others to also enjoy

### User Stories
#### First Time Visitor Goals - As a first time user who has not created an account, I want to be able to:
* Immediately understand the main purpose and use of the application, Paleo Recipes, and how to use it
* Search for specific recipes or view all recipes
* Register/ create a user account

#### Registered User Goals - As a registered user, I want to be able to:
* Learn more about what I can do on the Paleo Recipes App
* Add, edit, retrieve and delete my own paleo recipe(s)
* Add my own Paleo recipe(s), based on Categories
* Upload an image with my recipes
* Be able to add additional information about my recipe
* Have access to tools I may need in order to add, update or delete my recipes
* Search and view specific recipes (if already available on the App)
* Be forewarned of the consequences of what I am about to do on the App, such as deleting my recipes
* Have my own member user dashboard (read functionality)

#### Site Admin Goals - As an administrator, I want to be able to:
* Have the ability to maintain the Paleo Recipe App, in particular the categories
* Add, edit and delete my own recipes
* Add, edit, retrieve and delete any recipe by category
* Search and view specific recipes (if already available on the App)

## Scope
### Feature Ideas Planning
When planning the App features and scope, I drew up an Importance Viability analysis of these features, please see below:

| # | Feature | Importance | Viability |
| --- | --- | --- | --- |
| 1 | View, Create, Edit and Delete Recipes | 5 | 5 |
| 2 | View, Create, Edit and Delete Images with Recipes | 5 | 5 |
| 3 | View, Create, Edit and Delete Recipe Category | 5 | 5 |
| 4 | Create, Edit and Delete Account | 5 | 3 |
| 5 | Login and Logout to Account | 5 | 5 |
| 6 | Moderate Content Submitted by Registered Users | 5 | 1 |
| 7 | Send message and/ or feedback to Admin | 5 | 2 |
| 8 | Receive Notifications on users activities | 2 | 2 |
| 9 | Search for Recipes | 5 | 5 |
| 10 | Search Recipes by Ingredients | 3 | 1 |
| 11 | Search Recipes by Category | 5 | 2 |
| 12 | Share Recipes on Social Media | 3 | 3 |
| 13 | Display Suggested Recipes | 3 | 2 |
| 14 | Access to Custom User Dashboard (Read Functionality) | 4 | 5 |
| 15 | User Action Validation | 5 | 5 |

Based on the results of the Feature Ideas Planning, I have decided to attempt to implement Features numbers 1, 2, 3, 5, 9, 14 and 15 for this production release and park the remaining features due to time limitations.

### Functionality Requirements
* Clean and themed presentation of recipe details
* Intuitive App navigation
* Fresh-looking, appetising and themed use of images across the App
* Use of Defensive Programming to Safeguard Logged In Users (Members and Superadmin) about any unintended result of their actions

## Structure
### Topology Diagrams
The green elements in these diagrams illustrate the pages that are always accessible from the Navbar for all visitors.
The non-highlighted elements in these diagrams will return the user to the same page or to the home page. Add, edit and delete elements are only available to logged in users. The delete functions will return to:
- [INSERT]
- [INSERT]

#### Guest User
- [INSERT DIAGRAM]()

#### Registered User
- [INSERT DIAGRAM]()

#### Admin User
- [INSERT DIAGRAM]()

#### Jinja Template Structure and Relationships
- [INSERT DIAGRAM]()

### Database Schema and Structure
- ![COMBINED RELATIONAL(POSTGRES) AND NONRELATIONAL (MONGO )DATABASES SCHEMA](/documentation/testing/combined-postgres-mongo-db.png)


## Skeleton
### Wireframes
To view the wireframe created for this project, [click here]().

### Design
[Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used and customised for the front-end development.

#### Colour Scheme
![COLOURS](/documentation/user-stories/colours.webp)

#### Typography

I used Google Fonts to import the fonts I used across the application.

![DANCING SCRIPT](/documentation/user-stories/dancing-script.png)
![POPPINS](/documentation/user-stories/poppins.png)

#### Imagery
[INSERT HERE]()
The background image for the home page inspired the colour scheme and typography used for the App.

## Features
Breakdown of the features and elements implemented for the App.
### Multi Page Elements
#### Navbar
- Logo
- Home
- About

#### Footer
#### /home
#### /recipes
#### /search

### CRUD TABLE
| Page | Create | Read | Update | Delete |
| --- | --- | --- | --- | --- |
| home | | | | |
| recipes | | | | |

### Defensive Programming

# Technologies Used
* Languages:
    * [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the content and structure of the site.
    * [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the styling of the site.
    * [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactivity of the site.
    * [Python](https://www.python.org/) was used for the back end programming of the site.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    * Flask was used to handle the templating for the site.

* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
    * Flask-PyMongo provides MongoDB support for Flask applications.

* [pip](https://pip.pypa.io/en/stable/)
    * Pip is the package installer for Python, allowing us to install the packages we need for this site.

* [dnspython](https://www.dnspython.org/)
    * Dnspython is a DNS toolkit for python.

* [Werkzeug](https://wsgi.readthedocs.io/en/latest/what.html)
    * Werkzeug is a Web Server Gateway Interface web application library.

* [Jinja](https://www.palletsprojects.com/p/jinja/)
    * Jinja is a templating engine for Python, used to write Flask and other templating services.

* [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to create the wireframes for this project.

* [Git](https://git-scm.com/)
    * Git was used for version control and saving work in the repository, using the GitPod extension in Google Chrome to commit to GitHub.

* [Bootstrap 5](https://getbootstrap.com/)
    * Bootstrap is one of the most popular front-end open source toolkit and was used for ease of styling the Earthlings app.

* [Chrome](https://www.google.com/intl/en_uk/chrome/)
    * This project was created in the Google Chrome browser, and as such Chrome was used as the default testing browser.

* [Heroku](https://devcenter.heroku.com/)
    * Heroku is where we deploy this live site. Throughout, we have ensured the version being deployed to Heroku matches the development version by checking features and screen layouts on both versions.

* [MongoDB](https://www.mongodb.com/)
    * MongoDB is where we host our NoSQL database.

* [GitHub](https://github.com/)
    * GitHub is where we host our site.

* [Online-Convert](https://www.online-convert.com/)
    * Online-Convert was used to convert the png images to webp.

# Testing
All testing undertaken for this project can be found in the [Testing Document](/TESTING.md)

# Bugs, Issues and Solutions
| # | Bugs, Errors and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | NoneType error of object has no attribute 'startswith' when attempting to run the application | With the assistance of tutor team, the solution was to add ![this extra line of code]() to the init file and the Application successfully started running locally |
| 2 | NoneType error object has no attribute 'drivername' when attempting to generate and migrate the models into a new database in Postgres | With the assistance of tutor team, the solution was to remove the extra line of code (see error 1), if uri: , and replace it with ![this code block](). According to James from Tutor Support: This new code block "checks if you are in development/ local and if true, assigns the sql database uri to DB_URL from env.py. (DB_URL is the local database.) Otherwise, it assigns it to the Heroku one,  DATABASE_URL." The db.create_all() was then ![successfully executed](). |
| 3 | New user id (Primary Key) is not being stored as a user_id in MongoDB | The solution was to query Postgres db for the new user's id, save the result in a new variable and pass it on to MongoDB as a string using dot notation |
| 4 | The logged in user's chosen avatar won't render, despite three days of attempting to resolve the issue | Conscious of the development time remaining prior to submission due date, the remedy was to remove this feature.|
| 5 | Including the parameter of **username** to profile view throws a build error when a logged in user clicks on the register link on the navbar, despite having on the register route a redirect to profile view when a user is logged. | The solution is to remove the **username** parameter on the profile view. The logged in user is then redirected back to the profile view when the register link on the navbar is clicked. |
| 6 | Creating an index on mongodb via the CLI returned an error of "no module app found". Attempting to create said index using the create index form on mongo also resulted in "Index Build Failed. Error provided: Unknown error." | My solution: |


# Deployment & Local Development
## Deployment to Heroku
## Local Development
## Making Local Clone

# Credits
## Code
* The solution to implementing Cloudinary API to allow users to upload images was inspired by the Code Institute Slack Community and in partular, by [James Bennison's](https://github.com/JDBennison/playparkpubs) MS3 Project.
## Content
Sample recipes posted on the Paleo Recipes App were sourced from:
* [The Paleo Diet](https://thepaleodiet.com/)
* [Ambitious Kitchen](https://www.ambitiouskitchen.com/)
* [Paleo Running Momma](https://www.paleorunningmomma.com/)

## Media
## Resources
README and Testing Inspirations from [Nick Lennon's](https://github.com/nlenno1/moviewiki-ms3) and [Naoise Gaffney's](https://github.com/NaoiseGaffney/Training) individual README documentation for MS3.

# Acknowledgements

# Copyrights




