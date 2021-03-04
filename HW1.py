
import sys
import traceback
import Crypto.Cipher
# BEGIN SOLUTION
# please import only standard modules and make sure that your code compiles and runs without unhandled exceptions 
from Crypto.Cipher import AES
# END SOLUTION


def problem_1():
    with open("cipher1.bin", "rb") as cipher_file:  # rb means "read only in binary"
        cipher_text = cipher_file.read() # byte
    #print(cipher_text)
    # BEGIN SOLUTION
    iv=bytearray(16)
    key = bytearray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        
    aes = AES.new(key, AES.MODE_CBC, iv)
    plain_text = aes.decrypt(cipher_text)

    # END SOLUTION

    with open("plain1.txt", "wb") as plain_file:  # wb means writing in binary mode
        plain_file.write(plain_text)



def problem_2():
    with open("cipher2.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()
    
    # BEGIN SOLUTION
    iv=bytearray(16)
    rList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    key = bytearray(rList)

    ctext1 = cipher_text[:16]
    ctext2 = cipher_text[16:32]
    ctext3 = cipher_text[32:]
    

    # mtxt = ctext1+ctext2+ctext3
    # mtxt = ctext1+ctext3+ctext2
    # mtxt = ctext2+ctext1+ctext3
    # mtxt = ctext2+ctext3+ctext1
    # mtxt = ctext3+ctext1+ctext2
    modified_cipher_text = ctext3+ctext2+ctext1
    

    aes = AES.new(key, AES.MODE_CBC, iv)
    decd = aes.decrypt(modified_cipher_text)
    print("decd is ",decd)
 
    plain_text = decd
    # END SOLUTION

    with open("plain2.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def problem_3():
    with open("cipher3.bmp", "rb") as cipher_file:
        cipher_bmp = cipher_file.read()
    with open("msg3.bmp", "rb") as message_file:
        other_bmp = message_file.read()

    # BEGIN SOLUTION

    header = other_bmp[:1000]  
    modified_cipher_bmp = header + cipher_bmp[1000:]

    # END SOLUTION

    with open("cipher3_modified.bmp", "wb") as modified_cipher_file:
        modified_cipher_file.write(modified_cipher_bmp)


def problem_4():
    with open("plain4A.txt", "rb") as plain_file:
        plain_text_a = plain_file.read()
    with open("cipher4A.bin", "rb") as cipher_file:
        cipher_text_a = cipher_file.read()
    with open("cipher4B.bin", "rb") as cipher_file:
        cipher_text_b = cipher_file.read()

    # BEGIN SOLUTION
    # p1 xor c1 xor c2 = p2
    plain_text_b = bytes([ a ^ b ^ c for (a,b,c) in zip(bytes(plain_text_a), bytes(cipher_text_a), bytes(cipher_text_b)) ])
    print(plain_text_b)

    # END SOLUTION

    with open("plain4B.txt", "wb") as plain_file:
        plain_file.write(plain_text_b)


def problem_5():
    with open("cipher5.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    iv=bytearray(16)
    key = bytearray([0] * 16)
    
    for month in range(1,12):
        for day in range(1,31):
            for year in range(0,99):
                key = bytearray([month,day,year,0,0,0,0,0,0,0,0,0,0,0,0,0])
                aes = AES.new(key, AES.MODE_CBC, iv)
                decd = aes.decrypt(cipher_text)
                count =0
                for c in decd:
                    if 0 <= c and c <= 128:
                        count = count +1
                        if count == len(decd):
                            print("Moriarty's birth - month : "+str(month)+", day : "+str(day)+", year : "+str(year))
                            print(decd)
                            plain_text = decd

    # END SOLUTION

    with open("plain5.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def main():
    try:
        problem_1()
        problem_2()
        problem_3()
        problem_4()
        problem_5()
    except Exception:
        print("Exception:")
        traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
