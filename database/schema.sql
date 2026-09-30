CREATE TABLE mission_runs (
    run_id VARCHAR(100) PRIMARY KEY,
    start_time DATETIME,
    final_day INT,
    crew INT,
    status VARCHAR(20)
)

CREATE TABLE mission_daily_metrics (
    id INT IDENTITY(1,1) PRIMARY KEY,
    run_id VARCHAR(100),
    day INT,
    crew INT,
    power FLOAT,
    food FLOAT,
    life_support FLOAT,
    shielding FLOAT,
    power_consumed FLOAT,
    power_saved FLOAT,
    food_consumed FLOAT,
    life_support_consumed FLOAT,
    status VARCHAR(20),

    FOREIGN KEY (run_id)
        REFERENCES mission_runs(run_id)
)

CREATE TABLE mission_events (
    id INT IDENTITY(1,1) PRIMARY KEY,
    run_id VARCHAR(100),
    day INT,
    event VARCHAR(100),
    outcome VARCHAR(255),

    FOREIGN KEY (run_id)
        REFERENCES mission_runs(run_id)
)