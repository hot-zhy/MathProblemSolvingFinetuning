MATH_CHAT_BETA_SYSTEM_MESSAGE = 'You will use method of ratio calculation, addition, subtraction, grouping method to solve math problems.Please think step by step.And response briefly.'
MATH_CHAT_BETA_PROMPT = '''
Question:The math class in Think Academy starts at $9:00$ and ends at $10:00$. How long does the whole class last? 

Process:
The entire math class at Think Academy starts at 9:00 and ends at 10:00, the class time =  ending time - start time, so the class lasts for 1 hour
The answer is 1

Answer: 1

Question:A car departed $9$ minutes later than the scheduled time. In order to reach its destination on time, it has to increase its speed by $30 \\%$. If the usual speed of the car is $60$ mph, how far does this car have to travel to reach its destination? 

Process:
To find the distance the car has to travel to reach its destination, we need to consider the delayed departure and the increased speed.
Given:
The car departed 9 minutes later than the scheduled time.
The car needs to increase its speed by 30% to reach its destination on time.
The usual speed of the car is 60 mph.
Let's first calculate the increased speed:
The car needs to increase its speed by 30%. To increase by 30%, we multiply the usual speed by 1 + (30/100) or 1.3.
The increased speed is:
    60 mph * 1.3 = 78 mph
Now, we know that the car has to travel at an increased speed of 78 mph in order to reach its destination on time.
To find the distance the car has to travel, we need to know the time it takes to cover that distance.Since the only information given is the delayed departure of 9 minutes, we can assume that the car takes T hour to get to the destination at a speed of 60mph, then the car will take (T - 9/60) hour to get to the destination at the speed of 78mph.
We can set up a proportion to find the distance:

Usual speed * Time taken = Increased speed * Time taken
    60 * T= 78 * (T - 9/60)
    60 * T=78 (T - 0.15)
    60T = 78T- 11.7
    18T = 11.7
    T=0.65
Since it takes 0.65 hour to get to the destination at a usual speed.and distance = Usual speed * Time taken :
60*0.65=39 mile 
So the distance to the destination is 39mile.
The answer is 39.

Answer:39

Question:A length of rope is $3  \\text{m}$~long. It is cut into four unequal lengths. Three of the pieces are $147  \\text{cm}$,~$32.5  \\text{cm}$~and $67  \\text{cm}$. How long is the fourth piece? 

Process:
To find the length of the fourth piece of the rope, we can start by finding the total length of the three known pieces and then subtract it from the total length of the original rope.
Given information:
Original rope length:3m
Length of the three known pieces:147cm,32.5cm, and 67cm.
First, we need to convert the known lengths from centimeters to meters to match the unit of the original rope length:
    147cm=1.47m
    32.5cm=0.325m
    67cm=0.67m
Next, let's add up the lengths of the three known pieces:
    1.47m+0.325m+0.67m=2.465m
Now, we can find the length of the fourth piece by subtracting the sum of the lengths of the known pieces from the length of the original rope:
    3m−2.465m=0.535m
Therefore, the length of the fourth piece of the rope is0.535m.
The answer is 0.535

Answer:0.535


Question:A ball of mass 2 kg is gently pushed off the edge of a tabletop that is 5.0 m above the floor. Find the speed of the ball as it strikes the floor.

Process:
To find the speed of the ball as it strikes the floor, we can use the principle of conservation of energy. The potential energy of the ball at the tabletop is converted to kinetic energy as it falls.
Given information:
Mass of the ball: 2 kg
Height of the tabletop: 5.0 m
We can start by calculating the potential energy of the ball at the tabletop:
	Potential Energy = Mass * Gravity * Height
    Potential Energy = 2 kg * 9.8 m/s^2 * 5.0 m
    Potential Energy = 98 J
According to the conservation of energy, this potential energy will be converted to kinetic energy as the ball falls. The kinetic energy is given by:
	Kinetic Energy = 1/2 * Mass * Velocity^2
Since the ball is initially at rest, the initial kinetic energy is zero:
	Initial Kinetic Energy = 0 J
Therefore, the potential energy at the tabletop is equal to the final kinetic energy as it strikes the floor (which is also the total energy):
Potential Energy at tabletop = Final Kinetic Energy at floor
    98 J = 1/2 * 2 kg * Velocity^2
Simplifying the equation:
    98 J = 1 kg * Velocity^2
    Velocity^2 = 98 J / 1 kg
    Velocity^2 = 98 m^2/s^2
Taking the square root of both sides:
    Velocity = √(98 m^2/s^2) =  2√7
Therefore, the speed of the ball as it strikes the floor is  2√7 m/s.
The answer is  2√7

Answer: 2√7


Question:Sarah placed 10 chairs in a row, evenly spaced out. The total distance covered by the chairs is 36m. If Sarah removes 3 chairs and space out the chairs evenly again, what is the distance between every 2 chairs?

Process:
To find the distance between every two chairs after Sarah removes 3 chairs and spaces them evenly again, we first need to determine the number of chairs remaining.
Initially, Sarah had 10 chairs in a row evenly spaced out, Let's denote the distance between every two chairs as "d",and the number of intervals = number of chairs -1.
The total distance covered by the chairs is 36m, so we can write the equation as follows:
Total distance = (Number of chairs-1) * Distance between every two chairs
    36m = (10-1) * d
We can solve for "d" by dividing both sides of the equation by 9:
    d = 36m / 9
    d = 4m
Therefore, initially, the distance between every two chairs was 4m.
Now, Sarah removes 3 chairs, leaving us with 7 chairs. We want to find the new distance between every two chairs, which we'll call "d'".
We can use the same equation as before to solve for "d'":
Total distance = (Number of chairs-1) * Distance between every two chairs
    36m = 6 * d'
Solving for "d'", we divide both sides of the equation by 6:
    d' = 36m / 6
    d' = 6m
Therefore, after Sarah removes 3 chairs and spaces out the remaining 7 chairs evenly, the distance between every two chairs is 6 m.
The answer is 6

Answer:6

Q: 
'''.strip()
