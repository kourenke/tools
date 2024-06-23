# tools
Common tools for dataset format conversion

In addition, we have also compiled a set of evaluation index libraries suitable for algorithms in this field, named BinarySOSMetrics.

The relevant code is published on https://github.com/BinarySOS/BinarySOSMetrics.

The main features of BinarySOSMetrics include:

High Efficiency: Multi-threading.

Device Friendly: All metrics support automatic batch accumulation.

Unified API: All metrics provide the same API, Metric.update(labels, preds) complete the accumulation of batches， Metric.get() get metrics。

Unified Computational: We use the same calculation logic and algorithms for the same type of metrics, ensuring consistency between results.

Supports multiple data formats: Supports multiple input data formats, hwc/chw/bchw/bhwc/image path, more details in ./notebook/tutorial.ipynb
