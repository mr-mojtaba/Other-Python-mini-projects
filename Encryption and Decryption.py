while True:
    print("Choose Your Option:\n\t1) Encrypt Text\n\t2) Decrypt Text\n\t3) Exit")
    enter_option = input("Enter: ")

    if enter_option == ("1"):
        enter_text = input("Enter Text: ")
        encrypt_text = ""
        for c in enter_text:
            ch = ord(c) * 3 + 7
            encrypt_text += chr(ch)
        print("\nEncrypted text:", encrypt_text, "\n" + "*" * 15 + "\n")

    elif enter_option == ("2"):
        enter_text = input("Enter Text: ")
        decrypt_text = ""
        for u in enter_text:
            un = (ord(u) - 7) // 3
            decrypt_text += chr(un)
        print("\ndecrypted text:", decrypt_text, "\n" + "*" * 15 + "\n")

    elif enter_option == ("3"):
        print("\nHope to meet\n" + "*" * 12 + "\n")
        break

    else:
        print("\nYour Option Is Wrong!\nTry Again...\n" + "*" * 21 + "\n")
