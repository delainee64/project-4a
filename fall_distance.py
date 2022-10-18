# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/17/2022
# Description: Write a function named fall_distance that takes the time in seconds as
# an argument. The function should return the distance in meters that the object has fallen in that time.

# user_t = float(input("Enter a time in seconds\n"))
def fall_distance(time_seconds):
    """ Function calculates the distance an object falls due to gravity
        in a specific time period."""
    gravity = 9.8
    return .5 * gravity * time_seconds ** 2         # d=(1/2)gt**2
# print("Distance", fall_distance(user_t))
