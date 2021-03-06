def main():
    beratBadan = int(input("Berat Badan (kg)    : "))
    tinggiBadan = int(input("Tinggi Badan (cm)  : "))
    print("Dengan Berat Badan {}kg dan Tinggi Badan {}cm".format(beratBadan, tinggiBadan))
    BMI = float(beratBadan*10000/(tinggiBadan*tinggiBadan))
    print("BMI anda adalah  : {:.2f}".format(BMI))
    if BMI < 18.5:
        print("Anda Termasuk Kekurangan Berat badan")
    elif 25 > BMI >= 18.5:
        print("Anda Termasuk Normal")
    elif 30 > BMI >= 25:
        print("Anda Termasuk Kelebihan Berat Badan")
    else:
        print("Anda Termasuk Obesistas")


if __name__ == '__main__':
    main()
