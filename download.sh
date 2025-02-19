mkdir -p models

curl -L -o models/discogs-effnet-bs64-1.pb "https://essentia.upf.edu/models/feature-extractors/discogs-effnet/discogs-effnet-bs64-1.pb"
curl -L -o models/genre_discogs400-discogs-effnet-1.pb "https://essentia.upf.edu/models/classification-heads/genre_discogs400/genre_discogs400-discogs-effnet-1.pb"