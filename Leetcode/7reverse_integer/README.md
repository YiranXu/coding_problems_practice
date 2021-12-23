The solution is from https://www.youtube.com/watch?v=Io9ujnnR4sI
The basic idea is to pop the last digit of the number, push it to the back of result (by pushing the result forward by one digit) and repeat the process.

(In the process, to prevent overflow, check whether the result will be overflown if updated)

### side note:
1. if converting to string, when it converts back to int, we cannot simply use int() function because that might already cause overflow.
2. using abs() to avoid rewrite the divde and module function is partial correct. If the number input is MIN_INT, by using abs(), technically, it already overdlows.