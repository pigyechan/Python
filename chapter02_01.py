#기본 출력
print("python start!")

#separator 옵션
print('P', 'y' ,'t', sep = '!')

#end 옵션
print('welcome to', end='.')
print('IT News', end='1')

#file 옵션
import sys

print('Learn python', file=sys.stdout)
print()

#format 사용(d,s,f)
print('%s %s' %('one', 'two'))
print("{} {}".format('one', 'two'))

print('%10s' %('nice'))
print('{:>10}' .format('nice'))

print('%-10s' %('nice'))
print('{:10}' .format('nice'))


print('{:&>10}' .format('nice'))
print('{:&^10}' .format('nice'))

print('%.5s' %('nice'))