SELECT
	round(sum(o.amount_eur),0) as amount_eur,
	p.loc_country
FROM 
	public.projects p 
JOIN
	public.orders o on o.project_id = p.id
WHERE
	o.purchase_date >= '2024-01-01'
AND
	o.purchase_date < '2025-01-01'	
GROUP BY
	p.loc_country;
