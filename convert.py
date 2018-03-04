def convert():
    import jiphy
    import sys

    for file in sys.argv[1:]:
        code = open(file, "r").read();
        if file[-3:] == ".py":
            open(file[:-3]+".js", "w").write(jiphy.to.javascript(code))
        elif file[-3:] == ".js":
            open(file[:-3]+".py", "w").write(jiphy.to.python(code))
        
convert()



