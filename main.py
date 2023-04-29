from datetime import *

dogum = datetime.strptime(input("Doğum Tarihinizi  Giriniz (g.a.Y): "), "%g.%a.%Y")
yas = datetime.now() - dogum

print(f"{yas.total_seconds()} Saniye kadar yaşadınız ")
