-- Таблица для поставщиков
CREATE TABLE provider (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255)
);

-- Таблица для доставки
CREATE TABLE delivery (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    address TEXT NOT NULL,
    price DOUBLE PRECISION NOT NULL
);


-- Таблица для состояния заказов
CREATE TABLE order_states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Таблица для статуса покупателей
CREATE TABLE customer_states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Таблица для пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    login VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(255),
    sysuser INTEGER
);

-- Таблица для JWT-токенов
CREATE TABLE jwts (
    id SERIAL PRIMARY KEY,
    published TIMESTAMP DEFAULT NOW(),
    token TEXT NOT NULL,
    sysuser INTEGER
);

-- Таблица для товаров
CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    provider INTEGER REFERENCES provider(id) ON DELETE SET NULL,
    price DOUBLE PRECISION NOT NULL,
    quantity INTEGER NOT NULL
);

-- Таблица для покупателей
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(255),
    state INTEGER REFERENCES customer_states(id) ON DELETE SET NULL,
    sysuser INTEGER
);



-- Таблица для заказов
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer INTEGER REFERENCES customer(id) ON DELETE SET NULL,
    state INTEGER REFERENCES order_states(id) ON DELETE SET NULL,
    delivery INTEGER REFERENCES delivery(id) ON DELETE SET NULL,
    sum DOUBLE PRECISION NOT NULL,
    date DATE NOT NULL
);



-- Таблица для товаров в заказе
CREATE TABLE order_product (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    product INTEGER REFERENCES product(id) ON DELETE SET NULL,
    quantity INTEGER NOT NULL
);




