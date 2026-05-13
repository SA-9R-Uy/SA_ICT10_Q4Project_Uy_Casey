from pyscript import document


# Class definition
class Classmate:

    # This runs when a new object is created
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject


    # This method returns a sentence introduction
    def introduce(self):
        return f"💥 {self.name} from {self.section} likes {self.favorite_subject}."


# List storing classmates
classmates = [
    Classmate("Casey", "Ruby", "Python"),
    Classmate("Terry", "Ruby", "Math"),
    Classmate("Wally", "Ruby", "Science")
]


# Function for adding classmates
def add_classmate(e):

    # Get input values from HTML
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value


    # Check if any field is empty
    if name == "" or section == "" or subject == "":
        document.getElementById("output").innerHTML = "⚠️ Please complete all fields."
        return


    # Create new classmate object
    new_student = Classmate(name, section, subject)


    # Add object into list
    classmates.append(new_student)


    # Clear textboxes after adding
    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""


    # Confirmation message
    document.getElementById("output").innerHTML = f"✅ {name} added successfully!"


# Function for displaying classmates
def show_classmates(e):

    # Check if list is empty
    if len(classmates) == 0:
        document.getElementById("output").innerHTML = "No classmates available."
        return


    # Variable for storing output
    result = ""


    # Loop through classmates
    for student in classmates:
        result += student.introduce() + "<br><br>"


    # Display final result
    document.getElementById("output").innerHTML = result
