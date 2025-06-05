from supabase import create_client

SUPABASE_URL = "https://ypypuvchmodptwbvbwtb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlweXB1dmNobW9kcHR3YnZid3RiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5MDYwMjQsImV4cCI6MjA2MDQ4MjAyNH0.BvGZTOPigHlFwXTX9I81NWRyRz_V1jDU800aAtju57w"

class SupabaseClientSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return cls._instance

    def get_client(self):
        return self.client

supabase_singleton = SupabaseClientSingleton()
supabase = supabase_singleton.get_client()