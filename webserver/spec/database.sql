CREATE TABLE Devices (
    device_id        INT AUTO_INCREMENT,
    device_latitude  REAL NOT NULL,
    device_longitude REAL NOT NULL
);

CREATE TABLE Fires (
    detector_id   INT,
    suppressed    BOOL     DEFAULT FALSE,
    started_at    DATETIME NOT     NULL,
    suppressed_at DATETIME
);
