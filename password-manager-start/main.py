from tkinter import *
from tkinter import messagebox
import random, pyperclip, json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
			   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
			   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	nr_letters = random.randint(8, 10)
	nr_symbols = random.randint(2, 4)
	nr_numbers = random.randint(2, 4)

	letter_list = [random.choice(letters) for _ in range(nr_letters)]
	symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
	numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]

	password_list = letter_list + symbols_list + numbers_list
	random.shuffle(password_list)

	password_string = "".join(password_list)
	pyperclip.copy(password_string)
	password_entry.insert(0, password_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_to_file(updated_data):
	with open("data.json", "w") as data_file:
		json.dump(updated_data, data_file, indent=4)

def save():
	web = web_entry.get()
	email = email_username_entry.get()
	password = password_entry.get()
	new_data = {
		web: {
			"email": email,
			"password": password,
		}
	}

	if len(web) ==0 or len(password) == 0:
		messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
	else:
		try:
			with open("data.json", "r") as data_file:
				#reading old data
				data = json.load(data_file)
		except FileNotFoundError:
			write_to_file(new_data)
		else:
			# updating old data with new data
			data.update(new_data)
			#saving updated data
			write_to_file(data)
		finally:
			web_entry.delete(0, END)
			password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
	web = web_entry.get()
	try:
		with open("data.json") as file:
			data = json.load(file)
	except FileNotFoundError:
		messagebox.showinfo(title="Error", message="No Data File Found.")
	else:
		if web in data:
			messagebox.showinfo(title=web, message=f"Email: {data[web]["email"]}"
														f"\nPassword: {data[web]["password"]}")
		else:
			messagebox.showinfo(title="Error", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
web_entry = Entry(width= 21)
web_entry.grid(row=1, column=1, sticky="EW")
web_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_username_entry.insert(0, "johnjosil@yahoo.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

#Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")


window.mainloop()