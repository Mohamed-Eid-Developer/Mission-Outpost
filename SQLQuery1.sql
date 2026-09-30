-- =========================================
-- Mission Outpost Database Schema
-- =========================================

USE MissionOutpost;
GO


-- =========================================
-- 1. Mission Runs
-- =========================================

CREATE TABLE mission_runs
(
    run_id UNIQUEIDENTIFIER NOT NULL,
    start_time DATETIME2 NOT NULL,
    final_day INT NOT NULL,
    crew INT NOT NULL,
    status VARCHAR(20) NOT NULL,

    CONSTRAINT PK_mission_runs
        PRIMARY KEY (run_id),

    CONSTRAINT CK_mission_runs_crew
        CHECK (crew > 0),

    CONSTRAINT CK_mission_runs_final_day
        CHECK (final_day >= 1),

    CONSTRAINT CK_mission_runs_status
        CHECK (status IN ('RUNNING', 'COMPLETED', 'FAILED'))
);
GO


-- =========================================
-- 2. Mission Daily Metrics
-- =========================================

CREATE TABLE mission_daily_metrics
(
    run_id UNIQUEIDENTIFIER NOT NULL,
    day INT NOT NULL,
    crew INT NOT NULL,

    power DECIMAL(10,2) NOT NULL,
    food DECIMAL(10,2) NOT NULL,
    life_support DECIMAL(10,2) NOT NULL,
    shielding DECIMAL(10,2) NOT NULL,

    power_consumed DECIMAL(10,2) NOT NULL,
    power_saved DECIMAL(10,2) NOT NULL,

    food_consumed DECIMAL(10,2) NOT NULL,
    life_support_consumed DECIMAL(10,2) NOT NULL,

    status VARCHAR(20) NOT NULL,

    CONSTRAINT PK_mission_daily_metrics
        PRIMARY KEY (run_id, day),

    CONSTRAINT FK_daily_metrics_runs
        FOREIGN KEY (run_id)
        REFERENCES mission_runs(run_id),

    CONSTRAINT CK_daily_metrics_day
        CHECK (day >= 1),

    CONSTRAINT CK_daily_metrics_crew
        CHECK (crew > 0),

    CONSTRAINT CK_daily_metrics_resources
        CHECK (
            power >= 0
            AND food >= 0
            AND life_support >= 0
            AND shielding >= 0
        ),

    CONSTRAINT CK_daily_metrics_consumption
        CHECK (
            power_consumed >= 0
            AND power_saved >= 0
            AND food_consumed >= 0
            AND life_support_consumed >= 0
        ),

    CONSTRAINT CK_daily_metrics_status
        CHECK (status IN ('RUNNING', 'COMPLETED', 'FAILED'))
);
GO


-- =========================================
-- 3. Mission Events
-- =========================================

CREATE TABLE mission_events
(
    event_id INT IDENTITY(1,1) NOT NULL,
    run_id UNIQUEIDENTIFIER NOT NULL,
    day INT NOT NULL,

    event VARCHAR(50) NOT NULL,
    outcome VARCHAR(200) NOT NULL,

    CONSTRAINT PK_mission_events
        PRIMARY KEY (event_id),

    CONSTRAINT FK_mission_events_runs
        FOREIGN KEY (run_id)
        REFERENCES mission_runs(run_id),

    CONSTRAINT CK_mission_events_day
        CHECK (day >= 1)
);
GO

