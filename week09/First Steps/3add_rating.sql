ALTER TABLE Languages
ADD rating INTEGER;


UPDATE Languages
SET rating = 1
WHERE NAME='Python'

UPDATE Languages
SET rating = 2
WHERE NAME='GO'

UPDATE Languages
SET rating = 3
WHERE NAME='Java'

UPDATE Languages
SET rating = 4
WHERE NAME='Haskell'

UPDATE Languages
SET rating = 5
WHERE NAME='C#'

UPDATE Languages
SET rating = 6
WHERE NAME='Ruby'

UPDATE Languages
SET rating = 7
WHERE NAME='C++'

UPDATE Languages
SET rating = 8
WHERE NAME='JavaScript'

ALTER TABLE Languages DROP COLUMN rating;
