import pandas as pd

################################   Data Exploration   ################################

# Load the dataset
file_path = " add your filepath"
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
"""
Add your code here
"""

# Display basic information about the dataset

"""
Add your code here
"""

# Display statistical overview of numerical columns

"""
Add your code here
"""

# Display the first few rows of the dataframe

"""
Add your code here
"""

# Calculating the number of missing values in each column

"""
Add your code here
"""

# Displaying the number of missing values per column

"""
Add your code here
"""

##############################################################################################

################################   Data Cleaning   ################################

### Handle missing values and data inconsistencies.

# Replace missing values in 'Courier Status', 'currency', 'Amount', 'ship-city', 'ship-state', 'ship-postal-code', and 'ship-country' with appropriate values or methods
"""

Add your code here

# Forinstance: Fill missing courier statuses with 'Unknown'
# Forinstance; Forward fill missing currencies --> df['currency'].fillna(method='ffill', inplace=True) 
# Forinstance; Fill missing amounts with the mean value
# Forinstance; Fill missing shipping details with 'Missing'
"""


# Drop columns with a high percentage of missing values if they are not crucial
df.drop(columns=['fulfilled-by', 'Unnamed: 22', 'promotion-ids'], inplace=True)

# Check for and resolve any data inconsistencies, such as incorrect data types or unusual values
# Example: Ensure 'Qty' and 'Amount' do not have negative values
df['Qty'] = df['Qty'].clip(lower=0)
df['Amount'] = df['Amount'].clip(lower=0)

# Recheck the dataset after cleaning
#print(df.head())
#print(df.info())

### Standardize text data for uniformity (e.g., Category, Size, Style).

# Convert all text to lowercase for uniformity
df['Category'] = df['Category'].str.lower()
# Add one for 'Size' as well
df['Style'] = df['Style'].str.lower()

# Remove leading and trailing spaces
df['Category'] = df['Category'].str.strip()
# Add one for 'Size' as well
df['Style'] = df['Style'].str.strip()

# Replace any inconsistencies or typos, if known
# Example: Replacing 'smal' with 'small' in the 'Size' column
"""
Add your code here
"""
# add additonal typo suggestion such as 'bigg' for 'big' etc.

"""
Add your code here
"""

# Recheck the dataset after standardizing

"""
Add your code here
"""
# if everything in the output is in lowercase then it is succesfully standardized dataset


### Convert 'Date' to a suitable datetime format.

# Convert 'Date' from string to datetime format
# Assuming the date format in the CSV is 'MM-DD-YY'
df['Date'] = pd.to_datetime(df['Date'], "add your code here", errors='coerce')

# Check the conversion
"""
Add your code here
"""

##############################################################################################