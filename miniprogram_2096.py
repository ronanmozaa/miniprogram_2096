import random 

def main():
    print ("tebak angka 1 sampai 100")
    angkaacak = random.randint(1,100)
    tebakan = False 

    while not tebakan :
        tebak = input("tebakan anda :")
        tebak = int (tebak)

        if tebak == angkaacak:
            print ("tebakan anda benar !!")
            tebakan = True
        elif tebak > angkaacak :
            print ("tebakan anda terlalu besar")
        else :
            print ("tebakan anda terlalu kecil")

    print ("Terima kasih sudah bermain tebak angka")
if __name__ == "__main__":
    main()
