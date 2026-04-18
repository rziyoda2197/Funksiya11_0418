#1
def sozlar_soni(fayl_nomi):
    try:
        with open(fayl_nomi, "r") as f:
            matn = f.read()
            return len(matn.split())
    except FileNotFoundError:
        return "Fayl topilmadi!"
#2
def kassa_hisobla(narx, tolov):
    if narx < 0 or tolov < 0:
        print("Xato: manfiy qiymat kiritildi!")
        return

    if tolov >= narx:
        print(f"Qaytim: {round(tolov - narx, 2)}")
    else:
        print(f"Yetishmaydi: {round(narx - tolov, 2)}")

  #3
  def bmi_hisobla(boy, vazn):
    if boy <= 0 or vazn <= 0:
        print("Xato: noto‘g‘ri qiymat!")
        return

    bmi = vazn / (boy * boy)

    if bmi < 18.5:
        holat = "Ozganlik"
    elif bmi < 25:
        holat = "Normal"
    elif bmi < 30:
        holat = "Ortiqcha vazn"
    else:
        holat = "Semizlik"

    print(f"BMI = {round(bmi, 2)}, {holat}")
