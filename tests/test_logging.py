from ghostwater.utils.logging import get_logger


def test_logger_is_reused_without_duplicate_handlers():
    a = get_logger("gw.test")
    b = get_logger("gw.test")
    assert a is b
    assert len(a.handlers) == 1