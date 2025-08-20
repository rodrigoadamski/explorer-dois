import os

# Configuração temporária - usando SQLite para testar
# os.environ.setdefault('DATABASE_URL', 'postgresql://postgres.izdsgkstzompjvppofvp:terssaSup144@aws-1-us-east-2.pooler.supabase.com:6543/postgres?pool_mode=transaction')
os.environ.setdefault('DB_SSLMODE', 'require')

# Para usar o cliente Supabase (opcional)
os.environ.setdefault('SUPABASE_URL', 'https://izdsgkstzompjvppofvp.supabase.co')
# os.environ.setdefault('SUPABASE_ANON_KEY', '[YOUR-ANON-KEY]')
