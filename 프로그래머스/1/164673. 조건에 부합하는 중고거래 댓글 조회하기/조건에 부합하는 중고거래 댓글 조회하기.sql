-- 코드를 입력하세요
SELECT 
b.title, 
r.board_id, 
r.reply_id, 
r.writer_id, 
r.contents, 
date_format(r.created_date, '%Y-%m-%d') as created_date 
from used_goods_board b
inner join used_goods_reply r on b.board_id = r.board_id
where substr(b.created_date,1,7) = '2022-10'
order by r.created_date asc, b.title asc;