
import datetime

def print_greeting():
  """Basit bir selamlama mesajı yazdırır."""
  now = datetime.datetime.now()
  print(f"Hello! {now.strftime('%Y-%m-%d %H:%M:%S')} tarihinde GitHub repo'nu klonladın.")

if __name__ == "__main__":
  print_greeting()