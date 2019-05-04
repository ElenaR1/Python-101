SELECT speed,avg(price)
from pc
where speed > 500
GROUP BY speed