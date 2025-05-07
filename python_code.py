def convert_p6_to_p3():
    input_path = '/home/data/colorP6File.ppm'
    output_path = 'colorP3File.ppm'

    with open(input_path, 'rb') as f:
        magic = f.readline().strip()
        if magic != b'P6':
            raise ValueError("Not a valid P6 PPM file")

        def read_line():
            line = f.readline()
            while line.startswith(b'#') or line.strip() == b'':
                line = f.readline()
            return line

        size_line = read_line()
        width, height = map(int, size_line.strip().split())

        maxval_line = read_line()
        maxval = int(maxval_line.strip())
        if maxval > 255:
            raise ValueError("Only maxval up to 255 is supported")

        pixel_data = f.read(width * height * 3)

    with open(output_path, 'w') as out:
        out.write("P3\n")
        out.write(f"# Converted from P6 to P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{maxval}\n")

        for i in range(0, len(pixel_data), 3):
            r, g, b = pixel_data[i], pixel_data[i+1], pixel_data[i+2]
            out.write(f"{r} {g} {b}\n")

convert_p6_to_p3()
