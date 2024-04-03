# Child Care Schedule

## Description

Cameron and Jamie's child is almost 3 years old! Despite the child being more independent now, planning childcare activities and household chores is still a challenge for the couple. This program helps Cameron and Jamie generate a schedule for the day's activities.

## Problem Statement

Cameron and Jamie have a list of N activities to take care of during the day. Each activity happens during a specific interval throughout the day. Cameron and Jamie must assign each activity to one of them, so that neither of them is responsible for two activities that overlap. An activity that ends at time t is not considered overlapping with another activity that starts at time t.

## Usage

- The program takes input from the standard input.
- Each test case starts with a line containing an integer N, the number of activities to be assigned.
- Then, N lines follow. Line i of these lines (counting from 1) contains two integers Si and Ei. Activity i starts exactly Si minutes after midnight and ends exactly Ei minutes before midnight.

## Example

4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440

## Output

- For each test case, the program outputs one line containing "Case #x: y", where x is the number of the test case (starting from 1) and y is "IMPOSSIBLE" if there is no valid schedule according to the rules described, or a string containing exactly N characters. Character i in y should be 'C' if activity i is assigned to Cameron in your proposed schedule, and 'J' if it is assigned to Jamie.

## Constraints

- The number of test cases (T) is at most 100.
- The number of activities (N) is at most 100.
- The start and end times for each activity are between 0 and 1439 (inclusive).
- The input format is correct as described above.



## License

This project is licensed under the [MIT License](LICENSE).
