import subprocess
import sys


def test_hello_world_output(capsys):
    import hello  # noqa: F401

    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_hello_world_exit_code():
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout == "Hello, World!\n"
