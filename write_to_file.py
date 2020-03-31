def write_to_file(grid):
    output_file = open("outputfile.txt","w")
    for line in grid:
        output_file.write(str(line))
        output_file.write("\n")
    output_file.close()

