select * from {{ ref('my_seed') }}
union all
select null as id, null as name, null as some_date