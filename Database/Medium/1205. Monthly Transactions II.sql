/* Write your T-SQL query statement below */

with cte as (
select a.trans_id as id, 
       b.country,
       'chargeback' as state,
       b.amount,
       format(a.trans_date,'yyyy-MM') as month
from Chargebacks a
join Transactions b
on b.id = a.trans_id

union all

select id,
       country,
       state,
       amount,
       format(trans_date,'yyyy-MM') as month    
from Transactions
where state = 'approved'
)


select month,
       country,
       sum(case when state = 'approved' then 1 else 0 end) as approved_count,
       sum(case when state = 'approved' then amount else 0 end) as approved_amount,
       sum(case when state = 'chargeback' then 1 else 0 end) as chargeback_count,
       sum(case when state = 'chargeback' then amount else 0 end) as chargeback_amount
from cte
group by month , country







