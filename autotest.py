import subprocess
import random

def check_result(number):
    new_result = subprocess.run([f'C:/Users/podvo/anaconda3/python.exe', f'main.py'],
                          input=f'{number}\n', capture_output=True, text='utf-8').stdout
    original_result = subprocess.run(f'tickertapecrt.bas', input=f'{number}\n', shell=True,
                          capture_output=True, text='utf-8').stdout[:-45]

    return new_result == original_result


def test(a):
    assert check_result(a), f"INPUT {a}: RESULT: INVALID"
    print(f"INPUT {a}: RESULT: PASSED")


for i in range(5):
    test(random.randint(0, 100000))

test(144)
test(54385)
test(8743)
test(8)
test(0)
test(8497601958192589125)