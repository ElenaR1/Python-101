SELECT maker,avg(screen)
from laptop
join product on product.model=laptop.model
GROUP BY maker