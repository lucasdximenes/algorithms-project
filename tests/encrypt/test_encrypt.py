from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 1)

    assert encrypt_message("abc", 3) == "cba"
    assert encrypt_message("haikyuu!", 3) == "iah_!uuyk"
    assert encrypt_message("haikyuu!", 4) == "!uuy_kiah"
