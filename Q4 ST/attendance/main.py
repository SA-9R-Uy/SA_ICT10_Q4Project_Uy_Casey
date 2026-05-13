from pyscript import document

# NumPy for arrays
import numpy as np

# Matplotlib for graphs
import matplotlib.pyplot as plt


# Store attendance data
days = []
absences = []


# Function for displaying graph
def displaying(e):

    # Get values from HTML inputs
    day = document.getElementById('dayOfTheWeek').value
    absence = int(document.getElementById('absences').value)


    # Save values into lists
    days.append(day)
    absences.append(absence)


    # Convert absences into NumPy array
    converted_absences = np.array(absences)


    # Clear old graph
    plt.clf()


    # Create graph
    plt.plot(days, converted_absences, marker='o')


    # Graph title
    plt.title("Weekly Attendance")


    # Label names
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")


    # Add grid lines
    plt.grid()


    # Display graph
    plt.show()
