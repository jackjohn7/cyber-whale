
if __name__ == "__main__":
    from args import Args
    from sys import argv

    from sys import exit
    import cli_errors

    args = Args()

    try:
        args.parse()

    except cli_errors.CliError as e:
        print(e)
        print(cli_errors.usage(argv[0]))
        exit(1)
    except Exception as e:
        print("Oops... An unexpected error occurred")
        print(e)
        print(cli_errors.usage(argv[0]))
        exit(1)



