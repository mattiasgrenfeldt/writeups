from pwn import *

bytecode = open("bytecode_to_submit", "rb").read()

r = remote("bytecoooding.challenges.ooo", 5000)
#r = remote("localhost", 5000)

r.readuntil("Bytecode:")
r.send(bytecode)

r.readuntil("> ")

l = ["python3", "python2", "ocaml", "lua"]
for lang in l:
    r.sendline(lang)

r.sendline("")

r.interactive()

# done: "python3", "python2", "lua", "ocaml"

# left: "jvm", "ruby", "nodejs", "elisp"
