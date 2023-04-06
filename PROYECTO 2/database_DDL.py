
DDL = ''' 
-- Crear la tabla 'Users'
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    country_id INTEGER
);

-- Crear la tabla 'Countries'
CREATE TABLE Countries (
    country_id SERIAL PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    ISO_code VARCHAR(3) NOT NULL UNIQUE,
    continent VARCHAR(100) NOT NULL
);

-- Crear la tabla 'DateDim'
CREATE TABLE DateDim (
    date_id SERIAL PRIMARY KEY,
    date DATE UNIQUE NOT NULL,
    day INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    week_day INTEGER NOT NULL,
    hour INTEGER NOT NULL,
    minute INTEGER NOT NULL,
    is_weekend INTEGER NOT NULL
);

-- Crear la tabla 'PackageType'
CREATE TABLE PackageType (
    package_id SERIAL PRIMARY KEY,
    name_package VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)
);

-- Crear la tabla 'Discounts'
CREATE TABLE Discounts (
    discount_id SERIAL PRIMARY KEY,
    name_discount VARCHAR(20) NOT NULL UNIQUE,
    percentage NUMERIC(5, 2) NOT NULL CHECK (percentage BETWEEN 0 AND 100)
);

-- Crear la tabla 'Purchases' (tabla de hechos)
CREATE TABLE Purchases (
    purchase_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(user_id) ON DELETE CASCADE,
    package_id INTEGER REFERENCES PackageType(package_id),
    date_id INTEGER REFERENCES DateDim(date_id),
    discount_id INTEGER REFERENCES Discounts(discount_id),
    country_id INTEGER REFERENCES Countries(country_id),
    total_price NUMERIC(10, 2) NOT NULL CHECK (total_price >= 0)
);

-- Añadir la restricción de clave externa a la tabla 'Users'
ALTER TABLE Users
ADD CONSTRAINT fk_users_country_id
FOREIGN KEY (country_id) REFERENCES Countries(country_id);


 '''