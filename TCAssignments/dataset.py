import csv

# List of states in India with some dummy data
states_data = [
    {"State Name": "Andhra Pradesh", "Popular Food": "Pesarattu", "Population": "49577103", "Land Area": "160205", "Capital City": "Amaravati", "Gender Ratio": "993"},
    {"State Name": "Arunachal Pradesh", "Popular Food": "Thukpa", "Population": "1383727", "Land Area": "83743", "Capital City": "Itanagar", "Gender Ratio": "938"},
    {"State Name": "Assam", "Popular Food": "Masor Tenga", "Population": "31205576", "Land Area": "78438", "Capital City": "Dispur", "Gender Ratio": "958"},
    {"State Name": "Bihar", "Popular Food": "Litti Chokha", "Population": "104099452", "Land Area": "94163", "Capital City": "Patna", "Gender Ratio": "918"},
    {"State Name": "Chhattisgarh", "Popular Food": "Chana Samosa", "Population": "25545198", "Land Area": "135192", "Capital City": "Raipur", "Gender Ratio": "991"},
    {"State Name": "Goa", "Popular Food": "Fish Curry", "Population": "1458545", "Land Area": "3702", "Capital City": "Panaji", "Gender Ratio": "973"},
    {"State Name": "Gujarat", "Popular Food": "Dhokla", "Population": "60439692", "Land Area": "196024", "Capital City": "Gandhinagar", "Gender Ratio": "919"},
    {"State Name": "Haryana", "Popular Food": "Bajra Khichdi", "Population": "25351462", "Land Area": "44212", "Capital City": "Chandigarh", "Gender Ratio": "879"},
    {"State Name": "Himachal Pradesh", "Popular Food": "Dham", "Population": "6864602", "Land Area": "55673", "Capital City": "Shimla", "Gender Ratio": "972"},
    {"State Name": "Jharkhand", "Popular Food": "Thekua", "Population": "32988134", "Land Area": "79716", "Capital City": "Ranchi", "Gender Ratio": "948"},
    {"State Name": "Karnataka", "Popular Food": "Bisi Bele Bath", "Population": "61095297", "Land Area": "191791", "Capital City": "Bengaluru", "Gender Ratio": "973"},
    {"State Name": "Kerala", "Popular Food": "Appam", "Population": "33406061", "Land Area": "38863", "Capital City": "Thiruvananthapuram", "Gender Ratio": "1084"},
    {"State Name": "Madhya Pradesh", "Popular Food": "Bhutte Ka Kees", "Population": "72626809", "Land Area": "308252", "Capital City": "Bhopal", "Gender Ratio": "931"},
    {"State Name": "Maharashtra", "Popular Food": "Pav Bhaji", "Population": "112374333", "Land Area": "307713", "Capital City": "Mumbai", "Gender Ratio": "929"},
    {"State Name": "Manipur", "Popular Food": "Eromba", "Population": "2855794", "Land Area": "22327", "Capital City": "Imphal", "Gender Ratio": "985"},
    {"State Name": "Meghalaya", "Popular Food": "Jadoh", "Population": "2966889", "Land Area": "22429", "Capital City": "Shillong", "Gender Ratio": "989"},
    {"State Name": "Mizoram", "Popular Food": "Bai", "Population": "1097206", "Land Area": "21081", "Capital City": "Aizawl", "Gender Ratio": "976"},
    {"State Name": "Nagaland", "Popular Food": "Axone", "Population": "1978502", "Land Area": "16579", "Capital City": "Kohima", "Gender Ratio": "931"},
    {"State Name": "Odisha", "Popular Food": "Pakhala Bhata", "Population": "41974218", "Land Area": "155707", "Capital City": "Bhubaneswar", "Gender Ratio": "979"},
    {"State Name": "Punjab", "Popular Food": "Makki di Roti", "Population": "27743338", "Land Area": "50362", "Capital City": "Chandigarh", "Gender Ratio": "895"},
    {"State Name": "Rajasthan", "Popular Food": "Dal Baati Churma", "Population": "68548437", "Land Area": "342239", "Capital City": "Jaipur", "Gender Ratio": "928"},
    {"State Name": "Sikkim", "Popular Food": "Phagshapa", "Population": "610577", "Land Area": "7096", "Capital City": "Gangtok", "Gender Ratio": "890"},
    {"State Name": "Tamil Nadu", "Popular Food": "Idli", "Population": "72147030", "Land Area": "130058", "Capital City": "Chennai", "Gender Ratio": "996"},
    {"State Name": "Telangana", "Popular Food": "Hyderabadi Biryani", "Population": "35193978", "Land Area": "112077", "Capital City": "Hyderabad", "Gender Ratio": "988"},
    {"State Name": "Tripura", "Popular Food": "Mui Borok", "Population": "3673917", "Land Area": "10486", "Capital City": "Agartala", "Gender Ratio": "960"},
    {"State Name": "Uttar Pradesh", "Popular Food": "Tunday Kababi", "Population": "199812341", "Land Area": "243286", "Capital City": "Lucknow", "Gender Ratio": "912"},
    {"State Name": "Uttarakhand", "Popular Food": "Kafuli", "Population": "10086292", "Land Area": "53483", "Capital City": "Dehradun", "Gender Ratio": "963"},
    {"State Name": "West Bengal", "Popular Food": "Rosogolla", "Population": "91276115", "Land Area": "88752", "Capital City": "Kolkata", "Gender Ratio": "950"}
]
csv_file_path = 'indian_states_dataset.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["State Name", "Popular Food", "Population", "Land Area", "Capital City", "Gender Ratio"])
    writer.writeheader()
    for state in states_data:
        writer.writerow(state)

print(f"Dataset saved to {csv_file_path}")
