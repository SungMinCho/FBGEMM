#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import os

import torch

try:
    torch.ops.load_library(os.path.join(os.path.dirname(__file__), "fbgemm_gpu_py.so"))
except Exception as e:
    print(e)

# Since __init__.py is only used in OSS context, we define `open_source` here
# and use its existence to determine whether or not we are in OSS context
open_source: bool = True

# Trigger the manual addition of docstrings to pybind11-generated operators
import fbgemm_gpu.docs  # noqa: F401, E402

# Export the version string from the version file auto-generated by setup.py
from fbgemm_gpu.docs.version import __version__  # noqa: F401, E402

# Trigger meta operator registrations

from . import sparse_ops, split_embeddings_cache_ops  # noqa: F401, E402

# from . import sparse_ops # noqa: F401, E402
