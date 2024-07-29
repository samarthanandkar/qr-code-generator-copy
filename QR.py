import qrcode as qr 

'''
def input() :

    link = input(str(" Make my QR :"))
    print(link)


def qr() :   
    qr.make(link)
    input.save()
            
'''
x = input(str("give me link: "))
img = qr.make(x)
img.save(f"{img}.png")