DROP DATABASE IF EXISTS MUSEUM;
CREATE DATABASE MUSEUM;
USE MUSEUM;
CREATE TABLE ARTIST (
    Artist_name VARCHAR(50) NOT NULL,
    Date_born DATE,
    Date_died DATE,
    Country_of_origin VARCHAR(50),
    Epoch VARCHAR(50),
    Main_style VARCHAR(50),
    Descr TEXT,
    PRIMARY KEY (Artist_name)
);
CREATE TABLE ART_OBJECT (
    ID_no CHAR(9) NOT NULL,
    Year_created CHAR(4),
    Title VARCHAR(100) NOT NULL,
    Descr TEXT,
    Origin VARCHAR(50),
    Epoch VARCHAR(50),
    Collection_type VARCHAR(20) NOT NULL,
    Object_type VARCHAR(9) NOT NULL,
    Artist_name VARCHAR(50),
    PRIMARY KEY (ID_no),
    CONSTRAINT ARTOBJ CHECK (
        Object_type IN ('Painting', 'Sculpture', 'Statue', 'Other')
    ),
    CONSTRAINT ARTCOL CHECK (Collection_type IN ('Borrowed', 'Permanent')),
    CONSTRAINT ARTFK FOREIGN KEY (Artist_name) REFERENCES ARTIST(Artist_name) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE PAINTING (
    ID_no CHAR(9) NOT NULL,
    Paint_type VARCHAR(50),
    Drawn_on VARCHAR(50),
    Style VARCHAR(50),
    PRIMARY KEY (ID_no),
    CONSTRAINT PAINTFK FOREIGN KEY (ID_no) REFERENCES ART_OBJECT(ID_no) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE SCULPTURE (
    ID_no CHAR(9) NOT NULL,
    Material VARCHAR(50),
    Height_cm DECIMAL(10, 1),
    Weight_kg DECIMAL(10, 1),
    Style VARCHAR(50),
    PRIMARY KEY (ID_no),
    CONSTRAINT SCULPTFK FOREIGN KEY (ID_no) REFERENCES ART_OBJECT(ID_no) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE STATUE (
    ID_no CHAR(9) NOT NULL,
    Material VARCHAR(50),
    Height_cm DECIMAL(10, 1),
    Weight_kg DECIMAL(10, 1),
    Style VARCHAR(50),
    PRIMARY KEY (ID_no),
    CONSTRAINT STATFK FOREIGN KEY (ID_no) REFERENCES ART_OBJECT(ID_no) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE OTHER (
    ID_no CHAR(9) NOT NULL,
    Other_type VARCHAR(50),
    Style VARCHAR(50),
    PRIMARY KEY (ID_no),
    CONSTRAINT OTHERFK FOREIGN KEY (ID_no) REFERENCES ART_OBJECT(ID_no) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE PERMANENT_COLLECTION (
    ID_no CHAR(9) NOT NULL,
    Object_status VARCHAR(50),
    Cost DECIMAL(10, 2),
    Date_acquired DATE,
    PRIMARY KEY (ID_no),
    CONSTRAINT PERMOBJ CHECK (Collection_type IN ('Displayed', 'Stored', 'Loaned'))
    CONSTRAINT PERMFK FOREIGN KEY (ID_no) REFERENCES ART_OBJECT(ID_no) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE EXHIBITION (
    EX_ID CHAR(5) NOT NULL,
    Start_date DATE,
    End_date DATE,
    EX_name VARCHAR(100),
    PRIMARY KEY (EX_ID)
);
CREATE TABLE DISPLAYED_IN (
    EID CHAR(9) NOT NULL,
    ID_no CHAR(9) NOT NULL,
    PRIMARY KEY (ID_no, EID),
    CONSTRAINT DISPARTFK FOREIGN KEY (ID_no) REFERENCES ART_OBJECT(ID_no) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT DISPEXFK FOREIGN KEY (EID) REFERENCES EXHIBITION(EX_ID) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE COLLECTION (
    C_name VARCHAR(100) NOT NULL,
    C_type VARCHAR(50),
    Descr TEXT,
    Address VARCHAR(200),
    Phone VARCHAR(20),
    CP_first_name VARCHAR(50),
    CP_last_name VARCHAR(50),
    PRIMARY KEY (C_name)
);
CREATE TABLE BORROWED (
    ID_no CHAR(9) NOT NULL,
    Collection VARCHAR(100),
    Date_borrowed DATE,
    Date_returned DATE,
    PRIMARY KEY (ID_no),
    CONSTRAINT BORARTFK FOREIGN KEY (ID_no) REFERENCES ART_OBJECT(ID_no) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT BORCOLFK FOREIGN KEY (Collection) REFERENCES COLLECTION(C_name) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO ARTIST
VALUES (
        'Juan Fernandez',
        '1580-02-06',
        '1630-10-12',
        'Spanish',
        'Renaissance',
        'Baroque',
        'Spanish still-life painter.'
    ),
    (
        'Pablo Picasso',
        '1881-10-25',
        '1973-04-08',
        'Spanish',
        'Modern',
        'Cubism',
        'Renowned painter, sculptor, and co-founder of Cubism.'
    ),
    (
        'Cornelius Norbertus',
        '1630-03-27',
        '1683-07-06',
        'Flemish',
        'Baroque',
        'Trompe l''oeil',
        'Known for trompe l''oeil paintings.'
    ),
    (
        'Juan Gris',
        '1887-03-23',
        '1927-05-11',
        'Spain',
        'Modern',
        'Cubism',
        'Juan Gris was a Spanish painter and sculptor born in Madrid.'
    ),
    (
        'Pietro Torrigiano',
        '1472-08-17',
        '1528-02-13',
        'Italy',
        'Renaissance',
        'Sculpture',
        'Pietro Torrigiano was an Italian sculptor of the Renaissance.'
    ),
    (
        'Hans Holbein the Younger',
        '1497-03-30',
        '1543-05-28',
        'Germany',
        'Renaissance',
        'Portraiture',
        'Hans Holbein the Younger was a German painter and printmaker.'
    ),
    (
        'Marcus Gheeraerts the Younger',
        '1561-09-21',
        '1635-12-10',
        'Flanders',
        'Renaissance',
        'Portraiture',
        'Marcus Gheeraerts the Younger was a Flemish painter, known for his portraits.'
    ),
    (
        'Simone Leigh',
        '1967-01-01',
        null,
        'American',
        'Modern',
        'Contemporary art',
        'Sculptor and contemporary artist.'
    ),
    (
        'Theaster Gates',
        '1973-08-28',
        null,
        'American',
        'Modern',
        'Conceptual art',
        'Multidisciplinary artist.'
    ),
    (
        'Robert Pruitt',
        null,
        null,
        'American',
        'Modern',
        'Contemporary art',
        'Known for African American portraiture and mixed-media art.'
    ),
    (
        'Jakob Orfevre Blanck',
        null,
        null,
        'French',
        'Renaissance',
        'Baroque',
        'Cabinetmaker known for crafting decorative furniture.'
    ),
    (
        'Jean-Auguste-Dominique Ingres',
        '1780-08-29',
        '1867-01-14',
        'French',
        'Romanticism',
        'Neoclassicism',
        'Renowned painter known for "The Great Odalisque".'
    ),
    (
        'Jacques-Louis David',
        '1748-08-30',
        '1825-12-29',
        'French',
        'Neoclassicism',
        'Neoclassical art',
        'Famous for "The Sabines" and his neoclassical style.'
    ),
    (
        'Giovanni Paolo Panini',
        '1691-06-17',
        '1765-10-21',
        'Italian',
        'Baroque',
        'Vedutism',
        'Painter known for vedute paintings of Rome.'
    ),
    (
        'Eugenio Landesio',
        '1810-12-13',
        '1879-06-29',
        'Italian',
        'Romanticism',
        'Landscape painting',
        'Known for landscape paintings of Mexico.'
    ),
    (
        'John II Cleveley',
        null,
        null,
        'English',
        'Romanticism',
        'Maritime art',
        'Painter known for maritime landscapes, particularly of the Thames.'
    ),
    (
        'Francesco Righetti',
        '1835-06-29',
        '1917-08-01',
        'Swiss',
        'Neoclassicism',
        'Neoclassical art',
        'Architect known for his work in bronze sculpture.'
    );
INSERT INTO ART_OBJECT
VALUES (
        '111363504',
        '1544',
        'Field Armor of King Henry VIII',
        'Armor made for Henry VIII.',
        'Italian',
        'Renaissance',
        'Permanent',
        'Other',
        null
    ),
    (
        '198404671',
        '1600',
        'Bearing Cloth',
        'Needlework from England.',
        'British',
        'Renaissance',
        'Permanent',
        'Other',
        null
    ),
    (
        '120297468',
        '1564',
        'The Lewknor Table Carpet',
        'Ornamental table covering.',
        'Netherlandish',
        'Renaissance',
        'Permanent',
        'Other',
        null
    ),
    (
        '126339216',
        '1510',
        'Portrait Bust of John Fisher',
        'Sculpture of John Fisher.',
        'British',
        'Renaissance',
        'Permanent',
        'Sculpture',
        'Pietro Torrigiano'
    ),
    (
        '103967204',
        '1532',
        'Hermann von Wedigh III (died 1560)',
        'Portrait of Hermann von Wedigh III.',
        'German',
        'Renaissance',
        'Permanent',
        'Painting',
        'Hans Holbein the Younger'
    ),
    (
        '107937322',
        '1597',
        'Ellen Maurice',
        'Portrait of Ellen Maurice.',
        'Flemish',
        'Renaissance',
        'Permanent',
        'Painting',
        'Marcus Gheeraerts the Younger'
    ),
    (
        '260892373',
        '1916',
        'Bottle and Fruit Dish',
        'Cubist painting.',
        'Spanish',
        'Modern',
        'Permanent',
        'Painting',
        'Juan Gris'
    ),
    (
        '230840004',
        '1636',
        'Still Life with Four Bunches of Grapes',
        'Still-life painting of grapes.',
        'Spanish',
        'Renaissance',
        'Permanent',
        'Painting',
        'Juan Fernandez'
    ),
    (
        '208742683',
        '1912',
        'Still Life with Chair Caning',
        'Still-life painting of a newspaper.',
        'Spanish',
        'Modern',
        'Permanent',
        'Painting',
        'Pablo Picasso'
    ),
    (
        '260986041',
        '1665',
        'The Attributes of the Painter',
        'Painting of an artist''s studio wall',
        'Flemish',
        'Baroque',
        'Permanent',
        'Painting',
        'Cornelius Norbertus'
    ),
    (
        '375146957',
        '2019',
        '108 (Face Jug Series)',
        'Face jug.',
        'American',
        'Modern',
        'Permanent',
        'Sculpture',
        'Simone Leigh'
    ),
    (
        '371155323',
        '2020',
        'Signature Study',
        'High fire stoneware with glaze',
        'American',
        'Modern',
        'Permanent',
        'Statue',
        'Theaster Gates'
    ),
    (
        '388971469',
        '2019',
        'Birth and Rebirth and Rebirth',
        'African pastel portrait',
        'African',
        'Modern',
        'Permanent',
        'Other',
        'Robert Pruitt'
    ),
    (
        '437018134',
        '1677',
        'Chest of jewels of Louis XIV',
        'Decorated oak chest',
        'French',
        'Renaissance',
        'Borrowed',
        'Other',
        'Jakob Orfevre Blanck'
    ),
    (
        '489783717',
        '1814',
        'Grande Odalisque',
        'Oil painting of an odalisque.',
        'French',
        'Romanticism',
        'Borrowed',
        'Painting',
        'Jean-Auguste-Dominique Ingres'
    ),
    (
        '423318619',
        '1799',
        'The Sabines',
        'Painting of the intervention',
        'French',
        'Neoclassicism',
        'Borrowed',
        'Painting',
        'Jacques-Louis David'
    ),
    (
        '503335428',
        '1740',
        'Vue du Forum a Rome',
        'Painting of the forum in Rome.',
        'Italian',
        'Neoclassicism',
        'Borrowed',
        'Painting',
        'Giovanni Paolo Panini'
    ),
    (
        '555888385',
        '1857',
        'Vue de Real del Monte',
        'Painting of Real del Monte',
        'Italian',
        'Romanticism',
        'Borrowed',
        'Painting',
        'Eugenio Landesio'
    ),
    (
        '556140261',
        '1810',
        'Napoléon en Mars pacificateur',
        'Statue of Napoleon',
        'French',
        'Napoleonic',
        'Borrowed',
        'Sculpture',
        'Francesco Righetti'
    );
INSERT INTO PAINTING
VALUES ('103967204', 'Oil', 'Oak', 'Renaissance'),
    ('107937322', 'Oil', 'Oak', 'Renaissance'),
    ('260892373', 'Oil', 'Plywood', 'Cubism'),
    ('230840004', 'Oil', 'Canvas', 'Still-life'),
    ('208742683', 'Oil', 'Canvas', 'Still-life'),
    ('260986041', 'Oil', 'Canvas', 'Trompe l''Oeil'),
    ('489783717', 'Oil', 'Canvas', 'Orientalist'),
    ('423318619', 'Oil', 'Canvas', 'Neoclassical'),
    ('503335428', 'Oil', 'Canvas', 'Vedute'),
    ('555888385', 'Oil', 'Canvas', 'Landscape'),
    ('556140261', 'Oil', 'Canvas', 'Maritime');
INSERT INTO SCULPTURE
VALUES (
        '375146957',
        'Salt-fired porcelain',
        44.5,
        3.1,
        'Modern'
    ),
    (
        '126339216',
        'Polychrome terracotta',
        34,
        28.1,
        null
    );
INSERT INTO STATUE
VALUES (
        '371155323',
        'High fire stoneware',
        54.9,
        40.8,
        'Conceptual'
    ),
    ('556140261', 'Bronze', 46, 56.3, 'Neoclassical');
INSERT INTO OTHER
VALUES ('111363504', 'Armor', 'Maximilian'),
    ('198404671', 'Embroidery', 'Elizabethan'),
    ('120297468', 'Tapestry', 'Verdure'),
    ('388971469', 'Pastel Drawing', 'Contemporary'),
    ('437018134', 'Chest', 'Baroque');
INSERT INTO PERMANENT_COLLECTION
VALUES ('111363504', 'Displayed', 23622.97, '1931-08-03'),
    ('198404671', 'Displayed', 1042.99, '1995-04-15'),
    ('120297468', 'Stored', 2033.14, '1958-12-12'),
    ('126339216', 'Displayed', 6034.12, '1936-01-01'),
    ('103967204', 'Loaned', 3102.82, '1940-01-01'),
    ('107937322', 'Stored', 27332.26, '2017-01-01'),
    ('260892373', 'Displayed', 16953.00, '1956-01-01'),
    ('230840004', 'Loaned', 4647.65, '1964-11-25'),
    ('208742683', 'Displayed', 1987.19, '1979-03-16'),
    ('260986041', 'Stored', 2214.68, '1942-09-28'),
    ('375146957', 'Loaned', 1387.75, '2019-08-05'),
    ('371155323', 'Displayed', 3112.58, '2020-02-09'),
    ('388971469', 'Loaned', 1905.60, '2020-06-02');
INSERT INTO EXHIBITION
VALUES (
        'TU550',
        '2022-10-10',
        '2023-01-08',
        'The Tudors: Art and Majesty in Renaissance England'
    ),
    (
        'CU993',
        '2023-10-17',
        '2023-01-22',
        'Cubism and the Trompe l''Oeil Tradition'
    ),
    (
        'BP041',
        '2022-09-09',
        '2023-02-05',
        'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'
    ),
    (
        'ME171',
        '2023-07-01',
        '2023-08-10',
        'Timeless Expressions: A Retrospective of Masterpieces'
    ),
    (
        'NA405',
        '2023-08-25',
        '2023-10-05',
        'Transcending Timelines: Artistry Unveiled'
    );
INSERT INTO DISPLAYED_IN
VALUES ('TU550', '111363504'),
    ('TU550', '198404671'),
    ('TU550', '120297468'),
    ('TU550', '126339216'),
    ('TU550', '103967204'),
    ('TU550', '107937322'),
    ('CU993', '260892373'),
    ('CU993', '230840004'),
    ('CU993', '208742683'),
    ('CU993', '260986041'),
    ('BP041', '375146957'),
    ('BP041', '371155323'),
    ('BP041', '388971469'),
    ('ME171', '437018134'),
    ('ME171', '489783717'),
    ('ME171', '423318619'),
    ('NA405', '503335428'),
    ('NA405', '555888385'),
    ('NA405', '556140261');
INSERT INTO COLLECTION
VALUES (
        'Masterpieces of the Louvre',
        'Museum',
        'Artworks essential to history and the history of art',
        '123 Rue de la Galerie
Paris, France',
        '33123456789',
        'Emily',
        'Parker'
    ),
    (
        'National Museums Recovery',
        'Museum',
        'Artworks retrieved in Germany after World War II.',
        '789 Avenue de la Restitution
Paris, France',
        '33198765432',
        'David',
        'Thompson'
    );
INSERT INTO BORROWED
VALUES (
        '437018134',
        'Masterpieces of the Louvre',
        '2000-04-09',
        '2002-07-08'
    ),
    (
        '556140261',
        'Masterpieces of the Louvre',
        '2019-06-30',
        '2021-10-04'
    ),
    (
        '489783717',
        'National Museums Recovery',
        '2004-01-27',
        '2006-02-16'
    ),
    (
        '423318619',
        'National Museums Recovery',
        '1997-11-12',
        '1998-06-03'
    ),
    (
        '503335428',
        'National Museums Recovery',
        '1994-09-10',
        '1996-11-25'
    ),
    (
        '555888385',
        'National Museums Recovery',
        '1981-03-03',
        '1983-04-19'
    );
DROP ROLE IF EXISTS db_admin_role @localhost,
db_data_entry_role @localhost,
db_guest_role @localhost;
CREATE ROLE db_admin_role @localhost,
db_data_entry_role @localhost,
db_guest_role @localhost;
GRANT ALL PRIVILEGES ON MUSEUM.* TO db_admin_role @localhost;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON MUSEUM.* TO db_data_entry_role @localhost;
GRANT SELECT ON MUSEUM.* TO db_guest_role @localhost;
DROP USER IF EXISTS db_admin @localhost;
DROP USER IF EXISTS db_data_entry @localhost;
DROP USER IF EXISTS guest @localhost;
CREATE USER db_admin @localhost IDENTIFIED WITH mysql_native_password BY 'admin';
CREATE USER db_data_entry @localhost IDENTIFIED WITH mysql_native_password BY 'data';
CREATE USER guest @localhost;
GRANT db_admin_role @localhost TO db_admin @localhost;
GRANT db_data_entry_role @localhost TO db_data_entry @localhost;
GRANT db_guest_role @localhost TO guest @localhost;
SET DEFAULT ROLE ALL TO db_admin @localhost;
SET DEFAULT ROLE ALL TO db_data_entry @localhost;
SET DEFAULT ROLE ALL TO guest @localhost;