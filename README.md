# Shopify-Developer-Intern-Challenge

## Brief

### Step 1.

TASK: Build an inventory tracking web application for a logistics company. We are looking for a web application that meets the requirements listed below, along with one additional feature, with the options also listed below. 

You can tackle this challenge using any technology you want. This is an open-ended task, but we want to focus on high quality back-end code. Custom UIs and interactive frameworks like React are not necessary. Ideally, the web application can run within 15 minutes.

Please provide instructions on how to use your application. The application should be shared as a public Github repo that contains all the necessary configuration to be runnable from Replit without any additional setup.

Information: You can use frameworks, libraries and external dependencies to help you get to the parts you are interested in building, if this helps you; or start from scratch. When building, consider how more features could be added in the future. 

Please focus on what interests you the most. If you need inspiration, here are examples of what you can work on.


#### Basic CRUD Functionality. You should be able to:

- Create inventory items
- Edit Them
- Delete Them
- View a list of them

#### ONLY ONE OF THE FOLLOWING (We will only evaluate the first feature chosen, so please only choose one)

- When deleting, allow deletion comments and undeletion
- Ability to create warehouses/locations and assign inventory to specific locations
- Ability to create “shipments” and assign inventory to the shipment, and adjust inventory appropriately

#### Authentication and CSS/Design are not required and will not be considered during evaluation.

### Step 2: 

Run the app on Replit. Now that you have built your code in GitHub, you will import the project to replit where you will run the application
 
- Create a Replit account and follow the instructions (you can use the YouTube video) on how to get started
- Once you have created your account, link your GitHub challenge link to your Riplit account

## Instructions

- Create or login to an account at [Replit](https://replit.com)
- Click the New Repl button
- Choose to Import from GitHub

![Import](https://i.imgur.com/AjxK3oK.png)

- Provide this repositories URL [https://github.com/greenplastic90/Shopify-Developer-Intern-Challenge](https://github.com/greenplastic90/Shopify-Developer-Intern-Challenge) and click Import from GitHub

![Git Repo](https://i.imgur.com/F0lXHol.png)

- Select `Python` for language
- Configure the Run button with `python manage.py runserver 0:8000`, click Done

![configure](https://i.imgur.com/56LPRcw.png)

- Click on Console and run these commands one at a time and in order, `pip install pipenv` , `pipenv install django`

![install](https://i.imgur.com/H0zAjkR.png)

- In settings.py update `ALLOWED_HOSTS`, replace `shopify-developer-intern-challenge` with the name of your Replit repository, and replace `greenplastic90` with your Replit username ( No Capital Letters)

![settings.py](https://i.imgur.com/nG5mJ6w.png)
![ALLOWED_HOSTS](https://i.imgur.com/907aeFm.png)
- Click Run Button to start the app

## APIs

App is deployed at this [Replit Public Repository](https://replit.com/@greenplastic90/Shopify-Developer-Intern-Challenge#.replit)

### Warehouses
- Get all warehouses `Get` `https://shopify-developer-intern-challenge.greenplastic90.repl.co/warehouses/`
- Add a warehouse `Post` `https://shopify-developer-intern-challenge.greenplastic90.repl.co/warehouses/`

![JSON](https://i.imgur.com/HRF7Fwo.png)

### Inventory Items
- Get all inventory items `Get` `https://shopify-developer-intern-challenge.greenplastic90.repl.co/inventory-items/`
- Add inventory item `Post` `https://shopify-developer-intern-challenge.greenplastic90.repl.co/inventory-items/`

![JSON](https://i.imgur.com/vzChjQe.png)

- Update inventory item `Put` `https://shopify-developer-intern-challenge.greenplastic90.repl.co/inventory-items/{item-id}/`

![JSON](https://i.imgur.com/INuSx7d.png)

- Delete inventory item `Delete` `https://shopify-developer-intern-challenge.greenplastic90.repl.co/inventory-items/{item-id}/`

