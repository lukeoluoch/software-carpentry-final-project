import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import ast
import os
import homepage


def create_recipe_manager(current_user):

## ------------------------------ Create Frame ----------------------- ##



    # create the main window
    main_window = tk.Tk()
    main_window.title("Recipe Manager")
    main_window.geometry("800x600")
    
    img = ImageTk.PhotoImage(Image.open("recipe.jpg"))  
    l=tk.Label(image=img)
    l.place(x=0,y=0)

    # create the recipe frame
    recipe_frame = tk.Frame(main_window)
    recipe_frame.grid(row=1, column=0)

    # create the recipe listbox
    recipe_listbox = tk.Listbox(recipe_frame)
    recipe_label = tk.Label(recipe_frame, text="Recipes")
    recipe_label.grid(row=0,column=0)
    recipe_listbox.grid(row=1,column=0)

    # create the recipe details frame
    recipe_details_frame = tk.Frame(main_window)
    recipe_details_frame.grid(row=1,column=1)

    # create the recipe name label and entry widget
    recipe_name_label = tk.Label(recipe_details_frame, text="Recipe Name:")
    recipe_name_label.grid(row=0, column=0, sticky="e")
    recipe_name_entry = tk.Entry(recipe_details_frame)
    recipe_name_entry.grid(row=0, column=1)

    # create the cuisine origin label and entry widget
    cuisine_origin_label = tk.Label(recipe_details_frame, text="Cuisine Origin:")
    cuisine_origin_label.grid(row=1, column=0, sticky="e")
    cuisine_origin_entry = ttk.Combobox(recipe_details_frame, values=[ "American", "Italian", "Chinese", "Mexican","Other"])
    cuisine_origin_entry.grid(row=1, column=1)

    # create the dietary restrictions label and entry widget
    dietary_restrictions_label = tk.Label(recipe_details_frame, text="Dietary Restrictions:")
    dietary_restrictions_label.grid(row=2, column=0, sticky="e")
    dietary_restrictions_entry = ttk.Combobox(recipe_details_frame, values=["None","Vegetarian", "Vegan", "Gluten Free"])
    dietary_restrictions_entry.grid(row=2, column=1)

    # create the ingredients label and listbox
    ingredients_label = tk.Label(recipe_details_frame, text="Ingredients:")
    ingredients_label.grid(row=3, column=0, sticky="e")
    ingredients_listbox = tk.Listbox(recipe_details_frame)
    ingredients_listbox.grid(row=3, column=1)

    # create the ingredient name label and entry widget
    ingredient_name_label = tk.Label(recipe_details_frame, text="Ingredient Name:")
    ingredient_name_label.grid(row=4, column=0, sticky="e")
    ingredient_name_entry = tk.Entry(recipe_details_frame)
    ingredient_name_entry.grid(row=4, column=1)

    # create the calorie label and entry widget
    calorie_label = tk.Label(recipe_details_frame, text="Calorie:")
    calorie_label.grid(row=5, column=0, sticky="e")
    calorie_entry = tk.Entry(recipe_details_frame)
    calorie_entry.grid(row=5, column=1)

    # create the carbohydrates label and entry widget
    carbohydrates_label = tk.Label(recipe_details_frame, text="Carbohydrates:")
    carbohydrates_label.grid(row=6, column=0, sticky="e")
    carbohydrates_entry = tk.Entry(recipe_details_frame)
    carbohydrates_entry.grid(row=6, column=1)

    # create the fats label and entry widget
    fats_label = tk.Label(recipe_details_frame, text="Fats:")
    fats_label.grid(row=7, column=0, sticky="e")
    fats_entry = tk.Entry(recipe_details_frame)
    fats_entry.grid(row=7, column=1)

    # create the proteins label and entry widget
    proteins_label = tk.Label(recipe_details_frame, text="Proteins:")
    proteins_label.grid(row=8, column=0, sticky="e")
    proteins_entry = tk.Entry(recipe_details_frame)
    proteins_entry.grid(row=8, column=1)

    # create the proteins label and entry widget
    global checkbutton_var
    checkbutton_var = tk.IntVar() 
    fave_checkbox = tk.Checkbutton(recipe_details_frame, text="Mark as Favorite", variable=checkbutton_var, onvalue=1, offvalue=0)
    fave_checkbox.grid(row=9, column=1)

    # create the add, edit, and delete buttons
    add_button = tk.Button(recipe_details_frame, text="Add Ingredient")
    add_button.grid(row=10, column=1)
    edit_button = tk.Button(recipe_details_frame, text="Edit Ingredient")
    edit_button.grid(row=11, column=1)

    delete_button = tk.Button(recipe_details_frame, text="Delete Ingredient")
    delete_button.grid(row=12, column=1)    
    
    # create the search frame
    search_frame = tk.Frame(main_window)
    search_frame.grid(row=1, column=2, sticky='w')

    # create the search label and entry widgets
    search_label = tk.Label(search_frame, text="Search Recipes")
    search_label.grid(row=0, column=1)


    # create the cuisine origin label and combobox
    cuisine_origin_label = tk.Label(search_frame, text="Cuisine Origin:")
    cuisine_origin_label.grid(row=2, column=0, sticky="w")

    cuisine_origin_combobox = ttk.Combobox(search_frame, values=[ "American", "Italian", "Chinese", "Mexican","Other"])
    cuisine_origin_combobox.grid(row=2, column=1)

    # create the dietary restrictions label and checkboxes
    dietary_restrictions_label = tk.Label(search_frame, text="Dietary Restrictions:")
    dietary_restrictions_label.grid(row=3, column=0, sticky="w")

    dietary_restrictions_combobox = ttk.Combobox(search_frame, values=["None","Vegetarian", "Vegan", "Gluten Free"])
    dietary_restrictions_combobox.grid(row=3, column=1)

    # create the search button
    search_button = tk.Button(search_frame, text="Search")
    search_button.grid(row=4, column=1)


    # create the favorites frame
    favorites_frame = tk.Frame(main_window)
    favorites_frame.grid(row=2, column=0)


    # create the favorites label
    favorites_label = tk.Label(recipe_frame, text="Favorites:")
    favorites_label.grid(row=2, column=0)

    # create the favorites listbox
    favorites_listbox = tk.Listbox(recipe_frame)
    favorites_listbox.grid(row=3, column=0)


    # create the add recipe button
    add_recipe_button = tk.Button(main_window, text="Add/Edit Recipe")
    add_recipe_button.grid(row=4, column=0)


    # create the delete recipe button
    delete_recipe_button = tk.Button(main_window, text="Delete Recipe")
    delete_recipe_button.grid(row=5, column=0)

    # create the Refresh Lists button
    refresh_button = tk.Button(main_window, text="Refresh Lists")
    refresh_button.grid(row=6, column=0, sticky='s')


    # create the home button
    home_button = tk.Button(main_window, text="Return Home")
    home_button.grid(row=7, column=0, sticky='s')


    # create a dictionaries to store the recipe details (these is global)
    global current_recipe
    global recipes
    global favorites    
    
    current_recipe = {}
    recipes = {}
    favorites = {}
    
   ###### ---------------------------- Ingredient Button Functionalities ------------------------------------# 

    # create a function to add a new ingredient to the current recipe
    def add_ingredient():
        # get the values from the entry widgets
        name = ingredient_name_entry.get()
        calorie = calorie_entry.get()
        carbohydrates = carbohydrates_entry.get()
        fats = fats_entry.get()
        proteins = proteins_entry.get()
        
        # add the values to the current recipe dictionary
        current_recipe.setdefault("ingredients", []).append({
            "name": name,
            "calorie": calorie,
            "carbohydrates": carbohydrates,
            "fats": fats,
            "proteins": proteins
        })
        
        # clear the entry widgets
        ingredient_name_entry.delete(0, tk.END)
        calorie_entry.delete(0, tk.END)
        carbohydrates_entry.delete(0, tk.END)
        fats_entry.delete(0, tk.END)
        proteins_entry.delete(0, tk.END)
        
        # update the ingredients listbox
        update_ingredients_listbox()

    # create a function to edit an existing ingredient in the current recipe
    def edit_ingredient():
        # get the selected ingredient from the listbox
        selected_index = ingredients_listbox.curselection()
        if selected_index:
            selected_ingredient = current_recipe["ingredients"][selected_index[0]]
            
            # update the values in the current recipe dictionary
            selected_ingredient["name"] = ingredient_name_entry.get()
            selected_ingredient["calorie"] = calorie_entry.get()
            selected_ingredient["carbohydrates"] = carbohydrates_entry.get()
            selected_ingredient["fats"] = fats_entry.get()
            selected_ingredient["proteins"] = proteins_entry.get()
            
            # clear the entry widgets
            ingredient_name_entry.delete(0, tk.END)
            calorie_entry.delete(0, tk.END)
            carbohydrates_entry.delete(0, tk.END)
            fats_entry.delete(0, tk.END)
            proteins_entry.delete(0, tk.END)
            
            # update the ingredients listbox
            update_ingredients_listbox()

    # create a function to delete an existing ingredient from the current recipe
    def delete_ingredient():
        # get the selected ingredient from the listbox
        selected_index = ingredients_listbox.curselection()
        if selected_index:
            selected_ingredient = current_recipe["ingredients"][selected_index[0]]
            
            # remove the ingredient from the current recipe dictionary
            current_recipe["ingredients"].remove(selected_ingredient)
            
            # clear the entry widgets
            ingredient_name_entry.delete(0, tk.END)
            calorie_entry.delete(0, tk.END)
            carbohydrates_entry.delete(0, tk.END)
            fats_entry.delete(0, tk.END)
            proteins_entry.delete(0, tk.END)
            
            # update the ingredients listbox
            update_ingredients_listbox()

    # create a function to update the ingredients listbox
    def update_ingredients_listbox():
        # clear the listbox
        ingredients_listbox.delete(0, tk.END)
        
        # add the ingredients to the listbox
        for ingredient in current_recipe.get("ingredients", []):
            name = ingredient["name"]
            calorie = ingredient["calorie"]
            carbohydrates = ingredient["carbohydrates"]
            fats = ingredient["fats"]
            proteins = ingredient["proteins"]
            ingredients_listbox.insert(tk.END, f"{name} ({calorie} kcal, {carbohydrates} g carbs, {fats} g fats, {proteins} g proteins)")



    # bind the add, edit, and delete
    add_button.config(command=add_ingredient)
    edit_button.config(command=edit_ingredient)
    delete_button.config(command=delete_ingredient)
    
    
    
    # ------------------------------------- Recipe Button Functionalities -----------------------------------------------------#
    
    # function to update the recipe listbox
    def update_recipe_listbox():
        # clear the recipe listbox
        recipe_listbox.delete(0, tk.END)
        # add the recipes to the recipe listbox
        for recipe_name in recipes.keys():
            recipe_listbox.insert(tk.END, recipe_name)
            
    # function to update the favorite listbox
    def update_favorite_listbox():
        # clear the favorite listbox
        favorites_listbox.delete(0, tk.END)
        # add the favorites to the favorite listbox
        for favorite_name in favorites.keys():
            favorites_listbox.insert(tk.END, favorite_name)


    # load exisiting recipes
    def load_existing_recipes():
        # global current_user
        global recipes
        global favorites

        if (current_user):
            recipe_file = f"{current_user}-recipes.txt"
            favorites_file = f"{current_user}-favorites.txt"
            
            recipe_arr= []

    
            if os.path.isfile(recipe_file) == False:
                open(recipe_file, 'w').close()    
            
            if os.path.isfile(favorites_file) == False:
                open(favorites_file, 'w').close()    
                    
                    
            with open(recipe_file, "r") as file_input: 
                for line in file_input:
                    
                    if line.split("\n")[0]:
                        this_recipe = ast.literal_eval(line.split("\n")[0])
                        recipes[this_recipe['name']] = this_recipe
            
            with open(favorites_file, "r") as file_input: 
                for line in file_input:
                    
                    if line.split("\n")[0]:
                        this_recipe = ast.literal_eval(line.split("\n")[0])
                        favorites[this_recipe['name']] = this_recipe    
                        
            update_favorite_listbox()
            update_recipe_listbox()                                                            
                
        
    load_existing_recipes()



    def delete_recipe_from_txt(name):
        """ Deletes recipe from the recipes textfile

        Args:
            name (str): name of the recipe to be deleted
        """
        if (current_user):
            recipe_file = f"{current_user}-recipes.txt"
            favorites_file = f"{current_user}-favorites.txt"
            
            recipe_arr = []
            favorites_arr = []
            
            # iterate through all saved recipes    
            with open(recipe_file, "r") as file_input: 
                for line in file_input:
                    if line.split("\n")[0]:
                        this_recipe = ast.literal_eval(line.split("\n")[0])
                        
                        if name != this_recipe["name"]:
                            recipe_arr.append(this_recipe)
            
            # empty file
            open(recipe_file, "w").close()
            
            # repopulate file               
            for individual_recipe in recipe_arr:
            
                with open(recipe_file, 'a') as file:
                    file.write("\n"+str(individual_recipe))
            
            # iterate through all saved faves    
            with open(favorites_file, "r") as file_input: 
                for line in file_input:
                    if line.split("\n")[0]:
                        this_recipe = ast.literal_eval(line.split("\n")[0])
                        
                        if name != this_recipe["name"]:
                            favorites_arr.append(this_recipe)
            
            # empty file
            open(favorites_file, "w").close()
            
            # repopulate file         
            for individual_recipe in favorites_arr:
            
                with open(favorites_file, 'a') as file:
                    file.write("\n"+str(individual_recipe))
            


    # function to add a recipe to the recipe dictionary
    def add_recipe():
        # get the values from the entry widgets
        name = recipe_name_entry.get()
        cuisine = cuisine_origin_entry.get()
        dietary = dietary_restrictions_entry.get()
        ingredients = current_recipe
        global checkbutton_var
        
        # add the recipe to the recipes dictionary
        if name in recipes:
            recipes.pop(name)
            
        if name in favorites:
            favorites.pop(name)
            
        recipes[name] = {"name": name, "cuisine": cuisine, "dietary": dietary, "ingredients": ingredients}
        
        # global current_user
        
        recipe_file = f"{current_user}-recipes.txt"
        favorites_file = f"{current_user}-favorites.txt"
        
        with open(recipe_file, 'a') as file:
            file.write("\n"+str(recipes[name]))
        
        
        
        
        # favorites update
        if checkbutton_var.get() == 1:
            add_to_favorites()
            with open(favorites_file, 'a') as file:
                file.write("\n"+str(recipes[name]))
        
            
        # update the recipe listbox
        update_recipe_listbox()
        update_favorite_listbox()
        



    # function to delete a recipe from the recipe dictionary
    def delete_recipe():
        selected_recipe = recipe_listbox.get(tk.ACTIVE)
        selected_fave = favorites_listbox.get(tk.ACTIVE)
        # global current_user
        
        recipe_file = f"{current_user}-recipes.txt"
        favorites_file = f"{current_user}-favorites.txt"
        
        if selected_recipe:
            recipes.pop(selected_recipe)
            
            if selected_recipe in favorites:
                favorites.pop(selected_recipe)
            
            
            update_recipe_listbox()
            update_favorite_listbox()
            delete_recipe_from_txt(selected_recipe)
        


    def search_recipes():
        cuisine_origin = cuisine_origin_combobox.get()
        dietary_restrictions = dietary_restrictions_combobox.get()
        matching_recipes = []
        
        
        for recipe in recipes.values():
            if cuisine_origin.lower() in recipe["cuisine"].lower():
                if dietary_restrictions.lower() in recipe["dietary"].lower():
                    matching_recipes.append(recipe)
        recipe_listbox.delete(0, tk.END)
        for recipe in matching_recipes:
            recipe_listbox.insert(tk.END, recipe["name"])

    # function to update the recipe entry widgets based on the selected recipe
    def update_recipe_entry():
        selected_recipe = recipe_listbox.get(tk.ACTIVE)
        if selected_recipe:
            recipe = recipes[selected_recipe]
            recipe_name_entry.delete(0, tk.END)
            recipe_name_entry.insert(tk.END, recipe["name"])
            cuisine_origin_entry.delete(0, tk.END)
            cuisine_origin_entry.insert(tk.END, recipe["cuisine"])
            dietary_restrictions_entry.delete(0, tk.END)
            dietary_restrictions_entry.insert(tk.END, recipe["dietary"])
            
            global current_recipe
            current_recipe = recipe["ingredients"]
            update_recipe_listbox()
            update_favorite_listbox()
            

    

    # function to add a recipe to the favorites dictionary
    def add_to_favorites():
        # get the values from the entry widgets
        name = recipe_name_entry.get()
        cuisine = cuisine_origin_entry.get()
        dietary = dietary_restrictions_entry.get()
        ingredients = current_recipe
        
        # add the recipe to the recipes dictionary
        favorites[name] = {"name": name, "cuisine": cuisine, "dietary": dietary, "ingredients": ingredients}
        update_favorite_listbox()
        



            
    def refresh_lists():
        """ Refreshes both recipe and favorites litsboxes
        """
        update_recipe_listbox()
        update_favorite_listbox()


    def return_home():
        """ Returns the user to the homepage
        """
        main_window.destroy()
        homepage.create_homepage('test')


    # add functionality to recipe buttons
    add_recipe_button.config(command=add_recipe)
    delete_recipe_button.config(command=delete_recipe)
    refresh_button.config(command=refresh_lists)
    home_button.config(command=return_home)
    search_button.config(command=search_recipes)







    # start the tkinter event loop
    main_window.mainloop()


if __name__ == "__main__":
    create_recipe_manager('test')