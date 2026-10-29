import json
from importlib.resources import files

DATA = files("riftroute") / "data"


def load(name):
    return json.loads((DATA / name).read_text())


def test_nodes_shape():
    nodes = load("litein_nodes.json")
    assert nodes["metadata"]["coordinate_order"] == "lat, lon"
    assert nodes["depot"]["node_id"] == 0
    ids = [c["node_id"] for c in nodes["buying_centres"]]
    assert ids == list(range(1, len(ids) + 1))


def test_pinned_coordinates_in_range():
    nodes = load("litein_nodes.json")
    for node in [nodes["depot"], *nodes["buying_centres"]]:
        if node["lat"] is None:
            continue
        assert -90 <= node["lat"] <= 90
        assert -180 <= node["lon"] <= 180


def test_rules_have_sources():
    rules = load("rules.json")
    assert rules["max_hours_buying_centre_to_factory"]["value"] == 2.0
    assert rules["max_vehicle_turnaround_hours"]["value"] == 3.0
    assert rules["max_kg_per_bag"]["value"] == 12
    for rule in rules.values():
        assert rule["source"] and rule["section"]


def test_scenario_loads():
    scenario = load("scenarios/peak_day.json")
    assert scenario["fleet"] and scenario["centres"]
