a,b = 1/3, '1/3'

print('a=%f, b=%s'%(a, b))
print('a={}, b={}'.format(a,b))
print('a={:.3f}, b={}'.format(a,b))
print(f'a={a}, b={b}')
print(f'a={a:.3f}, b={b}')
print(f'{a=}, {b=}')
print(f'{a=:.3f}, {b=}')

print(f"""{f'''{f'{"{1+1}"}'}'''}""")

print('abcd    efgh'.count('    '))
print('abcd    efgh'.expandtabs().count('    '))

