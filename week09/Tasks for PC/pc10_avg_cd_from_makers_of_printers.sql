select avg(cd)
from pc
join product p on p.model=pc.model
where maker in
    (select maker
    from product
    where type='Printer');