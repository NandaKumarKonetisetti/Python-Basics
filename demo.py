import calculator

# IF we run this module then it will says name as main
#But if we are importing this module in another module then it will says as moddule name
print("Demo says ",__name__)
def funciton():
    print("In side function in demo")


if __name__ == "__main()__":
    funciton()
    print("Demo says ",__name__)

print("Demo says",__name__)