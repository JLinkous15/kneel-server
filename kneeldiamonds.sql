CREATE TABLE Metals
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE Sizes
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE Styles
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);
CREATE TABLE Orders
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    [metal_id] INTEGER NOT NULL,
    [size_id] INTEGER NOT NULL,
    [style_id] INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`)
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`)
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

INSERT INTO "Metals"
    VALUES (null, "Sterling", 25.50);
INSERT INTO "Metals"
    VALUES (null, "Silver", 32.00);
INSERT INTO "Metals"
    VALUES (null, "Gold", 54.90);
INSERT INTO "Metals"
    VALUES (null, "Platinum", 76.23);
INSERT INTO "Metals"
    VALUES (null, "Palladium", 92.40);

INSERT INTO Sizes
    VALUES (null, "Small", 5.00);
INSERT INTO Sizes
    VALUES (null, "Medium", 7.50);
INSERT INTO Sizes
    VALUES (null, "Large", 10.00);

INSERT INTO Styles
    VALUES (null, "Earring", 4.50);
INSERT INTO Styles
    VALUES (null, "Ring", 6.00);
INSERT INTO Styles
    VALUES (null, "Bracelet", 7.50);
INSERT INTO Styles
    VALUES (null, "Necklace", 9.23);
INSERT INTO Styles
    VALUES (null, "Crown", 20.70);

INSERT INTO Orders
    VALUES(null, 1, 3, 5);
INSERT INTO Orders
    VALUES(null, 4, 1, 4);
INSERT INTO Orders
    VALUES(null, 2, 3, 1);
INSERT INTO Orders
    VALUES(null, 1, 4, 3);
INSERT INTO Orders
    VALUES(null, 3, 3, 2);
INSERT INTO Orders
    VALUES(null, 4, 2, 2);
INSERT INTO Orders
    VALUES(null, 4, 5, 1);
INSERT INTO Orders
    VALUES(null, 2, 1, 4);
INSERT INTO Orders
    VALUES(null, 5, 5, 5);
INSERT INTO Orders
    VALUES(null, 2, 3, 2);
