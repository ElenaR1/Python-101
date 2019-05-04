select avg(price)
from
(
    select price
    from product p join pc
    on p.model=pc.model
    where maker='B'
 
    union all-- not union because it removes the duplicate rows
 
    select price
    from product p join laptop l
    on p.model=l.model
    where maker='B'
) AllPrices;