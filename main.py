#Variables globales

def run(number):
    # TODO
    #Variable local
    print(f"{number:.3f}")
    print(f"{number:f}")
    print(f"{number:8.2f}")
    print(f"{number:e}")
    print(f"{number:010.4f}")
    print(f"{number:19.5f}")
    return number

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    