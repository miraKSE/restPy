from supabase import create_client, Client

# Укажите ваш API Key и URL
# VByUxykAZ_n_He8 - pass for db
SUPABASE_URL = "https://qbvxupwunmlmympeoggp.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFidnh1cHd1bm1sbXltcGVvZ2dwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE0MzY2ODksImV4cCI6MjA0NzAxMjY4OX0.fRBrUG-qSXF4XxXtwrHhsLPXB7tnojgx6CaKjZGrqbQ"

# Создайте клиент
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Запрос к таблице "product"
response = supabase.table("product").select("*").execute()

# Печать результатов
print(response.data)

