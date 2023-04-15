let = ''

while let == "":
    let = input("\nInforme a letra: ").strip()
    if let != "⠀":
        let = let

if let not in 'abcdefghijklmnopqrstuvwxyz' and let not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print("este caracter não consta no alfabeto\n")
elif let not in 'aeiou' and let not in 'AEIOU':
    print("Consoante\n")
else:
    print("Vogal\n")

