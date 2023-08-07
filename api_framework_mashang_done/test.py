def c():
    try:
        open("beifan.apx")
    except Exception as e:
        print(1,e)
    except FileNotFoundError as e:
        print(2,e)
    print("i am c")
