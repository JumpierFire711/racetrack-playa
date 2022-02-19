# racetrack-playa
A little simulation I made back in 7th Grade to "simulate" the "mysterious" movement of rocks in Death Valley.

Here's a short description of what it does:

1. Draws a circle on a blank TK Canvas and initialises 5 turtles, putting them in an array to make iteration easier.
2. Disables the pen of all turtles, sets their position to the centre of the circle, and sets their heading (direction) to 225 degrees counterclockwise from the positive x-axis
3. Moves each turtle forward a random distance and turns it a random number of degrees left or right. If the turtle's heading is not between 180 and 270 degrees, the chance to turn left is adjusted to ensure that each turtle's path tends towards the Southwest direction.
