SELECT * FROM employees WHERE city <> 'Pune'; -- i thought it would give 9 rows 
-- count didnt match it , just got 7 values . The NUll values were also no printed 
-- i didnt expected this as i thought where will see NULL as not equal to pune so it will return it
-- but now i think that NULL is not written inside the null citys instead they are empty/blank and it could contain any city 
-- so maybe where interprets as the null values can contain any city it does not automatically assumes any city in it 
-- Any comparison with NULL is neither true nor false, and WHERE keeps only rows where the condition is true. So = NULL never matches anything.
SELECT * FROM employees WHERE city <> 'Pune' or CITY IS NULL; -- Prints 9 rows , evertyhing except pune 