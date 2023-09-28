// Module included in the following assemblies:
//
// * architecture/nvidia-gpu-architecture-overview.adoc

:_mod-docs-content-type: CONCEPT
[id="nvidia-gpu-cuda-mps_{context}"]
= CUDA Multi-Process Service

CUDA Multi-Process Service (MPS) allows a single GPU to use multiple CUDA processes. The processes run in parallel on the GPU, eliminating saturation of the GPU compute resources. MPS also enables concurrent execution, or overlapping, of kernel operations and memory copying from different processes to
enhance utilization.
