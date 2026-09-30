USE MissionOutpost
GO

SELECT *
FROM mission_runs

SELECT *
FROM mission_events

SELECT *
FROM mission_daily_metrics

GO

SELECT 
	COUNT(*) AS total_missions
FROM mission_runs

GO

SELECT 
	status,
	COUNT(*) AS total_missions
FROM mission_runs
GROUP BY status

GO

SELECT
    COUNT(*) AS total_missions,
    SUM(CASE WHEN status = 'COMPLETED' THEN 1 ELSE 0 END) AS completed_missions,
    SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) AS failed_missions
FROM mission_runs

GO

SELECT
    SUM(power_consumed) AS total_power_consumed
FROM mission_daily_metrics

GO

SELECT
    AVG(power_consumed) AS average_daily_power_consumed
FROM mission_daily_metrics

GO

SELECT TOP 5
    run_id,
    day,
    power_consumed
FROM mission_daily_metrics
ORDER BY power_consumed DESC

GO

SELECT
    SUM(power_saved) AS total_power_saved,
    AVG(power_saved) AS average_power_saved
FROM mission_daily_metrics

GO

SELECT
    run_id,
    day,
    power_consumed,
    power_saved
FROM mission_daily_metrics
WHERE power_saved > 0
ORDER BY day

GO

SELECT
    event,
    COUNT(*) AS event_count
FROM mission_events
GROUP BY event
ORDER BY event_count DESC

GO

SELECT
    e.run_id,
    e.day,
    e.event,
    e.outcome,
    d.power,
    d.food,
    d.life_support,
    d.shielding
FROM mission_events AS e
LEFT JOIN mission_daily_metrics AS d
    ON e.run_id = d.run_id
    AND e.day = d.day
ORDER BY e.run_id, e.day

GO

CREATE VIEW vw_mission_event_analysis AS
SELECT
    e.run_id,
    e.day,
    e.event,
    e.outcome,
    d.power,
    d.food,
    d.life_support,
    d.shielding,
    d.power_consumed,
    d.power_saved
FROM mission_events AS e
LEFT JOIN mission_daily_metrics AS d
    ON e.run_id = d.run_id
    AND e.day = d.day

GO






