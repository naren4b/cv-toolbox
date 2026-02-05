# Clone/build
mkdir resume-generator && cd resume-generator
# Copy code/files as above
pip install docker  # If needed

# Build Docker
docker build -t resume-gen .

# Run with your data.json (mount data dir)
docker run -v $(pwd)/data:/app/data resume-gen data.json

# Multiple: docker run -v $(pwd)/data:/app/data resume-gen data1.json data2.json
