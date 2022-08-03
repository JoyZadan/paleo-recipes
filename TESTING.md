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
* ![INSERT SCREENSHOT Home page](/documentation/validation/nu-html-index.webp)
* ![INSERT SCREENSHOT other page](/documentation/validation/nu-html-recipes.webp)
* ![INSERT SCREENSHOT other page](/documentation/validation/nu-html-add-recipe.webp)
* ![INSERT SCREENSHOT other page](/documentation/validation/nu-html-categories.webp)
* ![INSERT SCREENSHOT other page](/documentation/validation/nu-html-register.webp)
* ![INSERT SCREENSHOT other page](/documentation/validation//nu-html-login.webp)
* ![INSERT SCREENSHOT about page](/documentation/validation/about-html-validation.png)
* ![INSERT SCREENSHOT other page](/documentation/validation/nu-html-profile.webp)
### CSS: W3C CSS Validator Test Results
* ![INSERT SCREENSHOT Results](/documentation/validation/css-validation.webp)
* ![INSERT SCREENSHOT Warnings](/documentation/validation/css-warnings.webp)
### JavaScript: JSHint Linting Results
* ![INSERT SCREENSHOT scroll.js](/documentation/validation/jshint-validation.webp)
### Python: PEP8 online Test Results
* ![INSERT SCREENSHOT](/documentation/testing/pep8online.png)
### Lighthouse Test Results
* ![INSERT SCREENSHOT Home page](/documentation/testing/lighthouse-desktop-top.webp)
* ![INSERT SCREENSHOT other page](/documentation/testing/lighthouse-recipes.webp)
* ![INSERT SCREENSHOT other page](/documentation/testing/lighthouse-desktop-categories.webp)
* ![INSERT SCREENSHOT other page](/documentation/testing/lighthouse-add-recipe.webp)
* ![INSERT SCREENSHOT other page](/documentation/testing/lighthouse-profile.webp)
* ![INSERT SCREENSHOT other page](/documentation/testing/lighthouse-recipes.webp)
* ![INSERT SCREENSHOT other page](/documentation/testing/lighthouse-categories.webp)
* ![INSERT SCREENSHOT other page](/documentation/testing/lighthouse-recipes.webp)
* ![INSERT SCREENSHOT other page](/documentation/testing/lighthouse-recipes.webp)
* ![INSERT SCREENSHOT about mobile](/documentation/validation/about-lighthouse-mobile.png)
### a11y Color Contrast Accessibility for the Visually Impaired Test Results
* ![INSERT SCREENSHOT Home page](/documentation/testing/a11y-color-contrast-index.png)
* ![INSERT SCREENSHOT other page](/documentation/testing/a11y-color-contrast-recipes.png)
### WAVE Web Accessibility Evaluation Tool
* ![INSERT SCREENSHOT Home page](/documentation/validation/homepage-web-accessibility-test-summary.png)
* ![INSERT SCREENSHOT other page](/documentation/validation/homepage-web-accessibility-test.png)
* ![INSERT SCREENSHOT other page](/documentation/validation/recipes-web-accessibility-test-summary.png)
* ![INSERT SCREENSHOT other page](/documentation/validation/search-recipes-web-accessibility-summary.png)

## Responsive Design Testing
* ![INSERT SCREENSHOT Home page](/documentation/testing/responsiveness-1.png)
* ![INSERT SCREENSHOT other page](/documentation/testing/responsiveness-2.png)
* ![INSERT SCREENSHOT other page](/documentation/testing/responsiveness-3.png)
* ![INSERT SCREENSHOT other page](/documentation/testing/responsiveness-4.png)
* ![INSERT SCREENSHOT other page](/documentation/testing/responsiveness-5.png)
* ![INSERT SCREENSHOT other page](/documentation/testing/responsiveness-6.png)
* ![INSERT SCREENSHOT other page](/documentation/testing/responsiveness-7.png)
* ![INSERT SCREENSHOT other page](/documentation/testing/responsiveness-8.png)

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

