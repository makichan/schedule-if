import matplotlib.pyplot as plt
import random

# Function to generate a random color for each subject
def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Input: Number of classes available
num_classes = int(input("Enter the number of classes available: "))

# Input: Number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize the schedule as an empty dictionary
schedule = {}

# Define the time range from 08:00 AM to 06:00 PM
start_time = 8
end_time = 18

# Generate the schedule
for subject in range(1, num_subjects + 1):
    subject_name = input(f"Enter the name of subject {subject}: ")
    duration = float(input(f"Enter the duration of {subject_name} (in hours): "))
    
    # Find a random available class time for the subject
    while True:
        class_start_time = random.randint(start_time, end_time - int(duration))
        class_end_time = class_start_time + int(duration)
        
        # Check if the class time is available
        if all(class_end_time <= end for _, end in schedule.values()) and \
           all(class_start_time >= start for start, _ in schedule.values()):
            schedule[subject_name] = (class_start_time, class_end_time)
            break

# Print the schedule
print("\nSchedule:")
for subject, (start, end) in schedule.items():
    print(f"{subject}: {start:02d}:00 - {end:02d}:00")

# Create a plot of the schedule
fig, ax = plt.subplots(figsize=(10, 6))
for subject, (start, end) in schedule.items():
    color = random_color()
    ax.barh(subject, end - start, left=start, color=color, label=f"{subject} ({start:02d}:00 - {end:02d}:00)")

ax.set_xlabel("Time (24-hour format)")
ax.set_ylabel("Subjects")
ax.set_title("Class Schedule")
ax.set_xlim(start_time, end_time)
ax.set_xticks(range(start_time, end_time + 1))
ax.grid(axis="x", linestyle="--", alpha=0.7)
ax.legend()

plt.tight_layout()
plt.show()
