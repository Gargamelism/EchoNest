import argparse

import lessons.lesson_1 as lesson_1
import lessons.lesson_2 as lesson_2


def main():
    parser = argparse.ArgumentParser(description="A description of your project")
    parser.add_argument("--cmd", type=str, help="which command to run")

    args = parser.parse_args()

    {"lesson_1": lesson_1.main, "lesson_2": lesson_2.main}.get(args.cmd, lambda: parser.print_help())()


if __name__ == "__main__":
    main()
