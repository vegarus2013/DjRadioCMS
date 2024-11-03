FROM archlinux/archlinux:base-20241101.0.275768

WORKDIR /icecast_pack

RUN useradd -m -s /bin/false icecast

COPY pkg/* /icecast_pack

RUN echo 

RUN echo "[icecast_pack]" >> /etc/pacman.conf && \
    echo "SigLevel = Optional TrustAll" >> /etc/pacman.conf && \
    echo "Server = file:///icecast_pack" >> /etc/pacman.conf

RUN sed -i 's/^\[extra\]/# &/' /etc/pacman.conf && \
    sed -i 's/^Include = \/etc\/pacman.d\/mirrorlist/# &/' /etc/pacman.conf

RUN sed -i 's/^\[core\]/# &/' /etc/pacman.conf && \
    sed -i 's/^Include = \/etc\/pacman.d\/mirrorlist/# &/' /etc/pacman.conf

RUN pacman -Sy && pacman -S --noconfirm icecast

COPY etc/icecast.xml /etc/icecast.xml
COPY etc/mime.types /etc/mime.types
RUN chown icecast:icecast /etc/icecast.xml /etc/mime.types
RUN mkdir -p /var/log/icecast && chown icecast:icecast /var/log/icecast

EXPOSE 10253

USER icecast
CMD ["icecast", "-c", "/etc/icecast.xml"]
