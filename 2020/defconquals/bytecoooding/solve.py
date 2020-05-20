import os

pycode = 'print(open("flag").read())'

# dummyfile as prefix in zip
with open("__dummy", "wb") as f:
    f.write(os.urandom(3*1024))

# actual file
with open("__main__.py", "wb") as f:
    f.write(pycode)

os.system("zip bytecode __dummy __main__.py")
data = open("bytecode.zip", "rb").read()
os.system("rm bytecode.zip")

# Remove the first 4 bytes of the zip so that when the pythonX magic header is added again all the pointers line up.
data = data[4:]

# add in lua
# http://files.catwell.info/misc/mirror/lua-5.2-bytecode-vm-dirk-laurie/lua52vm.html
luamagic = "\x1B\x4C\x75\x61\x52\x00\x01\x04\x08\x04\x08\x00\x19\x93\x0D\x0A\x1A\x0A"
#luadata = open("flag-lua.out", "rb").read()
luadata = open("luacaml.bin", "rb").read()
luadata = luadata[len(luamagic):]
data = luadata + data[len(luadata):]


with open("bytecode_to_submit", "wb") as f:
    f.write(data)

# Files for testing below
p1 = b"\x03\xF3\x0D\x0A"
with open("bytecode2", "wb") as f:
    f.write(p1 + data)

p2 = b"\x33\x0D\x0D\x0A"
with open("bytecode3", "wb") as f:
    f.write(p2 + data)

with open("bytecodeLua", "wb") as f:
    f.write(luamagic + data)

ocamlmagic = b"\x43\x61\x6D\x6C\x31\x39\x39\x39\x4F\x30\x31\x31"
with open("bytecodeOcaml.cmo", "wb") as f:
    f.write(ocamlmagic + data)

# OOO{Look_at-You_u_must_be_the_code_master}
