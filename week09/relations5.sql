SELECT NAME
FROM MOVIEEXEC
WHERE NETWORTH > (SELECT NETWORTH 
				FROM MOVIEEXEC 
				WHERE NAME='Merv Griffin')