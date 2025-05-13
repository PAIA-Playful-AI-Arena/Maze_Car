export tag="4.1.2"
export game="maze_car"

docker buildx build --platform linux/amd64,linux/arm64 \
-t paiatech/${game}:${tag} -t paiatech/${game}:${tag}-PGE20250313 \
-f ./Dockerfile . --push