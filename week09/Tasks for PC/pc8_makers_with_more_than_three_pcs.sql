SELECT maker,count(*)
from product
WHERE type='PC'
GROUP BY maker
HAVING count(*)>=3
