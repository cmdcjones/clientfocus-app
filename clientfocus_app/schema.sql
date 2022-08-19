CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trainer_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    goals TEXT,
    notes TEXT,
    FOREIGN KEY (trainer_id) REFERENCES user (id)
        ON DELETE CASCADE
);

CREATE TABLE workout (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    trainer_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES client (id)
        ON DELETE CASCADE,
    FOREIGN KEY (trainer_id) REFERENCES user (id)
        ON DELETE CASCADE
);

CREATE TABLE exercise (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    workout_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    set_one_reps TEXT NOT NULL,
    set_one_weight TEXT NOT NULL,
    set_two_reps TEXT NOT NULL,
    set_two_weight TEXT NOT NULL,
    set_three_reps TEXT NOT NULL,
    set_three_weight TEXT NOT NULL,
    set_four_reps TEXT NOT NULL,
    set_four_weight TEXT NOT NULL,
    set_five_reps TEXT NOT NULL,
    set_five_weight TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (workout_id) REFERENCES workout (id)
        ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES client (id)
        ON DELETE CASCADE
);