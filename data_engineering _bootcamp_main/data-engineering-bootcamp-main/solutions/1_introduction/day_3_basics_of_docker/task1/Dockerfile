FROM ubuntu:22.04 AS builder
WORKDIR /BLD
RUN apt-get update -q && apt-get install -qy dpkg-dev devscripts \
    && apt-get clean && rm -rf /var/lib/apt
RUN sed -Ei.bak 's/^# deb-src /deb-src /' /etc/apt/sources.list
RUN apt-get update -q && apt-get source hello && apt-get build-dep -y hello \
    && apt-get clean && rm -rf /var/lib/apt
RUN cd hello-2.10/ && dpkg-buildpackage -rfakeroot -b -uc -us \
    && apt install -f ../hello_2.10-2ubuntu4_amd64.deb
FROM ubuntu:22.04
COPY --from=builder /usr/bin/hello /usr/bin/
ENTRYPOINT ["/usr/bin/hello", "-g"]
CMD ["Hello world!"]
