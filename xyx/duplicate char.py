input = [1,2,3,[5,6,[7,8],9,4],10,11]
new = []
def repeat(input1):
    for i in input1:
        if type(i) == list:
            repeat(i)
        else:
            new.append(i)
            #print(new)
    print(new)
repeat(input)





"""
#[1,2,3,4,5,6,7,8,9,10,11]
a=[]

def x():


for i in range(len(input)):
    if type(input[i]) == int:
        a.append(input[i])
    else:
        for j in range(len(input[i])):
            if type(input[i][j]) == int:
                a.append(input[i][j])
print(a)
#"""
# w= WebDriverWait()
# w.until(expected_conditions.element_to_be_clickable(driver,10))
#
# driver.save_screenshot()
#
# a= driver.window_handles
#
# 1. 401 vs 403
# 2. amazon list of iphones
# 3.

