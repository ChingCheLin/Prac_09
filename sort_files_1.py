import os


def main():

    os.chdir('FilesToSort')

    for filenames in os.listdir('.'):
        if os.path.isdir(filenames):
            continue

        extension = filenames.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        os.rename(filenames, "{}/{}".format(extension, filenames))
        print()

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains files:", filenames)


main()