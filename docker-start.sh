docker stop twirl >/dev/null
docker rm twirl >/dev/null
docker run -d \
  -it \
  --name twirl \
  --mount type=bind,source="$(pwd)",target=/twirl \
  archlinux:base-devel >/dev/null
docker exec -it twirl /bin/bash