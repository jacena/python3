age = 11

if age>=12:
    print('a')
elif age>=5:
    print('b')
else:
    print('c')


height = input('请输入你的身高：')
weight = input('请输入你的体重：')

height = float(height)
weight = float(weight)

bmi = height / weight
bmi = float(bmi)
print('我的BMI是： %.2f' % bmi)
if bmi>=32:
    print('严重肥胖')
elif bmi>=18:
    print('正常')
else:
    print('过轻')


