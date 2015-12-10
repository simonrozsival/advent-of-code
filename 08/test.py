from func import unescaped_length 

print(0 == unescaped_length('""'))
print(3 == unescaped_length('"abc"'))
print(1 == unescaped_length('"\\\""'))
print(1 == unescaped_length('"\\\\"'))
print(7 == unescaped_length('"aaa\\"aaa"'))
print(4 == unescaped_length('"\\xd2"'))
print(1 == unescaped_length('"\\x27"'))
print(2 == unescaped_length('"\\\\\\\\"'))