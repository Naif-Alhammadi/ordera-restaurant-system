import os
import csv

def admin_file(admin):
    os.makedirs("uploads", exist_ok=True)
    with open("uploads/admins", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Admin", "Phone", "Hash"])
        writer.writeheader()
        writer.writerow({"ID": admin._id,"Admin": admin._name, "Phone": admin._phone_number,"Hash": admin._password})


def employees_application(sender, message, application_status = "pending"):
    os.makedirs("uploads", exist_ok=True)
    with open("uploads/employees_application", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "experience", "message", "status"])
        writer.writeheader()
        writer.writerow({"name": sender.name, "age": sender.age, "experience": sender.experience, "message": message, "status": application_status})