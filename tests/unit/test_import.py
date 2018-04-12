"""Base library tests."""


def test_import():
    """Test basic import."""
    import importlib
    try:
        importlib.import_module('econopy')
    except ImportError:
        assert False