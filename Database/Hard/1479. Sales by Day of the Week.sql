select b.item_category as 'CATEGORY',
SUM(CASE WHEN datepart(dw,order_date) = 2 THEN quantity ELSE 0 END) as 'MONDAY',
SUM(CASE WHEN datepart(dw,order_date) = 3 THEN quantity ELSE 0 END) as 'TUESDAY',
SUM(CASE WHEN datepart(dw,order_date) = 4 THEN quantity ELSE 0 END) as 'WEDNESDAY',
SUM(CASE WHEN datepart(dw,order_date) = 5 THEN quantity ELSE 0 END) as 'THURSDAY',
SUM(CASE WHEN datepart(dw,order_date) = 6 THEN quantity ELSE 0 END) as 'FRIDAY',
SUM(CASE WHEN datepart(dw,order_date) = 7 THEN quantity ELSE 0 END) as 'SATURDAY',
SUM(CASE WHEN datepart(dw,order_date) = 1 THEN quantity ELSE 0 END) as 'SUNDAY'
from Items b
left join Orders a
on a.item_id = b.item_id
group by  b.item_category
order by b.item_category