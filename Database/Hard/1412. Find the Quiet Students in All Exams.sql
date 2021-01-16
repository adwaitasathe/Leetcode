/* Write your T-SQL query statement below */

with cte as (
select *,
       rank() over (partition by exam_id order by score ) as 'low_score',
       rank() over (partition by exam_id order by score desc ) as 'high_score'
    
from exam
)

select  distinct a.student_id , b.student_name
from cte a
left join student b
on a.student_id = b.student_id
where a.student_id not in  (select distinct student_id from cte where low_score = 1 or high_score = 1)