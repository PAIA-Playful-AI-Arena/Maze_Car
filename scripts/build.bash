export tag="latest"
export game="maze_car"

docker build \
-t ${game}:${tag} \
-f ./Dockerfile .
