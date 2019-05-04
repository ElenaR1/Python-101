SELECT avg(price)
from pc
join product p on p.model=pc.model
WHERE maker='A'