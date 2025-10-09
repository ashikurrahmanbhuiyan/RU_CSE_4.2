#!/usr/bin/env python3
"""
Test script to verify all ML libraries are installed correctly
"""

print("Testing ML environment setup...")
print("=" * 50)

libraries_to_test = [
    ("numpy", "np"),
    ("pandas", "pd"),
    ("matplotlib.pyplot", "plt"),
    ("seaborn", "sns"),
    ("sklearn", None),
    ("statsmodels.api", "sm"),
    ("mglearn", None),
]

failed_imports = []
successful_imports = []

for lib_name, alias in libraries_to_test:
    try:
        if alias:
            exec(f"import {lib_name} as {alias}")
            print(f"✅ {lib_name} (as {alias}) - OK")
        else:
            exec(f"import {lib_name}")
            print(f"✅ {lib_name} - OK")
        successful_imports.append(lib_name)
    except ImportError as e:
        print(f"❌ {lib_name} - FAILED: {e}")
        failed_imports.append(lib_name)

print("\n" + "=" * 50)
print(
    f"Summary: {len(successful_imports)} successful, {len(failed_imports)} failed")

if failed_imports:
    print(f"Failed imports: {failed_imports}")
else:
    print("🎉 All libraries installed successfully!")

# Test some basic functionality
print("\nTesting basic functionality...")
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris

    # Create simple test data
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)

    print(f"✅ Created DataFrame with shape: {df.shape}")
    print(f"✅ NumPy array operations work: {np.mean(df.iloc[:, 0]):.2f}")
    print("✅ All basic functionality tests passed!")

except Exception as e:
    print(f"❌ Functionality test failed: {e}")

print("\n🚀 Environment setup complete!")
