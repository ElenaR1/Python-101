ALTER TABLE Languages
ADD rating INTEGER
CHECK (rating>0 AND rating<10);

UPDATE Languages
SET rating = 1
WHERE language='Python';

UPDATE Languages
SET rating = 2
WHERE language='Go';

UPDATE Languages
SET rating = 3
WHERE language='Java';

UPDATE Languages
SET rating = 4
WHERE language='Haskell';

UPDATE Languages
SET rating = 5
WHERE language='C#';

UPDATE Languages
SET rating = 6
WHERE language='Ruby';

UPDATE Languages
SET rating = 7
WHERE language='C++';

UPDATE Languages
SET rating = 8
WHERE language='JavaScript';

