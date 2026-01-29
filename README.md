# fetch-control-v1

Fetch Control Model compatible with **Konnex AI Fetch Interface**

## Overview
This is a simple Vision-Language-Action compatible control policy
for the Fetch mobile manipulator.

The model accepts robot state observations and outputs a 13-dimensional
action vector normalized in [-1, 1].

Designed for testing, research, and AI miner onboarding.

## Interface Spec
- Observation input: vector state (dim = 50)
- Action output: 13-dim continuous action
- Output range: [-1, 1] (tanh)
- Framework: PyTorch

## Files
- `model.py` – Policy network definition
- `fetch_policy.pt` – Model weights
- `export_model.py` – Script to export model

## Status
Experimental / Testnet

## License
MIT
