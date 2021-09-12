name = "Robert" 

def main():
    print("main called", name)
    def nested_funcions():
        print("nested_function called", name)

    nested_funcions()
main()