SELECT SHIP
from OUTCOMES
join BATTLES b on b.name=OUTCOMES.BATTLE
where date like '1942%'