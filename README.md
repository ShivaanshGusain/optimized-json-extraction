This file contains the working of a high-performance data extractor from a JSON file, where I have used orjson and Numpy, extracting data of 200_000 people.
Specifically, finding out their ages and salaries to calculate the average age and average salary of the entire dataset.

The time constraint I had set for myself was that the entire code should run under 1 second.
Although I have not achieved that yet, I have gotten close to approximately 1.44 seconds, as calculated through the pref_counter() function in the time module.

This code does require tweaking, the more time part is from reading the data file, and the interpreter being slow. 

If we just calculate the time of the code after opening the data.json file, the time taken is about 0.20 seconds, which is well under the mark and suggests that 80-90% of the time 
is consumed by opening the JSON file.

NOTE
This also has the file where I have tried different methods and seen how they work and how much time they have taken.
