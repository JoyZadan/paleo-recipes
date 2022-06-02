# PALEO RECIPES

(INSERT HERE am i responsive screenshot)

# Project Overview
Welcome to Paleo Recipes, an App designed to ...

(INSERT HERE longer overview incl the what, why, who, where, how)

(INSERT HERE link to deployed App)

---

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
- [Bugs and Issues](#bugs-and-issues)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

</details>

---

# UX Development

## Strategy
### Project Goals
* To develop an App where users can easily find Paleo recipes, add and manage their own Paleo recipes and share their opinion on recipes and find other users' opinions and recipe contribution
* Use Mobile First design principle in building a responsive App
* Present the available information in a user friendly way
* Provide users the option to register, login and delete their account
* Provide registered users access to a full CRUD functionality
* Include defensive programming to enable users to make an informed decision when deleting recipes
* Handle any errors to help the users understand the issue and contact the App owner if any error should persist
### Business Goals
* Potentially include referral links to specialist sellers of Paleo-friendly ingredients
### User Demographic
* Ages 16 and above for viewing, registering and contributing to recipes
* Visitors who are interested in Paleo recipes
* Registered users who want to contribute and share their opinions
### User Stories
#### First Time Visitor Goals - As a first time user who has not created an account, I want to be able to:
* Immediately understand the main purpose and use of the application, Paleo Recipes, and how to use it
* Search for specific recipes or view all recipes
* Register/ create a user account
#### Registered User Goals - As a registered user, I want to be able to:
* Add, edit, retrieve and delete my own Paleo recipe(s)
* Add my own Paleo recipe(s), based on Categories
* Add, edit, retrieve and delete my review of the recipes
* Edit my account information
* Delete my account
#### Site Admin Goals - As an administrator, I want to be able to:
* Have the ability to maintain the Paleo Recipe App and its content
* Edit and delete any recipe
* Add, edit, retrieve and delete any recipe by category
* Add, edit, retrieve and delete any reviews

## Scope
### Feature Ideas Planning
When planning the App features and scope, I drew up an Importance Viability analysis of these features, please see below:

| # | Feature | Importance | Viability |
| --- | --- | --- | --- |
| 1 | View, Create, Edit and Delete Recipes | 5 | 5 |
| 2 | View, Create, Edit and Delete Recipe Reviews | 5 | 5 |
| 3 | View, Create, Edit and Delete Recipe Category | 5 | 5 |
| 4 | Create, Edit and Delete Account | 5 | 5 |
| 5 | Login and Logout to Account | 5 | 5 |
| 6 | Moderate Content Submitted by Registered Users | 5 | 1 |
| 7 | Send message and/ or feedback to Admin | 5 | 5 |
| 8 | Receive Notifications on users activities | 2 | 2 |
| 9 | Search for Recipes | 5 | 5 |
| 10 | Search Recipes by Ingredients | 3 | 1 |
| 11 | Search Recipes by Category | 5 | 3 |
| 12 | Share Recipes on Social Media | 3 | 3 |
| 13 | Display Suggested Recipes | 3 | 2 |
| 14 | User Input Validation | 5 | 5 |

Based on the results of the Feature Ideas Planning, I have decided to attempt to implement Features numbers 1, 2, 3, 4, 5, 7, 9, 14 for this production release and park the remaining features due to time limitations.

### Functionality Requirements
* Clean and themed presentation of recipe details
* Intuitive App navigation
* Fresh-looking, appetising and themed use of images across the App
* Contact the developer for feedback and bug reports

## Structure
### Topology Diagrams
The green elements in these diagrams illustrate the pages that are always accessible from the Navbar for all visitors.
The non-highlighted elements in these diagrams will return the use to the same page or to the home page. Add, edit and delete elements are only available to logged in users. The delete functions will return to:
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
- [INSERT SCHEMA FOR RELATIONAL DB]()
- [INSERT DB STRUCTURE FOR MONGODB]()


## Skeleton
To view the wireframe created for this project, [click here]().

### Design
[FINALISE: Bootstrap5 | Materialize]() was used and customised for the front-end development.

#### Colour Scheme
[INSERT HERE]()

#### Typography
[INSERT HERE]()

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
All testing undertaken for this project can be found in the [Testing Document](/readme_docs/testing.md)

# Bugs and Issues

# Deployment

# Credits
## Resources
README and Testing Inspirations from [Nick Lennon](https://github.com/nlenno1/moviewiki-ms3) and [Naoise Gaffney](https://github.com/NaoiseGaffney/Training)

# Acknowledgements



