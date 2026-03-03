# extract_password.py
OFF = 0x3EB8  # verified with: strings -a -t x

with open("CrackMeEasy.exe", "rb") as f:
    f.seek(OFF)
    out = bytearray()
    while True:
        b = f.read(1)
        if not b or b == b"\x00":
            break
        out += b

print(out.decode("ascii"))
