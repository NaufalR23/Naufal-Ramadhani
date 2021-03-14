elemenpokemon = (input('Masukkan elemen pokemon anda(fire/water/grass) :'))
attack = int(input('Masukkan attack pokemon anda(1-100) :'))
elemenlawan = (input('Masukkan elemen pokemon lawan(fire/water/grass) :'))

if elemenpokemon == elemenlawan:
    damage = attack * (100/100)
    print("Tidak terjadi perubahan kekuatan serangan")
    print("Attack sekarang :", damage)
elif elemenpokemon != elemenlawan:
    if elemenpokemon == "fire" and elemenlawan == "grass":
        damage = attack * (150/100)
        print("Serangan efektif!")
        print("Attack sekarang :", damage)
    elif elemenpokemon == "fire" and elemenlawan == "water":
        damage = attack * (50/100)
        print("Serangan tidak efektif")
        print("Attack sekarang :", damage)
    elif elemenpokemon == "water" and elemenlawan == "fire":
        damage = attack * (150/100)
        print("Serangan efektif!")
        print("Attack sekarang :", damage)
    elif elemenpokemon == "water" and elemenlawan == "grass":
        damage = attack * (50/100)
        print("Serangan tidak efektif")
        print("Attack sekarang :", damage)
    elif elemenpokemon == "grass" and elemenlawan == "water":
        damage = attack * (150/100)
        print("Serangan efektif!")
        print("Attack sekarang :", damage)
    elif elemenpokemon == "grass" and elemenlawan == "fire":
        damage = attack * (50/100)
        print("Serangan tidak efektif")
        print("Attack sekarang :", damage)
else:
    print("Elemen pokemon tidak ada")