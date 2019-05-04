SELECT maker
from product
JOIN pc on pc.model=product.model
where price= (SELECT max(price) from pc);