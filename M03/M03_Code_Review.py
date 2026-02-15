# Jennifer Bowers
# M03 Discussion - Code Review
# 2/12/2026

import os
from datetime import datetime

os.system("cls")

class User():
    def __init__(self, first_name, last_name, department, badge, email, phone):
        
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.badge = badge
        self.email = email
        self.phone = phone

    def describe_user(self):
        return f"Badge: {self.badge} \nLast Name: {self.last_name} \nFirst Name: {self.first_name} \nDepartment: {self.department} \nUser Email: {self.email} \nPhone: {self.phone} \nTimestamp: {time}\n"
    
    def greet_user(self):
        return f"Welcome back, {self.first_name} {self.last_name}!\nYou have successfully clocked into the '{self.department}' department at {formatted_time}.\n"

# List of user profiles
user_info1 = User("Jan", "Crocket", "Shipping", 1032, "jcrocket@work.com", "123-555-1234")
user_info2 = User("Derek", "Amberly", "Accounting", 5040, "damberly@work.com", "123-555-5678")
user_info3 = User("Alisha", "Deckert", "IT", 3024, "adeckert@work.com", "123-555-9123")
user_info4 = User("Brett", "Bailey", "Shipping", 4015, "bbailey@work.com", "123-555-4567")
user_info5 = User("Zoey", "Fencier", "Customer Service", 2056, "zfencier@work.com", "123-555-8912")

all_users = (user_info1, user_info2, user_info3, user_info4, user_info5)

for user in all_users:
    time = datetime.now()
    formatted_time = time.strftime("%I:%M:%S %p on %m-%d-%Y")
    print(f"--- Time Punch Station --- \n{user.greet_user()}\n{user.describe_user()}")