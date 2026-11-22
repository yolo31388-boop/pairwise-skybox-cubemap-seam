import pytest
import render.skybox_cubemap_seam as mod

CASES = [
    ("share_edge", (4, 1024)),
    ("mip_continuous", (2, 8)),
    ("matrix_normalize", (1.0, 2.0)),
    ("exposure_unify", (1.0, 2.0)),
    ("cross_face_draw", (2, 1024)),
    ("resolution_hint", (1024, 4096)),
    ("direction_sample", (0.5, -0.5)),
    ("reflection_sync", (1, 2)),
    ("hdr_preserve", (4.0, 1.0)),
    ("face_orientation", (3, 2)),
    ("seam_blend", (0.1, 0.2)),
    ("face_index", (-1.0, 2.0)),
    ("sample_dir", (0.0, 1.0)),
    ("edge_epsilon", (1, 1024)),
    ("env_rotation", (90.0, 0.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
