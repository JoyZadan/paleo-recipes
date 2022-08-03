# Paleo Recipes Testing Documentation

![amiresponsive mock-ups of Paleo Recipes App](documentation/testing/paleo-recipes.png)


## MANUAL TESTING
| Test| Goal | Result |
| :--- | :--- | :--- |
| paleorecipe logo renders across all possible device | with the font not changing | Pass |
| Responsiveness | Paleo Recipe app to be responsivess across all device | Pass |
| Flash Messages | Messages to successfully display and provide  users option to close the message | Pass |
| User search for recipe if == 0 | Provide Users feedback about their search query by adding if statement on search route function | Pass |
| Choose Category from dropdown | Categories should be available to choose from | Pass |
| Main Navlinks | Navlinks to work and not hiding a 500 internal server error | Pass |
| Profile Page User Dashboard secondary navlinks | Links work as expected, no broken link | Pass |
| Category ID | From Postgres, this gets stored in MongoDB as category_id for every recipe added | Pass |
| Associated Recipes | These get deleted when a category relevant to them is deleted by superadmin | Pass |
| Scroll to Top button | Works as expected without causing conflict with Jinja templating and or JavaScript | Pass |
| Modal is semantically correct | All HTML Validation to Pass and modal works with out causing a 500 Internal Server Error | Pass |


## Validation Results
### HTML: W3C Markup Validator Test Results
* [/home](/documentation/validation/index-html-validation.png)
* [/recipes](/documentation/validation/recipes-html-validation.png)
* [/add_recipe](/documentation/validation/add-recipe-html-validation.png)
* [/edit_recipe](/documentation/validation/edit-recipe-html-validation.png)
* [/categories](/documentation/validation/categories-html-validation.png)
* [/add_category](/documentation/validation/add-category-html-validation.png)
* [/edit_category](/documentation/validation/edit-category-html-validation.png)
* [/about](/documentation/validation/about-html-validation.png)
* [/profile](/documentation/validation/profile-user-html-validation.png)
* [/register](/documentation/validation/register-html-validation.png)
* [/login](/documentation/validation/login-html-validation.png)
* [/error](/documentation/validation/error-html-validation.png)

### CSS: W3C CSS Validator Test Results
* [css validation](/documentation/validation/css-validation-new.png)
* [css warnings](/documentation/validation/css-warnings-new.png)

### JavaScript: JSHint Linting Results
* [INSERT SCREENSHOT scroll.js](/documentation/validation/jshint-validation.webp)
* [INSERT SCREENSHOT script.js](/documentation/validation/script-js-validation.png)

### Python: PEP8 online Test Results
* [INSERT SCREENSHOT](/documentation/validation/pep8-validation-new.png)

### Lighthouse Test Results
* [/home](/documentation/testing/index-lighthouse-desktop.png)
* [/recipes](/documentation/testing/recipes-lighthouse-desktop.png)
* [/add_recipe](/documentation/testing/add-recipe-lighthouse-desktop.png)
* [/edit_recipe](/documentation/testing/edit-recipe-lighthouse-desktop.png)
* [/categories](/documentation/testing/categories-lighthouse-desktop.png)
* [/add_category](/documentation/testing/add-category-lighthouse-desktop.png)
* [/edit_category](/documentation/testing/edit-category-lighthouse-desktop.png)
* [/profile](/documentation/testing/profile-user-lighthouse-desktop.png)
* [/about](/documentation/testing/about-lighthouse-mobile.png)
* [/register](/documentation/testing/register-lighthouse-desktop.png)
* [/login](/documentation/testing/login-lighthouse-desktop.png)

### a11y Color Contrast Accessibility for the Visually Impaired Test Results
* [/home](/documentation/testing/a11y-color-contrast-index.png)
* [/recipes](/documentation/testing/a11y-color-contrast-recipes.png)

### WAVE Web Accessibility Evaluation Tool
* [/home](/documentation/validation/homepage-web-accessibility-test-summary.png)
* [/home](/documentation/validation/homepage-web-accessibility-test.png)
* [/recipes](/documentation/validation/recipes-web-accessibility-test-summary.png)
* [/search](/documentation/validation/search-recipes-web-accessibility-summary.png)

## Responsive Design Testing
* [/home - mobile](/documentation/testing/responsiveness-1.png)
* [/home - notebook](/documentation/testing/responsiveness-2.png)
* [/recipes - mobile](/documentation/testing/responsiveness-3.png)
* [/recipes - desktop](/documentation/testing/responsiveness-4.png)
* [/register - desktop](/documentation/testing/responsiveness-5.png)
* [/add_recipe - tablet](/documentation/testing/responsiveness-6.png)
* [/categories - notebook](/documentation/testing/responsiveness-7.png)
* [/about - tablet](/documentation/testing/responsiveness-8.png)
* [/profile - mobile1](/documentation/testing/profile-mobile1.png)
* [/profile - mobile2](/documentation/testing/profile-mobile2.png)
* [/profile - mobile3](/documentation/testing/profile-mobile3.png)
* [/profile - tablet1](/documentation/testing/profile-tablet1.png)
* [/profile - tablet2](/documentation/testing/profile-tablet2.png)
* [/profile - xl-screen](/documentation/testing/profile-xl-screen.png)

----

## Testing User Stories from UX Development Section
### First Time Visitor Goals - As a first time user who has not created an account, I want to be able to:
* Immediately understand the main purpose and use of the application, Paleo Recipes, and how to use it
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-1.png)
    * The first visitor is immediately greeted with a brief info Paleo Recipes with two calls to action
* Search for specific recipes or view all recipes
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-2.png)
    * On the recipes page, the first visitor is able to search for any available recipes
* Register/ create a user account
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-3.png)
     * On the register page, the first visitor is able to register and create an account with Paleo Recipes

### Registered User Goals - As a registered user, I want to be able to:
* Add, edit, retrieve and delete my own Paleo recipe(s)
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-4.png)
    * The registered user is able to add, edit, retrieve and delete his/her own Paleo recipe(s)
* Add my own Paleo recipe(s), based on Categories
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-5.png)
    * Frpm the add_recipe page, the registered user has access to available categories when adding his/her own recipe.
* Add, edit, retrieve and delete my review of the recipes
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-6.png)
    * The registered user is able to retrieve, edit and delete his/ her own recipe
* Upload an image with my recipes
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-7.png)
    * The registered user is able to upload an image when uploading his/ her recipe
* Search for specific recipes or view all recipes
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-2.png)
    * On the recipes page, the registered user is able to search for any available recipes
* Learn more about what I can do on the Paleo Recipes App
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-8.png)
    * From the User Dashboard (Profile Page)m registered users are provided additional information about what they are able to do when using the Application.
* Have my own member user dashboard (read functionality)
    * The screenshot immediately above shows the user dashboard example
* Be able to add additional information about my recipe
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-9.png)
    * An additional input area, called Additional Notes, is available on the add_recipe page for any registered users uploading a recipe
* Be forewarned of the consequences of what I am about to do on the App, such as deleting my recipes
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-9.png)
* Logged users provided warnings when attempting to perform a function which may have destructive or unavoidable consequences
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-10.png)

### Site Admin Goals - As an administrator, I want to be able to:
* Have the ability to maintain the Paleo Recipe App and its content
    * ![INSERT SCREENSHOT other page](/documentation/user-stories/user-story-11.png))
    * Superadmin users have the ability to main the Paleo Recipe App, one of which is being able to delete a category including all  recipes associated with the category being deleted. A popup warning comes up that provides the option for the super admin to confirm or cancel the action category deletion.
* Edit and delete any recipe
    * See screenshot above

