import argparse

import lessons.lesson_1 as lesson_1


def main():
    parser = argparse.ArgumentParser(description="A description of your project")
    parser.add_argument("--cmd", type=str, help="which command to run")

    args = parser.parse_args()

    {"lesson_1": lesson_1.main}.get(args.cmd, lambda: parser.print_help())()


if __name__ == "__main__":
    main()
