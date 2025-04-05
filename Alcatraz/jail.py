def main():
    print(open(__file__).read())
    print()
    print()
    print()
    print("I dare you to break me")
    text = input('>>> ')
    for keyword in ['builtins', 'dir', 'name', 'class', 'base', 'mro', 'globals', 'subprocess', 'eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write', '_']:
        if keyword in text.lower():
            print("Noob!")
            return;
    
    exec(text)
if __name__ == "__main__":
    main()
