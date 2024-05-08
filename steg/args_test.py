from args import Args
import cli_errors
import pytest

def test_file_not_found():
    with pytest.raises(cli_errors.FileNotFound):
        args = Args()
        args.parse(["-r", "-b", "-o10", "-i13", "-wtest.jpg"])
    with pytest.raises(cli_errors.FileNotFound):
        args = Args()
        args.parse(["-r", "-b", "-o10", "-i13", "-htest.jpg", "-wREADME.md"])
def test_bad_param():
    with pytest.raises(cli_errors.InvalidParam):
        args = Args()
        args.parse(["-r", "-b", "-oinvalid", "-i13", "-wsteg/steg.py"])
    with pytest.raises(cli_errors.InvalidParam):
        args = Args()
        args.parse(["-r", "-b", "-o10", "-iinvalid", "-wsteg/steg.py"])

def test_mutual_exclusion():
    with pytest.raises(cli_errors.TooManyModesSpecified):
        args = Args()
        args.parse(["-s", "-r", "-b"])
    with pytest.raises(cli_errors.TooManyModesSpecified):
        args = Args()
        args.parse(["-s", "-b", "-B"])

def test_unrecognized():
    with pytest.raises(cli_errors.UnrecognizedArgument):
        args = Args()
        args.parse(["-s", "-e"])
    with pytest.raises(cli_errors.UnrecognizedArgument):
        args = Args()
        args.parse(["-s", "test.py"])
    with pytest.raises(cli_errors.UnrecognizedArgument):
        args = Args()
        args.parse(["-s", "i50"])

def test_parse():
    args = Args()
    args.parse(["-s", "-b", "-o3", "-i5", "-wsteg/steg.py"])
    assert args.action == "store"
    assert args.data_mode == "bit"
    assert args.offset == 3
    assert args.interval == 5
    assert args.wrapper == "steg/steg.py"
    assert args.hidden is None

    args = Args()
    args.parse(["-s", "-b", "-o30", "-i52", "-wREADME.md", "-hsteg/steg.py"])
    print(args)
    assert args.action == "store"
    assert args.data_mode == "bit"
    assert args.offset == 30
    assert args.interval == 52
    assert args.wrapper == "README.md"
    assert args.hidden == "steg/steg.py"

