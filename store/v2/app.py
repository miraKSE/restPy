from flask import Flask, render_template, request, redirect, jsonify, session
from supabase import create_client, Client

app = Flask(__name__)
app.secret_key = 'a_very_secure_and_random_string'

# Настройки Supabase
SUPABASE_URL = "https://qbvxupwunmlmympeoggp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFidnh1cHd1bm1sbXltcGVvZ2dwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE0MzY2ODksImV4cCI6MjA0NzAxMjY4OX0.fRBrUG-qSXF4XxXtwrHhsLPXB7tnojgx6CaKjZGrqbQ"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def handle_response(response):
    """
    Универсальная обработка ответа Supabase.
    Проверяет, есть ли данные или ошибки, и возвращает результат.
    """
    if not response.data:
        raise ValueError("Ошибка запроса к Supabase")
    return response.data


@app.route('/')
def index():
    if 'user' in session:
        return redirect('/dashboard')
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        try:
            # Проверка учетных данных
            response = supabase.table("users").select("*").eq("login", login).eq("password", password).execute()
            users = handle_response(response)
            if not users:
                return render_template('login.html', error="Неверные учетные данные!")

            session['user'] = users[0]
            return redirect('/dashboard')
        except Exception as e:
            return render_template('login.html', error=str(e))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    return render_template('dashboard.html')


@app.route('/products', methods=['GET'])
def products():
    if 'user' not in session:
        return redirect('/login')

    search_query = request.args.get('search', '').strip()

    try:
        query = supabase.table("product").select("id, name, price, quantity, provider")
        if search_query:
            query = query.ilike("name", f"%{search_query}%")
        response = query.execute()
        products = handle_response(response)
        return render_template('products.html', products=products, search_query=search_query)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        provider_id = request.form.get('provider_id')

        try:
            # Добавление нового товара
            response = supabase.table("product").insert({
                "name": name,
                "price": float(price),
                "quantity": int(quantity),
                "provider": int(provider_id) if provider_id else None
            }).execute()
            handle_response(response)
            return redirect('/products')
        except Exception as e:
            return render_template('add_product.html', error=str(e))

    return render_template('add_product.html')

@app.route('/edit-product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        provider_id = request.form.get('provider_id')

        try:
            # Обновление данных продукта
            response = supabase.table("product").update({
                "name": name,
                "price": float(price),
                "quantity": int(quantity),
                "provider": int(provider_id) if provider_id else None
            }).eq("id", product_id).execute()
            handle_response(response)
            return redirect('/products')
        except Exception as e:
            return render_template('edit_product.html', error=str(e))

    try:
        # Получение текущих данных продукта
        response = supabase.table("product").select("*").eq("id", product_id).single().execute()
        product = handle_response(response)
        return render_template('edit_product.html', product=product)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/orders', methods=['GET', 'POST'])
def orders():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        state_id = request.form.get('state_id')
        delivery_id = request.form.get('delivery_id')
        sum_value = request.form.get('sum')
        date = request.form.get('date')

        try:
            # Добавление нового заказа
            response = supabase.table("orders").insert({
                "customer": int(customer_id),
                "state": int(state_id),
                "delivery": int(delivery_id) if delivery_id else None,
                "sum": float(sum_value),
                "date": date
            }).execute()
            handle_response(response)
            return redirect('/orders')
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    try:
        # Получение списка заказов
        response = supabase.table("orders").select("id, customer, state, delivery, sum, date").execute()
        orders = handle_response(response)
        return render_template('orders.html', orders=orders)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/customers', methods=['GET', 'POST'])
def customers():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        state_id = request.form.get('state_id')

        try:
            # Добавление нового покупателя
            response = supabase.table("customer").insert({
                "name": name,
                "email": email,
                "phone": phone,
                "state": int(state_id) if state_id else None,
                "sysuser": session['user']['id']
            }).execute()
            handle_response(response)
            return redirect('/customers')
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    try:
        # Получение списка покупателей
        response = supabase.table("customer").select("id, name, email, phone, state").execute()
        customers = handle_response(response)
        return render_template('customers.html', customers=customers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
