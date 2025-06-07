docker run -d -it \
    --name jekyll \
    -v /Users/lq/Documents/lqxyz.github.io/:/work\
    --workdir /work \
    amirpourmand/al-folio:slim \
    bash
