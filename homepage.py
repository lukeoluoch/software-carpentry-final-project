import tkinter as tk
from tkinter import ttk
import numpy as np
import tkcalendar
import os 
import ast
import re
import log_entry
from tkinter import messagebox
import login
import recipe_manager
from PIL import Image, ImageTk


def create_homepage(current_user):
    '''
    
    
    '''
    
    #Variables
    
    
    global current_calories 
    global default_calories 
    global current_carbs 
    global default_carbs 
    global current_fat 
    global default_fat 
    global current_protein 
    global default_protein 
    global current_food_log 
    global current_gym_log 
    
    
    current_calories = 0
    default_calories = 2000

    current_carbs = 0
    default_carbs = 250

    current_fat = 0
    default_fat = 100

    current_protein = 0
    default_protein = 200

    current_food_log = []
    current_gym_log =[]
    
    
    #---------------------------------------- User's Information Text-----------------------------------------#

    info_file = f"user_files/{current_user}-information.txt"
    
    if os.path.isfile(info_file) == False:
        with open(info_file, 'a') as file:
            file.write(f"Calorie Goal: {default_calories}\n")
            file.write(f"Carbohydrate Goal: {default_carbs}\n")
            file.write(f"Fats Goal: {default_fat}\n")
            file.write(f"Protein Goal: {default_protein}\n")

    else:
        global user_data
        user_data = []
        with open(info_file, "r") as file_input: 
            for line in file_input:
                user_data_line = line.split("\n")[0]                   
                user_data.append(int(re.findall(r'\d+', user_data_line)[0]))
        print(user_data)
        
        user_cal = user_data[0]
        user_carb = user_data[1]
        user_fat = user_data[2]
        user_protein = user_data[3]
        
        
        default_calories = user_cal
        default_carbs = user_carb
        default_fat = user_fat
        default_protein = user_protein
        
        
  #------------------------------------------- Button Commands ----------------------------------------------------#      
            
    
    
    
    
    
    # Add Food Button
    def add_food():
        
        filewin = tk.Toplevel(root)
        filewin.title("Add Food")
        filewin.geometry("250x250")
        name_var=tk.StringVar()
        cal_var= tk.StringVar()
        carb_var = tk.StringVar()
        fat_var = tk.StringVar()
        protein_var = tk.StringVar()
        
        def submit():
            
            global current_calories 
            global default_calories 
            global current_carbs 
            global default_carbs 
            global current_fat 
            global default_fat 
            global current_protein 
            global default_protein 
            global current_food_log 
    
            name=name_var.get()
            cal=int(cal_var.get())
            carb=int(carb_var.get())
            fat=int(fat_var.get())
            protein =int(protein_var.get())
            food_item = [name,cal,carb,fat,protein]
            
            current_food_log.append([food_item])
            
            print(current_food_log)
            name_var.set("")
            cal_var.set(0)
            carb_var.set(0)
            fat_var.set(0)
            protein_var.set(0)
            
            current_calories = current_calories + cal
            current_carbs = current_carbs + carb
            current_fat = current_fat + fat
            current_protein = current_protein + protein
            
            cal_label.config(text = "Calories: "+ str(current_calories)+ ' / '+ str(default_calories)+ ' kcal')        
            carb_label.config(text = "Carbohydrates: "+ str(current_carbs)+ ' / '+ str(default_carbs)+ ' grams')
            fat_label.config(text = "Fat: "+ str(current_fat)+ ' / '+ str(default_fat)+ ' grams')
            protein_label.config(text ="Protein: "+ str(current_protein)+ ' / '+ str(default_protein)+ ' grams')
            
            filewin.destroy()
            messagebox.showinfo("Kamehameha!", "Senzu Bean! Food Successfully Added.")
            
        
        entry_1 = tk.Entry(filewin, textvariable= name_var)
        entry_2 = tk.Entry(filewin, textvariable= cal_var)
        entry_3 = tk.Entry(filewin, textvariable= carb_var)
        entry_4 = tk.Entry(filewin, textvariable= fat_var)
        entry_5 = tk.Entry(filewin, textvariable= protein_var)
        
        label_1 = tk.Label(filewin, text = "Food Name")
        label_2 = tk.Label(filewin, text = "Calories")
        label_3 = tk.Label(filewin, text = "Carbohydrates (grams)")
        label_4 = tk.Label(filewin, text = "Total Fat (grams)")
        label_5 = tk.Label(filewin, text = "Protein (grams)")
        
        save_button = tk. Button(filewin, text= "Save", command= submit)
        
        label_1.pack()
        entry_1.pack()
        label_2.pack()
        entry_2.pack()
        label_3.pack()
        entry_3.pack()
        label_4.pack()
        entry_4.pack()
        label_5.pack()
        entry_5.pack()
        save_button.pack()
        return
    
    
    
    # Add Recipe Button
    def add_recipe():
        filewin = tk.Toplevel(root)
        filewin.title("Add Recipe")
        filewin.geometry("250x250")
        title = tk.Label(filewin, text='Recipe List')
        recipe_listbox = tk.Listbox(filewin)
        
        recipes = {}
        favorites = {}

        
        recipe_file = f"user_files/{current_user}-recipes.txt"
        
        
        recipe_arr= []
        recipe_names = []

            
        with open(recipe_file, "r") as file_input: 
            for line in file_input:
                
                if line.split("\n")[0]:
                    this_recipe = ast.literal_eval(line.split("\n")[0])
                    recipes[this_recipe['name']] = this_recipe
                    recipe_arr.append(this_recipe['ingredients'])
                    recipe_names.append(this_recipe['name'])
        
        
        print(recipe_names)
        # print(recipe_arr)
        
        
                        
        # clear the recipe listbox
        recipe_listbox.delete(0, tk.END)
        # add the recipes to the recipe listbox
        for recipe_name in recipes.keys():
            recipe_listbox.insert(tk.END, recipe_name)
        
        def submit():
            
            global current_calories 
            global default_calories 
            global current_carbs 
            global default_carbs 
            global current_fat 
            global default_fat 
            global current_protein 
            global default_protein 
            global current_food_log 
            
            for i in range (len(recipe_arr)):
                if recipe_names[i] == recipe_listbox.get(tk.ACTIVE):
                    ingredient_arr =recipe_arr[i]['ingredients']
                    for recipe in ingredient_arr:
                        
                        name= recipe['name']
                        cal=int(recipe['calorie'])
                        carb=int(recipe['carbohydrates'])
                        fat=int(recipe['fats'])
                        protein =int(recipe['proteins'])
                        food_item = [name,cal,carb,fat,protein]
                        
                        current_food_log.append([food_item])
                        print(current_food_log)
                        
                        
                        
                        
                        current_calories = current_calories + cal
                        current_carbs = current_carbs + carb
                        current_fat = current_fat + fat
                        current_protein = current_protein + protein
        
            
            
            
           
            
            cal_label.config(text = "Calories: "+ str(current_calories)+ ' / '+ str(default_calories)+ ' kcal')        
            carb_label.config(text = "Carbohydrates: "+ str(current_carbs)+ ' / '+ str(default_carbs)+ ' grams')
            fat_label.config(text = "Fat: "+ str(current_fat)+ ' / '+ str(default_fat)+ ' grams')
            protein_label.config(text ="Protein: "+ str(current_protein)+ ' / '+ str(default_protein)+ ' grams')
            
            filewin.destroy()
            messagebox.showinfo("Destructo Disk!", "Recipe Successfully Added. Beerus would be jealous!")
        
        
        
        save_button = tk. Button(filewin, text= "Save", command= submit)
        
        title.pack()
        recipe_listbox.pack()
        save_button.pack()
        return
    
    
    # Add Favorite Recipe Button
    def add_fave():
        filewin = tk.Toplevel(root)
        filewin.title("Add Favorite")
        filewin.geometry("250x250")
        title = tk.Label(filewin, text='Favorites List')
        recipe_listbox = tk.Listbox(filewin)
        
        recipes = {}
        favorites = {}

        
        recipe_file = f"user_files/{current_user}-favorites.txt"
        
        
        recipe_arr= []
        recipe_names = []

            
        with open(recipe_file, "r") as file_input: 
            for line in file_input:
                
                if line.split("\n")[0]:
                    this_recipe = ast.literal_eval(line.split("\n")[0])
                    recipes[this_recipe['name']] = this_recipe
                    recipe_arr.append(this_recipe['ingredients'])
                    recipe_names.append(this_recipe['name'])
        
        
        print(recipe_names)
        # print(recipe_arr)
        
        
                        
        # clear the recipe listbox
        recipe_listbox.delete(0, tk.END)
        # add the recipes to the recipe listbox
        for recipe_name in recipes.keys():
            recipe_listbox.insert(tk.END, recipe_name)
        
        def submit():
            
            global current_calories 
            global default_calories 
            global current_carbs 
            global default_carbs 
            global current_fat 
            global default_fat 
            global current_protein 
            global default_protein 
            global current_food_log 
            
            for i in range (len(recipe_arr)):
                if recipe_names[i] == recipe_listbox.get(tk.ACTIVE):
                    ingredient_arr =recipe_arr[i]['ingredients']
                    for recipe in ingredient_arr:
                        
                        name= recipe['name']
                        cal=int(recipe['calorie'])
                        carb=int(recipe['carbohydrates'])
                        fat=int(recipe['fats'])
                        protein =int(recipe['proteins'])
                        food_item = [name,cal,carb,fat,protein]
                        
                        current_food_log.append([food_item])
                        print(current_food_log)
                        
                        
                        
                        
                        current_calories = current_calories + cal
                        current_carbs = current_carbs + carb
                        current_fat = current_fat + fat
                        current_protein = current_protein + protein
        
            
            
            
           
            
            cal_label.config(text = "Calories: "+ str(current_calories)+ ' / '+ str(default_calories)+ ' kcal')        
            carb_label.config(text = "Carbohydrates: "+ str(current_carbs)+ ' / '+ str(default_carbs)+ ' grams')
            fat_label.config(text = "Fat: "+ str(current_fat)+ ' / '+ str(default_fat)+ ' grams')
            protein_label.config(text ="Protein: "+ str(current_protein)+ ' / '+ str(default_protein)+ ' grams')
            
            filewin.destroy()
            messagebox.showinfo("Final Flash!", "Favorite Recipe Successfully Added. Even Jiren can't compare!")
            
        
        
        
        save_button = tk. Button(filewin, text= "Save", command= submit)
        
        title.pack()
        recipe_listbox.pack()
        save_button.pack()
        return
    
    # Add Workout Button
    def add_workout():
        
        
        filewin = tk.Toplevel(root)
        filewin.title("Add Workout")
        filewin.geometry("250x250")
        name_var=tk.StringVar()
        type_var= tk.StringVar()
        sets_var = tk.StringVar()
        reps_var = tk.StringVar()
        volume_var = tk.StringVar()
        
        def submit():
            
            global current_gym_log 
    
            name=name_var.get()
            type=type_var.get()
            sets=int(sets_var.get())
            reps=int(reps_var.get())
            volume =int(volume_var.get())
            workout_item = [name,type,sets,reps,volume]
            
            current_gym_log.append([workout_item])
            
            print(current_gym_log)
            name_var.set("")
            type_var.set(0)
            reps_var.set("")
            sets_var.set(0)
            volume_var.set(0)

            
            filewin.destroy()
            messagebox.showinfo("Hyperbolic Time Chamber", "You've gone even FURTHER beyond! Workout recorded.")
            
        
        entry_1 = tk.Entry(filewin, textvariable= name_var)
        entry_2 = ttk.Combobox(filewin, textvariable= type_var, values=[ "Chest", "Back", "Triceps", "Biceps","Quads", "Hamstrings", "Glutes", "Shoulders"])
        entry_3 = tk.Entry(filewin, textvariable= sets_var)
        entry_4 = tk.Entry(filewin, textvariable= reps_var)
        entry_5 = tk.Entry(filewin, textvariable= volume_var)
        
        label_1 = tk.Label(filewin, text = "Exercise Name")
        label_2 = tk.Label(filewin, text = "Body Part")
        label_3 = tk.Label(filewin, text = "Sets")
        label_4 = tk.Label(filewin, text = "Reps")
        label_5 = tk.Label(filewin, text = "Total Volume (lb)")
        
        save_button = tk. Button(filewin, text= "Save", command= submit)
        
        label_1.pack()
        entry_1.pack()
        label_2.pack()
        entry_2.pack()
        label_3.pack()
        entry_3.pack()
        label_4.pack()
        entry_4.pack()
        label_5.pack()
        entry_5.pack()
        save_button.pack()
        return


    
    
    
    #------------------------------------------- Cascade Commands ----------------------------------------------------#
    
    # Add Change Calories and Macros
    def change_userdata():
        filewin = tk.Toplevel(root)
        filewin.title("Change Calories and Macronutrients")
        filewin.geometry("250x250")
        cal_var= tk.StringVar()
        carb_var = tk.StringVar()
        fat_var = tk.StringVar()
        protein_var = tk.StringVar()
        
        def submit():
            
            # Read user file
            user_data = []
            with open(info_file, "r") as file_input: 
                for line in file_input:
                    user_data_line = line.split("\n")[0]                   
                    user_data.append(int(re.findall(r'\d+', user_data_line)[0]))
            
            print(user_data)
                
            user_cal = user_data[0]
            user_carb = user_data[1]
            user_fat = user_data[2]
            user_protein = user_data[3]
                
                
            default_calories = user_cal
            default_carbs = user_carb
            default_fat = user_fat
            default_protein = user_protein
            
            
            # Get variables
            cal=int(cal_var.get())
            carb=int(carb_var.get())
            fat=int(fat_var.get())
            protein =int(protein_var.get())
            
            
            
            #Set default to variables
            
            default_calories = cal
            default_carbs = carb
            default_fat = fat
            default_protein = protein
            
            
            # Update Main Labels
            cal_label.config(text = "Calories: "+ str(current_calories)+ ' / '+ str(default_calories)+ ' kcal')        
            carb_label.config(text = "Carbohydrates: "+ str(current_carbs)+ ' / '+ str(default_carbs)+ ' grams')
            fat_label.config(text = "Fat: "+ str(current_fat)+ ' / '+ str(default_fat)+ ' grams')
            protein_label.config(text ="Protein: "+ str(current_protein)+ ' / '+ str(default_protein)+ ' grams')
            
            
            # empty file
            open(info_file, "w").close()
            
            # Rewrite file
            with open(info_file, 'a') as file:
                file.write(f"Calorie Goal: {default_calories}\n")
                file.write(f"Carbohydrate Goal: {default_carbs}\n")
                file.write(f"Fats Goal: {default_fat}\n")
                file.write(f"Protein Goal: {default_protein}\n")
            
            filewin.destroy()
            
        
       
        entry_2 = tk.Entry(filewin, textvariable= cal_var)
        entry_3 = tk.Entry(filewin, textvariable= carb_var)
        entry_4 = tk.Entry(filewin, textvariable= fat_var)
        entry_5 = tk.Entry(filewin, textvariable= protein_var)
        
        label_2 = tk.Label(filewin, text = "Calories")
        label_3 = tk.Label(filewin, text = "Carbohydrates (grams)")
        label_4 = tk.Label(filewin, text = "Total Fat (grams)")
        label_5 = tk.Label(filewin, text = "Protein (grams)")
        
        save_button = tk. Button(filewin, text= "Save", command= submit)
        

        label_2.pack()
        entry_2.pack()
        label_3.pack()
        entry_3.pack()
        label_4.pack()
        entry_4.pack()
        label_5.pack()
        entry_5.pack()
        save_button.pack()
        return
    
    # New Log Command
    def new_entry_log():  
        
        global current_calories 
        global default_calories 
        global current_carbs 
        global default_carbs 
        global current_fat 
        global default_fat 
        global current_protein 
        global default_protein         
        
        global current_food_log
        global current_gym_log 
        global user_data
        
        # Reset logs
        current_food_log = []
        current_gym_log = []
        
        
        current_calories = 0
        current_carbs = 0
        current_fat = 0
        current_protein = 0
        
        # Update Main Labels
        cal_label.config(text = "Calories: "+ str(current_calories)+ ' / '+ str(default_calories)+ ' kcal')        
        carb_label.config(text = "Carbohydrates: "+ str(current_carbs)+ ' / '+ str(default_carbs)+ ' grams')
        fat_label.config(text = "Fat: "+ str(current_fat)+ ' / '+ str(default_fat)+ ' grams')
        protein_label.config(text ="Protein: "+ str(current_protein)+ ' / '+ str(default_protein)+ ' grams')
        
        
        messagebox.showinfo("A New Day Dawns", "New Log Started. Don't Fall off Snakeway!")
        return
    
    
    # Submit an Entry Log Command
    def save_entry_log():
        
        log_file = f"user_files/{current_user}-log.txt"
    
        
            
        
        global current_food_log
        global current_gym_log 
        global user_data
        date = calendar.get_date()
        
        entry = log_entry.Log_Entry(user_data,date,current_food_log,current_gym_log)
        with open(log_file, 'a') as file:
            file.write("\n"+entry.to_String())
        
        messagebox.showinfo("You are the hope of the Universe!", "Entry Log Saved! No Mafuba Required...")
        return
    
    
    def view_all_logs():
        
        filewin = tk.Toplevel(root)
        filewin.title("All Logs")
        
        
        log_file = f"user_files/{current_user}-log.txt"
        with open(log_file) as f:
            lines = [line.rstrip('\n') for line in f]
            big_entry_array = []
            for line in lines:
                if(line):
                    big_entry_array.append(line.split(':'))
            for entry_array in big_entry_array:
                    date = entry_array[0]
                    label_1 = tk.Label(filewin, text = "Date: "+str(date))
                    label_1.pack()
                    
                    label_2 = tk.Label(filewin, text = "Food")
                    label_2.pack()
                    
                    foods = ast.literal_eval(entry_array[2])               
                    food_label_string = str()
                    for food in foods:
                        name = food[0][0]
                        cal = food[0][1]
                        carb = food[0][2]
                        fat = food[0][3]
                        protein = food[0][4]
                        food_label_string = food_label_string +  f"{name} ({cal} kcal, {carb} g carbs, {fat} g fats, {protein} g proteins)" +"\n"
                        
                    food_label = tk.Label(filewin, text = food_label_string)
                    food_label.pack()
                    
                    label_3 = tk.Label(filewin, text = "Workout")
                    label_3.pack()
                    workouts = ast.literal_eval(entry_array[3])
                    gym_label_string = str()
                    for workout in workouts:
                        name = workout[0][0]
                        body = workout[0][1]
                        sets = workout[0][2]
                        reps = workout[0][3]
                        volume = workout[0][4]
                        gym_label_string= gym_label_string +  f"{name} (Body Part: {body}, {sets} sets, {reps} reps, {volume} Total Volume (lb))"+ "\n"
                   
                    gym_label = tk.Label(filewin,text=gym_label_string)
                    gym_label.pack()
                    
                    
                    
                    
    def go_to_recipe_manager():
        root.destroy()
        recipe_manager.create_recipe_manager(current_user)
        
    
    def log_out():
        root.destroy()
        login.create_login_window()


        
    # Build Root 
    root = tk.Tk()
    root.title('Get In-Saiyan-ly Fit!')
    root.geometry('800x600')
    
    img = ImageTk.PhotoImage(Image.open("images/home.jpg"))  
    l=tk.Label(image=img)
    l.place(x=0,y=0)

    # Create Menu Bar
    menu_bar = tk.Menu(root)
    
    ## File Menu
    filemenu = tk.Menu(menu_bar, tearoff=0)
    filemenu.add_command(label="New Log", command=new_entry_log)
    filemenu.add_command(label="Save Log", command=save_entry_log)
    filemenu.add_command(label="View Logs", command=view_all_logs)
    filemenu.add_command(label="Log Out...", command=log_out)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=filemenu)
    
    ## Nutrition Menu
    foodmenu = tk.Menu(menu_bar, tearoff=0)
    foodmenu.add_command(label="Change Calorie and Macronutrient Goal...", command= change_userdata)
    foodmenu.add_separator()
    foodmenu.add_command(label="Go to Recipe Manager...", command = go_to_recipe_manager)
    menu_bar.add_cascade(label="Nutrition", menu=foodmenu)
    
    # ## Workout Menu
    # gymmenu = tk.Menu(menu_bar, tearoff=0)
    # menu_bar.add_cascade(label="Workouts", menu=gymmenu)
    
    
    
    
    ## Final Window Set Up
    date_label = tk.Label(root, text = "Date:")
    calendar = tkcalendar.DateEntry(root, selectmode = 'day')
    main_label = tk.Label(root, text = "Calories and Macronutrients:")
    cal_label = tk.Label(root, text = "Calories: "+ str(current_calories)+ ' / '+ str(default_calories)+ ' kcal')
    carb_label = tk.Label(root, text = "Carbohydrates: "+ str(current_carbs)+ ' / '+ str(default_carbs)+ ' grams')
    fat_label = tk.Label(root, text = "Fat: "+ str(current_fat)+ ' / '+ str(default_fat)+ ' grams')
    protein_label = tk.Label(root, text = "Protein: "+ str(current_protein)+ ' / '+ str(default_protein)+ ' grams')
    
    b1 = tk.Button(root, text = "Add Food",command=add_food )
    b2 = tk.Button(root, text = "Add Recipe", command=add_recipe)
    b3 = tk.Button(root, text = "Add Favorite Recipe", command=add_fave )
    b4 = tk.Button(root, text = "Add Workout", command=add_workout)
    
    date_label.pack(side='top')
    calendar.pack(side='top')
    main_label.pack(side = "top", pady=25)
    cal_label.pack(side='top')
    carb_label.pack(side='top')
    fat_label.pack(side='top')
    protein_label.pack(side = 'top')
    
    b1.place(x = 250, y = 350)
    b2.place(x = 350, y = 350)
    b3.place(x = 325, y = 400)
    b4.place(x = 450, y = 350)
    
    
    
    root.config(menu=menu_bar)
    root.mainloop()


if __name__ == "__main__":
    create_homepage('test')