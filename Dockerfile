FROM ubuntu

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    ninja-build \
    build-essential \
    libboost-program-options-dev \
    libboost-graph-dev \
    libboost-system-dev \
    libeigen3-dev \
    libflann-dev \
    libfreeimage-dev \
    libmetis-dev \
    libgoogle-glog-dev \
    libgtest-dev \
    libgmock-dev \
    libsqlite3-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev \
    libceres-dev \
    nvidia-cuda-toolkit \
    nvidia-cuda-toolkit-gcc

# Clone and build COLMAP
WORKDIR /opt
RUN git clone https://github.com/colmap/colmap.git && \
    cd colmap && \
    mkdir build && \
    cd build && \
    cmake .. -GNinja && \
    ninja && \
    ninja install

# Create output directory
RUN mkdir -p /workspace/output

# Set default working directory
WORKDIR /workspace

# Run COLMAP automatically
CMD ["colmap", "automatic_reconstructor", "--workspace_path", "/workspace/output", "--image_path", "/workspace/Route_reconstruct/test_imgs/e7"]
