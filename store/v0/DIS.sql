-- Наполнение таблицы provider (Поставщики)
INSERT INTO provider (name, phone, email, address) VALUES
('Поставщик 1', '+71234567890', 'provider1@example.com', 'г. Москва, ул. Ленина, д. 1'),
('Поставщик 2', '+79876543210', 'provider2@example.com', 'г. Санкт-Петербург, ул. Пушкина, д. 10'),
('Поставщик 3', '+74951234567', 'provider3@example.com', 'г. Казань, ул. Баумана, д. 15'),
('Поставщик 4', '+74232223333', 'provider4@example.com', 'г. Новосибирск, ул. Советская, д. 5');

-- Наполнение таблицы product (Товары)
INSERT INTO product (name, provider, price, quantity) VALUES
('Товар 1', 1, 100.00, 50),
('Товар 2', 2, 200.00, 30),
('Товар 3', 1, 150.50, 20),
('Товар 4', 3, 300.00, 15),
('Товар 5', 4, 250.75, 40),
('Товар 6', 2, 400.00, 10),
('Товар 7', 3, 175.00, 25),
('Товар 8', 1, 500.00, 5);

-- Наполнение таблицы customer_states (Статусы покупателей)
INSERT INTO customer_states (name) VALUES
('Новый'),
('Постоянный'),
('Заблокированный'),
('VIP');

-- Наполнение таблицы customer (Покупатели)
INSERT INTO customer (name, email, phone, state, sysuser) VALUES
('Иван Иванов', 'ivanov@example.com', '+71234567890', 1, 1),
('Петр Петров', 'petrov@example.com', '+79876543210', 2, 2),
('Анна Смирнова', 'smirnova@example.com', '+74951234567', 3, 3),
('Ольга Сидорова', 'sidorova@example.com', '+74232223333', 4, 4),
('Алексей Павлов', 'pavlov@example.com', '+79872123456', 1, 5),
('Мария Волкова', 'volkova@example.com', '+71239876543', 2, 6);

-- Наполнение таблицы order_states (Состояния заказов)
INSERT INTO order_states (name) VALUES
('Новый'),
('Обрабатывается'),
('Доставлен'),
('Отменен');

-- Наполнение таблицы delivery (Доставка)
INSERT INTO delivery (date, address, price) VALUES
('2024-11-11', 'г. Москва, ул. Ленина, д. 1', 300.00),
('2024-11-12', 'г. Санкт-Петербург, ул. Пушкина, д. 10', 450.00),
('2024-11-13', 'г. Казань, ул. Баумана, д. 15', 350.00),
('2024-11-14', 'г. Новосибирск, ул. Советская, д. 5', 400.00),
('2024-11-15', 'г. Екатеринбург, ул. Карла Маркса, д. 20', 500.00);

-- Наполнение таблицы orders (Заказы)
INSERT INTO orders (customer, state, delivery, sum, date) VALUES
(1, 1, 1, 500.00, '2024-11-11'),
(2, 2, 2, 700.00, '2024-11-12'),
(3, 3, 3, 1200.00, '2024-11-13'),
(4, 1, 4, 950.00, '2024-11-14'),
(5, 2, 5, 1400.00, '2024-11-15'),
(6, 1, 1, 250.00, '2024-11-11');

-- Наполнение таблицы order_product (Товары в заказе)
INSERT INTO order_product (order_id, product, quantity) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 3),
(2, 4, 1),
(3, 5, 4),
(3, 6, 2),
(4, 7, 3),
(4, 8, 1),
(5, 1, 5),
(5, 3, 2),
(6, 2, 1),
(6, 4, 2);

-- Наполнение таблицы users (Пользователи)
INSERT INTO users (login, password, role, sysuser) VALUES
('admin', 'hashed_password_admin', 'admin', 1),
('user1', 'hashed_password_user1', 'user', 2),
('user2', 'hashed_password_user2', 'user', 3),
('manager', 'hashed_password_manager', 'manager', 4),
('superadmin', 'hashed_password_superadmin', 'admin', 5),
('customer_support', 'hashed_password_support', 'support', 6);

-- Наполнение таблицы jwts (JWT-токены)
INSERT INTO jwts (published, token, sysuser) VALUES
(NOW(), 'token_example_1', 1),
(NOW(), 'token_example_2', 2),
(NOW(), 'token_example_3', 3),
(NOW(), 'token_example_4', 4),
(NOW(), 'token_example_5', 5),
(NOW(), 'token_example_6', 6);
