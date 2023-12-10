#1. Create Variables for Triatlon called award Swimming_time, cycling_time, running_time

swimming_time = int(input ("what is your swimming time result in minutes: "))
cycling_time = int(input ("what is your scyclingtime result in minutes: " ))
running_time = int(input ("what is your running time result in minutes: " ))


#2. create variable called "award" and add swimming_time,cycling_time,running_time together to calculate the total time. 
# time comes in number, add integer 

award = int(swimming_time + cycling_time + running_time)

#3. using if and elif function get the correct statement. The order is important as the first true statement execute other statement. 
# add the variable "award" to get total number in minutes 
#the order setting up condition is important the first true condition execute others

if award >= 111: # time range 111 + min / no award
    print ( "You are more then 10 minutes of the qualifying time:", award, "minutes. You have not qualified for any Award")

elif award <= 100: # time range 0-100 / Provincial Colour Award
  print ("You are within the qualifying time. Your total result is:", award,"minutes. You qualified for Provincial Colour Award")

elif award >= 106: # time range 106 -110 / Provincial Scroll Award
    print ("You are within 10 minutes of the qualifying time. " , award, "minutes. You qualified for Provincial Scroll Award")
    
elif award >= 101: # time range 101-105 / Half Colour Award
    print ("You are within 5 minutes of the qualifying time." , award, "minutes. You qualified for Provincial Half Colour Award")  


elif award <= 110: # time range 106 -110 / Provincial Scroll Award
    print ("You are within 10 minutes of the qualifying time. " , award, "minutes. You qualified for Provincial Scroll Award")

elif award <= 105: # time range 101-105 / Half Colour Award
    print ("You are within 5 minutes of the qualifying time." , award, "minutes. You qualified for Provincial Half Colour Award")






