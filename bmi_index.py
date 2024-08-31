class Bmi:
    def __init__(self):
        self.height = 0
        self.weight = 0
        self.bmi = 0
        self.name = ''
        self.category = ''
        self.menu()
    def menu(self):
        user_input = input("""
        HI HOW CAN I HELP YOU
        1. press to calculate bmi index
        2. press anything to exits
        """)
        if user_input == '1':
            self.calculate_bmi()
        else:
              exit()

    def classify_bmi(self):
        if self.bmi < 18.5:
            return("under weight")
        elif self.bmi >= 18.5 and self.bmi <= 24.9:
            return("category: normal weight")
        elif self.bmi >= 25 and self.bmi <= 29.9:
            return("category: over weight")
        else:
            return("category: obese")

    def save_to_file(self):
    # Save BMI record to a file.
        with open("bmi_records.txt", "a") as file:
            file.write(f"{self.name},{self.weight},{self.height},{self.bmi},{self.category}\n")

    def calculate_bmi(self):
      try:
        user_name = input("enter your name")
        self.name = user_name
        user_weight = int(input("enter the weight in kg"))
        self.weight = user_weight
        user_height = int(input("enter the height in m"))
        self.height = user_height
        if self.weight <= 0 or self.height <= 0:
           raise ValueError("Weight and height must be positive numbers.")

        bmi = (self.weight) /(( self.height)**2)
        self.category = self.classify_bmi()
        self.bmi = bmi
        self.print()
        self.save()

      except ValueError as e:
        print("Invalid input. Please enter valid numbers for weight and height.") 
        self.calculate_bmi()

    def print(self):
      print(f"Name: {self.name}")
      print('weight = {}'.format(self.weight))
      print('height = {}'.format(self.height))
      print('{}*{} = {}'.format(self.weight,self.height,self.bmi))
      print('your bmi = {}'.format(self.bmi))
      print('your category is ={}'.format(self.category))

    def save(self):
        save = input("Do you want to save this record? (yes/no): ")  
        if save.lower() == "yes":
            self.save_to_file()  
            print("Record saved successfully.")
        elif save.lower() == "no":
            print("Record not saved.")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
bmi1 = Bmi()

