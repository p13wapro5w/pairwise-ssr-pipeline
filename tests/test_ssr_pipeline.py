import pytest
from render import ssr_pipeline as mod

CASES = [
    ("blend_half", 'm.blend_reflections(1.0, 3.0, 0.5) == approx(2.0)'),
    ("blend_full", 'm.blend_reflections(1.0, 3.0, 1.0) == approx(1.0)'),
    ("blend_zero", 'm.blend_reflections(1.0, 3.0, 0.0) == approx(3.0)'),
    ("thick_positive", 'm.depth_thickness(2.0, 5.0) == approx(3.0)'),
    ("thick_clamp", 'm.depth_thickness(5.0, 2.0) == approx(0.0)'),
    ("mip_mid", 'm.roughness_mip(0.5, 8) == 4'),
    ("mip_high", 'm.roughness_mip(1.0, 8) == 8'),
    ("normal_flat", 'm.reconstruct_normal(0.0, 0.0, 1.0) == approx((0.0, 0.0, 1.0))'),
    ("normal_tilt", 'm.reconstruct_normal(1.0, 0.0, 1.0) == approx((-0.7071, 0.0, 0.7071), rel=1e-3)'),
    ("backface", 'm.is_backface(-1.0) is True'),
    ("frontface", 'm.is_backface(1.0) is False'),
    ("opaque_priority", 'm.depth_priority(1.0) == 1'),
    ("transparent_priority", 'm.depth_priority(0.5) == 0'),
    ("uv_scale", 'm.scaled_uv(0.5, 100.0, 200.0) == approx(0.25)'),
    ("ray_steps", 'm.ray_steps(2.0, 4.0) == 8')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
