# BSD 3-Clause License; see https://github.com/scikit-hep/awkward-1.0/blob/main/LICENSE

import pytest  # noqa: F401
import numpy as np  # noqa: F401
import awkward as ak  # noqa: F401


behavior = {}


@ak._v2.behaviors.mixins.mixin_class(behavior, "1030_point")
class AVeryVeryVeryLargeClassName:
    @property
    def mag2(self):
        return self.x**2 + self.y**2


def test():
    x = np.random.randint(0, 64, 128)
    y = np.random.randint(0, 64, 128)

    point_1030 = ak._v2.operations.structure.zip(
        {"x": x, "y": y}, behavior=behavior, with_name="1030_point"
    )
    assert isinstance(point_1030.mag2, ak._v2.Array)

    point = ak._v2.operations.structure.zip(
        {"x": x, "y": y}, behavior=behavior, with_name="AVeryVeryVeryLargeClassName"
    )
    with pytest.raises(AttributeError):
        assert isinstance(point.mag2, ak._v2.Array)