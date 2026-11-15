from ghostwater.utils.config import get_path, load_config


def test_config_loads():
    cfg = load_config()
    assert cfg["project"]["seed"] == 42


def test_drop_fractions_are_valid():
    cfg = load_config()
    fr = cfg["sparsity"]["drop_fractions"]
    assert fr == sorted(fr)
    assert all(0.0 <= x < 1.0 for x in fr)


def test_paths_resolve_inside_project():
    cfg = load_config()
    p = get_path(cfg, "data_raw")
    assert p.name == "raw"