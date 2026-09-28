from fabric_lab.core import *
def test_12_leaf_configs(): assert all(valid(leaf(i)) for i in range(1,13))
def test_three_vrfs(): assert set(TENANTS)=={"CORP","IOT","GUEST"}
def test_type2_type5_design_intent(): x=leaf(1); assert "vn-segment 10110" in x and "vni 50110" in x and "advertise l2vpn evpn" in x
def test_bfd_timing_evaluator(): assert convergence_ms(1000,1750)==750
