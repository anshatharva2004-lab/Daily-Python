def f_to_c(F):
    return 5*(F-32)/9

F = int(input("enter the tempreture in F : "))
c = f_to_c(F)
print(f"{round(c,2)}°c")