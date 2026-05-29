

# Smart Fitness Center Descriptive Analysis
import statistics
import matplotlib.pyplot as plt
member_names=["pravi","mouni","manvi","nikki","vinu"]
ages=[23,25,27,25,22]
workout_hours=[2,1.5,2.5,1,3]
calories_burned=[500,300,600,750,350]
print("-----Fitness Center DataSet------")
for i in range(len(member_names)):
  print(member_names[i],ages[i],workout_hours[i],calories_burned[i])
#Mean workout hours
mean_workout_hours=sum(workout_hours)/len(workout_hours)
print("\n Mean Workout Hours:",mean_workout_hours)
   #maximum Calories
highest_calories=max(calories_burned)
print("\n Highest Calories Burned:",highest_calories)
   #minimum calories
lowest_workout =min(workout_hours)
print("\n workout_hours:",workout_hours)
   #median
median_calories=statistics.median(calories_burned)
print("\n Median Calories:",median_calories)
   #Standard Deviation
std_dev=statistics.stdev(calories_burned)
print("\n Standard Deviation:",std_dev)
   #Variance
variance=statistics.variance(calories_burned)
print("\n Variance:",variance)
   #Most Active Member
index=calories_burned.index(highest_calories)
print("Most Active Member:",member_names[index])

    # add visualization
plt.bar(member_names,calories_burned)
plt.xlabel("Member Names")
plt.ylabel("Calories Burned")
plt.title("Calories Burned by Members")
plt.show()
