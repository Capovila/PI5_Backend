import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  "https://ypypuvchmodptwbvbwtb.supabase.co",
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlweXB1dmNobW9kcHR3YnZid3RiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5MDYwMjQsImV4cCI6MjA2MDQ4MjAyNH0.BvGZTOPigHlFwXTX9I81NWRyRz_V1jDU800aAtju57w"
);
