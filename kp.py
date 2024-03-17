import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_percentage():
    # Get the maximum number of cases allocated and the number of closed cases
    max_num = tbxMaxNum.get()
    num_achieved = tbxNumAch.get()

    if max_num == "":
        # Display a message box if the maximum number is not entered
        messagebox.showinfo("Missing Information", "Number of cases must be entered")
    elif num_achieved == "":
        # Display a message box if the number of closed cases is not entered
        messagebox.showinfo("Missing Information", "Number of closed cases must be entered")
    else:
        # Calculate the completion percentage
        percentage = float(num_achieved) / float(max_num) * 100
        lblPercentage2.config(text=f"{percentage:.2f}%")

        # Save data to a text file
        with open("KPI-data.txt", "a") as file:
            name = tbxName.get()
            # Write the calculated data to the text file
            file.write(f"Name: {name}, Case Assigned: {max_num}, Case Closed: {num_achieved}, Percentage: {percentage:.2f}%\n")

def clear_form():
    # Clear the input fields and the percentage label
    tbxName.delete(0, tk.END)
    tbxMaxNum.delete(0, tk.END)
    tbxNumAch.delete(0, tk.END)
    lblPercentage2.config(text="")

def read_data():
    # Clear the input fields and the percentage label
    clear_form()

    try:
        # Read data from the text file
        with open("KPI-data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)

        if lines:
            # Get the most recent line of data
            latest_data = lines[-1].strip()

            # Extract the values from the line
            data_parts = latest_data.split(",")
            print(len(data_parts))

            if len(data_parts) == 4:
                name = data_parts[0].strip().split("Name:")[1].strip()
                assigned_cases = int(data_parts[1].strip().split("Case Assigned:")[1].strip())
                closed_cases = int(data_parts[2].strip().split("Case Closed:")[1].strip())
                percentage_str = data_parts[3].strip().split("Percentage:")[1].strip()

                # Convert the percentage value to float
                percentage = float(percentage_str.strip("%"))

                # Set the values in the input fields
                tbxName.insert(0, name)
                tbxMaxNum.insert(0, assigned_cases)
                tbxNumAch.insert(0, closed_cases)

                # Calculate the completion percentage
                lblPercentage2.config(text=f"{percentage:.2f}%")
            else:
                messagebox.showinfo("Invalid Data", "The data in the file is invalid.")
        else:
            messagebox.showinfo("No Data", "The data file is empty.")
    except FileNotFoundError:
        messagebox.showinfo("File Not Found", "The data file is not found.")
    except (ValueError, IndexError):
        messagebox.showinfo("Invalid Data", "The data in the file is invalid.")

frmPercentage = tk.Tk()
frmPercentage.geometry("800x500")
frmPercentage.title("KPI Tracker")
frmPercentage.configure(background="gray")

# Create labels for name, assigned cases, closed cases, and percentage
lblName = tk.Label(frmPercentage, text="Your Name:", width=20, height=2, bg="gray", fg="white")
lblName.place(x=175, y=60)

lblMaxNum = tk.Label(frmPercentage, text="Assigned Cases:", width=20, height=2, bg="gray", fg="white")
lblMaxNum.place(x=175, y=130)

lblNumAch = tk.Label(frmPercentage, text="Closed Cases:", width=20, height=2, bg="gray", fg="white")
lblNumAch.place(x=175, y=200)

lblPercentage = tk.Label(frmPercentage, text="Percentage:", width=20, height=2, bg="gray", fg="white")
lblPercentage.place(x=175, y=270)

# Create entry boxes for name, maximum number, and number achieved
tbxName = tk.Entry(frmPercentage, bg="white")
tbxName.place(x=475, y=60, width=150, height=35)

tbxMaxNum = tk.Entry(frmPercentage, bg="white")
tbxMaxNum.place(x=475, y=130, width=150, height=35)

tbxNumAch = tk.Entry(frmPercentage, bg="white")
tbxNumAch.place(x=475, y=200, width=150, height=35)

# Create a label for displaying the calculated percentage
lblPercentage2 = tk.Label(frmPercentage, text="", width=20, height=2, bg="white")
lblPercentage2.place(x=475, y=270)

# Create a "Clear" button and associate it with the clear_form() function
cmdClear = tk.Button(frmPercentage, text="Clear", width=8, bg="white", fg="black", command=clear_form)
cmdClear.place(x=375, y=450)

# Create a "Calculate" button and associate it with the calculate_percentage() function
cmdCalculate = tk.Button(frmPercentage, text="Calculate", width=8, bg="white", fg="black", command=calculate_percentage)
cmdCalculate.place(x=375, y=400)

# Create a "Read Data" button and associate it with the read_data() function
cmdReadData = tk.Button(frmPercentage, text="Read Data", width=8, bg="white", fg="black", command=read_data)
cmdReadData.place(x=375, y=350)

# Start the main event loop to display the form and handle user interactions
frmPercentage.mainloop()