"""

Author:  Tyler Ingram
Date written: 12/01/24
Assignment:   Module 8 FINAL
Short Desc:  1) GUI App that will allow users to convert cooking units of measurement to another. 
             2) It will also allow users to enter a receipe and convert their serving sizes based on the input from the user.

"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class FoodApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Food Conversion App")
        self.geometry("1024x1024")

        # Background images
        self.bg_image = Image.open(r"Raes Cooking Conversions\images\Food Background.png")
        self.bg_image2 = Image.open(r"Raes Cooking Conversions\images\Food Background2.png")
        self.bg_image3 = Image.open(r"Raes Cooking Conversions\images\Food Background3.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_photo2 = ImageTk.PhotoImage(self.bg_image2)
        self.bg_photo3 = ImageTk.PhotoImage(self.bg_image3)

        # Frames
        self.home_frame = tk.Frame(self)
        self.unit_conversion_frame = tk.Frame(self)
        self.serving_size_frame = tk.Frame(self)

        self.setup_home_screen()
        self.setup_unit_conversion_screen()
        self.setup_serving_size_screen()

        self.show_frame(self.home_frame)

    def setup_home_screen(self):
        # Background
        bg_label = tk.Label(self.home_frame, image=self.bg_photo3)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Welcome Label
        welcome_label = tk.Label(
            self.home_frame,
            text="Welcome to Rae's Cooking Conversions! Select which feature you would like to use or exit to leave.",
            font=("Arial", 15),
            wraplength=280,
            justify="center",
        )
        welcome_label.place(relx=0.518, rely=0.35, anchor="center")

        # Buttons
        button_container = tk.Frame(self.home_frame)
        button_container.place(relx=0.5, rely=0.5, anchor="center")

        unit_conversion_btn = tk.Button(button_container, text="Unit Conversions", command=lambda: self.show_frame(self.unit_conversion_frame))
        serving_size_btn = tk.Button(button_container, text="Serving Size Conversion", command=lambda: self.show_frame(self.serving_size_frame))
        exit_btn = tk.Button(button_container, text="Exit", command=self.quit)

        unit_conversion_btn.pack(pady=(0,10))
        serving_size_btn.pack(pady=(0,10))
        exit_btn.pack(pady=(0,10))

    def setup_unit_conversion_screen(self):
        # Background
        bg_label = tk.Label(self.unit_conversion_frame, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Centering
        conversion_container = tk.Frame(self.unit_conversion_frame)
        conversion_container.place(relx=0.5, rely=0.5, anchor="center")

        # Input and Dropdown
        input_label = tk.Label(conversion_container, text="Enter value:")
        input_label.pack(pady=(10, 5))  # Spacing above and below
        self.input_value = tk.Entry(conversion_container)
        self.input_value.pack(pady=(0, 10))

        unit_label = tk.Label(conversion_container, text="Select unit:")
        unit_label.pack(pady=(10, 5))
        self.unit_dropdown = ttk.Combobox(conversion_container, values=[
            "Teaspoon (tsp)", "Tablespoon (tbsp)", "Fluid Ounce (fl oz)",
            "Cup (c)", "Pint (pt)", "Quart (qt)", "Gallon (gal)"
        ])
        self.unit_dropdown.pack(pady=(0, 10))

        # Buttons
        convert_btn = tk.Button(conversion_container, text="Convert", command=self.convert_units)
        convert_btn.pack(pady=(10, 10))

        self.unit_result_label = tk.Label(conversion_container, text="")
        self.unit_result_label.pack(pady=(10, 20))

        return_home_btn = tk.Button(conversion_container, text="Return Home", command=lambda: self.show_frame(self.home_frame))
        return_home_btn.pack(pady=(20, 30))


    def convert_units(self):
        value = self.input_value.get()
        unit = self.unit_dropdown.get()
        try:
            value = float(value)
            conversions = {
                "Teaspoon (tsp)": {
                    "Tablespoon (tbsp)": value / 3,
                    "Fluid Ounce (fl oz)": value / 6,
                    "Cup (c)": value / 48,
                    "Pint (pt)": value / 96,
                    "Quart (qt)": value / 192,
                    "Gallon (gal)": value / 768,
                },
                "Tablespoon (tbsp)": {
                    "Teaspoon (tsp)": value * 3,
                    "Fluid Ounce (fl oz)": value / 2,
                    "Cup (c)": value / 16,
                    "Pint (pt)": value / 32,
                    "Quart (qt)": value / 64,
                    "Gallon (gal)": value / 256,
                },
                "Fluid Ounce (fl oz)": {
                    "Teaspoon (tsp)": value * 6,
                    "Tablespoon (tbsp)": value * 2,
                    "Cup (c)": value / 8,
                    "Pint (pt)": value / 16,
                    "Quart (qt)": value / 32,
                    "Gallon (gal)": value / 128,
                },
                "Cup (c)": {
                    "Teaspoon (tsp)": value * 48,
                    "Tablespoon (tbsp)": value * 16,
                    "Fluid Ounce (fl oz)": value * 8,
                    "Pint (pt)": value / 2,
                    "Quart (qt)": value / 4,
                    "Gallon (gal)": value / 16,
                },
                "Pint (pt)": {
                    "Teaspoon (tsp)": value * 96,
                    "Tablespoon (tbsp)": value * 32,
                    "Fluid Ounce (fl oz)": value * 16,
                    "Cup (c)": value * 2,
                    "Quart (qt)": value / 2,
                    "Gallon (gal)": value / 8,
                },
                "Quart (qt)": {
                    "Teaspoon (tsp)": value * 192,
                    "Tablespoon (tbsp)": value * 64,
                    "Fluid Ounce (fl oz)": value * 32,
                    "Cup (c)": value * 4,
                    "Pint (pt)": value * 2,
                    "Gallon (gal)": value / 4,
                },
                "Gallon (gal)": {
                    "Teaspoon (tsp)": value * 768,
                    "Tablespoon (tbsp)": value * 256,
                    "Fluid Ounce (fl oz)": value * 128,
                    "Cup (c)": value * 16,
                    "Pint (pt)": value * 8,
                    "Quart (qt)": value * 4,
                },
            }

            if unit in conversions:
                result = f"Conversions for {value} {unit}:\n"
                for target_unit, converted_value in conversions[unit].items():
                    result += f"{converted_value:.2f} {target_unit}\n"
                self.unit_result_label.config(text=result)
            else:
                self.unit_result_label.config(text="Please select a valid unit.")
        except ValueError:
            self.unit_result_label.config(text="Invalid input. Please enter a numeric value.")

    def setup_serving_size_screen(self):
        # Background
        bg_label = tk.Label(self.serving_size_frame, image=self.bg_photo2)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Ingredents
        instructions_label = tk.Label(self.serving_size_frame, text="Enter ingredients, measurements, and select units. Then provide the recipe's number of servings and your desired number of servings!")
        instructions_label.pack(pady=10)
        self.ingredients = []
        units = ["Teaspoon (tsp)", "Tablespoon (tbsp)", "Fluid Ounce (fl oz)", "Cup (c)", "Pint (pt)", "Quart (qt)", "Gallon (gal)"]

        # Header
        header_frame = tk.Frame(self.serving_size_frame)
        header_frame.pack(pady=5)
        
        ingredient_header = tk.Label(header_frame, text="Ingredient Name", width=20, anchor="w")
        ingredient_header.pack(side=tk.LEFT, padx=5)
        
        measurement_header = tk.Label(header_frame, text="Measurement", width=15, anchor="w")
        measurement_header.pack(side=tk.LEFT, padx=5)
        
        unit_header = tk.Label(header_frame, text="Unit", width=15, anchor="w")
        unit_header.pack(side=tk.LEFT, padx=5)

        for i in range(10):
            row_frame = tk.Frame(self.serving_size_frame)
            row_frame.pack(pady=5)
            
            # Ingredient Label
            ingredient_label = tk.Label(row_frame, text=f"Ingredient {i+1}:")
            ingredient_label.pack(side=tk.LEFT, padx=5)
            
            # Ingredient Entry
            ingredient_entry = tk.Entry(row_frame, width=20)
            ingredient_entry.pack(side=tk.LEFT, padx=5)

            # Measurement Entry
            unit_entry = tk.Entry(row_frame, width=10)
            unit_entry.pack(side=tk.LEFT, padx=5)

            # Unit Dropdown - used Combobox
            unit_dropdown = ttk.Combobox(row_frame, values=units, width=15)
            unit_dropdown.pack(side=tk.LEFT, padx=5)

            # Append to save data
            self.ingredients.append((ingredient_entry, unit_entry, unit_dropdown))

        # Servings input
        current_servings_label = tk.Label(self.serving_size_frame, text="Current number of servings:")
        current_servings_label.pack(pady=5)
        self.current_servings = tk.Entry(self.serving_size_frame)
        self.current_servings.pack(pady=5)

        desired_servings_label = tk.Label(self.serving_size_frame, text="Desired number of servings:")
        desired_servings_label.pack(pady=5)
        self.desired_servings = tk.Entry(self.serving_size_frame)
        self.desired_servings.pack(pady=5)

        # Convert button
        convert_btn = tk.Button(self.serving_size_frame, text="Convert", command=self.convert_serving_size)
        convert_btn.pack(pady=20)

        # Output label
        self.serving_result_label = tk.Label(self.serving_size_frame, text="")
        self.serving_result_label.pack(pady=10)

        # Return home button
        return_home_btn = tk.Button(self.serving_size_frame, text="Return Home", command=lambda: self.show_frame(self.home_frame))
        return_home_btn.pack(pady=20)

    def convert_serving_size(self):
        try:
            current = int(self.current_servings.get())
            desired = int(self.desired_servings.get())
            factor = desired / current

            result = f"Updated Ingredients for {desired} servings:\n"
            for ingredient_entry, unit_entry, unit_dropdown in self.ingredients:
                ingredient = ingredient_entry.get()
                amount = unit_entry.get()
                unit = unit_dropdown.get()

                if amount:
                    scaled_amount = float(amount) * factor
                    result += f"{ingredient}: {scaled_amount:.2f} {unit}\n"

            self.serving_result_label.config(text=result)
        except ValueError:
            self.serving_result_label.config(text="Please enter valid numeric values for servings.")

    def show_frame(self, frame):

        # Forgets packs so not all 3 pics load at once.
        self.home_frame.pack_forget()
        self.unit_conversion_frame.pack_forget()
        self.serving_size_frame.pack_forget()
        frame.pack(fill="both", expand=True)
        frame.tkraise()

if __name__ == "__main__":
    app = FoodApp()
    app.mainloop()
