import ocean
import pytest


@pytest.mark.parametrize("wid, leng, neighbours", [(0, 0, 9), (0, 1, 15), (1, 0, 15), (1, 1, 24)])
def test_neigh(wid, leng, neighbours):
    assert len(ocean.neight(wid, leng)) == neighbours


@pytest.mark.parametrize(
    "position, countfish, countshrimp, new",
    [
        (0, 2, 2, 0),
        (0, 3, 0, 2),
        (0, 0, 3, 3),
        (0, 3, 3, 2),
        (2, 4, 0, 0),
        (2, 1, 0, 0),
        (2, 2, 0, 2),
        (3, 0, 4, 0),
        (3, 3, 3, 3),
        (3, 0, 1, 0),
    ],
)
def test_replace0(position, countfish, countshrimp, new):
    ocean.pole[2][1] = position
    ocean.fish = countfish
    ocean.shrimp = countshrimp
    assert ocean.replace(2, 1) == new
