USE museum;

-- 1) Show all tables and explain how they are related to one another (keys, triggers, etc.)
SHOW tables;
/* The ART_OBJECT table is referenced by the PAINTING, SCULPTURE, STATUE, OTHER, BORROWED, PERMANENT_COLLECTION, and DISPLAYED_IN tables to distinguish each art object from their ID numbers. The ARTIST table is referenced by the
ART_OBJECT table to record the names of the artists for each art object. The COLLECTION table is referenced by the BORROWED table in order to tell which borrowed collection the art_object belongs to. Finally the EXHIBITION table
is referenced by the DISPLAYED_IN table to associate art objects with exhibitions they are displayed in. All foreign key constraints specify cascade actions for both delete and update in order to ensure changes made to a parent table
will cascade to referencing tables, mainting referential integrity.*/

-- 2) A basic retrieval query: Display all Artist names.
SELECT Artist_name
FROM artist;

SELECT *
FROM artist;

SELECT *
FROM painting;

SELECT *
FROM art_object;

-- 3) A retrieval query with ordered results: Ordering art_object by the year they were created.
SELECT *
FROM art_object
ORDER BY Year_created;

-- 4) A nested retrieval query: Titles of Art that has Renaissance Epoch.
SELECT Title
FROM art_object
WHERE Artist_name IN (
	SELECT Artist_name
    FROM artist
    WHERE Epoch LIKE 'Renaissance');
    
-- 5) A retrieval query using joined tables: Titles of Art pieces that are paintings and their authors.
SELECT AO.ID_no, AO.Title, AO.Artist_name
FROM art_object AO
JOIN Painting P
	ON AO.Id_no = P.ID_no;

-- 6) An update operation with any necessary triggers
CREATE TABLE Artist_DateOfDeath_Log (
    Log_ID INT AUTO_INCREMENT PRIMARY KEY,
    Artist_name VARCHAR(50),
    Old_DateOfDeath DATE,
    New_DateOfDeath DATE,
    Update_Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //

CREATE TRIGGER ARTIST_UPDATE
AFTER UPDATE ON ARTIST
FOR EACH ROW
BEGIN
    IF OLD.Date_died != NEW.Date_died THEN
        INSERT INTO Artist_DateOfDeath_Log (Artist_name, Old_DateOfDeath, New_DateOfDeath)
        VALUES (NEW.Artist_name, OLD.Date_died, NEW.Date_died);
    END IF;
END;
//
DELIMITER ;

UPDATE ARTIST
SET Date_died = '1650-12-31'
WHERE Artist_name = 'Cornelius Norbertus Gijsbrechts';

-- 7) A deletion operation with any necessary triggers
CREATE TABLE ARCHIVED_ART_OBJECT (
    ID_no CHAR(9) NOT NULL,
    Year_created CHAR(4),
    Title VARCHAR(100) NOT NULL,
    Descr TEXT,
    Origin VARCHAR(50),
    Epoch VARCHAR(50),
    Collection_type VARCHAR(20) NOT NULL,
    Object_type VARCHAR(9) NOT NULL,
    Artist_name VARCHAR(50),
    Deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ID_no)
);
DELIMITER //
CREATE TRIGGER ARCHIVEOBJ
BEFORE DELETE ON ART_OBJECT
FOR EACH ROW
BEGIN
    INSERT INTO ARCHIVED_ART_OBJECT (ID_no, Year_created, Title, Descr, Origin, Epoch, Collection_type, Object_type, Artist_name)
    VALUES (OLD.ID_no, OLD.Year_created, OLD.Title, OLD.Descr, OLD.Origin, OLD.Epoch, OLD.Collection_type, OLD.Object_type, OLD.Artist_name);
END;
//
DELIMITER ;

DELETE FROM ART_OBJECT
WHERE ID_no = '111363504';