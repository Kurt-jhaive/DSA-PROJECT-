import pandas as pd

# ------------------------------------- Cat -------------------------------------
# Open the CSV file that will act as the database for the cats
cat_df = pd.read_csv('cat_description.csv')

# Create a list of pet_id, pet_name, breed, age, color, gender, size, description, image_path, availability, adopt_date
pet_id = cat_df['pet_id'].tolist()
pet_name = cat_df['pet_name'].tolist()
breed = cat_df['breed'].tolist()
age = cat_df['age'].tolist()
color = cat_df['color'].tolist()
gender = cat_df['color'].tolist()
size = cat_df['size'].tolist()
description = cat_df['description'].tolist()
image_path = cat_df['image_path'].tolist()
availability = cat_df['availability'].tolist()
adopt_date = cat_df['adopt_date'].tolist()